from flask import Flask, request, jsonify, render_template
from predict import load_model_and_vectorizer, predict_email

app = Flask(__name__)

# Load model and vectorizer
model_path = 'model.pkl'            # Path to your trained model file
vectorizer_path = 'vectorizer.pkl'  # Path to your vectorizer file
model, vectorizer = load_model_and_vectorizer(model_path, vectorizer_path)

@app.route('/')

def home():
    return render_template('index.html')  # Ensure you have an index.html in the templates folder

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()  # Get JSON data from POST request
    email_text = data.get('text', '')  # Get the email text from the request

    if not email_text:
        return jsonify({'error': 'No text provided for analysis'}), 400  # Return error if no text provided

    # Predict whether the email is Spam or Not Spam
    result = predict_email(email_text, model, vectorizer)
    return jsonify({'result': result})  # Return the prediction as JSON



if __name__ == '__main__':
    app.run(debug=True)
