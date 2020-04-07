import sys
from product_recommendantion_engine import RecommendationModel


def run():
    filename = 'data.txt'
    products = []

    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            products.append(arg.upper())
    else:
        raise TypeError('Missing arguments. Please type one or multiple products\n Ex: main.py AAA\n')

    re = RecommendationModel(filename)
    print(f"\n", *re.recommend_product(products), "\n", sep=' ')


if __name__ == "__main__":
    run()
