# Tolino Vocab Extractor
Tolino Vocab Extractor is a python utility to extract highlighted words from Tolino e-reader notes for vocabulary building.

## Installation
To run this app you need python 3.14.5+

``` bash
    git clone https://github.com/YOUR_USERNAME/tolino-vocab-extractor.git
    cd tolino-vocab-extractor
```
## Note Format
This script expects the following note format:

```text
Title (Author)
Highlight on page <number>: "word"
Added on <date>
```

##  How to use

1. Copy your `notes.txt` file from Tolino device to the script directory.
2. Run the script:

```bash
python tovox.py notes.txt
```

New words will be printed to console and all words are save in words.txt file with following format:
```text
<current date>
<list of words in new line>
```

## Options
To clear your existing words.txt:

``` bash
python tovox.py notes.txt --clear
```
