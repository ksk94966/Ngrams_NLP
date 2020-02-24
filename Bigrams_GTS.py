if __name__== "__main__":

    f = open(r"C:\Users\SAI KRISHNA\Desktop\UTD Imp docs\Sem 2\NLP\Assignment 2\NLP6320_POSTaggedTrainingSet-Windows.txt");
    
    #splitting sentence from the given data text file by stripping the trailing spaces

    corpus_Sentences = f.read().strip().split("\n")         #Step 1
    tokens_All = [];                                        #list for storing Unigrams
    list_Bigrams_EachSent = {};                             #dict for storing unique bigrams
    list_Bigrams_Combinations = {};                         #dict for storing all combinations of Bigrams
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
                if s not in list_Bigrams_EachSent:
                    list_Bigrams_EachSent[s] = 1
                else:
                    list_Bigrams_EachSent[s] += 1
            for j in range(0,len(temp_Sent_List)):
                k = temp_Sent_List[i] +" "+ temp_Sent_List[j]
                list_Bigrams_Combinations[k] = 0


        
    for i in list_Bigrams_Combinations.keys():
        if i in list_Bigrams_EachSent.keys():
            list_Bigrams_Combinations[i] =  list_Bigrams_EachSent[i]          #Getting and storing counts of all Combinations


    buckets = {}                                       #dict for storing frequency values

    for i in range(max(list_Bigrams_Combinations.values())+1):
        buckets[i] = 0
        for w in list_Bigrams_Combinations.keys():
            if(list_Bigrams_Combinations[w]==i):
                buckets[i] += 1
    
    buckets[len(buckets)] = 0                         #Storing the next count frequency as zero

    print(len(buckets))

    #Calcluating new counts based on good turing

    list_Bigrams_GTD = {}

    for k in list_Bigrams_Combinations.keys():
        Nc = buckets[list_Bigrams_Combinations[k]]
        Ncplus = buckets[list_Bigrams_Combinations[k]+1]
        list_Bigrams_GTD[k] =  (list_Bigrams_Combinations[k]+1)*(Ncplus/Nc)


    print(len(list_Bigrams_GTD))


    #Total seen pairs
    N = 0
    for i in range(1,len(buckets)):
        N += i*buckets[i]

    prob_Bigrams_GTD = {}

    for k in list_Bigrams_GTD.keys():
        prob_Bigrams_GTD[k] = list_Bigrams_GTD[k]/N

    print(len(prob_Bigrams_GTD))

    












