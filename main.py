from user_interface import UserInterface

if __name__ == "__main__":
    ui = UserInterface()
    
    # Example usage: adding jobs and candidates to the database
    ui.add_job("Software Developer", "Develop software applications using Python and Java", "Python, Java, Software Development")
    ui.add_job("Data Scientist", "Analyzing data using machine learning algorithms", "Machine Learning, Data Analysis, Python")
    ui.add_candidate("Alice", "Python, Data Analysis, SQL")
    ui.add_candidate("Bob", "Java, Software Development, Algorithms")
    
    # Matching candidates to jobs
    ui.match_candidates_to_jobs()
    
    # Displaying the results
    ui.display_results()
