import nltk
import json
import csv
from nltk.corpus import wordnet as wn
import collections
import datetime
import json
from os import listdir
from os.path import isfile, join

import functions

'''Update the below path on the computer before running the code'''

file_list = [f for f in listdir('/home/meet/sentiment-analysis/output_json') if
             isfile(join('/home/meet/sentiment-analysis/output_json', f))]
try:
    file_list.remove('.DS_Store')  # .DS_Store can exist some times while using PyCharm.
except:
    pass

for j in range(len(file_list)):
    open_file = '/home/meet/sentiment-analysis/output_json/' + str(file_list[j])
    with open(open_file) as f:
        data = json.load(f)
    for i in range(len(data)):
        polarity = data[i]['polarity'] + 1
        try:
            date_object = datetime.datetime.strptime(data[i]['Date'], '%B %d, %Y')
        except ValueError:
            date_object = datetime.datetime.strptime(data[i]['Date'], '%b %d, %Y')
        data[i]['polarity'] = polarity
        data[i]['dateObject'] = date_object

    date_list = [data[i]['dateObject'] for i in range(len(data))]

    polarity_monthly_list = functions.month_wise_dict(max(date_list), min(date_list))

    for i in range(len(data)):
        date_object = data[i]['dateObject']
        polarity = data[i]['polarity']
        polarity_monthly_list[str(date_object.month) + ', ' + str(date_object.year)] += polarity

    polarity_score_list = polarity_monthly_list.values()

    cumulative_monthly_dict = collections.OrderedDict()
    normalized_time_series_list = []
    for i in range(1, len(polarity_score_list)):
        polarity_score_list[i] = polarity_score_list[i] + polarity_score_list[i - 1]
        normalized_time_series_list.append(float(i) / (len(polarity_score_list) - 1))

    normalized_time_series_list.append(1)
    polarity_score_list[:] = [x / max(polarity_score_list) for x in polarity_score_list]
    normalized_time_series_dict = collections.OrderedDict()
    normalized_time_series_dict[0] = 0

    for i in range(len(normalized_time_series_list)):
        normalized_time_series_dict[float(normalized_time_series_list[i])] = polarity_score_list[i]

    with open('/home/meet/sentiment-analysis/normalized_polarity/normalized_polarity_' + str(file_list[j]),
              'w') as outfile:
        json.dump(normalized_time_series_dict, outfile)
    print "j is : " + str(j)
