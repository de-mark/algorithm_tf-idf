# Using TextBlob, a Python library for processing text data
from textblob import TextBlob
import os
import re
import math

TEXT_DIR = "documents_to_read"

def read_in_txt_files():
    # Blob is going to be a TextBlob version of the orginal .txt file
    blob_list = []
    name_list = []
    
    for root, dirs, files in os.walk(TEXT_DIR):
        for name in files:
            file_path = os.path.join(root, name)
            if name.endswith(".txt"):
                print(">> Reading in ", name)
                
                this_file = ""
                with open(file_path, 'r', encoding="UTF-8") as file_to_read:
                    for line in file_to_read:
                        this_file += line.rstrip().upper()
                blob_list.append(TextBlob(re.sub(r'[^\w\s]', '', this_file)))
                name_list.append(name)
                print("   Successfully added", name)
    return blob_list, name_list
           
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

# To combine [[word,imp]] with an overall dictionary
def merge_dict(dict1, dict2):
    for key, val in dict2:
        if key in dict1:
            dict1[key] += val
        else:
            dict1[key] = val


# Main program; runs at startup
def main():
    print("=" * 20)
    print("TF-IDF EXAMPLE")
    print("=" * 20)
    print("This program will automatically pull all .txt files from your documents_to_read folder and will report the top words in argument as well as their TF-IDF scores")
    print()
    print("Files must be (1) .txt and (2) UTF-8 encoded")
    print()
    
    # Once again, this is referred to as a blob instead of a document
    # since it's just a TextBlob version of the original .txt
    blob_list, name_list = read_in_txt_files()
    all_scores = {}
    
    for i, blob in enumerate(blob_list):
        print(f">> READING DOCUMENT: {name_list[i]}")
        scores = {word: tf_idf(word, blob, blob_list) for word in blob.words}
        words_sorted_best = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        words_sorted_worst = sorted(scores.items(), key=lambda x: x[1], reverse=False)
        
        print("    Top words:")
        for word, score in words_sorted_best[:10]:
            print(f"\t{word}: {score:.5f}")
        
        print()
        
        print("    Filtered words:")
        for word, score in words_sorted_worst[:10]:
            print(f"\t{word}: {score:.5f}")
        
        print()
        
        merge_dict(all_scores, words_sorted_best)
    
    print("=" * 20)
    
    all_scores = sorted(all_scores.items(), key=lambda x: x[1], reverse=True)
    print("OVERALL TOP WORDS:")
    
    for word, score in all_scores[:20]:
            print(f"\t{word}: {score:.5f}")
    

main()