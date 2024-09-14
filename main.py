# Taking user inputs
name = input("Enter your name: ")
age = input("Enter your age: ")
dob = input("Enter your date of birth (dd-mm-yyyy): ")
role = input("Enter your role (2-3 words, comma-separated): ")
address = input("Enter your address: ")
email = input("Enter your email: ")
degree = input("Enter your highest degree: ")
mobile_num = input("Enter your mobile number: ")
num_certificates = input("Enter the number of certificates: ")
num_projects = input("Enter the number of projects you are working on: ")
num_coding_langs = input("Enter the number of coding languages known: ")
hobbies = input("Enter your hobbies: ")
one_line_about = input("Write 2-3 lines about yourself: ")
heading_about = input("Enter a one-line heading for 'About': ")
facebook = input("Enter your Facebook link (or type 'no' if none): ")
instagram = input("Enter your Instagram link (or type 'no' if none): ")
github = input("Enter your GitHub link (or type 'no' if none): ")
linkedin = input("Enter your LinkedIn link (or type 'no' if none): ")
location_link = input("Enter your location link: ")
about_more = input("Write more about yourself: ")
summary = input("Write a detailed summary about yourself: ")
education_journey = input("Write about your education journey: ")
education_year = input("Enter the year for your education journey: ")
professional_experience = input("Describe your professional experience: ")
professional_year = input("Enter the year of your professional experience: ")
bullet1 = input("Enter main bullet point 1 for your experience: ")
bullet2 = input("Enter main bullet point 2 for your experience: ")
bullet3 = input("Enter main bullet point 3 for your experience: ")

# Creating fallbacks for social media links
facebook_link = facebook if facebook != "no" else "#"
instagram_link = instagram if instagram != "no" else "#"
github_link = github if github != "no" else "#"
linkedin_link = linkedin if linkedin != "no" else "#"

# Step 1: Modify the index.html file
with open("uu.html", "r") as file:
    html_content = file.read()

# Replacing the placeholders in index.html with user input
html_content = html_content.replace("<title>yourTitle</title>", f"<title>{name}'s Portfolio</title>")
html_content = html_content.replace('<h1 class="sitename">yourName</h1>', f'<h1 class="sitename">{name}</h1>')
html_content = html_content.replace('href="fbLink"', f'href="{facebook_link}"')
html_content = html_content.replace('href="instaLink"', f'href="{instagram_link}"')
html_content = html_content.replace('href="githubLink"', f'href="{github_link}"')
html_content = html_content.replace('href="linkedinLink"', f'href="{linkedin_link}"')
html_content = html_content.replace('<h2>yourName</h2>', f'<h2>{name}</h2>')
html_content = html_content.replace('commaSepSkills', role)
html_content = html_content.replace('oneLineAbout', one_line_about)
html_content = html_content.replace('headingForAbout', heading_about)
html_content = html_content.replace('<span>yourName</span>', f'<span>{name}</span>')
html_content = html_content.replace('<span>dob</span>', f'<span>{dob}</span>')
html_content = html_content.replace('<span>mobNum</span>', f'<span>{mobile_num}</span>')
html_content = html_content.replace('<span>Add</span>', f'<span>{address}</span>')
html_content = html_content.replace('<span>yourAge</span>', f'<span>{age}</span>')
html_content = html_content.replace('<span>yourDeg</span>', f'<span>{degree}</span>')
html_content = html_content.replace('<span>yourEmail</span>', f'<span>{email}</span>')
html_content = html_content.replace('<span>yourHobbies</span>', f'<span>{hobbies}</span>')

# Writing the modified content back to index.html
with open("uu.html", "w") as file:
    file.write(html_content)

# Step 2: Creating a new HTML file based on the user's name
file_name = f"{name.lower()}'s portfolio.html"

# Writing the modified content to the new file
with open(file_name, "w") as new_file:
    new_file.write(html_content)

print(f"{file_name} has been successfully created and modified.")