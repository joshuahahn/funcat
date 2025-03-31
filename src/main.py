#!/usr/bin/env python3 

import argparse
import ast # For Python abstract syntax tree

def parse_c(function, path):
    return

def parse_py(function_name, path):
    with open(path, 'r') as f:
        code = f.read()

    tree = ast.parse(code, filename=path)
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.name != function_name:
                continue

            start = node.lineno-1 # AST line numbers are 1-indexed
            end = node.end_lineno
            function_body = "\n".join(code.splitlines()[start:end])
            print(function_body)

            return

    print("error: function definition not found")
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", help="the name of the function")
    parser.add_argument("path", help="the path to search")
    args = parser.parse_args()
    function = args.function
    path = args.path

    filetype = path.split('.')[-1] if path else None
    if filetype not in ['c', 'py']:
        print("error: non-{C, Python} files not supported yet")

    if filetype == 'py':
        parse_py(function, path)

if __name__ == "__main__":
    main()
