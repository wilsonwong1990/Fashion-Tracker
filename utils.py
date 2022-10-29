"""
A module for some none specific website python functions. 

Author: Wilson Wong
Date: 10-29-2022
"""

import csv

def import_csv(filename):
    """
    Loads the CSV into a list for use later.

    parameter filename: A valid path and csv for a specific store.
    Precondition: a csv file
    """
    result = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            result.append(row)
    
    return result

def export_csv(list, filename):
    """
    Exports the list back into the CSV for storage.

    parameter list: a list to export to the filename

    parameter filename: A valid path and csv for a specific store.
    Precondition: a csv file
    """

    with open(filename, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')

        for row in list:
            csv_writer.writerow(row)
