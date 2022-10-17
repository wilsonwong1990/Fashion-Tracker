"""
Module for accessing and using Yoox.com

Author: Wilson Wong
Date: 10-17-2022
"""

import requests

def get_yoox_item(sku,gender):
    """
    Given a sku from Yoox, retrieve the price, description, and image of the item. Gender is needed
    to see what side of the store to retrieve.

    Parameter sku: A valid sku from yoox.com
    Parameter gender: men or women are valid.
    """

    url = "https://www.yoox.com/us/" + sku + "/item#dept=clothing" + gender
    header={'User-Agent': 'Mozilla/5.0'}

    item = requests.get(url,headers=header)
   # After retrieving item, extract price, description, and image
