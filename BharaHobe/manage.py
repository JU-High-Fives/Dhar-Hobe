#!/usr/bin/env python
import os
import sys

def main():
    """Main entry point."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute Django setup code after the app registry is ready
    def run():
        execute_from_command_line(sys.argv)

    # Check if the script is being executed directly
    if __name__ == '__main__':
        run()

main()
