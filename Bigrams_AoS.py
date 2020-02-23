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
                                    

    print("Count of Bigrams:",len(list_Bigrams_EachSent))                      #Count of Bigrams_all 66517
    print("Count of Bigrams Combinations:",len(list_Bigrams_Combinations))     #Count of All Bigrams Combinations 

    #print(tokens_All)

    count_Unigrams = {}

    for w in tokens_All:
        if w not in count_Unigrams:
            count_Unigrams[w] = 1
        else:
            count_Unigrams[w] += 1              #Storing Unigrams-count 

    print(count_Unigrams['as'])

    for i in list_Bigrams_Combinations.keys():
        if i in list_Bigrams_EachSent:
            list_Bigrams_Combinations[i] += 1       #Getting and storing counts of all Combinations

    print(list_Bigrams_Combinations['brainpower brainpower'])
    
    #Calculating the probabilities

    prob_Bigrams = {}

    for i in list_Bigrams_Combinations.keys():
        uni_str = i.split(" ")[0]
        prob_Bigrams[i] = (list_Bigrams_Combinations[i]+1)/(count_Unigrams[uni_str] + len(count_Unigrams))


    print(prob_Bigrams['brainpower brainpower'])   
