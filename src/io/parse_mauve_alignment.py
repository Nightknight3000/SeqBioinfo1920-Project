def parse_mauve_output(alignment_path):
    file_content = open(alignment_path, 'r').read()
    print(file_content.count("> 1"))
    print(file_content.count("> 2"))
    file_content = open(alignment_path, 'r').read().split('\n')
    alignment_infos = ["mauve", '', '', [], []]
    current = 0
    for i in range(0, len(file_content)):
        line = file_content[i]
        infoline_indicators = ['#', '>', '=']
        if line.startswith("#Sequence1File"):
            alignment_infos[1] = (line.split(' ')[-1])
        elif line.startswith("#Sequence2File"):
            alignment_infos[2] = (line.split(' ')[-1])

        if line and line[0] not in infoline_indicators:
            if file_content[i - 1][0] in infoline_indicators:
                if file_content[i - 1].startswith("> 1"):
                    alignment_infos[3].append(line)
                    current = 1
                elif file_content[i - 1].startswith("> 2"):
                    alignment_infos[4].append(line)
                    current = 2
                else:
                    print("Error: This should not happen!")
                    return []
            else:
                alignment_infos[2 + current][-1] += line

    return alignment_infos
