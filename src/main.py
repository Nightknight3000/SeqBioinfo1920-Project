import click
import sys

from src.io.parse_mauve_alignment import parse_mauve_output
from src.io.parse_mumer_maf import parse_mumer_output
from src.algorithm.count_stats import stat_counter
from src.io.write_statistics import write_stats
from src.io.write_fasta import write_collected_fasta
from src.io.write_circos_input import write_cyclic_alignment_table

__author__ = "Nantia Leonidou, Florian Riedl, Alexander Röhl"


@click.command()
@click.argument("input-paths", nargs=-1, type=str)
@click.option("-cf/-nf", "--collect-fastas/--not-collect-fastas", default=False, help="Use \'-cf\' to collect fasta files from alignments")
def main(input_paths, collect_fastas):
    print("Running Project Tasks")
    print("Authors: ", __author__, '\n')
    if not input_paths:
        input_paths = ("data/mauve/WGA_Ref1_Assembly/wga_ref1.alignment",
                       "data/mauve/WGA_Ref2_Assembly/wga_ref2.alignment",
                       "data/MUMmer/NC_002695/out.maf",
                       "data/MUMmer/NC_004431/out.maf")

    if check_commandline(input_paths, collect_fastas):
        sequence_infos = []
        print("Parse wga files.")
        for input_path in input_paths:
            if input_path.split('.')[-1] == "alignment":
                sequence_infos.append(parse_mauve_output(input_path))
            else:
                sequence_infos.append(parse_mumer_output(input_path))
            print(f"\tParsed {sequence_infos[-1][0]}-file containing {len(sequence_infos[-1][3])} subalignments.")
        print("Compute counts for insertions, deletions, and mismatches.")
        counts = stat_counter(sequence_infos)
        print("Write counts as csv-file.")
        write_stats(sequence_infos, counts)
        if collect_fastas:
            print("Write collected alignment sequences as fasta-files.")
            write_collected_fasta(sequence_infos)
        print("Write cyclic alignment table")
        write_cyclic_alignment_table(sequence_infos)
    print("Exit")
    sys.exit()


def check_commandline(input_paths, collect_fastas):
    if all([path.split('.')[-1] in ["alignment", "maf"] for path in input_paths]):
        print("All files of correct type.")
        if not collect_fastas:
            print("No fasta files will be collected.")
            return True
        else:
            print("Fasta-files will be collected.")
            return True
    else:
        print("All inputs should be either alignment- or maf-files.")
    return False
