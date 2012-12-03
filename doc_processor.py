import re

def text(file_path):
  return open(file_path, 'r').read()

def lines(file_path):
  return open(file_path, 'r').readlines()

def words(string):
  return re.split('[^a-zA-Z0-9_\-\']+|[--]', string)

def lower(words):
  return map(lambda word: word.lower(), words)

def no_blanks(words):
  return filter(lambda word: len(word), words)

def sanitized_words(string):
  return no_blanks(lower(words(string)))
