
def create_user_dictionary(file):
    users = {}
    for line in file:
        x = line.split()[0]
        products = []
        for p in line.split()[1:]:
            products.append(p)
            users[x] = products
    return users


def create_product_dictionary(users):
    recommendations = {}
    for user in users:
        for p in users[user]:
            recommendations[p] = []
    return recommendations


def fill_recommendations(recommendations, users):
    for product in recommendations:
        x = []
        for user in users:
            if product in users[user]:
                for other_product in users[user]:
                    if product != other_product:
                        x.append(other_product)

        recommendations[product] = set(x)


def get_product_recommendation(product, recommendations):
    print(f"\nFor the product {product}, We recommend the following:\n {recommendations[product]}\n")