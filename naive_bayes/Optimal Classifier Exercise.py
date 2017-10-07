import collections 
import operator
def NextWordProbability(sampletext,word):
    words = sampletext.split()
    word_freq_after_word=[words[num+1] for num,i in enumerate(words) if words[num]==word and num <len(words)]
    return collections.Counter(word_freq_after_word)

data_list = sample_memo.strip().split()
def LaterWords(sample,word,distance):
    dic={}
    word_count=len(data_list)
    words_after_word=NextWordProbability(sample,word)
    #Most_probable_word_after=[i for i in words_after_word]
    dic={(v,k) for (k,v) in words_after_word.items()}
    most_probable_word=sorted(dic, reverse=True)[0][1]
    
    #
    probabilities=[v/float(word_count) for v in words_after_word.values()]
    probs_words=dict(zip(words_after_word.keys(),probabilities))
    p1_sorted=sorted(probs_words.items(),key=operator.itemgetter(1),reverse=True)
    first_word_after=list(zip(*p1_sorted))[0][0]
    # 
    most_prob=probs_words[most_probable_word]
    #print ("probs_words: {}".format(probs_words))
    #print ("most_prob: {}".format(most_prob))
    
    
    for i in (1, distance+1):
        second_w=NextWordProbability(sample,most_probable_word)
        probabilities2=[v/float(word_count) for v in second_w.values()]
        probs_words2=dict(zip(second_w.keys(),probabilities2))
        probs_words2_sorted=sorted(probs_words2.items(),key=operator.itemgetter(1),reverse=True)
        prob_of_2ndword=(probs_words2_sorted)[0][1]
        most_prob2=most_prob*prob_of_2ndword
        prob_word1_word2=dict(zip(probs_words2.keys(),[most_prob*probs_words2[w] for w in probs_words2.keys()] ))
        prob_word1_word2_sorted=sorted(prob_word1_word2.items(),key=operator.itemgetter(1),reverse=True)
        unzip=list(zip(*prob_word1_word2_sorted))
        
        second_word=(unzip)[0][0]
        most_prob=prob_word1_word2[second_word]
        
        
    #print ("probs_words2: {}".format(probs_words2))
    #print ("second_w: {}".format(second_w))
    #print ("prob_of_2ndword: {}".format(prob_of_2ndword))
    #print ("most_prob2: {}".format(most_prob2))
    #print ("unzip: {}".format(unzip))
    
    return second_word
    
    

