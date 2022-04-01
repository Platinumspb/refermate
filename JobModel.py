import re

class JobModel:
    client: str
    position: str
    referral_bonus: str
    location: str
    salary_range: str
    remote: str
    view_details_link: str
    submit_candidate_link: str

    def __init__(self, job):
        self.client = job[0]
        self.position = job[1]
        self.referral_bonus = job[2]
        self.location = job[3]
        self.salary_range = job[4]
        self.remote = job[5]
        self.view_details_link = self.normalize_url(job[6])
        self.submit_candidate_link = self.normalize_url(job[7])

    def normalize_url(self, link):
        link.replace("['", "").replace("']", "")
        return link
