# Using TextBlob, a Python library for processing text data
#from textBlob import TextBlob
import os
import math

TEXT_DIR = "documents_to_read"

def read_in_txt_files():
    doc_list = []
    
    for root, dirs, files in os.walk(TEXT_DIR):
        for name in files:
            file_path = os.path.join(root, name)
            if name.endswith(".txt"):
                print(">> Reading in ", name)
                
                this_file = ""
                with open(file_path, 'r', encoding="UTF-8") as file_to_read:
                    for line in file_to_read:
                        this_file += line.rstrip()
                doc_list.append(this_file)
                print("   Successfully added", name)
    return doc_list
            

def main():
    print("=" * 20)
    print("TF-IDF EXAMPLE")
    print("=" * 20)
    print("This program will automatically pull all .txt files from your documents_to_read folder and will report the top words in argument as well as their TF-IDF scores")
    print()
    print("Files must be (1) .txt and (2) UTF-8 encoded")
    print()
    
    doc_list = read_in_txt_files()
    
    

main()