"""
Module for accessing and using Yoox.com

Author: Wilson Wong
Date: 10-17-2022
"""

import requests
from html.parser import HTMLParser

def get_yoox_item(sku,section,gender):
    """
    Given a sku from Yoox, retrieve the price, description, and image of the item. Gender is needed
    to see what side of the store to retrieve.

    Parameter sku: A valid sku from yoox.com
    Parameter section: String of the section of the website it is in
    Preconditon: valid sections are clothing, shoes, accessories, sale
    Parameter gender: men or women are valid.
    """

    url = "https://www.yoox.com/us/" + sku + "/item#dept=" + section + gender
    header={'User-Agent': 'Mozilla/5.0'}

    item = requests.get(url,headers=header)
    iteminfo = str(item.content)

    # Search the html content, find the class before the price, and the code after it to split the content for the price.
    html_pricestr = '</div><div class="MuiTitle4-title4 ItemInfo_currentPrice__n4v78"><span class=""><span>$'
    pricestroffset = len(html_pricestr)
    pricefirstdigit = iteminfo.find(html_pricestr) + pricestroffset
    html_pricestrlast = '</span></span></div></div></div></div></div><div class="item_color'
    pricelastdigit = iteminfo.find(html_pricestrlast)
    price = iteminfo[pricefirstdigit:pricelastdigit]
    price = price.strip()

    # Search the html content, find the string before the image and it's description, and the code after.
    html_imagestr = '<span style="cursor:zoom-in"><img alt='
    imageoffset = len(html_imagestr)
    imagefirstdigit = iteminfo.find(html_imagestr) + imageoffset
    html_imagestrlast = 'style="width:100%" width="387" height="490"'
    imagelastdigit = iteminfo.find(html_imagestrlast)
    htmlimagestr = iteminfo[imagefirstdigit:imagelastdigit]
    htmlimagestr = htmlimagestr.strip()
    # Example string: "OFF-WHITE™ T-shirt Red 100% Cotton" src="https://www.yoox.com/images/items/12/12878834OO_14_f.jpg?impolicy=crop&amp;width=387&amp;height=490"
    # The name of the item, find first " then find second "
    firstcolon = htmlimagestr.find('"')
    secondcolon = htmlimagestr[1:].find('"')
    description = htmlimagestr[firstcolon + 1:secondcolon + 1]
    srclocation = "src="
    firsturl = htmlimagestr.find(srclocation) + 5
    secondurl = len(htmlimagestr) - 1
    url = htmlimagestr[firsturl:secondurl]

    # export this as a dictionary
    result = {"item": description, "url": url, "price": price}

    return result
