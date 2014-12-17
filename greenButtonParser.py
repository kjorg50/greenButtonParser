#!/usr/bin/python
# Kyle Jorgensen, 16 Dec 2014
# A parser designed to take Green Button data from Southern California Edison, and then put it into a cleaner format
# for input into GSN (Global Sensor Networks)

import sys
import csv


def parseData(filename):
    f = open(filename, 'r', newline='')
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
    finally:
        f.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 greenButtonParser.py <green button csv file>\n")
    else:
        input_file = sys.argv[1]

        parseData(input_file)
