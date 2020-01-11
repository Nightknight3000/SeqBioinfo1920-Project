import os

from src.algorithm.extend_new_filepath_id import extend_new_filepath_by_copy_id


def write_stats(sequence_infos, counts):
    directory = "data/output/stats"
    # clear director, before filling with new results
    for file in os.listdir(directory):
        os.remove(directory + '/' + file)
    lines = ["Tool,Seq1,Seq2,Inputfile_ID,start_pos1,start_pos2,Insertions,Deletions,Mismatches,Is_Inverse,Seq2_Is_Translocated,Total_Length"]

    if len(sequence_infos) == len(counts):
        for i in range(0, len(sequence_infos)):
            current_alignment = sequence_infos[i]
            current_alcount = counts[i]
            if current_alcount:
                for j in range(0, len(current_alcount)):
                    count = current_alcount[j]
                    line = [current_alignment[0], current_alignment[1], current_alignment[2], i]
                    if j != len(current_alcount) - 1:
                        line.extend([current_alignment[5][j], current_alignment[6][j]])
                    else:
                        line.extend([current_alignment[5][0], current_alignment[6][0]])
                    line.extend(count)
                    if count == current_alcount[-1]:
                        line[0] += "_Total"
                    line = ','.join([str(element) for element in line])
                    lines.append(line)
                    if count == current_alcount[-1]:
                        lines.append(',,,,,,,,')
            else:
                print("\t\tError: No counts were defined for this file. Cannot write.")

        new_filepath = directory + "/statistics.csv"
        new_file = open(extend_new_filepath_by_copy_id(new_filepath, directory), 'w')
        new_file.write('\n'.join(lines))
        print("\tWrote csv-file from all supplied files")
        new_file.close()
    else:
        print("\tError: This should not be possible (see write_statistics.py).")

