import sys

sp="#####"

def distinct_2(path):
    inFile = open(path, mode="r", encoding="utf8")
    biword_set = set()
    all_bigram_count = 0
    for line in inFile.readlines():
        line = line.strip().split(" ")
        word_len = len(line)
        for idx in range(word_len - 1):
            biword_set.add(line[idx] + sp + line[idx + 1])
        biword_set.add("<BOS>" + sp + line[0])
        biword_set.add(line[word_len - 1] + sp + "<EOS>")
        all_bigram_count += (word_len + 1)

    distinct_bigram_count = len(biword_set)
    print("distinct_bigram: ", distinct_bigram_count)
    print("all_bigram: ", all_bigram_count)
    print("distinct 1: " + str(distinct_bigram_count / all_bigram_count))
    inFile.close()

distinct_2(sys.argv[1])
