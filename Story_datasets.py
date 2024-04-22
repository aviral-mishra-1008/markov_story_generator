#Fetch Dataset

'''
I thank Kaggle for providing an awesome databse on the topic of the sci-fi movies and articles for helping me and the community develop story generators and other nlp tasks
Link : https://www.kaggle.com/datasets/jannesklaas/scifi-stories-text-corpus
'''
import gdown

def get_scifi():
    file_id = '1IgllT89j3j0_pkp4xtcadRitk2Faq9N6'
    output_file = 'sciFi.zip'
    gdown.download(f'https://drive.google.com/uc?id={file_id}', output_file, quiet=False)

def get_Sherlock():
    raise NotImplementedError

def get_philosophy():
    raise NotImplementedError

