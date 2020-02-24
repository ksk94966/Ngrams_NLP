import sys
import re

if __name__== "__main__":

    path = sys.argv[1]    #for getting filename as argument
    f = open(path,"r")
    in_sent = sys.argv[2]        #getting testing string
    
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


        
    for i in dict_Bigrams_Combinations.keys():
        if i in dict_Bigrams_EachSent.keys():
            dict_Bigrams_Combinations[i] =  dict_Bigrams_EachSent[i]          #Getting and storing counts of all Combinations

    #print(max(dict_Bigrams_Combinations.values()))

    buckets = {}                                       #dict for storing frequency values

    for i in range(max(dict_Bigrams_Combinations.values())+1):
        buckets[i] = 0
        for w in dict_Bigrams_Combinations.keys():
            if(dict_Bigrams_Combinations[w]==i):
                buckets[i] += 1
    
    buckets[len(buckets)] = 0                         #Storing the next count frequency as zero

    #print(len(buckets))

    #Calcluating new counts based on good turing

    dict_Bigrams_GTD = {}

    for k in dict_Bigrams_Combinations.keys():
        Nc = buckets[dict_Bigrams_Combinations[k]]
        Ncplus = buckets[dict_Bigrams_Combinations[k]+1]
        if Ncplus == 0:
            dict_Bigrams_GTD[k] = 0
        else:
            dict_Bigrams_GTD[k] =  (dict_Bigrams_Combinations[k]+1)*(Ncplus/Nc)


    #print(len(dict_Bigrams_GTD))


    #Calculating Total seen pairs
    N = 0
    for i in range(1,len(buckets)):
        N += i*buckets[i]                  #Calculating Total Seen Bigrams

    prob_Bigrams_GTD = {}

    for k in dict_Bigrams_GTD.keys():                   #Calculating the Good turing probabilities
        if dict_Bigrams_Combinations[k] == 0:
            prob_Bigrams_GTD[k] = buckets[1]/N
        else:
            prob_Bigrams_GTD[k] = dict_Bigrams_GTD[k]/N

    # j = 0
    # for i in dict_Bigrams_GTD:
    #     if j>10:
    #         break
    #     j+=1
    #     print(dict_Bigrams_GTD[i])
        
    #print(len(prob_Bigrams_GTD))


    in_sent = in_sent.lower().split()               #Calculating for the given sentence
    prob_in = 1
    for i in range(0, len(in_sent)-1):
        if in_sent[i]+" "+in_sent[i+1] not in prob_Bigrams_GTD.keys():
            print(buckets[1]/N)
            prob_in *= buckets[1]/N
        else:
            print(prob_Bigrams_GTD[in_sent[i]+" "+in_sent[i+1]])
            prob_in *= prob_Bigrams_GTD[in_sent[i]+" "+in_sent[i+1]]
    
    
    print("Probability of given sentence using Good Turing:",prob_in)

