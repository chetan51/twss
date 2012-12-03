import twss_classifier
reload(twss_classifier)
from twss_classifier import *

train('dataset/twss.txt', 'yes')
train('dataset/non_twss.txt', 'no')

classify("wow, that's a hard one!")
classify("the dogs ate the speakers")

classify_file('dataset/test_twss.txt', 'yes')
classify_file('dataset/test_non_twss.txt', 'no')
