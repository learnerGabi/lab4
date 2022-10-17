# Make this file a minimalist API consumer 
# that displays the random meal recommendation 
# along with the price 
# (use a HTML template)

from flask import Flask
import requests
app = Flask(__name__)

@app.route('/consume')
def consumeAPI():
    print("test consumer")
    r = requests.get('http://api:6000/pickMeal')
    
    return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)