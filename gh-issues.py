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
for i in issues:
    body = i.body
    bodylist = body.split("\n")
    sku = bodylist[0]
    gender = bodylist[1]
    section = bodylist[2]
    size = bodylist[3]
    yoox.add_yoox_item_to_track(sku,section,gender,size)
    i.edit(state='closed')

    
    