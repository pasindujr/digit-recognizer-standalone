import tkinter as tk
from tkinter import messagebox
import re


# Function to validate a URL
def is_valid_url(url):
    # Use a regular expression to check for a valid URL pattern
    url_pattern = re.compile(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')
    return re.match(url_pattern, url)


# Function to save the URL to a variable
def save_url():
    url = url_entry.get()
    if is_valid_url(url):
        # URL is valid, save it to a variable
        global saved_url
        saved_url = url
        messagebox.showinfo("Success", "URL saved successfully!")
    else:
        messagebox.showerror("Error", "Invalid URL. Please enter a valid URL.")


# make window size bigger
root = tk.Tk()
root.geometry("500x500")
# change title
root.title("Digit Recognizer")

# Create a label and an entry widget for the URL
# add some margin above the label
url_label = tk.Label(root, text="Enter URL:", pady=10)
url_entry = tk.Entry(root, width=40)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=save_url)

# Pack the widgets to add them to the window
url_label.pack()
url_entry.pack()
submit_button.pack()

# Initialize the saved_url variable
saved_url = None

root.mainloop()
