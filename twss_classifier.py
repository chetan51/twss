import classifier
from doc_processor import *
import os
import pickle

model_path = "model.p"

def load():
  if os.path.exists(model_path):
    print "Loading model..."
    model = pickle.load(open(model_path, "rb"))
    classifier.load(model)
  else:
    print "Training model..."
    train('dataset/twss.txt', 'yes')
    train('dataset/non_twss.txt', 'no')
    model = classifier.model
    pickle.dump(model, open(model_path, "wb"))

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
