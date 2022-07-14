""" If your classes have been implemented according to the specifications, 
this file should run without errors.
"""
import FileChooser as FileChooser
from Document import *

jsondoc = FileChooser.open('./capitals.json')
assert isinstance(jsondoc, Document)    # jsondoc is an instance of a subclass of Document
assert type(jsondoc) is JsonDocument    # jsondoc is, more specifically, a JsonDocument

old_len = len(jsondoc.doc)              # keep track of the original document length
jsondoc.append({                        # append something
    'state': 'Texas',
    'capital': 'Austin'
})
new_len = len(jsondoc.doc)
assert new_len > old_len                # see if the append worked (i.e. made the document longer)
jsondoc.save()                          # save the doc
jsondoc = FileChooser.open('./capitals.json')
assert len(jsondoc.doc) == new_len      # see if the saved and reopened doc has the same length

# do it over again with the CsvDocument

csvdoc = FileChooser.open('./capitals.csv')
assert isinstance(csvdoc, Document)     # csvdoc is an instance of a subclass of Document
assert type(csvdoc) is CsvDocument      # csvdoc is, more specifically, a CsvDocument

old_len = len(csvdoc.doc)               # keep track of the original document length
csvdoc.append({                         # append something
    'state': 'Texas',
    'capital': 'Austin'
})
new_len = len(csvdoc.doc)
assert new_len > old_len                # see if the append worked (i.e. made the document longer)
csvdoc.save()                           # save the doc
csvdoc = FileChooser.open('./capitals.csv')
assert len(csvdoc.doc) == new_len       # see if the saved and reopened doc has the same length