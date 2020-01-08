def parse_mumer_output(alignment_path):
    file_content = open(alignment_path, 'r').read().split('\n')
    # alignment_infos structure:
    # [str("mumer"), str(name of seq_1), str(name of seq2), str_lst(seqs of seq_1),
    #  str_lst(seqs of seq_2), int_lst(startpos of seqs in seq_1), int_lst(startpos of seqs in seq_1)]
    # here: startposition (= index + 1)
    alignment_infos = ["mumer", '', '', [], [], [], []]
    for i in range(0, len(file_content)):
        line = file_content[i]
        if line.startswith('s'):
            if not alignment_infos[1]:
                alignment_infos[1] = line.split(' ')[1]
            elif line.split(' ')[1][:6] == alignment_infos[1][:6]:
                alignment_infos[3].append(line.split(' ')[-1].upper())
                alignment_infos[5].append(int(line.split(' ')[2]) + 1)
            elif not alignment_infos[2]:
                alignment_infos[2] = line.split(' ')[1]
            elif line.split(' ')[1][:6] == alignment_infos[2][:6]:
                alignment_infos[4].append(line.split(' ')[-1].upper())
                alignment_infos[6].append(int(line.split(' ')[2]) + 1)
            else:
                print("Error: This should not happen!")
                return []

    return alignment_infos
