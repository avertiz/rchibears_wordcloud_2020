import requests
import json
import time
import codecs
import pandas as pd

class Rchibearstext():
    def __init__(self, name, start_time, end_time, subreddit = 'chibears', 
                                             submission_url = 'https://api.pushshift.io/reddit/search/submission/', 
                                             comments_url = 'https://api.pushshift.io/reddit/search/comment/'):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.subreddit = subreddit
        self.submission_url = submission_url
        self.comments_url = comments_url

    def getSubmissions(self, after):
        r = requests.get(self.submission_url, params= {'subreddit':self.subreddit, 'size':'500', 'after':after, 'before':self.end_time})
        data = json.loads(r.text)
        return pd.json_normalize(data['data'])

    def getComments(self, after):
        r = requests.get(self.comments_url, params= {'subreddit':self.subreddit, 'size':'500', 'after':after, 'before':self.end_time})
        data = json.loads(r.text)
        return pd.json_normalize(data['data'])
    
    def createFile(self, filepath):
        f = codecs.open(filepath + self.name + ".txt", "a", encoding='utf8')
        placeholder = self.start_time
        submissions = self.getSubmissions(after = placeholder)
        while len(submissions) != 0:
            print("Getting submissions....",placeholder)
            for row in range(len(submissions)):
                try:
                    if submissions['removed_by_category'].iloc[row] is not None:
                        f.write(str(submissions['title'].iloc[row]) + " ")
                        f.write(str(submissions['selftext'].iloc[row]) + " ")
                except Exception as e: 
                    print(e)
            placeholder = submissions['created_utc'].max()
            time.sleep(2.1)
            try:
                submissions = self.getSubmissions(after = placeholder)
            except Exception as e: 
                print(e)
        print("Submissions complete.")
        placeholder = self.start_time
        comments = self.getComments(after = placeholder)
        while len(comments) != 0:            
            print("Getting comments....",placeholder)
            for row in range(len(comments)):
                try:
                    f.write(str(comments['body'].iloc[row]) + " ") 
                except Exception as e: 
                    print(e)        
            placeholder = comments['created_utc'].max()
            try:
                comments = self.getComments(after = placeholder)
            except Exception as e: 
                    print(e)  
            time.sleep(2.1)
        print("Comments complete.")
        f.close()