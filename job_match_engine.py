from nlp_utils import preprocess_text, calculate_text_similarity

class JobMatchEngine:
    def __init__(self, job_database, candidate_database):
        self.job_database = job_database
        self.candidate_database = candidate_database

    def match_jobs(self, candidate_name):
        """
        Match jobs to a candidate based on their skills.

        Args:
            candidate_name (str): Name of the candidate to match jobs for.

        Returns:
            list: List of tuples containing matched jobs and their similarity scores.
        """
        candidate = self.candidate_database.find_candidate_by_name(candidate_name)
        if not candidate:
            print(f"Candidate '{candidate_name}' not found in the database.")
            return []

        candidate_skills = preprocess_text(candidate.skills)
        job_matches = []
        for job in self.job_database.get_jobs():
            job_skills = preprocess_text(job.skills)
            similarity_score = calculate_text_similarity(" ".join(candidate_skills), " ".join(job_skills))
            job_matches.append((job, similarity_score))
        return sorted(job_matches, key=lambda x: x[1], reverse=True)

    def recommend_jobs(self, candidate_name, num_recommendations=5):
        """
        Recommend top jobs for a candidate based on their skills.

        Args:
            candidate_name (str): Name of the candidate.
            num_recommendations (int): Number of jobs to recommend.

        Returns:
            list: List of recommended job titles.
        """
        matched_jobs = self.match_jobs(candidate_name)
        recommended_jobs = [job[0].title for job in matched_jobs[:num_recommendations]]
        return recommended_jobs
