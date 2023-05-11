# Using TextBlob, a Python library for processing text data
#from textBlob import TextBlob
import os
import math

TEXT_DIR = "documents_to_read"

def read_in_txt_files():
    # Blob is going to be an unformatted / no space String version of the orginal .txt file
    blob_list = []
    
    for root, dirs, files in os.walk(TEXT_DIR):
        for name in files:
            file_path = os.path.join(root, name)
            if name.endswith(".txt"):
                print(">> Reading in ", name)
                
                this_file = ""
                with open(file_path, 'r', encoding="UTF-8") as file_to_read:
                    for line in file_to_read:
                        this_file += line.rstrip()
                blob_list.append(this_file)
                print("   Successfully added", name)
    return blob_list
           
# Creates the TF score for TF-IDF
# TF awards higher scores to words that have a higher frequency in the current document           
def tf(word, blob):
    return blob.words.count(word) / len(blob.words) 

# Used by IDF to figure out how many of the provided documents have
# this particular word
def n_documents_containing_word(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

# IDF checks to see how many of the documents have this word to ensure
# words like 'and' or 'the' are not given disproportionate importance
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_documents_containing_word(word, bloblist)))

# Uses TF and IDF to generate the TF-IDF
def tf_idf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

def main():
    print("=" * 20)
    print("TF-IDF EXAMPLE")
    print("=" * 20)
    print("This program will automatically pull all .txt files from your documents_to_read folder and will report the top words in argument as well as their TF-IDF scores")
    print()
    print("Files must be (1) .txt and (2) UTF-8 encoded")
    print()
    
    # Once again, this is referred to as a blob instead of a document
    # since it's just a string version of the original .txt
    blob_list = read_in_txt_files()
    
    

main()