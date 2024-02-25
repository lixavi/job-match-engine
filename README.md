# Job Match Engine

This is a Python-based job matching system using NLP techniques and cosine similarity algorithms for skill and job alignment.

## Overview

The job match engine consists of multiple components:

- `main.py`: Entry point of the program.
- `job.py`: Defines the Job class.
- `candidate.py`: Defines the Candidate class.
- `nlp_utils.py`: Contains NLP utilities for processing text data.
- `cosine_similarity.py`: Implements cosine similarity calculation.
- `job_database.py`: Manages the database of available jobs.
- `candidate_database.py`: Manages the database of candidates.
- `job_match_engine.py`: Implements the core logic of the job matching engine.
- `user_interface.py`: Provides the user interface for interacting with the system.
- `requirements.txt`: Contains the required dependencies for the project.

## Usage

1. First, ensure you have all dependencies installed by running:
    ```
    pip install -r requirements.txt
    ```

2. Then, run the main script:
    ```
    python main.py
    ```

3. Follow the instructions in the user interface to add jobs, candidates, match candidates to jobs, and view the results.

## Dependencies

- `nltk`: Natural Language Toolkit for NLP processing.
- `scikit-learn`: Library for machine learning algorithms.
- `numpy`: Library for numerical computing.
