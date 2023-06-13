from flask import Flask
from custom_point_instantiator import get_custom_point_value

app = Flask(__name__)


@app.route("/get_custom_point_value/<custom_point>")
def get_custom_point_value(custom_point):
    return get_custom_point_value(custom_point)


if __name__ == "__main__":
    app.run(debug=True)
