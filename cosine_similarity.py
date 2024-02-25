import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(vector1, vector2):
    """
    Calculate cosine similarity between two vectors.

    Args:
        vector1 (list or numpy array): First vector.
        vector2 (list or numpy array): Second vector.

    Returns:
        float: Cosine similarity between the two vectors.
    """
    if len(vector1) == 0 or len(vector2) == 0:
        return 0.0
    
    # Convert lists to numpy arrays
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    
    # Calculate cosine similarity
    similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    return similarity

def calculate_similarity_matrix(vectors):
    """
    Calculate cosine similarity matrix for a list of vectors.

    Args:
        vectors (list of lists or numpy arrays): List of vectors.

    Returns:
        numpy array: Cosine similarity matrix.
    """
    num_vectors = len(vectors)
    similarity_matrix = np.zeros((num_vectors, num_vectors))
    for i in range(num_vectors):
        for j in range(num_vectors):
            similarity_matrix[i][j] = calculate_cosine_similarity(vectors[i], vectors[j])
    return similarity_matrix
