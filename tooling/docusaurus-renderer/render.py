#!/usr/bin/env python3

from loader import load_foundation
from writer import write_all


def main():

    print("ATON Markdown Renderer")
    print("======================")
    print()

    print("Loading Foundation...")

    model = load_foundation()

    print(f"Loaded {len(model.artifacts)} artifacts.")
    print()

    print("Rendering Markdown...")

    write_all(model)

    print()
    print("Done.")


if __name__ == "__main__":
    main()
