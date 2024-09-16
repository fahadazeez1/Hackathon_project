import tkinter as tk
from tkinter import messagebox
import os

# Function to generate the HTML file with user inputs
def generate_html():
    try:
        # Retrieve user inputs
        name = entries["Name"].get()
        age = entries["Age"].get()
        mobile_num = entries["Mobile Number"].get()
        email = entries["Email"].get()
        address = entries["Address"].get()
        dob = entries["DOB"].get()
        cert_name = entries["Certificate Name"].get()
        num_certificates = entries["Number of Certificates"].get()
        num_projects = entries["Number of Projects"].get()
        num_coding_langs = entries["Number of Languages"].get()
        num_grp_work = entries["Number of Group Works"].get()
        first_project = entries["First Project"].get()
        second_project = entries["Second Project"].get()
        third_project = entries["Third Project"].get()
        facebook_link = entries["Facebook"].get()
        instagram_link = entries["Instagram"].get()
        github_link = entries["GitHub"].get()
        linkedin_link = entries["LinkedIn"].get()
        school_name = entries["School Name"].get()
        school_year = entries["School Period"].get()
        school_journey = entries["School Journey"].get()
        college_name = entries["College Name"].get()
        education_year = entries["College Period"].get()
        education_journey = entries["College Journey"].get()
        hobbies = entries["Hobbies"].get()
        role1 = entries["Role 1"].get()
        period1 = entries["Period 1"].get()
        bullet1_1 = entries["Role 1 Bullet 1"].get()
        bullet1_2 = entries["Role 1 Bullet 2"].get()
        bullet1_3 = entries["Role 1 Bullet 3"].get()
        bullet1_4 = entries["Role 1 Bullet 4"].get()
        summary = entries["Summary"].get()

        # Open the base HTML file and replace placeholders with user inputs
        with open("index.html", "r") as file:
            html_content = file.read()

        html_content = html_content.replace("<title>yourTitle</title>", f"<title>{name}'s Portfolio</title>")
        html_content = html_content.replace('<h1 class="sitename">yourName</h1>', f'<h1 class="sitename">{name}</h1>')
        html_content = html_content.replace('href="fbLink"', f'href="{facebook_link}"')
        html_content = html_content.replace('href="instaLink"', f'href="{instagram_link}"')
        html_content = html_content.replace('href="githubLink"', f'href="{github_link}"')
        html_content = html_content.replace('href="linkedinLink"', f'href="{linkedin_link}"')
        html_content = html_content.replace('<h2>yourName</h2>', f'<h2>{name}</h2>')
        html_content = html_content.replace('commaSepSkills', role1)
        html_content = html_content.replace('oneLineAbout', school_journey)
        html_content = html_content.replace('headingForAbout', "About Me")
        html_content = html_content.replace('<span>yourName</span>', f'<span>{name}</span>')
        html_content = html_content.replace('<span>dob</span>', f'<span>{dob}</span>')
        html_content = html_content.replace('<span>mobNum</span>', f'<span>{mobile_num}</span>')
        html_content = html_content.replace('<span>Add</span>', f'<span>{address}</span>')
        html_content = html_content.replace('<span>yourAge</span>', f'<span>{age}</span>')
        html_content = html_content.replace('<span>yourDeg</span>', f'<span>{college_name}</span>')
        html_content = html_content.replace('<span>yourEmail</span>', f'<span>{email}</span>')
        html_content = html_content.replace('<span>yourHobbies</span>', f'<span>{hobbies}</span>')
        html_content = html_content.replace('totalNum1', str(num_certificates))
        html_content = html_content.replace('cirtName', cert_name)
        html_content = html_content.replace('totalNum2', str(num_projects))
        html_content = html_content.replace('totalNum3', str(num_coding_langs))
        html_content = html_content.replace('totalNum4', str(num_grp_work))
        html_content = html_content.replace('<p><em>SummarySumm</em></p>', f'<p><em>{summary}</em></p>')
        html_content = html_content.replace('<h4>commaSepSkill1</h4>', f'<h4>{role1}</h4>')
        html_content = html_content.replace('<h5>periodProf1</h5>', f'<h5>{period1}</h5>')
        html_content = html_content.replace('<li>bulletProf11</li>', f'<li>{bullet1_1}</li>')
        html_content = html_content.replace('<li>bulletProf12</li>', f'<li>{bullet1_2}</li>')
        html_content = html_content.replace('<li>bulletProf13</li>', f'<li>{bullet1_3}</li>')
        html_content = html_content.replace('<li>bulletProf14</li>', f'<li>{bullet1_4}</li>')

        # Save the modified content to a new HTML file named after the user
        with open(f"{name}.html", "w") as new_file:
            new_file.write(html_content)

        # Show success message
        messagebox.showinfo("Success", "Done! HTML file created successfully.")

    except Exception as e:
        # Show error message if anything goes wrong
        messagebox.showerror("Error", f"Not Done! An error occurred: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Portfolio Generator")

# Create a canvas and a frame within the window for scrolling
canvas = tk.Canvas(window)
scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

# Function to configure the scrollbar
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

# Add the frame to the canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Configure the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create a dictionary to hold the input fields
entries = {}

# Define the input fields
fields = [
    "Name", "Age", "Mobile Number", "Email", "Address", "DOB",
    "Certificate Name", "Number of Certificates", "Number of Projects",
    "Number of Languages", "Number of Group Works", "First Project",
    "Second Project", "Third Project", "Facebook", "Instagram",
    "GitHub", "LinkedIn", "School Name", "School Period",
    "School Journey", "College Name", "College Period", "College Journey",
    "Hobbies", "Role 1", "Period 1", "Role 1 Bullet 1",
    "Role 1 Bullet 2", "Role 1 Bullet 3", "Role 1 Bullet 4", "Summary"
]

# Create and place entry widgets dynamically inside the scrollable frame
for field in fields:
    label = tk.Label(scrollable_frame, text=field)
    label.pack()
    entry = tk.Entry(scrollable_frame)
    entry.pack()
    entries[field] = entry

# Create the submit button inside the scrollable frame
submit_button = tk.Button(scrollable_frame, text="Submit", command=generate_html)
submit_button.pack()

# Place the canvas and scrollbar in the window
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Run the Tkinter event loop
window.mainloop()