import classifier
from doc_processor import *

def train(file_path, classification):
  for line in lines(file_path):
    classifier.train(line, classification)

def classify(item):
  return classifier.classify(item)

def probabilities(title):
  return [(classification, classifier.probability(title, classification)) for classification in classifier.classifications()]

def classify_file(file_path, expected_classification):
  failures = set()
  success_count = 0
  total_items = 0
  for line in lines(file_path):
    classification = classify(line)
    if classification == expected_classification: success_count += 1
    else: failures.add(line)
    total_items += 1
  
  print "Expected classification: " + expected_classification
  print "Success rate: " + str((100.0 * success_count) / total_items) + "%"
  print "Failures: "
  for failure in failures: print "\t" + failure
