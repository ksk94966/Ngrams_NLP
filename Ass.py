if __name__== "__main__":

    f = open(r"C:\Users\SAI KRISHNA\Desktop\UTD Imp docs\Sem 2\NLP\Assignment 2\NLP6320_POSTaggedTrainingSet-Windows.txt");
    
    #splitting sentence from the given data text file by stripping the trailing spaces

    corpus_Sentences = f.read().strip().split("\n")            #Step 1

    tokens_All = [];
    for sente in corpus_Sentences:
        token_sent = sente.strip().split(" ")                   #dividing by space first
        for x in token_sent:
            temp = x.strip().split("_")[0].lower()
            tokens_All.append(temp)                             #Step 2
    
    print(tokens_All)                                           #Got all the token words from the given text file

    #to get vocabulary we need to eliminate the duplicates

    vocab_All = []

    for i in tokens_All: 
        if i not in vocab_All: 
            vocab_All.append(i)
 
    print(vocab_All);                                           #Got all the vocabulary

    print(len(tokens_All));                                     #count od tokens is 68737
    print(len(vocab_All));                                      #count is vocabulary is 7602


    #Generating Unigrams

    count_Unigrams = {}

    for w in tokens_All:
        if w not in count_Unigrams:
            count_Unigrams[w] = 1
        count_Unigrams[w] += 1
        
    
    print(count_Unigrams)                               #count of unigrams


    prob_Unigrams = {}

    for x in count_Unigrams:
        prob_Unigrams[x] = count_Unigrams[x]/len(tokens_All)
    
    print(prob_Unigrams);                               #probabilities of unigrams