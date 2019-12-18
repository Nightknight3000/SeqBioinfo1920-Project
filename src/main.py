import click
import sys

from src.io.parse_mauve_alignment import parse_mauve_output
from src.io.parse_mumer_maf import parse_mumer_output
from src.algorithm.count_stats import stat_counter
from src.io.write_statistics import write_stats
from src.io.write_fasta import write_collected_fasta

__author__ = "Nantia Leonidou, Florian Riedl, Alexander Röhl"


@click.command()
@click.option("-i", "--input-paths", nargs=4, type=str,
              default=("data/mauve/WGA1_Ref1_revCompl/wga1_revCompl_ref1.alignment",
                       "data/mauve/WGA2_Ref2_revCompl/wga2_revCompl_ref2.alignment",
                       "data/MUMmer/NC_002695/out.maf", "data/MUMmer/NC_004431/out.maf"), required=True)
@click.option("-cf/-nf", "--collect-fastas/--dont-collect-fastas", default=False)
def main(input_paths, collect_fastas):
    print("Running Project Tasks")
    print("Authors: ", __author__, '\n')
    if check_commandline(input_paths, collect_fastas):
        sequence_infos = []
        for input_path in input_paths:
            if input_path.split('.')[-1] == "alignment":
                sequence_infos.append(parse_mauve_output(input_path))
            else:
                sequence_infos.append(parse_mumer_output(input_path))
        # for alignment_infos in sequence_infos:
        #     for i in range(0, len(alignment_infos)):
        #         alignment_info = alignment_infos[i]
        #         if i not in [3, 4]:
        #             print(alignment_info)
        #         else:
        #             sumlen = 0
        #             for alignment_i in alignment_info:
        #                 sumlen += len(alignment_i)
        #             print('', len(alignment_info))
        #             print('', '', sumlen)
        #     print()
        print("Compute counts for insertions, deletions, and mismatches.")
        counts = stat_counter(sequence_infos)
        print("Write counts as csv-file.")
        write_stats(sequence_infos, counts)
        if collect_fastas:
            print("Write collected alignment sequences as fastas.")
            write_collected_fasta(sequence_infos)
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
