from flask import Flask, render_template, jsonify, request
import pickle, pandas

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def mainpage():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	content = request.json

	filename = 'finalized_model.sav'
	# load the model from disk
	loaded_model = pickle.load(open(filename, 'rb'))


	for fieldname in content:
		content[fieldname] = [content[fieldname]]

	X_input = pandas.DataFrame(content)

	result = loaded_model.predict(X_input)

	return jsonify(result= result[0])
