sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

#
#   Maximum Likelihood Hypothesis
#
#
#   In this quiz we will find the maximum likelihood word based on the preceding word
#
#   Fill in the NextWordProbability procedure so that it takes in sample text and a word,
#   and returns a dictionary with keys the set of words that come after, whose values are
#   the number of times the key comes after that word.
#   
#   Just use .split() to split the sample_memo text into words separated by spaces.
import string
def NextWordProbability(sampletext,word):
    sampletext=sampletext.translate(string.maketrans("",""),string.punctuation)
    dic={}
    lis = [i.lower() for i in sampletext.split()]
    #new_st = sampletext.split(word)[1]
    #lis = [i.lower() for i in new_st.split()]
    for n,i in enumerate(lis):
        if i==word and n < len(lis)-1:
            dic[lis[n+1]] = dic.get(lis[n+1],0)+1
            
    for k,v in dic.items():
        dic[k]=v / float(sum(dic.values()))
        
    return dic
    

    import collections 
def NextWordProbability(sampletext,word):
    words = sampletext.split()
    word_freq_after_word=[words[num+1] for num,i in enumerate(words) if words[num]==word and num <len(words)]
    return collections.Counter(word_freq_after_word)
