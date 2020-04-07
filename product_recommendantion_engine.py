from tqdm import tqdm
from typing import Dict, List


class RecommendationModel:
    def __init__(self, filename) -> None:
        self.users: Dict[str, List[str]] = {}
        self.filename = filename

    def create_user_sets(self) -> None:
        # print("\nCreating Dictionary...\n")
        for line in tqdm(self.filename):
            user = line.split()[0]
            products = []
            for p in line.split()[1:]:
                products.append(p)
                self.users[user] = products

    def flatter(self, recommendations) -> set:
        flat_list_recommendations = [item for sublist in recommendations for item in sublist]
        return set(flat_list_recommendations)

    def recommend_product(self, products) -> set:
        self.create_user_sets()
        products = list(products)
        recommendations = []

        # print("\nLooking for recommendations...\n")

        for user in tqdm(self.users):
            if set(products).issubset(self.users[user]):
                recommended_product = list(set(self.users[user]) - set(products))
                if len(recommended_product) > 0:
                    recommendations.append(recommended_product)

        # if len(recommendations) == 0:
        #     return None
        return self.flatter(recommendations)
