import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.geometry('1500x700')

# Load the image using PIL
bg_image = Image.open("assets/img/tempp.jpg")

# bg_image = Image.open(r"C:\Users\dell\OneDrive\Desktop\Hackathon_project\assets\img\tempBack.png")
  # Replace with your image path
# bg_image = Image.open(r"C:\Users\dell\OneDrive\Desktop\Hackathon_project\assets\img\tempBack.png")

bg_image = bg_image.resize((1500, 700), Image.Resampling.LANCZOS)  # Resize to fit window
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Label widget to hold the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire window

# Create fields on top of the background image
tk.Label(root, text="Name:", bg='#ffffff').place(x=50, y=50)  # Label with background color
name_entry = tk.Entry(root)
name_entry.place(x=150, y=50)

tk.Label(root, text="Email:", bg='#ffffff').place(x=50, y=100)
email_entry = tk.Entry(root)
email_entry.place(x=150, y=100)

tk.Label(root, text="Phone:", bg='#ffffff').place(x=50, y=150)
phone_entry = tk.Entry(root)
phone_entry.place(x=150, y=150)

# Run the Tkinter event loop
root.mainloop()