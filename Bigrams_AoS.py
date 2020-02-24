import sys
import re

if __name__== "__main__":

    path = sys.argv[1]    #for getting filename as argument
    f = open(path,"r")
    in_sent = sys.argv[2]     #getting testing sentence

    #splitting sentence from the given data text file by stripping the trailing spaces

    corpus_Sentences = f.read().strip().split("\n")         #Step 1
    tokens_All = [];                                        #list for storing Unigrams
    dict_Bigrams_EachSent = {};                             #dict for storing unique bigrams
    dict_Bigrams_Combinations = {};                         #dict for storing all combinations of Bigrams
    for sentence in corpus_Sentences:
        temp_Sent_List = []
        token_sent = sentence.strip().split(" ")
        for x in token_sent:
            temp = x.strip().split("_")[0].lower()
            tokens_All.append(temp)
            temp_Sent_List.append(temp)
        for i in range(0,len(temp_Sent_List)):
            if(i<len(temp_Sent_List)-1):
                s =temp_Sent_List[i] +" "+ temp_Sent_List[i+1]
                if s not in dict_Bigrams_EachSent:
                    dict_Bigrams_EachSent[s] = 1
                else:
                    dict_Bigrams_EachSent[s] += 1
            for j in range(0,len(temp_Sent_List)):
                k = temp_Sent_List[i] +" "+ temp_Sent_List[j]
                dict_Bigrams_Combinations[k] = 0
                                    

    #print("Count of Bigrams:",len(dict_Bigrams_EachSent))                      #Count of Bigrams_all 66517
    #print("Count of Bigrams Combinations:",len(dict_Bigrams_Combinations))     #Count of All Bigrams Combinations 

    #print(tokens_All)

    dict_count_Unigrams = {}

    for w in tokens_All:
        if w not in dict_count_Unigrams:
            dict_count_Unigrams[w] = 1
        else:
            dict_count_Unigrams[w] += 1              #Storing Unigrams-count 

    #print(dict_count_Unigrams['as'])

    for i in dict_Bigrams_Combinations.keys():
        if i in dict_Bigrams_EachSent.keys():
            dict_Bigrams_Combinations[i] =  dict_Bigrams_EachSent[i]       #Getting and storing counts of all Combinations

    #print(dict_Bigrams_Combinations['brainpower brainpower'])
    
    #Calculating the probabilities

    prob_Bigrams = {}

    for i in dict_Bigrams_Combinations.keys():
        uni_str = i.split(" ")[0]
        prob_Bigrams[i] = (dict_Bigrams_Combinations[i]+1)/(dict_count_Unigrams[uni_str] + len(dict_count_Unigrams))


    #print(prob_Bigrams['brainpower brainpower'])   


    in_sent = in_sent.lower().split()                   #Calculating for the given sentence
    prob_in = 1
    for i in range(0, len(in_sent)-1):
        if in_sent[i]+" "+in_sent[i+1] not in prob_Bigrams.keys():
            #print(1/(dict_count_Unigrams[in_sent[i]] + len(dict_count_Unigrams)))
            prob_in *=  1/(dict_count_Unigrams[in_sent[i]] + len(dict_count_Unigrams))
        else:
            #print(prob_Bigrams[in_sent[i]+" "+in_sent[i+1]])
            prob_in *= prob_Bigrams[in_sent[i]+" "+in_sent[i+1]]
    

    print("Probability of given sentence for Add one Smoothing:",prob_in)