import os

from src.algorithm.extend_new_filepath_id import extend_new_filepath_by_copy_id


def write_collected_fasta(sequence_infos):
    directory = "data/output/fastas"
    # clear director, before filling with new results
    for file in os.listdir(directory):
        os.remove(directory + '/' + file)
    fasta_lineskip = 60

    for seq_info in sequence_infos:
        sequences = [[seq_info[1].split('\\')[-1], ''.join(seq_info[3])], [seq_info[2].split('\\')[-1], ''.join(seq_info[4])]]
        for seq in sequences:
            if not seq[0].endswith(".fasta"):
                seq[0] = seq[0] + ".fasta"
            new_filepath = directory + '/' + seq[0]
            fasta_file = open(extend_new_filepath_by_copy_id(new_filepath, directory), 'w')
            file_content = "> " + ''.join(seq[0].split('.')[:-1]) + '\n'
            file_content += '\n'.join([seq[1][i:i + fasta_lineskip] for i in range(0, len(seq[1]), fasta_lineskip)])
            fasta_file.write(file_content)
            print("FASTA-file written")
            fasta_file.close()
