import sys
import re

if __name__== "__main__":

    path = sys.argv[1]    #for getting filename as argument
    f = open(path,"r")
    in_sent = sys.argv[2]
    
    #splitting sentence from the given data text file by stripping the trailing spaces

    corpus_Sentences = f.read().strip().split("\n")             #Step 1

    tokens_All = [];
    for sente in corpus_Sentences:
        token_sent = sente.strip().split(" ")                   #dividing by space first
        for x in token_sent:
            temp = x.strip().split("_")[0].lower()
            tokens_All.append(temp)                             #Step 2
    
    #print(tokens_All)                                           #Got all the token words from the given text file

    #to get vocabulary we need to eliminate the duplicates

    vocab_All = []

    for i in tokens_All: 
        if i not in vocab_All: 
            vocab_All.append(i)
 
    #print(vocab_All);                                         #Got all the vocabulary

    #print(len(tokens_All));                                   #count of tokens is 68737
    #print(len(vocab_All));                                    #count is vocabulary is 7602


    #Generating Unigrams

    dict_count_Unigrams = {}

    for w in tokens_All:
        if w not in dict_count_Unigrams:
            dict_count_Unigrams[w] = 1
        else:
            dict_count_Unigrams[w] += 1
        
    
    #print(dict_count_Unigrams)                                   #dict of count of  unigrams

    prob_Unigrams = {}

    for x in dict_count_Unigrams:
        prob_Unigrams[x] = dict_count_Unigrams[x]/len(tokens_All)
    
    #print(prob_Unigrams);                                   #probabilities of unigrams


    in_sent = in_sent.lower().split()           #Calculating for the given sentence
    prob_in = 1
    for i in range(0, len(in_sent)):
        #print(prob_Unigrams[in_sent[i]])
        prob_in *= prob_Unigrams[in_sent[i]]
    
    print("Unigram probability for given sentence:",prob_in)