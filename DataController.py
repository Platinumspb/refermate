from DataProvider.GoogleSheetsDataProvider import GoogleSheetsDataProvider
from JobModel import JobModel


class DataController:

    def get_list_of_jobs_from_google_sheets(self):
        data_provider = GoogleSheetsDataProvider()
        creds = data_provider.authenticate()
        return data_provider.get_jobs(creds)

    def create_job_model_list(self, list_of_jobs):
        list_of_job_models = []
        for job in list_of_jobs:
            job_model = JobModel(job)
            list_of_job_models.append(job_model)
        return list_of_job_models
