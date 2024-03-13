from flask import Flask, render_template
from redis import StrictRedis

app = Flask(__name__)
redis = StrictRedis(host='redis', port=6379, db=0)

@app.route('/')
def index():
    # Increment hit counter in Redis
    redis.incr('hits')
    # Retrieve the current hit count
    hits = redis.get('hits').decode('utf-8')
    return render_template('index.html', hits=hits)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
