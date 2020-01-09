import pandas as pd


def write_cyclic_alignment_table(sequence_infos):
    for i in range(0, len(sequence_infos)):
        path = f"data/output/cyclic_alignment_table/circos_table_0{i + 1}.tsv"
        header = ["data", "data"]
        header.extend([i for i in range(len(sequence_infos[i][3]))])
        row_list = []
        col_labels = ["data", "data"]
        col_labels.extend([f"A{i}" for i in range(len(sequence_infos[i][3]))])
        row_list.append(col_labels)

        seq2_sort_list = [seq for start_pos, seq in sorted(zip(sequence_infos[i][6], sequence_infos[i][4]))]
        for y in range(0, len(seq2_sort_list)):
            line_lst = [len(seq2_sort_list) - 1 - y + len(sequence_infos[i][3]), f"B{y}"]
            len_val = len(seq2_sort_list[y])
            for x in range(0, len(sequence_infos[i][3])):
                if len_val == len(sequence_infos[i][3][x]):
                    line_lst.append(len_val)
                else:
                    line_lst.append(0)
            row_list.append(line_lst)
        data = pd.DataFrame(data=row_list, columns=header)
        data.to_csv(path, sep='\t', mode='w', index=False)
        print(f"\tWrote cyclic alignment from {sequence_infos[i][0]}-file.")
