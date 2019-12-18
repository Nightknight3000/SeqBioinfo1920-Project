import os

from src.algorithm.extend_new_filepath_id import extend_new_filepath_by_copy_id


def write_stats(sequence_infos, counts):
    directory = "data/output/stats"
    # clear director, before filling with new results
    for file in os.listdir(directory):
        os.remove(directory + '/' + file)
    lines = ["Tool,Seq1,Seq2,Inputfile_ID,Insertions,Deletions,Mismatches,Is_Inverse,Total_Length"]

    if len(sequence_infos) == len(counts):
        for i in range(0, len(sequence_infos)):
            current_alignment = sequence_infos[i]
            current_alcount = counts[i]
            if current_alcount:
                for count in current_alcount:
                    line = [current_alignment[0], current_alignment[1], current_alignment[2], i]
                    line.extend(count)
                    if count == current_alcount[-1]:
                        line[0] += "_Total"
                    line = ','.join([str(element) for element in line])
                    lines.append(line)
                    if count == current_alcount[-1]:
                        lines.append('')
            else:
                print("Error: No counts were defined for this file. Cannot write.")

        new_filepath = directory + "/statistics.csv"
        new_file = open(extend_new_filepath_by_copy_id(new_filepath, directory), 'w')
        new_file.write('\n'.join(lines))
        print("CSV-file written")
        new_file.close()
    else:
        print("Error: This should not be possible (see write_statistics.py).")

