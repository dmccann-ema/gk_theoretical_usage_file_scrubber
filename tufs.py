from theoretical_use_file_scrubber.app import main
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true')
    return parser.parse_args()


main.main(**vars(get_args()))