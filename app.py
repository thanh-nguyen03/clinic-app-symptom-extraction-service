from flask import Flask, request, jsonify
import spacy

nlp = spacy.load("en_core_sci_sm")

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/extract-symptoms', methods=['POST'])
def extract_symptoms():
    data = request.get_json()
    text = data.get("input", "")

    app.logger.info(f"Received text: {text}")
    doc = nlp(text)

    # Extract symptoms (entities labeled as 'DISEASE' or similar)
    symptoms = [x.text for x in doc.ents]

    return jsonify({
        "symptoms": symptoms
    })


if __name__ == '__main__':
    app.run(port=5000)
