name = input("Enter your name: ")
age = input("Enter your age: ")
dob = input("Enter your date of birth (dd-mm-yyyy): ")
address = input("Enter your address: ")
email = input("Enter your email: ")
degree = input("Enter your highest degree: ")
mobile_num = input("Enter your mobile number: ")
hobbies = input("Enter your hobbies : ")



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






cert_name = (input("Enter the name of the certificate you have done the most: ") )
num_certificates = int(input("Enter the number of certificates: "))



num_projects = input("Enter the number of projects you are worked on: ")
num_coding_langs = input("Enter the number of coding languages known: ")
num_grp_work = input("Enter the number work done by your group: ")

firstProjectType = input("Enter the first project you want to add in your portfolio: ")
secondProjectType = input("Enter the second project you want to add in your portfolio: ")
thirdProjectType = input("Enter the third project you want to add in your portfolio: ")



heading_about = input("Enter a one-line heading for 'About': ")
one_line_about = input("Write 2-3 lines about yourself: ")
# about_more = input("Write more about yourself: ")
summary = input("Write a detailed summary about yourself: ")

# facebook = input("Enter your Facebook link (or type 'no' if none): ")
location = input("Enter your location link: ")




schoolName=input("Write your school name from where you complete your Matriculation and Intermediate Education ")
schoolYear=input("Enter the year for your Matriculation and Intermediate Education: ")
schoolJourney=input("Write about your Matriculation and Intermediate education journey: ")
collegeName=input("Write your college name from where you complete/parsue your higher Education ")
education_year = input("Enter the year for your education journey: ")
education_journey = input("Write about your Higher Education journey: ")


num_skills = int(input("How many skills do you want to add? "))
skills = []
levels = []
for i in range(num_skills):
    skill_name = input(f"Enter skill {i + 1} name: ")
    skill_level = int(input(f"Enter {skill_name} level from 0 to 100: "))
    skills.append(skill_name)
    levels.append(skill_level)


facebook = input("Do you want to add a Facebook link to your portfolio? (y/n): ").strip().lower()
facebook_link = input("Enter your Facebook link: ") if facebook == 'y' else 'no'
instagram = input("Do you want to add an Instagram link to your portfolio? (y/n): ").strip().lower()
instagram_link = input("Enter your Instagram link: ") if instagram == 'y' else 'no'
github = input("Do you want to add a GitHub link to your portfolio? (y/n): ").strip().lower()
github_link = input("Enter your GitHub link: ") if github == 'y' else 'no'
linkedin = input("Do you want to add a LinkedIn link to your portfolio? (y/n): ").strip().lower()
linkedin_link = input("Enter your LinkedIn link: ") if linkedin == 'y' else 'no'


def replace_social_media_placeholder(html_content, platform, placeholder, class_name, icon_class, link):
    if link and link.lower() != 'no':
        return html_content.replace(f'<!-- {placeholder} -->', f'<a href="{link}" class="{class_name}"><i class="bi {icon_class}"></i></a>')
    return html_content










# Step 1: Modify the index.html file
with open("index.html", "r") as file:
    html_content = file.read()

# Replacing the placeholders in index.html with user input
html_content = html_content.replace("<title>yourTitle</title>", f"<title>{name}'s Portfolio</title>")
html_content = html_content.replace('<h1 class="sitename">yourName</h1>', f'<h1 class="sitename">{name}</h1>')
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


html_content = html_content.replace('firPort', firstProjectType)
html_content = html_content.replace('secPort', secondProjectType)
html_content = html_content.replace('thiPort', thirdProjectType)



html_content = html_content.replace('<p>addCon</p>', f'<p>{address}</p>')
html_content = html_content.replace('<p>mobCon</p>', f'<p>{mobile_num}</p>')
html_content = html_content.replace('<p>emailCon</p>', f'<p>{email}</p>')
html_content = html_content.replace('<strong class="px-1 sitename">userName\'s portfolio</strong>', f'<strong class="px-1 sitename">{name}\'s portfolio</strong>')

# html_content = html_content.replace('<strong class="px-1 sitename">userName portfolio</strong>', f'<strong class="px-1 sitename">{name} portfolio</strong>')
html_content = html_content.replace('<!--mapLink-->', location)







for i in range(num_skills):
    skill_div = f"""
    <div class="progress">
        <span class="skill"><span>{skills[i]}</span> <i class="val">{levels[i]}%</i></span>
        <div class="progress-bar-wrap">
            <div class="progress-bar" role="progressbar" aria-valuenow="{levels[i]}" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
    </div>
    """
    html_content = html_content.replace(f"<!-- enter{i+1}skill -->", skill_div)


html_content = replace_social_media_placeholder(html_content, "Facebook", "linkfb", "facebook", "bi-facebook", facebook_link)
html_content = replace_social_media_placeholder(html_content, "Instagram", "linkinsta", "instagram", "bi-instagram", instagram_link)
html_content = replace_social_media_placeholder(html_content, "GitHub", "linkgit", "github", "bi-github", github_link)
html_content = replace_social_media_placeholder(html_content, "LinkedIn", "linklink", "linkedin", "bi-linkedin", linkedin_link)




file_name = f"{name.lower()}'s portfolio.html"

# Writing the modified content to the new file
with open(file_name, "w") as new_file:
    new_file.write(html_content)