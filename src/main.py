import click
import sys

__author__ = "Nantia Leonidou, Florian Riedl, Alexander Röhl"


@click.command()
@click.option("-i", "--input-filepath", nargs=2, default="data")
@click.option("-fasta/-nfasta", "--collect-fastafile/--ncollect-fastafile", default=False)
@click.option("-of", "--output-fastapath", default='')
def main(input_filepath, collect_fastafile, output_fastapath):
    print("Running Project Tasks")
    print("Authors: ", __author__, '\n')
    if check_commandline(input_filepath, collect_fastafile, output_fastapath):
        print()
    print("Exit")
    sys.exit()


def check_commandline(input_filepath, collect_fastafile, output_fastapath):
    if (collect_fastafile and output_fastapath) or (not collect_fastafile):
        return True
    else:
        print("Error: If a fasta-file should be collected, please provide an outputpath.")
        return False
