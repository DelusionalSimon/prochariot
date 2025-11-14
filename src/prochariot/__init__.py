"""
proChariot: An LLM-guided analysis tool for prokaryotic genomes.

This package can be run in the command line using the `prochariot` command 
or imported as a module to run its functions in Python scripts.
"""

# Import functions from the core module
from .core import analyze, parse_bakta_tsv

# This tells Python what to export when a user does 'from prochariot import *'
__all__ = ['analyze', 'parse_bakta_tsv']