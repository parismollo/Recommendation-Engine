# Recommendation Engine


## Try it out !
1. Clone the repo 
* ```git clone [repository URL]```
2. Run the following command to get product recommendations:
* ```python product_recommendation_engine.py AAA ZZZ```

Try with any product or set of products.


## How it works?
The objective of this project is to recommend a product or a list of products for a user. The recommendation is based on the **similiraty of purchases among customers**. 
Example:
* Given a 5 users purchases record dataset (.txt format)

```
U1 AAA BBB CCC
U2 AAA BBB DDD
U3 AAA III LLL
U4 LLL OOO HHH
U5 JJJ EEE SSS
```

Users that consume product AAA and BBB would be (according to the algorithm), recommended to buy product DDD. A python class named *RecommendationModel* is responsible to all the data handling tasks and for the recommendation function, from creating a dictionary with each user purchases, later used for statistical analysis. The class also has the method responsible to recommmend products,the method *recommend_product*.

The method *recommend_product* uses the built-in *set* type in order to verify if the inputs (products) are a subset of other users purchases.

## Project architecture 

The project is composed of 4 main files:

* *recommendation_model.py*:
There you can find the class RecommendationModel, that holds the methods responsible for the recommendation algorithm/logic.

* *main.py*:
Handle the inputs from the parallel algorithm (file *product_recommendation_engine.py*) and call the recommend_product method

* *product_recommendation_engine.py*:
Parallel algorithm 


* *stream_in_splitter.py*:
Split the 1 * 10⁶ rows dataset into 200 files of 5000 rows in order to increase performance and reduce the burden of processig among the cpu's.




