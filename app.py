from flask import Flask
from redis import StrictRedis

app = Flask(__name__)
redis = StrictRedis(host='redis', port=6379, encoding='utf-8', decode_responses=True)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)