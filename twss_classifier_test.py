import twss_classifier
reload(twss_classifier)

twss_classifier.load()

# print twss_classifier.classify("wow, that's a hard one!")
# print twss_classifier.classify("the dogs ate the speakers")

twss_classifier.classify_file('dataset/test_twss.txt', 'yes')
twss_classifier.classify_file('dataset/test_non_twss.txt', 'no')
