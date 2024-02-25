from job import Job

class JobDatabase:
    def __init__(self):
        self.jobs = []

    def add_job(self, title, description, skills):
        """
        Add a new job to the database.

        Args:
            title (str): Title of the job.
            description (str): Description of the job.
            skills (str): Skills required for the job.
        """
        job = Job(title, description, skills)
        self.jobs.append(job)

    def remove_job(self, job):
        """
        Remove a job from the database.

        Args:
            job (Job): Job object to be removed.
        """
        if job in self.jobs:
            self.jobs.remove(job)
        else:
            print(f"{job.title} is not in the database.")

    def get_jobs(self):
        """
        Get all jobs from the database.

        Returns:
            list: List of Job objects.
        """
        return self.jobs

    def find_job_by_title(self, title):
        """
        Find a job by its title.

        Args:
            title (str): Title of the job to find.

        Returns:
            Job or None: Job object if found, else None.
        """
        for job in self.jobs:
            if job.title == title:
                return job
        return None
