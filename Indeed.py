from Nav import nav
from JobBoard import *

class Indeed(JobBoard):
    # Select the correct Date Bin For Filtering
    def __minDateBin__(self, date_bins):
        for i in range(len(date_bins)):
            if self.days_ago<=date_bins[i][0]:
                return i
        return "Nope"
    
    def __init__(self, JobTitle, JobLocation, DaysAgo):
        super().__init__(JobTitle, JobLocation, DaysAgo)
        
        
        def addJobs(available_jobs):
            raw = soup(self.browser.html, 'html.parser').html
            raw.find_all("li", class_="css-5lfssm")
            for job in raw.find_all("div", class_="cardOutline"):
                available_jobs["job_title"].append(job.find("span").get_text())
                available_jobs["company"].append(job.find("span", class_="css-1x7z1ps eu4oa1w0").get_text())
                available_jobs["location"].append(job.find("div", class_="css-t4u72d eu4oa1w0").get_text())
                available_jobs["job_search"].append(self.job_title)
                available_jobs["date_range"].append(self.days_ago)
            return pd.DataFrame(available_jobs)

        
        ## Navigation
        # Visit Dice
        self.browser.visit("http://www.indeed.com") 
        # Fill Job
        self.browser.find_by_css("#text-input-what").fill(self.job_title)
        # Fill Job's Location
        self.browser.find_by_css("#text-input-where").clear()
        self.browser.find_by_css("#text-input-where").fill(self.job_location)
        # Click on Search
        self.__click__(nav["Indeed"]["click1"])
        
        
        ## Filter Jobs
        # Select Date Range
        time.sleep(random()*4+2)
        self.browser.find_by_id("filter-dateposted").click()
        date_range = self.__minDateBin__([(1, "last_24_hours"),
                                          (3, "last_3_days"),
                                          (7, "last_7_days"),
                                          (14, "last_14_days")])
        if date_range != "Nope":
            time.sleep(random()*2)
            date_selections=self.browser\
                .find_by_css(".is-dropdownOpen")[0]\
                .find_by_css("li")
            date_selections[date_range].click()
    
    
        ## Add Jobs
        available_jobs = {"job_title": [], "company": [],  "location": [], "job_search": [], 
                          "date_range": []}
        self.available_jobs = addJobs(available_jobs)