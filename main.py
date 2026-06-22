import sys
import argparse


def read_words_file(cacheFile):
    cacheWords = []
    cacheFile.seek(0)
    for line in cacheFile:
        line = line.replace("\n", "")
        cacheWords.append(line)

    return cacheWords


def read_note_file(noteFile):
    noteWords = []
    for line in noteFile:
        i = line.find('\"')
        if (i != -1):
            i2 = line.find('\"', i+1)
            line = line[i+1:i2]
            noteWords.append(line)

    return noteWords


def get_new_words(noteFile, cacheFile):
    noteWords = read_note_file(noteFile)
    cacheWords = read_words_file(cacheFile)

    return set(noteWords) - set(cacheWords)


def print_new_words(noteFile, cacheFile):
    diff = get_new_words(noteFile, cacheFile)
    for a in diff:
        cacheFile.write(a + "\n")
        print(a)


def main():
    parser = argparse.ArgumentParser(
        prog="tolino-notes", description="Simple program that takes your highlights from tolino notes and save all new words to file and print it")
    parser.add_argument("filename")
    parser.add_argument("-c", "--clear", action="store_true",
                        help="clear words.txt file")
    args = parser.parse_args()

    if (args.clear):
        open("words.txt", "w").close()
        sys.exit(0)

    cacheFile = open("words.txt", "a+")
    noteFile = open(args.filename, "r")

    print_new_words(noteFile, cacheFile)

    noteFile.close()
    cacheFile.close()


main()
