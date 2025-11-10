"""
Command-Line Interface (CLI) for the proChariot package.

This module provides the main command-line entry point for running
the proChariot analysis. It uses 'click' to parse user arguments
and pass them to the core analysis functions.
"""

# -------------[ LIBRARIES ]-------------
import click
import json
import sys
from .core import analyze  

# -------------[ COMMANDS ]-------------
@click.command()
@click.version_option(version="0.1.0", prog_name="proChariot")
@click.option(
    '-i', '--input-dir',
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True),
    required=True,
    help='Path to the Bakta output directory.'
)
@click.option(
    '-s', '--species',
    type=str,
    default=None,
    help='(Optional) Name of the species (e.g., "Enterococcus faecium").'
)
@click.option(
    '-n', '--note',
    type=str,
    default=None,
    help='(Optional) A short note for context (e.g., "Clinical isolate").'
)


# -------------[ MAIN ]-------------
def main(input_dir: str, species: str | None = None, note: str | None = None) -> None:
    """
    proChariot: An LLM-guided analysis tool for prokaryotic genomes.

    This command reads annotation files from an input directory,
    builds a query, and uses an LLM to generate a structured
    analysis report in JSON format.

    Examples
    --------
    ### Basic run, print to screen
    $ prochariot -i /path/to/bakta/

    ### Save output to a file
    $ prochariot -i /data/run1/ -s "K. pneumoniae" > report.json

    ### Pretty-print to screen by piping into the built-in json.tool
    $ prochariot -i /data/run3/ -s "E. coli" -n "found in oceanic sample" | python -m json.tool

    ### Use in a pipeline with jq to parse all features on the first contig
    $ prochariot -i efaceum/bakta/ -s "E. faecium" -n "Clinical isolate from a blood sample" | jq .contigs[0].features
    """
    
    # Print starting message to stderr
    click.echo(f"[proChariot] Starting analysis on: {input_dir}", err=True)
    
    try:
        # Call analyze() without the output_directory argument.
        # It will default to None.
        report_data = analyze(
            input_directory=input_dir,
            species=species,
            note=note
        )
        
        # Print the final JSON data to standard output (stdout)
        click.echo(json.dumps(report_data, indent=2))
        
    except Exception as e:
        click.echo(f"[proChariot] Error: {e}", err=True)
        sys.exit(1)


# -------------[ ENTRY POINT ]-------------
if __name__ == "__main__":
    main()