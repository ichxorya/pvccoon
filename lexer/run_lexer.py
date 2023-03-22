# This program is used to run the lexer (core/lexer.py).

import sys
import subprocess

# Define the default input file path
input_path = "examples/example_fib.vc"

# Define the command to run the lexer.py file
cmd = ["python", "core/lexer.py", input_path]

# use subprocess to run the command
subprocess.run(cmd)
