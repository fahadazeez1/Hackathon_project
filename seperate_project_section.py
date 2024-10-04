import tkinter as tk

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
        project_label.grid(row=0, column=project_num - 1, sticky='w', padx=10, pady=15)
        
        project_entry = tk.Entry(input_frame)
        project_entry.grid(row=1, column=project_num - 1, padx=10, pady=15)
        
        # Create 3 Photo input fields for each project
        for photo_num in range(1, 4):
            label_text = f"photo {photo_num} of project {project_num}"
            photo_label = tk.Label(input_frame, text=label_text)
            photo_label.grid(row=photo_num * 2, column=project_num - 1, sticky='w', padx=10, pady=15)
            
            photo_entry = tk.Entry(input_frame)
            photo_entry.grid(row=photo_num * 2 + 1, column=project_num - 1, padx=10, pady=15)

# Main window
root = tk.Tk()
root.geometry('800x600')
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



update_input_fields(selected_option.get())




root.mainloop()