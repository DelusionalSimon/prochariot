"""
Core analysis logic for the proChariot package.

This module contains the main functions of the proChariot library.

Functions included:
    - analyze: Main function to perform LLM-guided analysis of prokaryotic genomes.
"""
# -------------[ LIBRARIES ]-------------
from pathlib import Path
import groq

# -------------[ HELPERS ]-------------

# Section for future _helper() functions

# -------------[ CORE COMPONENTS ]-------------
def parse_bakta_tsv(tsv_file: Path) -> list[dict]
    """
    Parses a Bakta .tsv file into a clean list of dictionaries.

    This function is publicly available. It parses the main columns
    and unnests the 'DbXrefs' column into a nested dictionary.

    Parameters
    ----------
    tsv_file : Path
        The path object pointing to the Bakta .tsv file.

    Returns
    -------
    list[dict]
        A list of dictionaries, where each dict is a processed feature.
    """
    pass

# -------------[ CORE FUNCTION ]-------------
def analyze(input_directory: str, output_directory: str | None = ".", species: str | None = None, note: str | None = None) -> str:
    """
    Performs an LLM-guided analysis of a Bakta output directory.

    This is the main function for the proChariot library. It locates the 
    annotation files, builds a core prompt, and uses an LLM to generate
    a summary report that is saved to a specified location as a JSON file.

    Parameters
    ----------
    input_directory : str
        Path to the Bakta/Prokka output directory.
    output_directory : str
        Path to save the final analysis report.
        Defaults to the current working directory.
    species : str, optional
        The name of the species (e.g., "Enterococcus faecium").
        Defaults to None.
    note : str, optional
        A short note for context (e.g., "Clinical isolate").
        Defaults to None.

    Returns
    -------
    str
        The JSON-formatted analysis report.

    """
    #TODO: Implement function logic
    pass

