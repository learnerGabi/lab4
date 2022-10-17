#Make this file a minimalist API endpoint that randomly offers a random pick out of 
#15 meal recommendations along with a price
#The endpoint delivers 1 meal recommendation in JSON format

#from html(API) and put the data to database (JSON)
import json
from optparse import Values
from flask import Flask
import random
import json
app = Flask(__name__)

#input from API
@app.route('/pickMeal', methods=['GET'])
def pickMeal():
    mealWithPrice = {
        "Meal1" : "Meal1: 5 dollars",
        "Meal2" : "Meal2: 15 dollars",
        "Meal3" : "Meal3: 25 dollars",
        "Meal4" : "Meal4: 35 dollars",
        "Meal5" : "Meal5: 45 dollars",
        "Meal6" : "Meal6: 55 dollars",
        "Meal7" : "Meal7: 65 dollars",
        "Meal8" : "Meal8: 75 dollars",
        "Meal9" : "Meal9: 85 dollars",
        "Meal10" : "Meal10: 95 dollars",
        "Meal11" : "Meal11: 105 dollars",
        "Meal12" : "Meal12: 115 dollars",
        "Meal13" : "Meal13: 125 dollars",
        "Meal14" : "Meal14: 135 dollars",
        "Meal15" : "Meal15: 145 dollars",
     }

    res = random.choice(list(mealWithPrice.values()))

    #app.logger.info("pickMeal API was called")
    return json.dumps(res)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)