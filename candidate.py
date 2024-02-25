class Candidate:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.applications = []

    def apply_for_job(self, job):
        if job not in self.applications:
            self.applications.append(job)
            job.add_applicant(self)
        else:
            print(f"{self.name} has already applied for {job.title}")

    def withdraw_application(self, job):
        if job in self.applications:
            self.applications.remove(job)
            job.remove_applicant(self)
        else:
            print(f"{self.name} has not applied for {job.title}")

    def get_applications(self):
        return self.applications
