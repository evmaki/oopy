""" This module implements three classes, described in the following.

Document: a superclass which defines the interface to documents
   JsonDocument: a subclass which implements document handling for json files
   CsvDocument:  a subclass which implements document handling for csv files
"""
import json, csv

class Document:
    def __init__(self, path: str):
        pass

    def append(self, content: dict):
        pass

    def save(self):
        pass

    def read(self):
        pass

class JsonDocument(Document):
    def __init__(self, path: str):
        with open(path) as fp:
            self.path = path
            self.doc = json.load(fp)

    def __str__(self) -> str:
        return str(self.doc)

    def append(self, content: dict):
        self.doc.append(content)

    def save(self):
        with open(self.path, 'w') as fp:
            json.dump(self.doc, fp)

    def read(self):
        for item in self.doc:
            yield item


class CsvDocument(Document):
    def __init__(self, path: str):
        with open(path) as fp:
            self.path = path
            self.doc = []

            for row in csv.reader(fp):
                self.doc.append(row)

    def __str__(self) -> str:
        return str(self.doc)

    def append(self, content: dict):
        # get the document header
        header = self.doc[0]

        # create an empty list that we can fill with values that are present in the dict
        row = ['' for _ in range(0, len(header))]

        # for each column, value pair in the passed dict, fill in the blanks in the row
        for col, val in content.items():
            row[header.index(col)] = val
        
        # append the row to the doc
        self.doc.append(row)

    def save(self):
        with open(self.path, 'w') as fp:
            writer = csv.writer(fp)

            for row in self.doc:
                writer.writerow(row)

    def read(self):
        for item in self.doc:
            yield item