from __future__ import division # floating point division
import collections
from doc_processor import *

# Options [with defaults]

guessing = {
  'assumed_probability': lambda feature, total_classifications: 1 / total_classifications if total_classifications else 0,
  'weight': 1
}

extract_features = lambda item: sanitized_words(item)

# Model

model = {}

model['features']        = {}
model['classifications'] = {}
model['samples']         = {}

# Methods

def train(item, classification):
  for feature in extract_features(item): add_sample(feature, classification)
  update_model(model, 'classifications', classification)
 
def add_sample(feature, classification):
  update_model(model, 'features',        feature)
  update_model(model, 'samples',         (feature, classification))

def update_model(model, key, value):
  if value in model[key]:
    model[key][value] += 1
  else:
    model[key][value] = 1

def normalize_probabilities(probabilities):
  total = sum(probabilities)
  if total == 0: return [0]
  return [probability / total for probability in probabilities]

def p_feature_given_classification(feature, classification):
  if (feature, classification) not in model['samples']: return 0
  return model['samples'][(feature, classification)] / model['classifications'][classification]

def weighted_p_feature_given_classification(feature, classification):
  count_feature = 0 if feature not in model['features'] else model['features'][feature]
  total_classifications = len(model['classifications'].keys())
  assumed_probability = guessing['assumed_probability'](feature, total_classifications)
  numerator   = guessing['weight'] * assumed_probability + count_feature * p_feature_given_classification(feature, classification)
  denominator = guessing['weight'] + count_feature
  if denominator == 0: return 0
  return numerator / denominator

def p_classification(classification):
  total_samples = sum(model['samples'].values())
  if not classification in model['classifications'] or total_samples == 0: return 0
  return model['classifications'][classification] / total_samples

def p_classification_given_features(classification, features):
  p = 1
  for feature in features: p *= weighted_p_feature_given_classification(feature, classification)
  return p * p_classification(classification)

def normalized_p_classification_given_features(classification, features):
  # TODO: Cache values for a speed boost
  classifications = [classification] + [c for c in model['classifications'].keys() if c != classification]
  probabilities = [p_classification_given_features(c, features) for c in classifications]
  return normalize_probabilities(probabilities)[0]

def classifications():
  return model['classifications'].keys()

def features():
  return model['features'].keys()

def probability(item, classification):
  features = extract_features(item)
  return normalized_p_classification_given_features(classification, features)

def classify(item):
  features = extract_features(item)
  classification_probabilities = [(classification, normalized_p_classification_given_features(classification, features)) for classification in model['classifications'].keys()]
  return max(classification_probabilities, key = lambda tup: tup[1])[0]