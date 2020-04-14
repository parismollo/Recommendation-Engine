from tqdm import tqdm
from typing import Dict, List


class RecommendationModel:
    def __init__(self, filename) -> None:
        self.users: Dict[str, List[str]] = {}
        self.filename = filename

    def create_user_sets(self) -> None:
        # print("\nCreating Dictionary...\n")
        for line in self.filename:
            if len(line.split()) > 0:
                user = line.split()[0]
                products = []
                for p in line.split()[1:]:
                    products.append(p)
                    self.users[user] = products
            else:
                continue

    def flatter(self, recommendations) -> set:
        flat_list_recommendations = [item for sublist in recommendations for item in sublist]
        return set(flat_list_recommendations)

    def recommend_product(self, products) -> set:
        self.create_user_sets()
        products = list(products)
        recommendations = []

        # print("\nLooking for recommendations...\n")

        for user in self.users:
            if set(products).issubset(self.users[user]):
                recommended_product = list(set(self.users[user]) - set(products))
                if len(recommended_product) > 0:
                    recommendations.append(recommended_product)

        # if len(recommendations) == 0:
        #     return None
        return self.flatter(recommendations)

    def most_similar_users(self, user_input):
        user_points = {}
        for user in tqdm(self.users):
            if user != user_input:
                a = self.users[user_input]
                b = self.users[user]
                points = len(set(a) & set(b))
                if points >= 1:
                    user_points[user] = points
        return user_points

    def most_similar_products(self, user_input):
        users_points = self.most_similar_users(user_input)
        if len(users_points) > 0:
            print(f"\nYour products: {self.users[user_input]} - USER: {user_input}\n")
            counter = 0
            print("\n       ---------TOP 10 Recommendations---------\n")
            for k in sorted(users_points, key=users_points.get, reverse=True):
                counter += 1
                if counter < 11:
                    print(f"{k}: {list(self.users[k])} - {users_points[k]} similar product(s)")
                else:
                    break
        else:
            print('No similar purchases...')
