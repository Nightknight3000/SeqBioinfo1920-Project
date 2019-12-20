def stat_counter(sequence_infos):
    counts = []
    for alignment_infos in sequence_infos:
        print('', "Start count of " + alignment_infos[0] + "-file")
        count = []
        seqs_1 = alignment_infos[3]
        seqs_2 = alignment_infos[4]
        if len(seqs_1) == len(seqs_2):
            total_ins = 0
            total_dels = 0
            total_mism = 0
            total_inv = 0
            total_len = 0
            for i in range(0, len(seqs_1)):
                ins = 0
                dels = 0
                mism = 0
                inv = []
                xlen = len(seqs_1[i])
                if len(seqs_1[i]) == len(seqs_2[i]):
                    for j in range(0, len(seqs_1[i])):
                        c1 = seqs_1[i][j]
                        c2 = seqs_2[i][j]
                        rc2 = seqs_2[i][len(seqs_2[i]) - 1 - j]
                        if c1 == '-':
                            ins += 1
                        elif c2 == '-':
                            dels += 1
                        elif c1 != c2:
                            mism += 1
                        if c1 == rc2:
                            inv.append(True)
                        else:
                            inv.append(False)
                    inv = all(inv)
                    total_ins += ins
                    total_dels += dels
                    total_mism += mism
                    total_inv += 1 if inv else 0
                    total_len += xlen
                    count.append([ins, dels, mism, inv, xlen])
                else:
                    print('', '', "Error: The contained sequences with ID = " + str(i + 1) +
                          " of " + str(len(seqs_1)) + ", though assumed to be aligned, do not have the same length.")
            count.append([total_ins, total_dels, total_mism, total_inv, total_len])
            counts.append(count)
        else:
            print('', '', "Number of blocks for sequence 1 and sequence 2 are not equal."
                          "Please check input, and revise code.")
            counts.append([])
    return counts
