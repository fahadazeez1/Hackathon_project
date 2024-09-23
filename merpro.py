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



num_projectss = input("Enter the number of projects you are worked on: ")
num_coding_langs = input("Enter the number of coding languages known: ")
num_grp_work = input("Enter the number work done by your group: ")



heading_about = input("Enter a one-line heading for 'About': ")
one_line_about = input("Write 2-3 lines about yourself: ")
summary = input("Write a detailed summary about yourself: ")

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










# Step 1: Modify the updated_index.html file
with open("updated_index.html", "r") as file:
    html_content = file.read()



# merging code-------------------------------------------------------------
while True:
    try:
        num_projects = int(input("How many projects do you have (max 3)? "))
        if 1 <= num_projects <= 3:
            break
        else:
            print("Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

projects = [input(f"Enter the name of project {i + 1}: ") for i in range(num_projects)]

# First set of placeholders and replacements
placeholders1 = ['<!-- 1prop -->', '<!-- 2prop -->', '<!-- 3prop -->']
filter_classes = ['filter-app', 'filter-product', 'filter-books']

# Replace placeholders in the content for project names
for i in range(3):
    if i < num_projects:
        html_content = html_content.replace(placeholders1[i], f'<li data-filter=".{filter_classes[i]}">{projects[i]}</li>')
    else:
        html_content = html_content.replace(placeholders1[i], '')

# Second set of placeholders and replacements with specific HTML blocks for each project
placeholders2 = ['<!-- 11pro -->', '<!-- 12pro -->', '<!-- 13pro -->',
                 '<!-- 21pro -->', '<!-- 22pro -->', '<!-- 23pro -->',
                 '<!-- 31pro -->', '<!-- 32pro -->', '<!-- 33pro -->']

# Instead of a template, specific HTML code for each project
replacements2 = []


if num_projects >= 1:
    replacements2 += [
        '''<div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-app">
              <div class="portfolio-content h-100">
                <img src="p21.png" class="img-fluid" alt="">
                <div class="portfolio-info">
                  <h4>{}</h4>
                  <a href="p21.png" title="Project" data-gallery="portfolio-gallery-app" class="glightbox preview-link">
                    <i class="bi bi-zoom-in"></i></a>
                </div>
              </div>
            </div>'''.format(projects[0]),
        '''<div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-app">
              <div class="portfolio-content h-100">
                <img src="p22.png" class="img-fluid" alt="">
                <div class="portfolio-info">
                  <h4>{}</h4>
                  <a href="p22.png" title="Project" data-gallery="portfolio-gallery-app" class="glightbox preview-link">
                    <i class="bi bi-zoom-in"></i></a>
                </div>
              </div>
            </div>'''.format(projects[0]),
        '''<div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-app">
              <div class="portfolio-content h-100">
                <img src="p23.png" class="img-fluid" alt="">
                <div class="portfolio-info">
                  <h4>{}</h4>
                  <a href="p23.png" title="Project" data-gallery="portfolio-gallery-app" class="glightbox preview-link">
                    <i class="bi bi-zoom-in"></i></a>
                </div>
              </div>
            </div>'''.format(projects[0])
    ]

if num_projects >= 2:
    replacements2 += [
        '''<div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-product">
              <div class="portfolio-content h-100">
                <img src="p11.png" class="img-fluid" alt="">
                <div class="portfolio-info">
                  <h4>{}</h4>
                  <a href="p11.png" title="Project" data-gallery="portfolio-gallery-product" class="glightbox preview-link">
                    <i class="bi bi-zoom-in"></i></a>
                </div>
              </div>
            </div>'''.format(projects[1]),
        '''<div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-product">
              <div class="portfolio-content h-100">
                <img src="p12.png" class="img-fluid" alt="">
                <div class="portfolio-info">
                  <h4>{}</h4>
                  <a href="p12.png" title="Project" data-gallery="portfolio-gallery-product" class="glightbox preview-link">
                    <i class="bi bi-zoom-in"></i></a>
                </div>
              </div>
            </div>'''.format(projects[1]),
        '''<div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-product">
              <div class="portfolio-content h-100">
                <img src="p13.png" class="img-fluid" alt="">
                <div class="portfolio-info">
                  <h4>{}</h4>
                  <a href="p13.png" title="Project" data-gallery="portfolio-gallery-product" class="glightbox preview-link">
                    <i class="bi bi-zoom-in"></i></a>
                </div>
              </div>
            </div>'''.format(projects[1])
    ]

if num_projects >= 3:
    replacements2 += [
        '''<div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-books">
              <div class="portfolio-content h-100">
                <img src="p31.png" class="img-fluid" alt="">
                <div class="portfolio-info">
                  <h4>{}</h4>
                  <a href="p31.png" title="Project" data-gallery="portfolio-gallery-book" class="glightbox preview-link">
                    <i class="bi bi-zoom-in"></i></a>
                </div>
              </div>
            </div>'''.format(projects[2]),
        '''<div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-books">
              <div class="portfolio-content h-100">
                <img src="p32.png" class="img-fluid" alt="">
                <div class="portfolio-info">
                  <h4>{}</h4>
                  <a href="p32.png" title="Project" data-gallery="portfolio-gallery-book" class="glightbox preview-link">
                    <i class="bi bi-zoom-in"></i></a>
                </div>
              </div>
            </div>'''.format(projects[2]),
        '''<div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-books">
              <div class="portfolio-content h-100">
                <img src="p33.png" class="img-fluid" alt="">
                <div class="portfolio-info">
                  <h4>{}</h4>
                  <a href="p33.png" title="Project" data-gallery="portfolio-gallery-book" class="glightbox preview-link">
                    <i class="bi bi-zoom-in"></i></a>
                </div>
              </div>
            </div>'''.format(projects[2])
    ]


# Replace placeholders for project HTML blocks
for placeholder, replacement in zip(placeholders2, replacements2):
    html_content = html_content.replace(placeholder, replacement)



# ---------------------------------------------------------------------------
# Replacing the placeholders in updated_index.html with user input
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
html_content = html_content.replace('totalNum2', str(num_projectss))
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
print(f"{name} portfolio created succesfully")    