import os
import sys
import json
import random
import re
from sets import Set

# to transform the json formated input file and saved the transformed data in training file
if __name__ == "__main__":
    input_file = sys.argv[1]
    word2vec_training_file = sys.argv[2]


    word2vec_training = open(word2vec_training_file, "w")

    with open(input_file, "r") as lines:
        for line in lines:
            entry = json.loads(line.strip())
            # stripe() remove all white space in line or stripe(c) remove all c in line
            #json.loads() decode the json formatted doc. into python object
            # json object is transfered into python dist (map)
            # json format: { lablei : valuei, label1: value1, ..
}
    # entry is a map, if it contains title, adID, query,
    # 把json file中，每一line 中的 title 对应的value 解析出来，存入variable title，
    #
            if  "title" in entry and "adId" in entry and "query" in entry:
                    title = entry["title"].lower().encode('utf-8')
                    query = entry["query"].lower().encode('utf-8')

                    #remove number from query
                    new_query_tokens = []
                    query_tokens = query.split(" ")
                    for q in query_tokens:
                        if q.isdigit() == False and len(q) > 1:
                            new_query_tokens.append(q)

                    new_title_tokens = []
                    title_tokens = title.split(" ")
                    for t in title_tokens:
                        if t.isdigit() == False and len(t) > 1:
                            new_title_tokens.append(t)
                    
                    query = " ".join(new_query_tokens)
                    title = " ".join(new_title_tokens)
                    
                    word2vec_training.write(query)
                    word2vec_training.write(" ")
                    word2vec_training.write(title)
                    word2vec_training.write('\n')

  word2vec_training.close()
