# coding: utf-8
import os
for file in os.scandir(dir):
    if file.is_file():
        print("file: " + file.name)
        validateJSONL(file, 3)
