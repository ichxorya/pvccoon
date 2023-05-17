# Import libraries.
import sys

# Main function.
if __name__ == "__main__":
    # Check the arguments.
    if len(sys.argv) < 2:
        print("Usage: python parser.py <path>")
        print("Or: python parser.py --test (to parse examples)")
        sys.exit(1)

    arg = sys.argv[1]

    # Check the argument.
    if arg == '--test':
        run_examples()

    else:
        pass
