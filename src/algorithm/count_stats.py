def stat_counter(sequence_infos):
    for alignment_infos in sequence_infos:
        seqs_1 = alignment_infos[3]
        seqs_2 = alignment_infos[4]
        print(len(seqs_1) == len(seqs_2))
    print()
