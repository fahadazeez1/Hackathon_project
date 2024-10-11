import tkinter as tk
from PIL import Image, ImageTk

# Create the main window with a fixed geometry
root = tk.Tk()
root.geometry('1500x700')

# Load the main background image using PIL
bg_image = Image.open("assets/img/tempp.jpg")  # Main background image path
bg_image = bg_image.resize((1500, 700), Image.Resampling.LANCZOS)  # Resize to fit window 1500x700
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Label widget to hold the main background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire window

# Function to create a labeled entry with a background image
def create_labeled_entry(text, x, y, image_path):
    # Load the background image for the label
    field_image = Image.open(image_path)
    field_image = field_image.resize((300, 50), Image.Resampling.LANCZOS)  # Resize for the entry background
    field_photo = ImageTk.PhotoImage(field_image)

    # Create a Label with the background image
    label_bg = tk.Label(root, image=field_photo)
    label_bg.image = field_photo  # Keep a reference to avoid garbage collection
    label_bg.place(x=x, y=y)

    # Create a Label for the field name
    tk.Label(root, text=text, bg='white', font=("Arial", 14)).place(x=x + 10, y=y + 5)

    # Create an Entry field and return it
    entry = tk.Entry(root)
    entry.place(x=x + 100, y=y + 5)  # Place entry next to the label
    return entry  # Return the entry widget

# Create labeled entries with background images for each field and store them in variables
name_entry = create_labeled_entry("Name:", 100, 50, "assets/img/tempp.jpg")  # Field background
email_entry = create_labeled_entry("Email:", 440, 50, "assets/img/tempp.jpg")  # Field background
phone_entry = create_labeled_entry("Phone:", 780, 50, "assets/img/tempp.jpg")  # Field background
phone_entry2 = create_labeled_entry("Dob:", 100, 110, "assets/img/tempp.jpg")  # Field background
phone_entry2 = create_labeled_entry("Address:", 440, 110, "assets/img/tempp.jpg")  # Field background
phone_entry2 = create_labeled_entry("Hobbies:", 780, 110, "assets/img/tempp.jpg")  # Field background

# Function to retrieve and print the entered values
def print_values():
    name_value = name_entry.get()  # Get value from Name entry
    email_value = email_entry.get()  # Get value from Email entry
    phone_value = phone_entry.get()  # Get value from Phone entry
    phone_value2 = phone_entry2.get()  # Get value from Phone entry
    
    print(f"Name: {name_value}, Email: {email_value}, Phone: {phone_value}")

# Button to print the values
submit_button = tk.Button(root, text="Submit", command=print_values)
submit_button.place(x=50, y=200)  # Place the button below the entry fields

# Run the Tkinter event loop
root.mainloop()