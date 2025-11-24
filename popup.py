import tkinter as tk
from tkinter import ttk
import threading

class LoadingPopup:
    result = None

    def __init__(self, parent=None, title=None, text=None):
        if title is None:
            title="Loading..."

        if text is None:
            text = "Please wait, loading..."
        
        self.popup = tk.Toplevel(parent)
        self.popup.title(title)
        self.popup.geometry("300x100")
        self.popup.resizable(False, False)
        
        # Center the popup on screen
        self.popup.update_idletasks()
        x = (self.popup.winfo_screenwidth() // 2) - (300 // 2)
        y = (self.popup.winfo_screenheight() // 2) - (100 // 2)
        self.popup.geometry(f"300x100+{x}+{y}")
        
        # Make it modal (grab focus)
        self.popup.grab_set()
        self.popup.focus_force()
        
        # Prevent closing with X button
        self.popup.protocol("WM_DELETE_WINDOW", lambda: None)
        
        # Main frame
        frame = tk.Frame(self.popup)
        frame.pack(expand=True)
        
        # Loading label
        self.label = tk.Label(frame, text=text, font=("Helvetica", 10))
        self.label.pack(pady=10)
        
        # Spinner (ttk.Progressbar in indeterminate mode acts as a spinner)
        self.spinner = ttk.Progressbar(frame, mode='indeterminate', length=200)
        self.spinner.pack(pady=10)
        self.spinner.start(10)  # Start the animation
        
    def close(self):
        """Close the loading popup"""
        if self.popup.winfo_exists():
            self.popup.grab_release()
            self.popup.destroy()

def start_loading(func, title, text):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Create and show loading popup
    loading = LoadingPopup(root, title, text)
    
    # Run the main program in a separate thread
    def run_main():
        loading.result = func()
        # Close popup when done (using after to stay in main thread)
        root.after(0, loading.close)
        root.after(100, root.quit)  # Allow mainloop to end
    
    thread = threading.Thread(target=run_main, daemon=True)
    thread.start()

    root.mainloop()

    return loading