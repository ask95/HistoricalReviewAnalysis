import collections

from textblob import TextBlob


def generate_sentiment(review):
    review_object = TextBlob(review['Content'])
    review_polarity = 0
    sentence_count = len(review_object.sentences)
    for sentence in review_object.sentences:
        review_polarity = review_polarity + sentence.sentiment.polarity
    review_polarity = review_polarity/sentence_count
    output={}
    output['polarity'] = review_polarity
    output['Ratings'] = review['Ratings']
    output['ReviewID'] = review['ReviewID']
    output['Date'] = review['Date']
    return output


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


def less_than_or_equal_to(current_month, current_year, latest_month, latest_year):
    if current_year < latest_year:
        return True
    elif current_year == latest_year:
        if current_month <= latest_month:
            return True
        else:
            return False
    else:
        return False


def month_wise_dict(d1, d2):
    earliest_month = d2.month
    earliest_year = d2.year
    latest_month = d1.month
    latest_year = d1.year
    current_month = earliest_month
    current_year = earliest_year
    month_dict = collections.OrderedDict()
    while less_than_or_equal_to(current_month, current_year, latest_month, latest_year):
        month_dict[str(current_month) + ', ' + str(current_year)] = 0
        if current_month == 12:
            current_year += 1
            current_month = 1
        else:
            current_month += 1
    return month_dict
