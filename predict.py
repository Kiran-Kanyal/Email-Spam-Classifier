import pickle

def load_model_and_vectorizer(model_path, vectorizer_path):
    """Load the model and vectorizer from specified paths."""
    with open(model_path, 'rb') as model_file, open(vectorizer_path, 'rb') as vectorizer_file:
        model = pickle.load(model_file)
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

def predict_email(email_text, model, vectorizer):
    """Predict whether the email is spam or not."""
    # Transform the email text using the loaded vectorizer
    email_transformed = vectorizer.transform([email_text])

    # Predict using the loaded model
    prediction = model.predict(email_transformed)

    # Return prediction as a string ('Spam' or 'Not Spam')
    result = 'Spam' if prediction[0] == 1 else 'Not Spam'
    return result

# Example usage
if __name__ == "__main__":
    model_path = 'model.pkl'          # Path to your trained model file
    vectorizer_path = 'vectorizer.pkl' # Path to your vectorizer file

    # Load model and vectorizer
    model, vectorizer = load_model_and_vectorizer(model_path, vectorizer_path)

    # Example email text for prediction
    email_text = "Congratulations! You have won a $1,000 gift card. Claim it now!"
    result = predict_email(email_text, model, vectorizer)
    print(f'Prediction: {result}')
