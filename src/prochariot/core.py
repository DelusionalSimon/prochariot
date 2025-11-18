"""
Core analysis logic for the proChariot package.

This module contains the main functions of the proChariot library
that perform the LLM-guided analysis of prokaryotic genomes
based on Bakta annotation files.

Functions included:
    Core Analysis Function:
        - analyze
    Core Components:
        - parse_bakta_tsv
    Helper Functions:        
        - _dbxrefs_to_dict
        - _df_to_json
"""
# -------------[ LIBRARIES ]-------------
from pathlib import Path
import pandas as pd
from groq import Groq
import os
import sys

# -------------[ INTERNAL CONSTANTS ]-------------
LLM_MODEL = "llama-3.3-70b-versatile"
ESSENTIAL_COLS = ['Sequence Id', 'Locus Tag', 'Gene', 'Product', 'DbXrefs']

# -------------[ HELPERS ]-------------
def _dbxrefs_to_dict(dbxrefs: str) -> dict:
    """
    Converts a DbXrefs string from a Bakta .tsv file into a dictionary.

    Parameters
    ----------
    dbxrefs : str
        The DbXrefs string from a Bakta .tsv file.

    Returns
    -------
    dict
        A dictionary representation of the DbXrefs.
    """
    dbxrefs_dict = {}

    # Handle missing values
    if pd.isna(dbxrefs):
        return dbxrefs_dict

    entries = dbxrefs.split(", ")
    for entry in entries:
        if ":" in entry:
            key, value = entry.split(":", 1)
            dbxrefs_dict[key] = value
    return dbxrefs_dict

def _df_to_json(df: pd.DataFrame) -> str:
    """
    Converts a Pandas DataFrame to a JSON-formatted string.

    This function ensures proper handling NaN values and
    prunes the data to make the json output fit within the
    token limits of the LLM. 

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to convert.

    Returns
    -------
    str
        The JSON-formatted string representation of the DataFrame.
    """

    #TODO: The structure of the output JSON must be adjusted to fint within LLM token limits.
    # Look into orienting the JSON differently (e.g., 'split', 'table', etc.) to optimize size.
    # Consider summarizing or truncating more data.

    #TODO: This function may be revived for hallucination checking or more advanced JSON creation down the line

    # Replace all pandas 'NaN' with Python's 'None'
    df = df.replace({pd.NA: None})

    # Prune DataFrame to remove unnecessary columns
    df_pruned = df[ESSENTIAL_COLS]

    # Prune Dataframe to only keep named genes
    df_final = df_pruned[~df['Gene'].isna()]
    
    # Convert the DataFrame to a JSON string
    return df_final.to_json(orient="records")


def _call_groq_llm(prompt: str) -> str:
    """
    Calls the Groq API with a given prompt and returns the response.

    Parameters
    ----------
    prompt : str
        The prompt to send to the Groq API.

    Returns
    -------
    str
        The response from the Groq API.
    """
    
    # Retrieve the API key from environment variables
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        # This is the correct place for this error
        raise ConnectionError(            
            "Please set your groq API key: 'export GROQ_API_KEY=your_key_here'"
        )   
    print("API Key found, initializing Groq client...")

        # Initialize the Groq client
    try:
        client = Groq(api_key=api_key)
    except Exception as e:
        # This will catch specific Groq API errors, authentication failures, etc.
        print(f"Error: Failed to initialize Groq client. Details: {e}")
        sys.exit(1)
    print("Groq client initialized.")

    # Send the prompt to the Groq API and get the response
    try:
        chat_completion = client.chat.completions.create(
            messages = [
                {"role": "user", "content": prompt}
            ],
            model = LLM_MODEL,
        )
    except Exception as e:
        print(f"Error: Failed to get response from Groq API. Details: {e}")
        sys.exit(1)

    # Return the content of the response    
    return chat_completion.choices[0].message.content


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

    # Clean up # from the colunm names
    df.columns = [col.lstrip("# ") for col in df.columns]

    # Parse the 'DbXrefs' column into a nested dictionary
    df['DbXrefs'] = df['DbXrefs'].apply(_dbxrefs_to_dict)

    return df

# -------------[ CORE ANALYZE FUNCTION ]-------------
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

    # Test pipeline
    df = parse_bakta_tsv(TSV_PATH)
    json_output = _df_to_json(df)
    
    # Check size of json output compared to df
    print(f"JSON output size: {len(json_output)} characters")
    print(f"DataFrame size: {len(str(df))} characters")

    # test LLM call
    print(_call_groq_llm(json_output))
    