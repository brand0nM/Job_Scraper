from Nav import nav
from JobBoard import *

class Dice(JobBoard):
    def __init__(self, JobTitle, JobLocation, DaysAgo):
        super().__init__(JobTitle, JobLocation, DaysAgo)

            
        ## Scroll Pages and add Available Jobs List
        def getJobs(available_jobs, page):
            # Collect Unique Jobs as a Tile
            def addJobs(available_jobs):
                raw = soup(self.browser.html, 'html.parser').html
                for job in raw.find_all("dhi-search-card"):
                    available_jobs["company"].append(job.find("a", class_="ng-star-inserted").get_text())
                    available_jobs["job_title"].append(job.find("a", class_="card-title-link normal").get_text())
                    available_jobs["description"].append(job.find("div", class_="card-description").get_text())
                num_listings = math.ceil(int(raw.find_all("span")[3].get_text())/20)\
                    if (self.job_location.lower()=="remote") else \
                    math.ceil(int(raw.find_all("span")[4].get_text())/20)
                return (available_jobs, num_listings)
            time.sleep(2)
            new_jobs = addJobs(available_jobs)
            self.browser.find_by_css(".pagination > li")[-1].click()
            return new_jobs[0] if page==new_jobs[1] else getJobs(new_jobs[0], page+1)
        
        
        ## Navigation
        # Visit Dice
        self.browser.visit("http://www.dice.com") 
        # Fill Job
        self.__fill__(nav["Dice"]["fill1"], self.job_title)
        # Fill Job's Location
        self.__fill__(nav["Dice"]["fill2"], self.job_location)
        # Click on Search
        self.__click__(nav["Dice"]["click1"])

        
        ## Filter Results
        # Select in Person- If non remote else
        if self.job_location.lower()=="remote":
            self.__click__(nav["Dice"]["click2"]["remote"])
        else:
            self.__click__(nav["Dice"]["click2"]["in-person"]) 
        # Select Date Range
        date_bin = self.__minDateBin__([(0, "last_day"),(1, "last_3"),(6, "last_7")])
        if date_bin != "Nope":
            self.__click__(nav["Dice"]["click3"][date_bin])
    
    
        ## Add Jobs
        available_jobs = {"company": [], "job_title": [], "description": []}            
        self.available_jobs = pd.DataFrame(getJobs(available_jobs, 1))