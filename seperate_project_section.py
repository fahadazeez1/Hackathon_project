import tkinter as tk
from tkinter import filedialog
import shutil
import os

# Path to existing directory
target_directory = 'assets/img'

def update_input_fields(selection):
    # Clear the existing fields
    for widget in input_frame.winfo_children():
        widget.destroy()

    # Number of projects
    if selection == "1":
        num_projects = 1
    elif selection == "2":
        num_projects = 2
    elif selection == "3":
        num_projects = 3
    else:
        num_projects = 0

    # Create new input fields for each project
    for project_num in range(1, num_projects + 1):
        # Project Name Label and Entry
        project_label = tk.Label(input_frame, text=f"Project {project_num} Name:")
        project_label.grid(row=0, column=project_num - 1, sticky='w', padx=10, pady=5)
        
        project_entry = tk.Entry(input_frame)
        project_entry.grid(row=1, column=project_num - 1, padx=10, pady=5)
        
        # Create 3 Photo input fields for each project
        for photo_num in range(1, 4):
            label_text = f"photo {photo_num} of project {project_num}"
            photo_label = tk.Label(input_frame, text=label_text)
            photo_label.grid(row=photo_num * 2, column=project_num - 1, sticky='w', padx=10, pady=5)
            
            # Photo Upload Button
            photo_button = tk.Button(input_frame, text="Select Photo", command=lambda p=project_num, n=photo_num: select_photo(p, n))
            photo_button.grid(row=photo_num * 2 + 1, column=project_num - 1, padx=10, pady=5)

def select_photo(project_num, photo_num):
    # Open file dialog to select photo
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        # Create the filename in the required format
        new_filename = f"p{project_num}{photo_num}.png"
        dest_path = os.path.join(target_directory, new_filename)
        
        # Copy the selected file to the destination path
        shutil.copy(file_path, dest_path)
        print(f"Saved {new_filename} to {target_directory}")

# Main window
root = tk.Tk()
root.geometry('600x600')  # Larger window to fit all fields comfortably
root.resizable(True, True)  # Allow window resizing
root.title("Dynamic Input Fields with Project Name and Photos")

# Dropdown options
options = ["1", "2", "3"]
selected_option = tk.StringVar(value=options[0])

# Dropdown menu
dropdown = tk.OptionMenu(root, selected_option, *options, command=update_input_fields)
dropdown.pack(pady=10)

# Frame to hold input fields
input_frame = tk.Frame(root)
input_frame.pack()

# Initial display of input fields
update_input_fields(selected_option.get())

# Run the Tkinter main loop
root.mainloop()