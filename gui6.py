import tkinter as tk
from PIL import Image, ImageTk  # Use Pillow for image handling

# Create the main window
root = tk.Tk()
root.title("Image in Tkinter Grid")
root.geometry("500x500")

# Load the image (JPG, PNG, etc.)
img = Image.open("main1.png")  # Replace 'your_image.jpg' with your file path
img = img.resize((50, 50), Image.LANCZOS)  # Resize the image if necessary
img = ImageTk.PhotoImage(img)

# Create a Label widget to display the image
image_label = tk.Label(root, image=img)

# Position the image using grid
image_label.grid(row=0, column=5, padx=67, pady=10)  # You can adjust row, column, padding

# Run the application
root.mainloop()