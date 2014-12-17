#!/usr/bin/python
# Kyle Jorgensen, 16 Dec 2014
# A parser designed to take Green Button data from Southern California Edison, and then put it into a cleaner format
# for input into GSN (Global Sensor Networks)

import sys
import csv

NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def printHeader(outfile):
    f_out = open(outfile, 'w', newline='')
    writer = csv.writer(f_out)
    writer.writerow(["Time Period Start", "Time Period End", "Usage (Real energy in kilowatt-hours)", "Reading Quality"])


def parseData(infile, outfile):
    f_in = open(infile, 'r', newline='')
    reader = csv.reader(f_in)
    printHeader(outfile)

    try:
        for row in reader:
            if len(row[0]) > 0 and row[0][0] in NUMBERS:
                appendToFile(outfile, row)

    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(infile, reader.line_num, e))
    finally:
        f_in.close()


def appendToFile(filename, data):
    f_out = open(filename, 'a', newline='')
    writer = csv.writer(f_out)
    times = data[0].split("to")

    for i in range(len(times)):
        times[i] = times[i].strip()

        # check for weird unicode character that sometimes is included
        if times[i][-1] == "†":
            times[i] = times[i][:-1]

    writer.writerow([times[0], times[1], data[1], data[2]])
    f_out.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 greenButtonParser.py <green button csv file>\n")
    else:
        input_file = sys.argv[1]
        output_file = input_file.split('.')[0] + "_parsed.csv"

        parseData(input_file, output_file)

        print("Parsing complete! Output is in " + output_file)