import click
import sys


@click.command()
@click.option("-i", "--input-filepath", nargs=2, default="data")
@click.option("-fasta/-nfasta", "--collect-fastafile/--ncollect-fastafile", default=False)
@click.option("-of", "--output-fastapath", default='')
def main(input_filepath, collect_fastafile, output_fastapath):
    if check_commandline(input_filepath, collect_fastafile, output_fastapath):
        print()
    sys.exit()


def check_commandline(input_filepath, collect_fastafile, output_fastapath):
    if (collect_fastafile and output_fastapath) or (not collect_fastafile):
        return True
    else:
        print("Error: If a fasta-file should be collected, please provide an outputpath.")
        return False
