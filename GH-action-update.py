"""
A helper to be called by GitHub Actions to run an update against csvs.

Author: Wilson Wong
Date: 11-06-2022
"""

import yoox
import os
os.replace("store-csvs/yoox.csv", "store-csvs/yoox-old.csv")
yoox.update_yoox_csv("store-csvs/yoox.csv")