# importing relavent libraries
import pickle
from flask import Flask, request, render_template
from keras.models import load_model
from PIL import Image
import numpy as np

app = Flask(__name__) # created a Flask application instance

# loading pre-trained model
with open('m1.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


# loading phishing detection model
phishing_detection_model = load_model('phishing_detection_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/desc')
def phishing_description():
    # rendering the phishing description page
    return render_template('desc.html')

@app.route('/dl')
def deep_learning_model():
    # endering the dl.html page
    return render_template('dl.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            # getting the user's input from the form
            domain = request.form.get('domainInput')

            # removing "https://" if it is in the input
            if domain.startswith("https://"):
                domain = domain[len("https://"):]

            # making predictions using the loaded model
            result = model.predict([domain])  # sending the domain as a string

            # mapping the result to "secure" or "non-secure"
            if result[0] == 'good':
                label = "This website is Secure."
            else:
                label = "This website is potentially a Phishing Threat."

            # Display the result
            return render_template('home.html', result=label)
        except Exception as e:
            return str(e)
    else:
        # handle GET requests for the same route (e.g., initial page load)
        return render_template('home.html')
    
@app.route('/predict_image', methods=['POST'])
def predict_image():
    try:
        # checking if an image file is provided
        if 'image' not in request.files:
            return "No image file provided."

        # getting the uploaded image file
        image_file = request.files['image']

        # ensuring the file has an allowed extension (e.g., only accept 'jpg' and 'png')
        allowed_extensions = {'jpg', 'jpeg', 'png'}
        if not image_file.filename.lower().endswith(tuple(allowed_extensions)):
            return "Invalid image file format. Allowed formats are JPG and PNG."

        # loading and preprocess the image using PIL
        img = Image.open(image_file)
        img = img.convert('RGB')  # ensuring it's in RGB format
        img = img.resize((224, 224))  # resizing the image to match the VGG16 input size
        img = np.array(img)
        img = np.expand_dims(img, axis=0)

        # using the phishing_detection_model for prediction
        phishing_prediction = phishing_detection_model.predict(img)

        # interpreting the phishing_detection_model prediction result
        if phishing_prediction > 0.5:
            phishing_result = "This website is potentially a Phishing Threat."
        else:
            phishing_result = "This website is Secure."

        return f"Prediction: {phishing_result}"

    except Exception as e:
        return str(e)



if __name__ == "__main__":
    app.run(debug=True)