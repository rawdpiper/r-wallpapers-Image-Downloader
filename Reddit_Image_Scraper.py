import praw
import urllib.request
import os

f = open("Credentials.txt", 'r')
id_ = f.readline().strip()
secret = f.readline().strip()
password = f.readline().strip()
username = f.readline().strip()

reddit = praw.Reddit(
    client_id="{}".format(id_),
    client_secret="{}".format(secret),
    password="{}".format(password),
    user_agent="Reddit Media Downloader",
    username="{}".format(username),
)

parts = []
fol_dir = os.path.join(os.getcwd(), "Images")
if not os.path.exists(fol_dir):
    os.makedirs(fol_dir)
    print("Image Folder created")
else:
    print("Image Folder has already been previously created")

for submission in reddit.subreddit("wallpapers").top("all"):
    parts = submission.url.split("/")
    urllib.request.urlretrieve(submission.url, os.path.join(fol_dir, parts[3]))
