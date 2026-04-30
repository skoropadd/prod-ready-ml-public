# argparse_cli.py
"""CLI using argparse."""

import argparse


def say_hi(name):
    """Say hi."""
    print(f"Hello {name}")


def main():
    """Run the main function."""
    parser = argparse.ArgumentParser(description="CLI using argparse")
    parser.add_argument("name", type=str, help="Name")
    args = parser.parse_args()
    say_hi(name=args.name)


if __name__ == "__main__":
    main()
