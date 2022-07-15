""" TODO This module implements three classes, described in the following.

Document: a superclass which defines the interface to documents
   JsonDocument: a subclass which implements document handling for json files
   CsvDocument:  a subclass which implements document handling for csv files
"""
class Document():
   def __init__(self, path: str):
      pass

   def __str__(self):
      pass

   def append(self, item: dict):
      pass

   def save(self):
      pass

   def read(self):
      pass

import json

class JsonDocument(Document):
   def __init__(self, path: str):
      with open(path) as fp:
         self.path = path
         self.doc = json.load(fp)

   def __str__(self):
      return str(self.doc)

   def append(self, item: dict):
      self.doc.append(item)

   def save(self):
      with open(self.path, 'w') as fp:
         json.dump(self.doc, fp)

   def read(self):
      pass

import csv

class CsvDocument(Document):
   def __init__(self, path: str):
      with open(path) as fp:
         self.path = path
         self.doc = []

         for row in csv.reader(fp):
            self.doc.append(row)

   def __str__(self):
      return str(self.doc)

   def append(self, item: dict):
      # { 'state': 'TX', 'capital': 'Austin' }
      # ['TX', 'Austin']
      self.doc.append(list(item.values()))

   def save(self):
      with open(self.path, 'w') as fp:
         writer = csv.writer(fp)

         for row in self.doc:
            writer.writerow(row)

   def read(self):
      pass


# jsondoc = JsonDocument('./capitals.json')
# print(jsondoc)
# jsondoc.append({'state': 'Texas', 'capital': 'Austin'})
# jsondoc.save()

# csvdoc = CsvDocument('./capitals.csv')
# csvdoc.append({ 'state': 'TX', 'capital': 'Austin' })
# print(csvdoc)
# csvdoc.save()