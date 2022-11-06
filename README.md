## Fashion Tracker 

Utilizing GitHub Actions and GitHub Pages to query for a list of items on various fashion websites to track the price and quantity over time. 

Currently works for:

    - Yoox.com

## Intro

An all in one pricing and quantity tracker for some fashion sites. The [main page](https://blog.wwong.me/Fashion-Tracker/) is hosted via GitHub Pages on the `gh-pages` branch. This branch uses [derekeder/csv-to-html-table](https://github.com/derekeder/csv-to-html-table) with some few modifications to `index.html` to create hyperlinks and display images.

Items are added via GitHub Issues in this format:

```
sku
gender
section
size
```

When an issue is added, a [GitHub Action](https://github.com/wilsonwong1990/Fashion-Tracker/blob/main/.github/workflows/issues-to-items.yml) is triggered and runs a python script `gh-issues.py` to add the item to the `store-csvs\yoox.csv` on the `gh-pages` branch. GitHub Actions then redeploys the GitHub Page to update this information.

### Adding items via Slack using Zapier

A very simple Zapier App is used to forward Slack messages to a GitHub Issue:

https://zapier.com/shared/slack-to-github/522ef3d29f86b299658c192e7c2fd117a2b1b86f

In the same format as above, an issue is opened via Slack which then triggers the GitHub Action.



## To Do

* [ ] Fix quantity checker in yoox.py. Currently always reports 1
* [ ] Add GitHub Action to update prices periodically
* [ ] Add a remove item function or auto remove when quantity drops to 0
* [ ] Only trigger the Add Item Action when the label is `new item`

