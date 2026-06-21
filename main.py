import sys
from optparse import OptionParser


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


usage = "usage: %prog [options] <FILE>"
parser = OptionParser(usage)
parser.add_option("-c", "--clear", action="store_true",
                  help="clear words")

(options, args) = parser.parse_args()


if (options.clear):
    open("words.txt", "w").close()
    sys.exit(0)

cacheFile = open("words.txt", "a+")
noteFile = open(sys.argv[len(sys.argv) - 1], "r")

print_new_words(noteFile, cacheFile)


noteFile.close()
cacheFile.close()
