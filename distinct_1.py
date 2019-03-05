import sys

def distinct_1(path):
    inFile = open(path, mode="r", encoding="utf8")
    char_set = set()
    all_unigram_count = 0
    for line in inFile.readlines():
        line = line.strip().split(" ")
        sent = ""
        for word in line:
            sent += word
        for char in sent:
            char_set.add(char)
        all_unigram_count += len(sent)
    distinct_unigram_count = len(char_set)
    print("distinct_unigram: ", distinct_unigram_count)
    print("all_unigram: ", all_unigram_count)
    print("distinct 1: " + str(distinct_unigram_count / all_unigram_count))
    inFile.close()


distinct_1(sys.argv[1])