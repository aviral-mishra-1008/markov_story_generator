from Story_dataset import *
from Models import Markov

#get_scifi()  #To Download the dataset for training, downloads the set to roo directory

processedText = Markov.processText()
model = Markov.train(processedText)
model.save()

