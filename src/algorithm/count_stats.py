def stat_counter(sequence_infos):
    counts = []
    for alignment_infos in sequence_infos:
        print("\tStart count of " + alignment_infos[0] + "-file")
        count = []
        seqs_1 = alignment_infos[3]
        seqs_2 = alignment_infos[4]
        sorted_pos_seq2 = sorted(alignment_infos[6])
        if len(seqs_1) == len(seqs_2):
            total_ins = 0
            total_dels = 0
            total_mism = 0
            total_inv = 0
            total_translocs = 0
            total_len = 0
            for i in range(0, len(seqs_1)):
                ins = 0
                dels = 0
                mism = 0
                inv = []
                transloc = False
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

                    if i != len(seqs_1) - 1:
                        current_sorted_pos_i = sorted_pos_seq2.index(alignment_infos[6][i])
                        next_sorted_pos_i = sorted_pos_seq2.index(alignment_infos[6][i + 1])
                        if current_sorted_pos_i == len(sorted_pos_seq2) - 1:
                            if next_sorted_pos_i != 0:
                                transloc = True
                                total_translocs += 1
                        else:
                            if current_sorted_pos_i > next_sorted_pos_i:
                                transloc = True
                                total_translocs += 1
                        # print(current_sorted_pos_i, next_sorted_pos_i, transloc, total_translocs)

                    inv = all(inv)
                    total_ins += ins
                    total_dels += dels
                    total_mism += mism
                    total_inv += 1 if inv else 0
                    total_len += xlen
                    count.append([ins, dels, mism, inv, transloc, xlen])
                else:
                    print("\t\tError: The contained sequences with ID = " + str(i + 1) +
                          " of " + str(len(seqs_1)) + ", though assumed to be aligned, do not have the same length.")
            count.append([total_ins, total_dels, total_mism, total_inv, total_translocs, total_len])
            counts.append(count)
        else:
            print("\t\tNumber of blocks for sequence 1 and sequence 2 are not equal."
                          "Please check input, and revise code.")
            counts.append([])
    return counts
