"""
Access GitHub issues to add new items to track.

Author: Wilson Wong
Date: 11-05-2022
"""

from github import Github
import yoox
import os

token = os.environ['Token']

g = Github(token)
repo = g.get_repo("wilsonwong1990/Fashion-Tracker")
issues = repo.get_issues()
#body = issues[0].body
#print("body is:" + body)
#bodylist = body.split("\n")
#sku = bodylist[0]
#print("sku is: " + sku)
#gender = bodylist[1]
#print("gender is:" + gender)
#section = bodylist[2]
#print("section is:" + section)
#size = bodylist[3]
#print("size is:" + size)
#yoox.add_yoox_item_to_track(sku,section,gender,size)
#issues[0].edit(state='closed')

for i in issues:
    if "new item" in str(i.labels):
        body = i.body    
        print("body is:" + body)
        bodylist = body.split("\n")
        sku = bodylist[0]
        print("sku is: " + sku)
        gender = bodylist[1]
        print("gender is:" + gender)
        section = bodylist[2]
        print("section is:" + section)
        size = bodylist[3]
        print("size is:" + size)
        yoox.add_yoox_item_to_track(sku,section,gender,size)
        i.edit(state='closed')