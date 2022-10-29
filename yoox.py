"""
Module for accessing and using Yoox.com

Author: Wilson Wong
Date: 10-17-2022
"""

import requests
from html.parser import HTMLParser
import json

def is_number(s):
    """
    Taken from https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-represents-a-number-float-or-int
    Checks if the the string is a number by trying to make it a float.
    s: some string to check
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_yoox_item(sku,section,gender,size):
    """
    Given a sku from Yoox, retrieve the price, description, and image of the item. Gender is needed
    to see what side of the store to retrieve.

    Parameter sku: A valid sku from yoox.com
    Parameter section: String of the section of the website it is in
    Preconditon: valid sections are clothing, shoes, accessories, sale
    Parameter gender: men or women are valid.
    Parameter size: Size of the item. If it is shoes, 6-13US are valid. If it's clothing, XXS-XXL, and if it's pants, XXS-XXL or 28-36.
    """
    # xxxs = 1, xxs= 2, xs = 3, s=4, m=5, l=6
    # shoe sizes
    # id 3 is 6, 4 is 6.5, 5 is 7, 6 is 7.5, 7 is 8, 8 is 8.5, 9 is 9, 10 is 9.5, 11 is 10
    # pants size
    # id 4 s 30, id 5 is 31, id 6 is 32

    if is_number(size) == True:
        # Shoe sizes are under 15
        if float(size) < 16.0 and section == "shoes":
            size = float(size)
            if size == 6:
                sizeid = 3
            elif size == 6.5:
                sizeid = 4 
            elif size == 7:
                sizeid = 5
            elif size == 7.5:
                sizeid = 6
            elif size == 8:
                sizeid = 7
            elif size == 8.5:
                sizeid = 8
            elif size == 9:
                sizeid = 9
            elif size == 9.5:
                sizeid = 10
            elif size == 10:
                sizeid = 11
            elif size == 10.5:
                sizeid = 12
            elif size == 11:
                sizeid = 13
            elif size == 11.5:
                sizeid = 14
            elif size == 12:
                sizeid = 15
            elif size == 12.5:
                sizeid = 16
            elif size == 13:
                sizeid = 17
        # pants sizes are usually start at 28 and up
        if float(size) > 25.0 and section == "clothing":
            size = float(size)
            # Very odd but size 26 has an id of 10
            if size == 26:
                sizeid = 10
            elif size == 28:
                sizeid = 1
            elif size == 30:
                sizeid = 2
            elif size == 32:
                sizeid = 3
            elif size == 34:
                sizeid = 4
            elif size == 36:
                sizeid = 5
            elif size == 38:
                sizeid = 6
    elif size.isalpha() == True:
        if size == "XXXS":
            sizeid = 1
        elif size == "XXS":
            sizeid = 2
        elif size == "XS":
            sizeid = 3
        elif size == "S":
            sizeid = 4
        elif size == "M":
            sizeid = 5
        elif size == "L":
            sizeid = 6
        elif size == "XL":
            sizeid = 7
        elif size == "XXL":
            sizeid = 8
    else:
        # -1 is as if the size doesn't exist.
        sizeid = -1
    
    url = "https://www.yoox.com/us/" + sku + "/item#dept=" + section + gender + "&sizeid=" + str(sizeid)
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

    # Find sizes. Example dictionary [{"availableSizesIds":[{"id":2,"quantity":1}]
    html_sizestr = '[{"availableSizesIds":['
    sizelistfirst = iteminfo.find(html_sizestr)
    sizelistlast = iteminfo[sizelistfirst:].find("]")
    sizes = iteminfo[sizelistfirst + 22 :sizelistfirst + sizelistlast + 1]
    sizelist = list(eval(sizes))
    quantity = 0
    for s in sizelist:
        if s.get("id") == sizeid:
            quantity = s.get("quantity")
    # export this as a dictionary
    result = {"item": description, "url": url, "price": price, "size": size, "quantity": quantity}

    return result