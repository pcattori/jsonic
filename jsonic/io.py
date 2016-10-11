import collections
import json

def stream_file(f):
    '''TODO docstring'''
    for line in f:
        yield json.loads(line)

def write_file(records, f):
    '''TODO docstring'''
    for record in records:
        print(json.dumps(record), file=f)

def stream_filepath(filepath, encoding='utf8'):
    '''TODO docstring'''
    with open(filepath, 'r', encoding=encoding) as f:
        for record in stream_file(f):
            yield record

def write_filepath(records, filepath, encoding='utf8'):
    '''TODO docstring'''
    with open(filepath, 'w', encoding=encoding) as f:
        write_file(records, f)

