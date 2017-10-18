import collections
import datetime
import json
from os import listdir
from os.path import isfile, join
import csv

#import functions


no_of_rating_clusters = 5

with open('/Users/anikeshkamath/Documents/sentiment-analysis/csv/RatingandFeature.csv', mode='r') as infile:
    reader = csv.reader(infile)
    ratings_features = dict((rows[0], rows[1:]) for rows in reader)

lst_dic = []

for i in range(no_of_rating_clusters):
    lst_dic.append({})


for i in ratings_features:
    clus = int(ratings_features[i][0])
    dic_to_be_updated = lst_dic[clus - 1]
    features = ratings_features[i][1:]
    #print lst_dic[clus - 1]
    dic_to_be_updated.update({i: features})
'''Update the below path on the computer before running the code'''
'''
file_list = [f for f in listdir('/Users/anikeshkamath/Documents/sentiment-analysis/normalized_polarity') if
             isfile(join('/Users/anikeshkamath/Documents/sentiment-analysis/normalized_polarity', f))]
try:
    file_list.remove('.DS_Store')  # .DS_Store can exist some times while using PyCharm.
except:
    pass

print file_list

mydict = {}
'''
for i in range(len(lst_dic)):
    csv_name = '/Users/anikeshkamath/Documents/sentiment-analysis/csv/RatingCluster'+ str(i+1) + '.csv'
    with open(csv_name, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for j in lst_dic[i]:
            #key = str(file_list[j])
            try:
                #val1 = ratings[key]
                #val2 = features[key]
                row = [j] + lst_dic[i][j]
                writer.writerow(row)
            except:
                print "Outlier!"


'''
    open_file = '/Users/anikeshkamath/Documents/sentiment-analysis/normalized_polarity/' + str(file_list[j])
    with open(open_file) as f:
    data = json.load(f)
    total = 0
    for i in range(len(data)):
    y = float(data[i]['Ratings']['Overall'])
    total += y
    average = total/len(data)
    mydict.update({str(file_list[j]): average})
    
    with open('/Users/anikeshkamath/Documents/sentiment-analysis/csv/RatingandFeature.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
    row = [key, value]
    writer.writerow(row)
    
    '''






