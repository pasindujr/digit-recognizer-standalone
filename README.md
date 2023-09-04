# Digit Recognizer Standalone

## Table of Contents
- [Project Description](#project-description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Project Description

This project is a simple yet powerful example of digit recognition using Python and Machine Learning. It leverages a trained machine learning model to predict the digit contained within an image provided via a URL. The project includes a graphical user interface (GUI) built with Tkinter to make it user-friendly and accessible.

## Requirements

The external libraries and dependencies required to run your project. You can generate a "requirements.txt" file using `pip freeze > requirements.txt`:

```bash
# requirements.txt
certifi==2023.7.22
charset-normalizer==3.2.0
idna==3.4
joblib==1.3.2
numpy==1.25.2
Pillow==10.0.0
requests==2.31.0
scikit-learn==1.3.0
scipy==1.11.2
threadpoolctl==3.2.0
urllib3==2.0.4
```

## Installation

```python
# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install project dependencies
pip install -r requirements.txt

```

## Usage

```python
# Run the project
python main.py
```
<ol>
  <li>Launch the application.</li>
  <li>Enter the URL of an image containing a handwritten digit in the input field.</li>
  <li>Click the "Predict" button.</li>
  <li>View the predicted digit and the processed image.
</li>
</ol>


