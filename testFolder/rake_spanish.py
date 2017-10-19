from __future__ import absolute_import
from __future__ import print_function
__author__ = 'a_medelyan'
import rake

# EXAMPLE: Extracting single words from a French text

# spanish stopwords
stoppath = "SpanishStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file and setting phrase length in words to 1
rake_object = rake.Rake(stoppath, 5, 1, 4)

# 2. run on RAKE on a given text
sample_file = open("data/docs/spanish/text.txt", 'r')
text = sample_file.read()
keywords = rake_object.run(text)

# 3. print results
print("Keywords:", keywords)
