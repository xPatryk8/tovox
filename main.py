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


def print_all(noteFile, cacheFile):
    noteWords = read_note_file(noteFile)

    for w in noteWords:
        print(w)

    diff = get_new_words(noteFile, cacheFile)
    for a in diff:
        cacheFile.write(a + "\n")


def print_new(noteFile, cacheFile):
    diff = get_new_words(noteFile, cacheFile)
    for a in diff:
        cacheFile.write(a + "\n")
        print(a)


def save_to(noteFile, cachedFile, saveFileName):
    saveFile = open(saveFileName, "w")
    diff = get_new_words(noteFile, cacheFile)

    for w in diff:
        saveFile.write(w + "\n")


usage = "usage: %prog [options] <FILE>"
parser = OptionParser(usage)
parser.add_option("-a", "--all", action="store_true",
                  help="print all words in file")
parser.add_option("-s", "--save",  metavar="<FILE1>",
                  help="save new words to <FILE1>")
parser.add_option("-c", "--clear", action="store_true",
                  help="clear cached words")

(options, args) = parser.parse_args()


if (options.clear):
    open("words", "w").close()
    sys.exit(0)

cacheFile = open("words", "a+")
noteFile = open(sys.argv[len(sys.argv) - 1], "r")

if (options.all):
    print_all(noteFile, cacheFile)
if (options.save):
    save_to(noteFile, cacheFile, options.save)
else:
    print_new(noteFile, cacheFile)


noteFile.close()
cacheFile.close()
