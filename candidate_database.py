from candidate import Candidate

class CandidateDatabase:
    def __init__(self):
        self.candidates = []

    def add_candidate(self, name, skills):
        """
        Add a new candidate to the database.

        Args:
            name (str): Name of the candidate.
            skills (str): Skills possessed by the candidate.
        """
        candidate = Candidate(name, skills)
        self.candidates.append(candidate)

    def remove_candidate(self, candidate):
        """
        Remove a candidate from the database.

        Args:
            candidate (Candidate): Candidate object to be removed.
        """
        if candidate in self.candidates:
            self.candidates.remove(candidate)
        else:
            print(f"{candidate.name} is not in the database.")

    def get_candidates(self):
        """
        Get all candidates from the database.

        Returns:
            list: List of Candidate objects.
        """
        return self.candidates

    def find_candidate_by_name(self, name):
        """
        Find a candidate by their name.

        Args:
            name (str): Name of the candidate to find.

        Returns:
            Candidate or None: Candidate object if found, else None.
        """
        for candidate in self.candidates:
            if candidate.name == name:
                return candidate
        return None
