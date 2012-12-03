import twss_classifier
from doc_processor import *
reload(twss_classifier)

def classify_file(file_path, expected_classification):
  failures = set()
  success_count = 0
  total_items = 0
  for line in lines(file_path):
    classification = twss_classifier.classify(line)
    if classification == expected_classification: success_count += 1
    else: failures.add(line)
    total_items += 1
  
  print "Expected classification: " + expected_classification
  print "Success rate: " + str((100.0 * success_count) / total_items) + "%"
  print "Failures: "
  for failure in failures: print "\t" + failure

## Main test
twss_classifier.load()

# print twss_classifier.classify("wow, that's a hard one!")
# print twss_classifier.classify("the dogs ate the speakers")

classify_file('dataset/test_twss.txt', 'yes')
classify_file('dataset/test_non_twss.txt', 'no')
