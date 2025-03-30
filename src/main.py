#!/usr/bin/env python3 

import argparse

def parse_c(function, path):
    return

def parse_py(function, path):
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", help="the name of the function")
    parser.add_argument("path", help="the path to search")
    args = parser.parse_args()
    function = args.function
    path = args.path

    filetype = path.split('.')[-1] if path else None
    print(filetype)
    if filetype not in ['c', 'py']:
        print("error: non-{C, Python} files not supported yet")

if __name__ == "__main__":
    main()
