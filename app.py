import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

if __name__ == 'main':
 app.run(debug=True, port=int(os.environ.get('PORT', 5000)))