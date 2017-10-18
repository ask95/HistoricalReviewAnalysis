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

for j in range(len(file_list)):
	open_file = '/Users/anikeshkamath/sentiment-analysis/normalized_polarity/' + str(file_list[j])
	with open(open_file) as f:
		data = json.load(f)
	total = 0
	for i in data:
		x = float(i)
		y = float(data[i])
		diff = y - x
		total += diff
		
	average = total/(len(data))
	average
	mydict.update({str(file_list[j]): average})

print mydict

with open('feature_averageVal.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
       writer.writerow([key, value])
	


   
