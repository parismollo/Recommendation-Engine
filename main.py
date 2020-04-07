import sys
from product_recommendantion_engine import RecommendationModel

filename = sys.stdin
products = sys.argv[1]


def replaceMultiple(mainString, toBeReplaces, newString):
    for elem in toBeReplaces:
        if elem in mainString:
            mainString = mainString.replace(elem, newString)

    return mainString


def str_to_list(products):
    products_str = replaceMultiple(products, ['\n', '\r', "'"], "")
    products_list = products_str.strip('][').split(', ')
    return products_list


re = RecommendationModel(filename)
print(f"\n", *re.recommend_product(str_to_list(products)), "\n", sep=' ')
