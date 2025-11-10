"""
Core analysis logic for the proChariot package.

This module contains the main functions of the proChariot library.

Functions included:
    - analyze: Main function to perform LLM-guided analysis of prokaryotic genomes.
"""
# -------------[ LIBRARIES ]-------------
import groq


# -------------[ FUNCTIONS ]-------------
def analyze(input_directory: str, output_directory: str = ".", species: str | None = None, note: str | None = None) -> str:
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
        The path to the final analysis report.

    """
    #TODO: Implement function logic
    #TODO: output json
    pass

