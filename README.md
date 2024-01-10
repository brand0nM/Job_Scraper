# Job Scraper
## Overview
Finding the right job can be a time-consuming process. This package automates the collection of this job data from the top 6 search engines, LinkedIn, ZipRecruiter, Indeed, Monster, Dice, and Google.

### Purpose
Using selenium, beautifulSoup, and pyautogui this python-based webscraper has three main functions.

It first navigates a job board's homepage and searches for the user's specified job title/location.

Then, it will filter the results (in the website) by widening the search radius (to within 100 miles), excluding remote positions (if not remote), and 
eliminating jobs outside the search window's timeframe.

Finally, it writes each dataframe to its respective subdirectory with the date and whether the search was remote.
## Demo

https://github.com/brand0nM/Job_Scraper/assets/79609464/bac82b4f-4139-471f-8979-2b288c595715


## Summary
This package allows for easy automation of scraping job data. Using a scheduler like chron, one can set and leave this script- only considering the aggregated job's data.
