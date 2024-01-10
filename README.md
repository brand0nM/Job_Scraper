# Job Scraper
## Overview
Finding the right job can be a time consuming process. This package automates the collection of this data, and allows the user to spend less time scowering the web.

### Purpose
Using selenium, beautifulSoup, and pyautogui this python based webscraper has three main functions.

It first navigates a job board's homepage and search for the user's specfied job title/location.

Then, it will filter the returned results by widdening the search radius (to within 100 miles), excluding remote positions (if not remote), and 
eliminating jobs outside of the search windows timeframe.

Finally, Writing each dataframe to its respective subdireectory with the date and whether the search was remote.
## Demo
![Demo]("https://youtu.be/aaF_v897k6c")

## Summary
This package allows for easy automation of scraping job data. Using a scheduler like chron, one can set and leave this script- only considering the aggregated job's data.
