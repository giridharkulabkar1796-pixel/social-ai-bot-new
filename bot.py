import os
import random
import time
import schedule

from instagrapi import Client

username = "rugveddigital"
password = "gKrkrk@91"

cl = Client()

code = input("Enter 2FA Code: ")

cl.login(
    username,
    password,
    verification_code=code
)

print("Instagram Login Successful ✅")

# CONTENT FOLDER
CONTENT_FOLDER = "content"

# USED POSTS STORAGE
used_posts = []

def upload_post():

    all_posts = os.listdir(CONTENT_FOLDER)

    remaining_posts = [
        post for post in all_posts
        if post not in used_posts
    ]

    if not remaining_posts:
        print("All Posts Uploaded ✅")
        return

    selected_post = random.choice(remaining_posts)

    post_path = os.path.join(
        CONTENT_FOLDER,
        selected_post
    )

    caption = """
🚀 Grow Your Business Online

🌐 https://instagram.com/rugveddigital

📈 Meta Ads
📈 Google Ads
📈 Social Media Marketing
📈 Lead Generation
📈 Brand Growth

📩 DM @rugveddigital

#digitalmarketing
#socialmedia
#metaads
#googleads
#instagrammarketing
#marketingagency
#businessgrowth
#socialmediamarketing
#contentmarketing
#branding
#adsmanager
#smallbusiness
#onlinebusiness
#marketingtips
#rugveddigital
"""


    cl.photo_upload(
        post_path,
        caption
    )

    used_posts.append(selected_post)

    print(f"{selected_post} Uploaded ✅")

# DAILY POST TIME
schedule.every().day.at("08:13").do(upload_post)

print("Auto Posting Started 🚀")

while True:
    schedule.run_pending()
    time.sleep(1)