import praw
import config
import time
import courseScrapper

def bot_login():
    print("Logging in ...")
    reddit = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "UoftC0urseB0t 0.1")
    print("Logged in")
    
    return reddit

def run_bot(r, comments_id):
    subredit = r.subreddit('tests')
    comments = r.subreddit('tests').comments(limit=25)
    
    for comment in r.subreddit('tests').comments(limit=25):
        if "!UoftC0urseB0t" in comment.body and comment.id not in comments_id:  
            s=str(comment.body).split()[1]
            comm = courseScrapper.course(str(s))
            comment.reply(comm)
            comments_id.append(comment.id)                
        
    time.sleep(10)

r = bot_login()
comments_id = []
while True:
    run_bot(r, comments_id)


