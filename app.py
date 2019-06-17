from flask import Flask, request, jsonify


# load the app
# anything that is going to be called can be loaded right here as well
# such as a model (instead of loading it with each call)
app = Flask(__name__)

# simple GET example
@app.route('/')
def index():
    return "Hello, World!"

# POST example
@app.route('/predict', methods=['POST'])
def predict_number():
    number = request.json["number"]

    # NB you have to return a string
    # there are a few exceptions
    return str(number * 4)

if __name__ == '__main__':
    app.run(debug=True)

