"""Author: Nomah S."""

import os
import argparse
from pathlib import Path


def get_target():
    #create parser
    my_parser = argparse.ArgumentParser(prog='find_location', usage='%(prog)s.py [options] target', description='Finds and returns the location of a file')

    # add the arguments
    my_parser.add_argument('Target', metavar='target', type=str, help='the item you are trying to find.')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    target = args.Target
    
    return target


def find_locations(target):
   
    home  = str(Path.home()) # set to home directory
    os.chdir(home)
    locations = []
    
    for root, dirs, files in os.walk('.', topdown=False):
        if target in files or target in dirs:
            locations.append(root)
    return locations



if __name__ == '__main__':
    target = get_target()
    locations = find_locations(target)
    if locations:
        print(f"target locations: {locations}")
    else:
        print(f"{target} not found.")
    
