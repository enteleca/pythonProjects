from collections import Counter
import string
import praw

reddit = praw.Reddit(client_id='Rv6c7azBAFvTDQ', client_secret='sdvCdgY6L_9AWp_2FHw_rpsO5so', username='wallstreetbetshotbot', password='wallstreetbetsbot', user_agent='amerikayo')
subreddit = reddit.subreddit('wallstreetbets')

postlist = list(subreddit.hot(limit=1))
my_tickers = []
prohibited = ['WSB', 'LORD', 'THE', 'D', 'WOW', 'RH', 'OIL', 'GANG', 'W', 'AF', 'ATH', 'API', 'EOD', 'A', 'GIVE', 'ME', 'IS', 'BUT', 'YOLO', 'I', 'GOP', 'MOON', 'FD', 'MLF', 'MCR', 'BUY', 'THIS', 'DIP', 'PUMP', 'F', 'FUC', 'FUCK', 'FK', 'BUM', 'UP', 'DOWN', 'TO', 'THAT', 'AND', 'WE', 'ARE', 'GOING','ON', 'NO', 'FED', 'FEDS', 'IN', 'IS', 'MADE', 'ON', 'FOR', 'WONT', 'MY', 'FUCKED', 'FUCK', 'UR', 'L', 'LOL', 'LMAO']

for comment in subreddit.stream.comments():
    if comment.parent_id[3:] == postlist[0].id: #check if its a daily thread comment
        body = comment.body.translate(comment.body.maketrans("","",string.punctuation)).split(' ') #reformat comment
        for word in body:
            if word.isupper() and len(word) < 5 and word not in prohibited: #primitive ticker validation. In future, think about checking if ticker returns stock info from api to validate
                my_tickers.append(word) #append to list of tickers that has appeared
                print(word)
        print("-"*30)  
        print("")      
        print(comment.body)
        print("")
        print('Update Stock Tickers: {}'.format(dict(Counter(my_tickers).most_common(8))))
        print("")
