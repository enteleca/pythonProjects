from collections import Counter
import string
import praw

#Do
#
# "    pip install praw    "
# in your terminal / console.
#
#You need to find your reddit ClientID and ClientSecret keys in your account information.
#Find it by going to your account settings in the old reddit website. 
#If you can't figure out how to do it, just look up "how to find reddit client ID" on google.
#
#After that, insert your username and password (you can use any account including one that you just create) of the 
#account you just go the clientID and clientSecret from. 
#
#user_agent is just another reddit username, you can literally use any username I believe. Just put a valid reddit username
#in there.



#Insert ClientID and ClientSecret below in the '' marks.
reddit = praw.Reddit(client_id='', client_secret='', 

#Insert your username and password below in the '' marks.
username='', 
password='', 

#Insert any reddit username below in the '' marks
user_agent='')

#Code to generate the 5 most popular tickers of the day in WSB.
subreddit = reddit.subreddit('wallstreetbets')

postlist = list(subreddit.hot(limit=1))
my_tickers = []
prohibited = ['WSB', 'LORD', 'THE', 'D', 'WOW', 'RH', 'OIL', 'GANG', 'W', 'AF', 'ATH', 'API', 'EOD', 'A', 'GIVE', 'ME', 'IS', 'BUT', 'YOLO', 'I', 'GOP', 'MOON', 'FD', 'MLF', 'MCR', 'BUY', 'THIS', 'DIP', 'PUMP', 'F', 'FUC', 'FUCK', 'FK', 'BUM', 'UP', 'DOWN', 'TO', 'THAT', 'AND', 'WE', 'ARE', 'GOING','ON', 'NO', 'FED', 'FEDS', 'IN', 'IS', 'MADE', 'ON', 'FOR', 'WONT', 'MY', 'FUCKED', 'FUCK', 'WHY', 'IT', 'DUMB', 'UR', 'L', 'YOU', 'LOL', 'LMAO']

for comment in subreddit.stream.comments():
    if comment.parent_id[3:] == postlist[0].id: #check if its a daily thread comment
        body = comment.body.translate(comment.body.maketrans("","",string.punctuation)).split(' ') #reformat comment
        for word in body:
            if word.isupper() and len(word) < 5 and word not in prohibited: #primitive ticker validation. In future, think about checking if ticker returns stock info from api to validate
                my_tickers.append(word) #append to list of tickers that has appeared
        print("-"*30)  
        print("")      
        #Remove this line below if you don't want the comments.
        print(comment.body)
        print("")
        #Remove this line below if you don't want to see the popular tickers and just want to see the live comments.
        print('Update Stock Tickers: {}'.format(dict(Counter(my_tickers).most_common(8))))
        print("")
