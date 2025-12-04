#!/usr/bin/env python3

"""Entry point for the Rewild Journal CLI.

This small wrapper exists so that students and instructors can simply run
`python rewild.py` from the project root, as described in the README.
"""

from cli.rewild_journal import main


if __name__ == "__main__":  # pragma: no cover - thin wrapper
  main()
