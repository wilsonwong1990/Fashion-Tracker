"""
Slack helper file for the Fashion Tracker repository.
Author: Wilson Wong
Date: 11-17-2022
"""

from slack_sdk.webhook import WebhookClient
url = "https://hooks.slack.com/services/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"
webhook = WebhookClient(url)

def send_slack(text):
    """
    Send a Slack message into the Slack channel via the webhook url above.

    Parameter text: A string
    """
    response = webhook.send(text)
    assert response.status_code == 200
    assert response.body == "ok"