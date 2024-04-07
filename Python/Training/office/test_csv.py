import sys
import os
import csv
 
def test_writer():
    print("\n\ntest_writer")
    with open('names.csv', 'w', newline='') as csv_file:
        header = ['first', 'last']
        writer = csv.DictWriter(csv_file, fieldnames=header)
        
        writer.writeheader()
        writer.writerow({'first': 'Jack', 'last': 'Hill'})
        writer.writerow({'first': 'James', 'last': 'Mitch'})

def test_reader():
    print("\n\ntest_reader")
    with open('names.csv', 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)

def test_reader_as_dict():
    print("\n\ntest_reader_as_dict")
    with open('names.csv', 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row)

if __name__ == '__main__':
    test_writer()
    test_reader()
    test_reader_as_dict()