import sys
from recommendation_model import RecommendationModel

user_input = sys.argv[1].capitalize()
filename = sys.stdin

if user_input[0] == 'U' and user_input[-1].isdigit():
    re = RecommendationModel(filename)
    re.create_user_sets()
    re.most_similar_products(user_input)
else:
    print('Please user the following writing: U[number]\n Ex: U10')
