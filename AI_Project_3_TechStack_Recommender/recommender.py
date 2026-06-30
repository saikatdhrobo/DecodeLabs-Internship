import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TechStackRecommender:

    def __init__(self, csv_path):

        self.data = pd.read_csv(csv_path)

        # TF-IDF Vectorizer

        self.vectorizer = TfidfVectorizer(stop_words="english")

        # Convert all skills into vectors

        self.skill_vectors = self.vectorizer.fit_transform(
            self.data["Skills"]
        )

    def recommend(self, user_skills, top_n=3):

        # Convert list to sentence

        user_profile = " ".join(user_skills)

        # Convert user profile into TF-IDF vector

        user_vector = self.vectorizer.transform([user_profile])

        # Cosine Similarity

        similarity = cosine_similarity(
            user_vector,
            self.skill_vectors
        ).flatten()

        # Add scores

        self.data["Score"] = similarity

        # Sort descending

        recommendations = self.data.sort_values(
            by="Score",
            ascending=False
        )

        return recommendations.head(top_n)