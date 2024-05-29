# Markov Story Generator

This mini-project was developed by me during the CSN14403 (Introduction to Artificial Intelligence) course at MNNIT, using the knowledge about the Markov Models and how they can be used to make a very basic story generator
that helped me explore the realm of NLP (Natural Language Processing). This model was trained on the kaggle's sci-fi stories dataset and relies on keyword identification to generate a markov chain based story. 

[Link To DataSet](https://www.kaggle.com/datasets/jannesklaas/scifi-stories-text-corpus)

# Project Setup
1. Clone The Project
`git clone https://github.com/aviral-mishra-1008/markov_story_generator`
2. Run makeModel.py and it will generate a markov model, here you need to ensure your root directory has the above provided dataset, the model will get saved into root directory
3. Now on any fresh python file, model can be loaded by writing :
`from Models import Markov`
4. After initializing a class of markov type
`model = Markov()`
5. Load Saved Model
`model.load_model("path_to_saved_model")`
6. Generate Story
`story = model.generate_story(limit=<DESIRED LENGTH>, start=<KEYWORD>)`
7. This will generate a story of given size, starting with given keyword

Note: This is just a fun project to explore NLP domain, the stories may or may not be logical, its at the end of the day generating random words which aren't exactly random as some words are more likely to come together than other words, this in turn induces certain degree of sense in the stories generated but in long length this effect fades quickly giving way to vague and often montonous stories!
Explore, contribute and suggest changes!

# GOOD LUCK!
