"""
Core analysis logic for the proChariot package.

This module contains the main functions of the proChariot library.

Functions included:
    - analyze: Main function to perform LLM-guided analysis of prokaryotic genomes.
"""
# -------------[ LIBRARIES ]-------------
from pathlib import Path
import pandas as pd
import groq

# -------------[ HELPERS ]-------------

# Section for future _helper() functions

# -------------[ CORE COMPONENTS ]-------------
def parse_bakta_tsv(tsv_file: Path) -> pd.DataFrame:
    """
    Parses a Bakta .tsv file into a clean Pandas DataFrame.

    This function is publicly available. It parses the main columns
    and unnests the 'DbXrefs' column into a nested dictionary.

    Parameters
    ----------
    tsv_file : Path
        The path object pointing to the Bakta .tsv file.

    Returns
    -------
    pd.DataFrame
        A Pandas DataFrame containing the parsed data.
    """
   
    # Read the TSV file into a DataFrame
    # Skipping the first 5 metadata rows
    df = pd.read_csv(tsv_file, sep="\t", header=5) 

    return df

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


# -------------[ TESTING HARNESS ]-------------
if __name__ == "__main__":

    # Testing constants
    TSV_PATH = Path("../../test_data/st177_vre_bakta/assembly.tsv")

    # Test the parse_bakta_tsv function
    df = parse_bakta_tsv(TSV_PATH)
    print(df.head())