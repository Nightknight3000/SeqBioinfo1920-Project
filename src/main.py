import click
import sys

from src.io.parse_mauve_alignment import parse_mauve_output
from src.io.parse_mumer_maf import parse_mumer_output
from src.algorithm.count_stats import stat_counter

__author__ = "Nantia Leonidou, Florian Riedl, Alexander Röhl"


@click.command()
@click.option("-i", "--input-paths", nargs=4, type=str,
              default=("data/mauve/WGA1_Ref1_revCompl/wga1_revCompl_ref1.alignment",
                       "data/mauve/WGA2_Ref2_revCompl/wga2_revCompl_ref2.alignment",
                       "data/mumer/nc_002695/out.maf", "data/mumer/nc_004431/out.maf"), required=True)
# @click.option("-of", "--output-fastapaths", nargs=4, type=str,
#               default=("data/output/mauve_al1.fasta", "data/output/mauve_al2.fasta",
#                        "data/output/mumer_al1.fasta", "data/output/mumer_al2.fasta"))
@click.option("-of", "--collected-fastapaths", nargs=4, type=str, default="")
def main(input_paths, collected_fastapaths):
    print("Running Project Tasks")
    print("Authors: ", __author__, '\n')
    if check_commandline(input_paths, collected_fastapaths):
        print(input_paths)
        print(collected_fastapaths)
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
        stat_counter(sequence_infos)
    print("Exit")
    sys.exit()


def check_commandline(input_paths, collected_fastapaths):
    if all([path.split('.')[-1] in ["alignment", "maf"] for path in input_paths]):
        print("All files of correct type.")
        if not collected_fastapaths:
            print("No fasta files will be collected.")
            return True
        else:
            print("Fasta-files will be collected.")
            return True
    else:
        print("All inputs should be either alignment- or maf-files.")
    return False
