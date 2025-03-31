funcat
======

function + cat

Quick and lightweight tool to print contents of a function to stdout.
I find that I have to print the contents of a specific function pretty often,
whether it's to copy & paste to send to others for review or to create
snapshots of a function over time.

I only work in C and Python, so those are all that this tool supports (for now).
I also intend to make the Python portion of this to rely less on the AST
library (since it is quite expensive).

I also intend to add recursive function searching, in case you want to search
for a function definition across multiple files. There are also probably
instances where a function is defined twice (e.g. functions defined differently
across #ifdef #else statements), so funcat should support that.


Usage
=====

Add this directory to your PATH and you can run:
```
funcat <function-name> <path-to-code>
```
