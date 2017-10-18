import collections
import datetime
import json
from os import listdir
from os.path import isfile, join
import csv

#import functions


with open('/Users/anikeshkamath/Documents/sentiment-analysis/csv/averageOverallRating.csv', mode='r') as infile:
    reader = csv.reader(infile)
    ratings = dict((rows[0],rows[2]) for rows in reader)

with open('/Users/anikeshkamath/Documents/sentiment-analysis/csv/tenfeature_averageVal.csv', mode='r') as infile:
    reader = csv.reader(infile)
    features = dict((rows[0],rows[1:]) for rows in reader)


'''Update the below path on the computer before running the code'''

file_list = [f for f in listdir('/Users/anikeshkamath/Documents/sentiment-analysis/normalized_polarity') if
             isfile(join('/Users/anikeshkamath/Documents/sentiment-analysis/normalized_polarity', f))]
try:
	file_list.remove('.DS_Store')  # .DS_Store can exist some times while using PyCharm.
except:
	pass

print file_list

mydict = {}

with open('/Users/anikeshkamath/Documents/sentiment-analysis/csv/RatingandFeature.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for j in range(len(file_list)):
        key = str(file_list[j])
        try:
            val1 = ratings[key]
            val2 = features[key]
            row = [key] + [val1] + val2
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

   
