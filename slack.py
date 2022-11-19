"""
Slack helper file for the Fashion Tracker repository.
Author: Wilson Wong
Date: 11-17-2022
"""
import os
import utils
from slack_sdk.webhook import WebhookClient

url = os.environ['SLACK_PRICEDROP_WEBHOOK']
#print(str(url))
webhook = WebhookClient(url)

def send_slack(message):
    """
    Send a Slack message into the Slack channel via the webhook url above.

    Parameter message: A string
    """
    response = webhook.send(text=message)
    assert response.status_code == 200
    assert response.body == "ok"

# Import store-csvs
# Check if current price is lower than last price
# Check if current price is lower than lowest price
# If either is true, send a slack message with price changes and url

yooxlist = utils.import_csv("store-csvs/yoox.csv")

for item in yooxlist:
    itemdescription = item[0]
    itemdescription = itemdescription.strip("'")
    itemurl = item[1]
    itemprice = item[2]
    itemsize = item[3]
    itemsize = itemsize.strip("'")
    itemquantity = item[4]
    itemsection = item[5]
    itemsection = itemsection.strip("'")
    itemgender = item[6]
    itemgender = itemgender.strip("'")
    itemsku = item[7]
    itemsku = itemsku.strip("'")
    itemlastprice = item[8]
    itemlastprice = itemlastprice.strip("'")
    itemlowprice = item[9]
    itemlowprice = itemlowprice.strip("'")
    
    if (itemprice == itemlowprice) and (itemprice != itemlastprice):
        message = "Lowest price detected" + '\n' + "Item: " + str(itemdescription) + '\n' + "Current Price: " + str(itemprice) + '\n' + "Last Price: " + str(itemlastprice) + '\n' + str(url)
    elif itemprice < itemlastprice:
        message = "Lower price detected" + '\n' + "Item: " + str(itemdescription) + '\n' + "Current Price: " + str(itemprice) + '\n' + "Last Price: " + str(itemlastprice) + '\n' + str(url)
    # Debugging test
    else:
        message = "Testing ignore" + '\n' + "Item: " + str(itemdescription) + '\n' + "Current Price: " + str(itemprice) + '\n' + "Last Price: " + str(itemlastprice) + '\n' + str(url)
    send_slack(message)