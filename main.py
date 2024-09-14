# Taking user inputs
name = input("Enter your name: ")
age = input("Enter your age: ")
dob = input("Enter your date of birth (dd-mm-yyyy): ")
role = input("Enter your role (2 words, comma-separated): ")

periodProf1 = input("Enter the period for your first role: ")
bulletProf11 = input("Enter bullet point 1 for your first role: ")
bulletProf12 = input("Enter bullet point 2 for your first role: ")
bulletProf13 = input("Enter bullet point 3 for your first role: ")
bulletProf14 = input("Enter bullet point 4 for your first role: ")
commaSepSkill1 = role.split(",")[0]

periodProf2 = input("Enter the period for your second role: ")
bulletProf21 = input("Enter bullet point 1 for your second role: ")
bulletProf22 = input("Enter bullet point 2 for your second role: ")
bulletProf23 = input("Enter bullet point 3 for your second role: ")
bulletProf24 = input("Enter bullet point 4 for your second role: ")
commaSepSkill2 = role.split(",")[1]



address = input("Enter your address: ")
email = input("Enter your email: ")
degree = input("Enter your highest degree: ")
mobile_num = input("Enter your mobile number: ")



cert_name = (input("Enter the name of the certificate: ") )
num_certificates = int(input("Enter the number of certificates: "))
num_projects = input("Enter the number of projects you are worked on: ")
num_coding_langs = input("Enter the number of coding languages known: ")
num_grp_work = input("Enter the number work done by your group: ")


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
schoolName=input("Write your school name from where you complete your Matriculation and Intermediate Education ")
schoolYear=input("Enter the year for your Matriculation and Intermediate Education: ")
schoolJourney=input("Write about your education journey: ")
collegeName=input("Write your college name from where you complete/parsue your higher Education ")
education_year = input("Enter the year for your education journey: ")
education_journey = input("Write about your Higher Education journey: ")

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
skills = []
levels = []

for i in range(1, 9):  
    skill_name = input(f"Enter skill {i} name: ")
    skill_level = int(input(f"Enter {skill_name} level from 0 to 100: "))
    
    skills.append(skill_name)
    levels.append(skill_level)









    

# Step 1: Modify the index.html file
with open("bp.html", "r") as file:
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


html_content = html_content.replace('totalNum1', str(num_certificates))
html_content = html_content.replace('cirtName', cert_name)
html_content = html_content.replace('totalNum2', str(num_projects))
html_content = html_content.replace('totalNum3', str(num_coding_langs))
html_content = html_content.replace('totalNum4', str(num_grp_work))



html_content = html_content.replace('<p><em>SummarySumm</em></p>', f'<p><em>{summary}</em></p>')
html_content = html_content.replace('<li>addSumm</li>', f'<li>{address}</li>')
html_content = html_content.replace('<li>mobNumSumm</li>', f'<li>{mobile_num}</li>')
html_content = html_content.replace('<li>emailSumm</li>', f'<li>{email}</li>')
html_content = html_content.replace('<h4>yourNameSumm</h4>', f'<h4>{name}</h4>')


html_content = html_content.replace('<h5>yearEdu</h5>', f'<h5>{education_year}</h5>')
html_content = html_content.replace('<p><em>CollegeNameEdu</em></p>', f'<p><em>{collegeName}</em></p>')
html_content = html_content.replace('<p>courseStatusEdu</p>', f'<p>{education_journey}</p>')

html_content = html_content.replace('<h5>periodMatric</h5>', f'<h5>{schoolYear}</h5>')
html_content = html_content.replace('<p><em>schoolnameEdu</em></p>', f'<p><em>{schoolName}</em></p>')
html_content = html_content.replace('<p>schoolStatusEdu</p>', f'<p>{schoolJourney}</p>')

html_content = html_content.replace('<h4>commaSepSkill1</h4>', f'<h4>{commaSepSkill1}</h4>')
html_content = html_content.replace('<h5>periodProf1</h5>', f'<h5>{periodProf1}</h5>')
html_content = html_content.replace('<li>bulletProf11</li>', f'<li>{bulletProf11}</li>')
html_content = html_content.replace('<li>bulletProf12</li>', f'<li>{bulletProf12}</li>')
html_content = html_content.replace('<li>bulletProf13</li>', f'<li>{bulletProf13}</li>')
html_content = html_content.replace('<li>bulletProf14</li>', f'<li>{bulletProf14}</li>')

html_content = html_content.replace('<h4>commaSepSkill2</h4>', f'<h4>{commaSepSkill2}</h4>')
html_content = html_content.replace('<h5>periodProf2</h5>', f'<h5>{periodProf2}</h5>')
html_content = html_content.replace('<li>bulletProf21</li>', f'<li>{bulletProf21}</li>')
html_content = html_content.replace('<li>bulletProf22</li>', f'<li>{bulletProf22}</li>')
html_content = html_content.replace('<li>bulletProf23</li>', f'<li>{bulletProf23}</li>')
html_content = html_content.replace('<li>bulletProf24</li>', f'<li>{bulletProf24}</li>')





for i in range(8):  # Loop through each skill
    skill_name = skills[i]
    skill_level = levels[i]
    
 
    skill_placeholder = f'<span class="skill"><span>skill{i+1}</span> <i class="val">skill{i+1}ValPer</i></span>'
    #                            <div class="progress-bar" role="progressbar" aria-valuenow="s3val" aria-valuemin="0" aria-valuemax="100"></div>
    progress_bar_placeholder = f'<div class="progress-bar" role="progressbar" aria-valuenow="s{i+1}val" aria-valuemin="0" aria-valuemax="100"></div>'
    
    # Replace placeholders with actual values
    html_content = html_content.replace(skill_placeholder, 
                                        f'<span class="skill"><span>{skill_name}</span> <i class="val">{skill_level}%</i></span>')
    html_content = html_content.replace(progress_bar_placeholder, 
                                        f'<div class="progress-bar" role="progressbar" aria-valuenow="{skill_level}" aria-valuemin="0" aria-valuemax="100"></div>')


# Writing the modified content back to index.html
with open("bp.html", "w") as file:
    file.write(html_content)

# Step 2: Creating a new HTML file based on the user's name
file_name = f"{name.lower()}'s portfolio.html"

# Writing the modified content to the new file
with open(file_name, "w") as new_file:
    new_file.write(html_content)

print(f"{file_name} has been successfully created and modified.")