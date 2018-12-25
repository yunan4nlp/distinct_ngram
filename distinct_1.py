import sys

def distinct_1(path):
    inFile = open(path, mode="r", encoding="utf8")
    word_set = set()
    all_unigram_count = 0
    for line in inFile.readlines():
        line = line.strip().split(" ")
        for word in line:
            all_unigram_count += 1
            word_set.add(word)
    distinct_unigram_count = len(word_set)
    print("distinct_unigram: ", distinct_unigram_count)
    print("all_unigram: ", all_unigram_count)
    print("distinct 1: " + str(distinct_unigram_count / all_unigram_count))
    inFile.close()


distinct_1(sys.argv[1])