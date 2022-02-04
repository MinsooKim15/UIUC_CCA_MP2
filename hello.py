from flask import Flask, request
from flask_caching import Cache
app = Flask(__name__)
config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)


@app.route('/', methods= ["GET"])
def get():
    seed = cache.get("seed")
    if seed != None:
        return str(seed)
    else:
        return str(0)
@app.route('/', methods= ["POST"])
def post():
    params = request.get_json()
    try:
        cache.set("seed", int(params["num"]))
        return "succeed"
    except ValueError:
        return "Failed"


if __name__ == "__main__":
    app.run()