def parse_mauve_output(alignment_path):
    file_content = open(alignment_path, 'r').read().split('\n')
    # alignment_infos structure:
    # [str("mumer"), str(name of seq_1), str(name of seq2), str_lst(seqs of seq_1),
    #  str_lst(seqs of seq_2), int_lst(startpos of seqs in seq_1), int_lst(startpos of seqs in seq_1)]
    # here: startposition (= index)
    alignment_infos = ["mauve", '', '', [], [], [], []]
    current = 0
    for i in range(0, len(file_content)):
        line = file_content[i]
        infoline_indicators = ['#', '>', '=']
        if line.startswith("#Sequence1File"):
            alignment_infos[1] = line.split(' ')[-1].split('\\')[-1].split('.')[0]
        elif line.startswith("#Sequence2File"):
            alignment_infos[2] = line.split(' ')[-1].split('\\')[-1].split('.')[0]

        if line and line[0] not in infoline_indicators:
            if file_content[i - 1][0] in infoline_indicators:
                if file_content[i - 1].startswith("> 1"):
                    alignment_infos[3].append(line)
                    alignment_infos[5].append(int(file_content[i - 1].split(':')[1].split('-')[0]))
                    current = 1
                elif file_content[i - 1].startswith("> 2"):
                    alignment_infos[4].append(line)
                    alignment_infos[6].append(int(file_content[i - 1].split(':')[1].split('-')[0]))
                    current = 2
                else:
                    print("Error: This should not happen!")
                    return []
            else:
                alignment_infos[2 + current][-1] += line

    # isolate aligned blocks
    for i in range(0, len(alignment_infos[3])):
        seqs_1 = alignment_infos[3][i]
        seqs_2 = alignment_infos[4][i]
        if len(seqs_1) != len(seqs_2):
            alignment_infos[3] = alignment_infos[3][:i]
            alignment_infos[4] = alignment_infos[4][:i]
            alignment_infos[5] = alignment_infos[5][:i]
            alignment_infos[6] = alignment_infos[6][:i]
            break

    return alignment_infos
