def parse_mumer_output(alignment_path):
    file_content = open(alignment_path, 'r').read().split('\n')
    alignment_infos = ["mumer", '', '', [], []]
    for i in range(0, len(file_content)):
        line = file_content[i]
        if line.startswith('s'):
            if not alignment_infos[1]:
                alignment_infos[1] = line.split(' ')[1]
            elif line.split(' ')[1][:6] == alignment_infos[1][:6]:
                alignment_infos[3].append(line.split(' ')[-1].upper())
            elif not alignment_infos[2]:
                alignment_infos[2] = line.split(' ')[1]
            elif line.split(' ')[1][:6] == alignment_infos[2][:6]:
                alignment_infos[4].append(line.split(' ')[-1].upper())
            else:
                print("Error: This should not happen!")
                return []
    return alignment_infos
