import sys
import argparse
import datetime


def read_words_file(wordsFile):
    try:
        with open(wordsFile, "r") as file:
            return {line.strip() for line in file}
    except FileNotFoundError:
        return set()


def read_note_file(noteFile):
    noteWords = []
    with open(noteFile, "r", encoding="utf-8") as file:
        for line in file:
            words = line.split('"')
            if len(words) >= 3:
                word = words[1].strip()
                if word:
                    noteWords.append(word)

    return noteWords


def get_new_words(noteFile, cacheFile):
    noteWords = read_note_file(noteFile)
    cacheWords = read_words_file(cacheFile)
    newWords = []

    for word in noteWords:
        if word not in cacheWords:
            newWords.append(word)
            cacheWords.add(word)

    return newWords


def main():
    parser = argparse.ArgumentParser(
        prog="tolino-notes",
        description="Extract new highlighted words and append them to words.txt"
    )
    parser.add_argument("filename")
    parser.add_argument("-c", "--clear", action="store_true",
                        help="clear words.txt file")
    args = parser.parse_args()

    wordsFilename = "words.txt"

    if args.clear:
        open("words.txt", "w").close()
        sys.exit(0)

    new_words = get_new_words(args.filename, wordsFilename)

    if new_words:
        with open(wordsFilename, "a") as file:
            now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            file.write(now + '\n')
            for word in new_words:
                file.write(word + '\n')
                print(word)


if __name__ == "__main__":
    main()
