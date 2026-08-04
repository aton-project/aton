#!/usr/bin/env python3

from loader import scan_foundation
from writer import write_all


def main():

    print("ATON Markdown Renderer")
    print("======================")
    print()

    print("Loading Foundation...")

    artifacts = scan_foundation()

    print(f"Loaded {len(artifacts)} artifacts.")
    print()

    print("Rendering Markdown...")

    write_all(artifacts)

    print()
    print("Done.")


if __name__ == "__main__":
    main()
