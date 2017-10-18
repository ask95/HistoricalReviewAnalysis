import collections
import datetime
import json
from os import listdir
from os.path import isfile, join
import csv

#import functions

'''Update the below path on the computer before running the code'''

file_list = [f for f in listdir('/Users/anikeshkamath/Documents/sentiment-analysis/output_json') if
             isfile(join('/Users/anikeshkamath/Documents/sentiment-analysis/output_json', f))]
try:
	file_list.remove('.DS_Store')  # .DS_Store can exist some times while using PyCharm.
except:
	pass

mydict = {}

for j in range(len(file_list)):
    open_file = '/Users/anikeshkamath/Documents/sentiment-analysis/output_json/' + str(file_list[j])
    with open(open_file) as f:
        data = json.load(f)
        total = 0
        for i in range(len(data)):
            y = float(data[i]['Ratings']['Overall'])
            total += y
        average = total/len(data)
        mydict.update({str(file_list[j]): average})

with open('/Users/anikeshkamath/Documents/sentiment-analysis/csv/averageOverallRating.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
        row = [key, value]
        writer.writerow(row)
	


   
