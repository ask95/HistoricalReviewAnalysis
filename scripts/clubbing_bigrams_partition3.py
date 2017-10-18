import nltk
import json
import csv
from nltk.corpus import wordnet as wn
from os import listdir
from os.path import isfile, join

P = open("/home/meet/sentiment-analysis/lexicon/positive-words.txt", "r")
N = open("/home/meet/sentiment-analysis/lexicon/negative-words.txt","r")
pos = P.read()
neg = N.read()
positive = pos.split("\n")
negative = neg.split("\n")
count = 0
dic1 = {}
dic2 = {}
nouns = []
present_bigrams_1 = []
present_bigrams_2 = []
present_bigrams_3 = []
l = []

noun_dict = {'eat': ['restaurant', 'deli', 'eateries', 'eating'], 'value':['value', 'deal', 'rate', 'budget', 'bet','discount','price'], 'time' : ['experience', 'thing', 'idea'
                                                                                                                                                   ,'night', 'sleep','feel', 'time', 'start','stay', 'comfort','idea','night'], 'staff':['staff', 'service', 'effort','cleaning','care'],'room': ['choice','room', 'rooms', 'hotel','bedding','place', 'bathroom','features','washroom'],
    'location':['location', 'place', 'walk','weather','way','view','attractions', 'area','parts', 'sunlight','weather'], 'internet': ['wifi', 'internet', 'wireless','zone'],
    'breakfast': ['breakfast','food', 'continental','breaky', 'coffee'], 'items': ['items', 'shampoo', 'amenities','pool'], 'parking': ['parking','valet'],
        'travel':['bus','travel','shuttle','travel','city'], 'food':['food','sandwich','seafood']}

adj_dict = {'bad':['bad','mediocre','terrible','poor','hefty','worst','dirty','uncomfortable'], 'good':['good','nice','comfortable','pleasant','impeccable',
                                                                                                        'upscale','great','best','better','attractive','fabulous','wonderful','attractive'],
    'cheap': ['cheap','economical','reasonable', 'inexpensive'], 'free': ['free', 'complementary']}


# here is where the csv is to be changed - for different partitions- different dictionaries  
with open('/home/meet/sentiment-analysis/csv/RatingCluster3_withSentiCluster.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = dict((rows[0],rows[1]) for rows in reader)
    
# file_list = [f for f in listdir('/home/meet/sentiment-analysis/normalized_polarity') if
#              isfile(join('/home/meet/sentiment-analysis/normalized_polarity', f))]

file_list = mydict.keys()

try:
    file_list.remove('.DS_Store')  # .DS_Store can exist some times while using PyCharm.
except:
    pass

dic_cluster1 = {}
dic_cluster2 = {}
dic_cluster3 = {}

for i in range(len(file_list)):
    with open('/home/meet/sentiment-analysis/json 2/' + str(file_list[i].replace('normalized_polarity_output_','').replace('_',''))) as f:
        data = json.load(f)
    # try:
    print 'here'
    file_no = int(mydict['normalized_polarity_output_hotel_'+str(file_list[i]).replace('normalized_polarity_output_hotel_','')])
    print file_no
    count+=1
    print "count is : " + str(count)
    # print 'normalized_polarity_output_hotel_'+str(file_list[i])
    # except:
    #     pass



    #list storing bigrams in dictionary
    

    #to obtain sentences
    def bigram_extraction(dic1,present_bigrams):
        for j in range(0,len(data["Reviews"])):
            l.append(data["Reviews"][j]["Content"])
            st1 = l[j].replace("!", ".")
            st1 = st1.replace("?", ".")
            lst = st1.split(".")

        #list of sentences is obtained. Now bigram is to be obtained (adjective, noun)

            for k in lst:
                sample_text = nltk.word_tokenize(k)
                #sample text is list of words in the sentence. k is a particular sentence

                lst1 = nltk.pos_tag(sample_text)
                #print lst1

                #for bigrams the adjective has to be adjacent to the noun. this bigram will be added to dict
                if len(lst1) > 1:
                    temp = lst1[0]

                    for i in range(1, len(lst1)):

                        if temp[1] in ['JJ','JJR','JJS'] and lst1[i][1] in ['NN','NNP','NNPS','NNS']:
                            if temp[0] in positive or temp[0] in negative:
                                noun = (lst1[i][0]).lower()
                                adj = temp[0].lower()
                                
                                for n1 in noun_dict:
                                    if noun in noun_dict[n1]:
                                        noun = n1
                                        break
                            
                                # for a1 in adj_dict:
                                #     if adj in adj_dict[a1]:
                                #         adj = a1
                                #         break
                
                                bigram = adj + "\t" + noun
                                
                                if (len(present_bigrams) == 0):
                                    dic1.update({bigram : 1})
                                    present_bigrams.append(bigram)

                                if (bigram not in present_bigrams) and (len(present_bigrams) != 0):

                                    syns = []
                                    syn = wn.synsets(adj)

                                    #for bigram under consideration, finding equivalent words and storing
                                    #them in list syns

                                    for s in syn:
                                        for sy in s.lemma_names():
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

    if file_no == 1:
        bigram_extraction(dic_cluster1,present_bigrams_1)
    elif file_no == 2:
        bigram_extraction(dic_cluster2,present_bigrams_2)
    elif file_no == 3:
        bigram_extraction(dic_cluster3,present_bigrams_3)

        #plt.plot(x_data, y_data, color = 'black')

                    
    #print len(dic1), "everyboody  say hey--o!"

def file_writer(printed_dict, f_name):
    g = open(f_name, 'a')
    writer = csv.writer(g)
    for key, value in printed_dict.items():
        try:
            #print "Hi"
            writer.writerow([key, value])
        except:
            print key,value

    g.close()

file_writer(dic_cluster1, '/home/meet/sentiment-analysis/results/partition_3_bigrams_cluster1.csv')
file_writer(dic_cluster2, '/home/meet/sentiment-analysis/results/partition_3_bigrams_cluster2.csv')
file_writer(dic_cluster3, '/home/meet/sentiment-analysis/results/partition_3_bigrams_cluster3.csv')

