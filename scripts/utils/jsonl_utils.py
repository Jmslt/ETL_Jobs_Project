'''Module to check the validity and work with jsonl files.
This is needed because the json module can validate files
by itself, but struggles with large files and outputs
a lot of noise in the terminal.'''
import json


def validateJSON(file, nbrOfChars):
    '''Iterates over the lines of a jsonl file and
    validates the line is correct. If it is not
    valid jsonl, it will print the number of errors
    and the characters that caused them.
    nbrOFChars -> chars to print before error chars
    => 10 is great for most cases'''

    with open(file, "r") as jsonlFile:
        countErrors = 0
        errorCharsSet = set()
        for line_number, line in enumerate(jsonlFile, start=1):
            try:
                json.loads(line)
            except json.JSONDecodeError as e:
#                print(f"Invalid JSON on line {line_number}")
#                print(f"Error: {e.msg}")
#                print(f"Position: {e.pos}")
                errorCharsStr = line[e.pos-nbrOfChars:e.pos]
                countErrors += 1
                errorCharsSet.add(errorCharsStr)
#               print(f"Error characters: {errorCharsStr}")
                continue
        print(f"There are {countErrors} errors in jsonl file ")
        print(f"The errors were related to the characters: \n")
        return errorCharsSet
