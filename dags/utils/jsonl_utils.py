'''Module to check the validity and work with jsonl files.
This is needed because the json module can validate files
by itself, but struggles with large files and outputs
a lot of noise in the terminal.'''
import json

from fileinput import FileInput


def validate_jsonl(file, nbrOfCharsBefore=5, nbrOfCharsAfter=0, printLine=False):
    '''Iterates over the lines of a jsonl file and
    validates the line is correct. If it is not
    valid jsonl, it will print the number of errors
    and the characters that caused them.
    nbrOFChars -> chars to print before error chars
    => 5 is great for most cases'''

    with open(file, "r") as jsonlFile:
        count_errors = 0
        error_chars_set = set()
        for line_number, line in enumerate(jsonlFile, start=1):
            try:
                json.loads(line)
            except json.JSONDecodeError as e:
                if printLine is True:
                    print(f"Invalid JSON on line {line_number}")
                error_chars = line[e.pos-nbrOfCharsBefore:e.pos+nbrOfCharsAfter]
                count_errors += 1
                error_chars_set.add(error_chars)
                continue
        print(f"There are {count_errors} errors in .jsonl file: {file.name}")
        print(f"The errors were related to the characters: \n {error_chars_set}")
        return error_chars_set

def clean_jsonl(file):
    '''Cleans out the <doublequote> that makes
    the jsonl file unusable '''
    with FileInput(file, inplace=True) as jsonlFile:
        for line in jsonlFile:
            print(line.replace('\\\\"', ''), end='')
