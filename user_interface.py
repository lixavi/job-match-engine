from job_database import JobDatabase
from candidate_database import CandidateDatabase
from job_match_engine import JobMatchEngine

class UserInterface:
    def __init__(self):
        self.job_database = JobDatabase()
        self.candidate_database = CandidateDatabase()
        self.job_match_engine = JobMatchEngine(self.job_database, self.candidate_database)

    def add_job(self, title, description, skills):
        """
        Add a new job to the system.

        Args:
            title (str): Title of the job.
            description (str): Description of the job.
            skills (str): Skills required for the job.
        """
        self.job_database.add_job(title, description, skills)

    def add_candidate(self, name, skills):
        """
        Add a new candidate to the system.

        Args:
            name (str): Name of the candidate.
            skills (str): Skills possessed by the candidate.
        """
        self.candidate_database.add_candidate(name, skills)

    def match_candidates_to_jobs(self):
        """
        Match candidates to available jobs and store the results.
        """
        for candidate in self.candidate_database.get_candidates():
            job_matches = self.job_match_engine.match_jobs(candidate.name)
            setattr(candidate, 'job_matches', job_matches)

    def display_results(self):
        """
        Display the matched jobs for each candidate.
        """
        for candidate in self.candidate_database.get_candidates():
            print(f"Job matches for candidate {candidate.name}:")
            for job, similarity_score in candidate.job_matches:
                print(f" - {job.title} (Similarity Score: {similarity_score})")
            print()  # Empty line for clarity
