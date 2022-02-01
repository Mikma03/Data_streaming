# import niezbednych bibliotek
import praw
from urllib.parse import quote_plus
import datetime
import time

# ponizsze dwie biblioteki sluza nam do zabawy z zatrzymywaniem kodu w bardziej 'programistyczny' sposob
import sys
import os

# przypisujemy 
client_id = 'xxx'
secret = 'xxx'
user_agent = 'Test_11'
username="No-Blueberry-6622"
password="xxx"

# uzywamy moduly praw do zaladowania odpowiednich zmiennych
reddit = praw.Reddit(client_id=client_id, 
                     client_secret=secret, 
                     user_agent=user_agent, 
                     username=username, 
                     password=password
                    )

# bardzo wazna czesc: ladujemy swoj portfel
reply_template = "0x097d5082a9805e3cdc5d38473f08c6fb76e1eb33 Thanks!"
commented_list = []

# budujemy funkcje wraz z wywolaniem 
def run_example():
    subreddit_list = ['opensea', 'NFT', 'NFTsMarketplace', 'NFTExchange', 'NFTgiveaway', 'NFTMarketplace', 'NFTmarket', 'NFTArt_Finance', 'OpenSeaNFT' ]
    while True:
        # try:
            for submission in reddit.subreddit("+".join(subreddit_list)).new():
                keywords = ['comment', 'drop', 'giveaway', 'free', 'address below', 'wallet bellow', 'wallet', 'address']
                title = submission.title.lower()
                submission_id = submission.id
                if submission_id not in commented_list and any(keyword in title for keyword in keywords):
                    submission.upvote()
                commented_list.append(submission_id)
                print(submission.subreddit ,"||", title, "||", datetime.datetime.fromtimestamp(submission.created), "||", datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

                # szalenie istatna czesc gdyz dzieki tej czesci nasz program nie komentuje tego co juz bylo poniewaz nie cofa sie 
                break

            # trzeba zastsowac usypianie programu aby reddit nie blokowal pewnych komentarzy gdy beda zbyt czesto - ograniczenia API
            time.sleep(60)

            # dzieki zastosowaniu sys mamy przyjemne zatrzymanie programu jakby ktos chcial uruchomic go z konsoli
            if len(commented_list) >= 2:
                sys.exit()
        
        #ponizszy kod wyrzucal wyjatek bardzo szeroki, dlatego na te chwile zostala instrukcja if aby zatrzymac program
        # except:
            # print("Problem z siecia...")

if __name__ == "__main__":
    run_example()


# if len(commented_list) >= 5:
#     exit()