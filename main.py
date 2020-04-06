from product_recommendantion_engine import create_product_dictionary, create_user_dictionary, fill_recommendations, get_product_recommendation

import sys

filename = 'example.txt'


with open(filename) as f:
    users = create_user_dictionary(f)

print(f"\nUSERS:\n{users}\n")

a = 'Apple'
b = 'Date'
for user in users:
    if a in users[user] and b in users[user]:
        print(f"{user}\n")
# recommendations = create_product_dictionary(users)
# fill_recommendations(recommendations, users)

# for product in sys.argv[1:]:
#     get_product_recommendation(product, recommendations)