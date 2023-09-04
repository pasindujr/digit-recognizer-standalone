import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import requests
import io
import joblib

model = joblib.load('digit-recognizer-model.pkl')

# Define the preprocess_single_image function
def preprocess_single_image(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image_data = response.content
        threshold = 128

        # Create a PIL Image object from the downloaded image data
        img = Image.open(io.BytesIO(image_data))

        # Resize the image to 28x28 pixels
        img = img.resize((28, 28))

        # Convert the image to grayscale
        img = img.convert('L')

        # Apply thresholding to binarize the image
        img = img.point(lambda p: p < threshold and 255)

        # Normalize the image to [0, 1]
        img_array = np.array(img).astype(np.float32) / 255.0

        return img_array
    except Exception as e:
        print(f"Error preprocessing image: {str(e)}")
        return None

# Define the predict_image function
def predict_image():
    # Get the URL from the input field
    url = url_entry.get()
    print(url)

    # Preprocess the image
    img_array = preprocess_single_image(url)

    if img_array is not None:
        # Reshape the image array to match the input shape expected by the model
        img_array = img_array.reshape(1, 784)

        # Make a prediction using the loaded model
        prediction = model.predict(img_array)
        print(prediction[0])

        # Display the prediction in the label
        prediction_label.config(text=f"Predicted Digit: {prediction[0]}")

        # Display the processed image with a larger size
        img = Image.fromarray((img_array[0] * 255).astype('uint8').reshape(28, 28))
        img = img.resize((200, 200))  # Increase the size here
        img = ImageTk.PhotoImage(image=img)
        image_label.config(image=img)
        image_label.image = img
    else:
        messagebox.showerror("Error", "Invalid URL or image processing failed")

# Create the main window
root = tk.Tk()
root.title("Image Prediction")

# Create and layout GUI components
frame = ttk.Frame(root, padding=10)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

url_label = ttk.Label(frame, text="Enter Image URL:")
url_label.grid(column=0, row=0, sticky=tk.W)

url_entry = ttk.Entry(frame, width=50)
url_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

predict_button = ttk.Button(frame, text="Predict Image", command=predict_image)  # Add padding here
predict_button.grid(column=0, row=1, columnspan=2)

image_label = ttk.Label(frame)
image_label.grid(column=0, row=2, columnspan=2)

prediction_label = ttk.Label(frame, text="")
prediction_label.grid(column=0, row=3, columnspan=2)

# Start the GUI main loop
root.mainloop()
