import collections
import datetime
import json
from os import listdir
from os.path import isfile, join
import csv

#import functions

'''Update the below path on the computer before running the code'''

file_list = [f for f in listdir('/Users/anikeshkamath/sentiment-analysis/normalized_polarity') if
             isfile(join('/Users/anikeshkamath/sentiment-analysis/normalized_polarity', f))]
try:
	file_list.remove('.DS_Store')  # .DS_Store can exist some times while using PyCharm.
except:
	pass

mydict = {}

def addition_for_average(K, total_list, freq_list, iX, iY):
    if (int(iX/0.1) == K):
        diff = iY - iX
        total_list[K] += diff
        freq_list[K] += 1

for j in range(len(file_list)):
	open_file = '/Users/anikeshkamath/sentiment-analysis/normalized_polarity/' + str(file_list[j])
	with open(open_file) as f:
		data = json.load(f)

        total_score_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        no_of_reviews = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
        for i in data:
            x = float(i)
            y = float(data[i])
            for k in range(10):
                addition_for_average(k, total_score_list, no_of_reviews, x, y)

        average = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for l in range(10):
            try:
                average[l] = total_score_list[l]/no_of_reviews[l]
            except:
                pass
    
        mydict.update({str(file_list[j]): average})

print mydict

with open('tenfeature_averageVal.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
        row = [key] + value
        writer.writerow(row)
	


   
