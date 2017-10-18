import nltk
import json
import csv
from nltk.corpus import wordnet as wn


P = open("positive-words.txt", "r")
N = open("negative-words.txt","r")
pos = P.read()
neg = N.read()
positive = pos.split("\n")
negative = neg.split("\n")

##dic1={}
##dic2={}
##nouns = []
##present_bigrams = []


##l=[]

noun_dict = {'eat': ['restaurant', 'deli', 'eateries', 'eating'], 'value':['value', 'deal', 'rate', 'budget', 'bet','discount','price'], 'time' : ['experience', 'thing', 'idea'
    ,'night', 'sleep','feel', 'time', 'start','stay', 'comfort','idea','night'], 'staff':['staff', 'service', 'effort','cleaning','care'],'room': ['choice','room', 'rooms', 'hotel','bedding','place', 'bathroom','features','washroom'],
    'location':['location', 'place', 'walk','weather','way','view','attractions', 'area','parts', 'sunlight','weather'], 'internet': ['wifi', 'internet', 'wireless','zone'],
    'breakfast': ['breakfast','food', 'continental','breaky', 'coffee'], 'items': ['items', 'shampoo', 'amenities','pool'], 'parking': ['parking','valet'],
      'travel':['bus','travel','shuttle','travel','city'], 'food':['food','sandwich','seafood']}

adj_dict = {'bad':['bad','mediocre','terrible','poor','hefty','worst','dirty','uncomfortable'], 'good':['good','nice','comfortable','pleasant','impeccable',
                'upscale','great','best','better','attractive','fabulous','wonderful','attractive'],
            'cheap': ['cheap','economical','reasonable', 'inexpensive'], 'free': ['free', 'complementary']}

oneone = [44,
46,
61]


for i in oneone:
    if i not in [32, 67,68,69]:
        x=i
        print x
        l = []
        dic1={}
        nouns = []
        present_bigrams = []
        filename=str(x)+'.json'
        
        with open(filename) as data_file:
            data=json.load(data_file)
            


        #list storing bigrams in dictionary
        

        #to obtain sentences
        with open(filename) as data_file:
            data=json.load(data_file)


        #list storing bigrams in dictionary
        

        #to obtain sentences
        for j in range(0,len(data["Reviews"])):
            l.append(data["Reviews"][j]["Content"])
            st1 = l[j].replace("!", ".")
            st1 = st1.replace("?", ".")
            lst = st1.split(".")

            print "Hi1"

        #list of sentences is obtained. Now bigram is to be obtained (adjective, noun)
    ##        part1 = lst[1:(count/3)]
    ##        part2 = lst[(count/3):2*(count/3)]
    ##        part3 = lst[2*(count/3):]
    ##
    ##        total_set = []
            #print "HI"
            for k in range(len(lst)):
                sample_text = nltk.word_tokenize(lst[k])
                #sample text is list of words in the sentence. k is a particular sentence

                lst1 = nltk.pos_tag(sample_text)
                #print "HI"
                
                #for bigrams the adjective has to be adjacent to the noun. this bigram will be added to dict 
                if len(lst1) > 1:
                    temp = lst1[0]
                    print "HI"
                
                    for i in range(1, len(lst1)):

                        if temp[1] in ['JJ','JJR','JJS'] and lst1[i][1] in ['NN','NNP','NNPS','NNS']:                        
                            if temp[0] in positive or temp[0] in negative:
                                
                                noun = (lst1[i][0]).lower()
                                adj = temp[0].lower()
                                
                                for n1 in noun_dict:
                                    if noun in noun_dict[n1]:
                                        noun = n1
                                        break
                                    
                                for a1 in adj_dict:
                                    if adj in adj_dict[a1]:
                                        adj = a1
                                        break
                                    
                                bigram = adj + "\t" + noun 
                                
                                #if lst1[i][0] not in positive and lst1[i][0] not in negative:
                                #print temp[0]
                                if (len(present_bigrams) == 0):
                                    dic1.update({bigram : 1})
                                    present_bigrams.append(bigram)
                                    
                                if (bigram not in present_bigrams) and (len(present_bigrams) != 0):
                                    
                                    syns = []
                                    syn = wn.synsets(adj)

                                    #for bigram under consideration, finding equivalent words and storing 
                                    #them in list syns

                                    for s in syn:
                                        for sy in s.lemma_names:
                                            syns.append(sy)
                                            #print sy
                                    #print syns
                                    #print "\n I am here \n"

                                    c = 0

                                    for b in present_bigrams:
                                        b_tok = nltk.word_tokenize(b)
                                                            
                                            
                                        if (b_tok[1] == noun) and (b_tok[0] in syns):
                                            dic1[b] += 1
                                            c = 1
                                            break

                                    if (c == 0):
                                        dic1.update({bigram : 1})
                                        present_bigrams.append(bigram)
                                    #print present_bigrams
                                    #print "I am here"
                                        

                                    #dic1.update({bigram : 1})
                                    #present_bigrams.append(bigram)    
                                else:
                                    dic1[bigram] += 1
                        temp = lst1[i]

                        print "Hi2"

outputfile = "bigrams_senti3rating2.csv"

g = open(outputfile, 'wb')
writer = csv.writer(g)

for key, value in dic1.items():
    if value > 1:
        try:
            #print "Hi"
            writer.writerow([key, value])
        except:
            print key,value

g.close()



            
                        
##                            
##            #print len(dic1), "everyboody  say hey--o!"
##
##            
##        ##f = open('bigrams2_Cluster3.csv', 'a')
##        ##writer = csv.writer(f)
##        ##for key, value in dic1.items():
##        ##    try:
##        ##        #print "Hi"
##        ##        writer.writerow([key, value])
##        ##    except:
##        ##        print key,value
##        ##
##        ##f.close()
##        ##'''
##        ##                            if lst1[i][0] not in nouns:
##                                        
##        '''                                
##                                        
##                                    #print len(dic)
##
##            
##
##
##    '''
##
##    '''
##
##
##		

