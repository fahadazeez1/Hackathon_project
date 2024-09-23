import tkinter as tk
from tkinter import ttk
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        # Create a canvas
        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        # Bind the configure event to adjust scroll region
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        # Create a window inside the canvas for the scrollable frame
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Configure the canvas to work with the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Grid everything
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Allow the frame to expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Set a minimum size for the canvas to improve visibility
        self.canvas.config(width=1250, height=600)  # Adjust dimensions as neededs
# Create the main application window
root = tk.Tk()
root.title("Form with Scrollbar using Grid")
root.geometry("600x600")  # Increased height for more space

# Add the scrollable frame
scrollable_container = ScrollableFrame(root)
scrollable_container.grid(row=0, column=0, sticky="nsew")
h11 = tk.Label(scrollable_container.scrollable_frame, text="ENTER DETAILS,GET PORTFOLIO", padx=10, pady=5,font=("arial",20,"bold"))
h11.grid(row=0, column=0,columnspan=7,sticky="nsew")


#_______________________________________________________________________________________



#**************************************personal

h12 = tk.Label(scrollable_container.scrollable_frame, text="-------------------------------------Personal details-----------------------------------", padx=10, pady=5,font=("arial",15))
h12.grid(row=1, column=0,columnspan=7,sticky="nsew")





lab1 = tk.Label(scrollable_container.scrollable_frame, text="Name", padx=1, pady=15)
lab1.grid(row=2, column=0, sticky="w")
names = tk.Entry(scrollable_container.scrollable_frame)
names.grid(row=2, column=1, padx=10, pady=15)

lab2 = tk.Label(scrollable_container.scrollable_frame, text="Age", padx=1, pady=15)
lab2.grid(row=2, column=3, sticky="w")
ages = tk.Entry(scrollable_container.scrollable_frame)
ages.grid(row=2, column=4, padx=10, pady=15)


lab3 = tk.Label(scrollable_container.scrollable_frame, text="DOB", padx=10, pady=15)
lab3.grid(row=2, column=5, sticky="w")
dobs = tk.Entry(scrollable_container.scrollable_frame)
dobs.grid(row=2, column=6, padx=10, pady=15)


lab4 = tk.Label(scrollable_container.scrollable_frame, text="Address", padx=10, pady=15)
lab4.grid(row=3, column=0, sticky="w")
addresss = tk.Entry(scrollable_container.scrollable_frame)
addresss.grid(row=3, column=1, padx=10, pady=15)


lab5 = tk.Label(scrollable_container.scrollable_frame, text="Mobile number", padx=10, pady=15)
lab5.grid(row=3, column=3, sticky="w")
mobile_nums = tk.Entry(scrollable_container.scrollable_frame)
mobile_nums.grid(row=3, column=4, padx=10, pady=15)



lab6 = tk.Label(scrollable_container.scrollable_frame, text="Email", padx=10, pady=15)
lab6.grid(row=3, column=5, sticky="w")
emails = tk.Entry(scrollable_container.scrollable_frame)
emails.grid(row=3, column=6, padx=10, pady=15)


lab7 = tk.Label(scrollable_container.scrollable_frame, text="Hobbies", padx=10, pady=15)
lab7.grid(row=4, column=0, sticky="w")
hobbiess = tk.Entry(scrollable_container.scrollable_frame)
hobbiess.grid(row=4, column=1, padx=10, pady=15)

lab71 = tk.Label(scrollable_container.scrollable_frame, text="About Yourself", padx=10, pady=15)
lab71.grid(row=4, column=3, sticky="w")
abouts = tk.Entry(scrollable_container.scrollable_frame)
abouts.grid(row=4, column=4, padx=10, pady=15)

lab72 = tk.Label(scrollable_container.scrollable_frame, text="Highest Degree", padx=10, pady=15)
lab72.grid(row=4, column=5, sticky="w")
degrees = tk.Entry(scrollable_container.scrollable_frame)
degrees.grid(row=4, column=6, padx=10, pady=15)





#********************************************education
h13 = tk.Label(scrollable_container.scrollable_frame, text="-------------------------------Educational Details-----------------------------", padx=10, pady=15,font=("arial",15))
h13.grid(row=5, column=0,columnspan=7,sticky="nsew")


lab8 = tk.Label(scrollable_container.scrollable_frame, text="School Name", padx=10, pady=15)
lab8.grid(row=6, column=0, sticky="w")
schoolNames = tk.Entry(scrollable_container.scrollable_frame)
schoolNames.grid(row=6, column=1, padx=10, pady=15)

lab29=tk.Label(scrollable_container.scrollable_frame,text="Passout Year",padx=10,pady=15)
lab29.grid(row=6,column=3,sticky="w")
schoolYears=tk.Entry(scrollable_container.scrollable_frame)
schoolYears.grid(row=6,column=4,padx=10,pady=15)

lab31=tk.Label(scrollable_container.scrollable_frame,text="Journey",padx=10,pady=15)
lab31.grid(row=6,column=5,sticky="w")
schoolJourneys=tk.Entry(scrollable_container.scrollable_frame)
schoolJourneys.grid(row=6,column=6,padx=10,pady=15)


lab9 = tk.Label(scrollable_container.scrollable_frame, text="College Name", padx=10, pady=15)
lab9.grid(row=7, column=0, sticky="w")
collegeNames = tk.Entry(scrollable_container.scrollable_frame)
collegeNames.grid(row=7, column=1, padx=10, pady=15)

lab30=tk.Label(scrollable_container.scrollable_frame,text="Passout Year",padx=10,pady=15)
lab30.grid(row=7,column=3,sticky="w")
education_years=tk.Entry(scrollable_container.scrollable_frame)
education_years.grid(row=7,column=4,padx=10,pady=15)

lab32=tk.Label(scrollable_container.scrollable_frame,text="Journey",padx=10,pady=15)
lab32.grid(row=7,column=5,sticky="w")
education_journeys=tk.Entry(scrollable_container.scrollable_frame)
education_journeys.grid(row=7,column=6,padx=10,pady=15)



#*******************************************************LINKS

h14 = tk.Label(scrollable_container.scrollable_frame, text="--------------------------------Social Media Link----------------------------", padx=10, pady=15,font=("arial",15))
h14.grid(row=8, column=0,columnspan=7,sticky="nsew")


lab21 = tk.Label(scrollable_container.scrollable_frame, text="Facebook link (type no to skip)", padx=10, pady=15)
lab21.grid(row=9, column=0, sticky="w")
facebook_links = tk.Entry(scrollable_container.scrollable_frame)
facebook_links.grid(row=9, column=1, padx=10, pady=15)


lab22 = tk.Label(scrollable_container.scrollable_frame, text="Github link (type no to skip)", padx=10, pady=15)
lab22.grid(row=9, column=3, sticky="w")
github_links = tk.Entry(scrollable_container.scrollable_frame)
github_links.grid(row=9, column=4, padx=10, pady=15)

lab23 = tk.Label(scrollable_container.scrollable_frame, text="Linkedin link (type no to skip)", padx=10, pady=15)
lab23.grid(row=9, column=5, sticky="w")
linkedin_links = tk.Entry(scrollable_container.scrollable_frame)
linkedin_links.grid(row=9, column=6, padx=10, pady=15)

lab24 = tk.Label(scrollable_container.scrollable_frame, text="Instagram link (type no to skip)", padx=10, pady=15)
lab24.grid(row=10, column=0, sticky="w")
instagram_links = tk.Entry(scrollable_container.scrollable_frame)
instagram_links.grid(row=10, column=1, padx=10, pady=15)

lab241 = tk.Label(scrollable_container.scrollable_frame, text="Location link", padx=10, pady=15)
lab241.grid(row=10, column=3, sticky="w")
location_links = tk.Entry(scrollable_container.scrollable_frame)
location_links.grid(row=10, column=4, padx=10, pady=15)

#****************************************************professional details
h15 = tk.Label(scrollable_container.scrollable_frame, text="--------------------------Professional Summary------------------------", padx=10, pady=15,font=("arial",15))
h15.grid(row=11, column=0,columnspan=7,sticky="nsew")


lab10 = tk.Label(scrollable_container.scrollable_frame, text="Role (comma separated)", padx=10, pady=15)
lab10.grid(row=12, column=0, sticky="w")
roles = tk.Entry(scrollable_container.scrollable_frame)
roles.grid(row=12, column=1, padx=10, pady=15)

lab11 = tk.Label(scrollable_container.scrollable_frame, text="period of your first role", padx=10, pady=15)
lab11.grid(row=12, column=3, sticky="w")
periodProf1s = tk.Entry(scrollable_container.scrollable_frame)
periodProf1s.grid(row=12, column=4, padx=10, pady=15)

lab16 = tk.Label(scrollable_container.scrollable_frame, text="period of your first role", padx=10, pady=15)
lab16.grid(row=12, column=5, sticky="w")
periodProf2s = tk.Entry(scrollable_container.scrollable_frame)
periodProf2s.grid(row=12, column=6, padx=10, pady=15)



lab12 = tk.Label(scrollable_container.scrollable_frame, text="Point for the Role 1", padx=10, pady=15)
lab12.grid(row=13, column=0, sticky="w")
bulletProf11s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf11s.grid(row=13, column=1, padx=10, pady=15)

lab13 = tk.Label(scrollable_container.scrollable_frame, text="Point for the Role 1", padx=10, pady=15)
lab13.grid(row=13, column=3, sticky="w")
bulletProf12s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf12s.grid(row=13, column=4, padx=10, pady=15)

lab14 = tk.Label(scrollable_container.scrollable_frame, text="Point for the Role 1", padx=10, pady=5)
lab14.grid(row=13, column=5, sticky="w")
bulletProf13s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf13s.grid(row=13, column=6, padx=10, pady=5)

lab15 = tk.Label(scrollable_container.scrollable_frame, text="Point for the Role 1", padx=10, pady=15)
lab15.grid(row=14, column=0, sticky="w")
bulletProf14s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf14s.grid(row=14, column=1, padx=10, pady=15)



lab17 = tk.Label(scrollable_container.scrollable_frame, text="Point for the Role 2", padx=10, pady=15)
lab17.grid(row=14, column=3, sticky="w")
bulletProf21s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf21s.grid(row=14, column=4, padx=10, pady=15)

lab18 = tk.Label(scrollable_container.scrollable_frame, text="Point for the Role 2", padx=10, pady=15)
lab18.grid(row=14, column=5, sticky="w")
bulletProf22s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf22s.grid(row=14, column=6, padx=10, pady=15)

lab19 = tk.Label(scrollable_container.scrollable_frame, text="Point for the Role 2", padx=10, pady=15)
lab19.grid(row=15, column=0, sticky="w")
bulletProf23s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf23s.grid(row=15, column=1, padx=10, pady=15)

lab20 = tk.Label(scrollable_container.scrollable_frame, text="Point for the Role 2", padx=10, pady=15)
lab20.grid(row=15, column=3, sticky="w")
bulletProf24s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf24s.grid(row=15, column=4, padx=10, pady=15)

lab21 = tk.Label(scrollable_container.scrollable_frame, text="Summary", padx=10, pady=15)
lab21.grid(row=15, column=5, sticky="w")
summarys = tk.Entry(scrollable_container.scrollable_frame)
summarys.grid(row=15, column=6, padx=10, pady=15)


#***********************************************************************************SKILL

h16 = tk.Label(scrollable_container.scrollable_frame, text="--------------------------Skills------------------------", padx=10, pady=15,font=("arial",15))
h16.grid(row=16, column=0,columnspan=7,sticky="nsew")


lab34=tk.Label(scrollable_container.scrollable_frame,text="Skill 1 Name (if any)",padx=10,pady=15)
lab34.grid(row=18,column=0,sticky="w")
s1names=tk.Entry(scrollable_container.scrollable_frame)
s1names.grid(row=18,column=1,padx=10,pady=15)



lab35=tk.Label(scrollable_container.scrollable_frame,text="Skill 2 Name (if any)",padx=10,pady=15)
lab35.grid(row=19,column=0,sticky="w")
s2names=tk.Entry(scrollable_container.scrollable_frame)
s2names.grid(row=19,column=1,padx=10,pady=15)

lab36=tk.Label(scrollable_container.scrollable_frame,text="Skill 3 Name (if any)",padx=10,pady=15)
lab36.grid(row=20,column=0,sticky="w")
s3names=tk.Entry(scrollable_container.scrollable_frame)
s3names.grid(row=20,column=1,padx=10,pady=15)

lab37=tk.Label(scrollable_container.scrollable_frame,text="Skill 4 Name (if any)",padx=10,pady=15)
lab37.grid(row=21,column=0,sticky="w")
s4names=tk.Entry(scrollable_container.scrollable_frame)
s4names.grid(row=21,column=1,padx=10,pady=15)

lab38=tk.Label(scrollable_container.scrollable_frame,text="Skill 5 Name (if any)",padx=10,pady=15)
lab38.grid(row=22,column=0,sticky="w")
s5names=tk.Entry(scrollable_container.scrollable_frame)
s5names.grid(row=22,column=1,padx=10,pady=15)

lab39=tk.Label(scrollable_container.scrollable_frame,text="Skill 6 Name (if any)",padx=10,pady=15)
lab39.grid(row=23,column=0,sticky="w")
s6names=tk.Entry(scrollable_container.scrollable_frame)
s6names.grid(row=23,column=1,padx=10,pady=15)

lab40=tk.Label(scrollable_container.scrollable_frame,text="Skill 7 Name (if any)",padx=10,pady=15)
lab40.grid(row=24,column=0,sticky="w")
s7names=tk.Entry(scrollable_container.scrollable_frame)
s7names.grid(row=24,column=1,padx=10,pady=15)

lab41=tk.Label(scrollable_container.scrollable_frame,text="Skill 8 Name (if any)",padx=10,pady=15)
lab41.grid(row=25,column=0,sticky="w")
s8names=tk.Entry(scrollable_container.scrollable_frame)
s8names.grid(row=25,column=1,padx=10,pady=15)

lab351=tk.Label(scrollable_container.scrollable_frame,text="Level 1",padx=10,pady=15)
lab351.grid(row=18,column=3)
s1vals=tk.Entry(scrollable_container.scrollable_frame)
s1vals.grid(row=18,column=4,padx=10,pady=15)

lab352=tk.Label(scrollable_container.scrollable_frame,text="Level 2",padx=10,pady=15)
lab352.grid(row=19,column=3)
s2vals=tk.Entry(scrollable_container.scrollable_frame)
s2vals.grid(row=19,column=4,padx=10,pady=15)

lab353=tk.Label(scrollable_container.scrollable_frame,text="Level 3",padx=10,pady=15)
lab353.grid(row=20,column=3)
s3vals=tk.Entry(scrollable_container.scrollable_frame)
s3vals.grid(row=20,column=4,padx=10,pady=15)

lab354=tk.Label(scrollable_container.scrollable_frame,text="Level 4",padx=10,pady=15)
lab354.grid(row=21,column=3)
s4vals=tk.Entry(scrollable_container.scrollable_frame)
s4vals.grid(row=21,column=4,padx=10,pady=15)

lab355=tk.Label(scrollable_container.scrollable_frame,text="Level 5",padx=10,pady=15)
lab355.grid(row=22,column=3)
s5vals=tk.Entry(scrollable_container.scrollable_frame)
s5vals.grid(row=22,column=4,padx=10,pady=15)

lab356=tk.Label(scrollable_container.scrollable_frame,text="Level 6",padx=10,pady=15)
lab356.grid(row=23,column=3)
s6vals=tk.Entry(scrollable_container.scrollable_frame)
s6vals.grid(row=23,column=4,padx=10,pady=15)

lab357=tk.Label(scrollable_container.scrollable_frame,text="Level 7",padx=10,pady=15)
lab357.grid(row=24,column=3)
s7vals=tk.Entry(scrollable_container.scrollable_frame)
s7vals.grid(row=24,column=4,padx=10,pady=15)

lab358=tk.Label(scrollable_container.scrollable_frame,text="Level 8",padx=10,pady=15)
lab358.grid(row=25,column=3)
s8vals=tk.Entry(scrollable_container.scrollable_frame)
s8vals.grid(row=25,column=4,padx=10,pady=15)

# Certificates and Projects section
h17 = tk.Label(scrollable_container.scrollable_frame, text="-------------------------- Your Achievements at a Glance ------------------------", padx=10, pady=15,font=("arial",15))
h17.grid(row=26, column=0,columnspan=7,sticky="nsew")

lab42=tk.Label(scrollable_container.scrollable_frame,text="Certificate Name ",padx=10,pady=15)
lab42.grid(row=27,column=0,sticky="w")
cirtnames=tk.Entry(scrollable_container.scrollable_frame)
cirtnames.grid(row=27,column=1,padx=10,pady=15)

lab43=tk.Label(scrollable_container.scrollable_frame,text="Num of Certificates",padx=10,pady=15)
lab43.grid(row=27,column=3,sticky="w")
cirtnums=tk.Entry(scrollable_container.scrollable_frame)
cirtnums.grid(row=27,column=4,padx=10,pady=15)

lab44=tk.Label(scrollable_container.scrollable_frame,text="Num of Languages ",padx=10,pady=15)
lab44.grid(row=27,column=5,sticky="w")
num_coding_langss=tk.Entry(scrollable_container.scrollable_frame)
num_coding_langss.grid(row=27,column=6,padx=10,pady=15)

lab50=tk.Label(scrollable_container.scrollable_frame,text="Project name 1 (if any)",padx=10,pady=15)
lab50.grid(row=28,column=0,sticky="w")
pro1names=tk.Entry(scrollable_container.scrollable_frame)
pro1names.grid(row=28,column=1,padx=10,pady=15)

lab51=tk.Label(scrollable_container.scrollable_frame,text="Project name 2 (if any)",padx=10,pady=15)
lab51.grid(row=28,column=3,sticky="w")
pro2names=tk.Entry(scrollable_container.scrollable_frame)
pro2names.grid(row=28,column=4,padx=10,pady=15)

lab52=tk.Label(scrollable_container.scrollable_frame,text="Project name 3 (if any)",padx=10,pady=15)
lab52.grid(row=28,column=5,sticky="w")
pro3names=tk.Entry(scrollable_container.scrollable_frame)
pro3names.grid(row=28,column=6,padx=10,pady=15)
#_______________________________________________________________________________________

def gen():
    name=names.get()
    age=ages.get()
    dob=dobs.get()
    address=addresss.get()
    email=emails.get()
    mobile_num=mobile_nums.get()
    degree=degrees.get()
    hobbies=hobbiess.get()
    role=roles.get()
    periodProf1=periodProf1s.get()
    bulletProf11=bulletProf11s.get()
    bulletProf12=bulletProf12s.get()
    bulletProf13=bulletProf13s.get()
    bulletProf14=bulletProf14s.get()
    periodProf2=periodProf2s.get()
    bulletProf21=bulletProf21s.get()
    bulletProf22=bulletProf22s.get()
    bulletProf23=bulletProf23s.get()
    bulletProf24=bulletProf24s.get()
    commaSepSkill1 = role.split(",")[0]
    commaSepSkill2 = role.split(",")[1]
    cert_name=cirtnames.get()
    num_certificates=cirtnums.get()
    num_coding_langs=num_coding_langss.get()
    one_line_about=abouts.get()
    summary=summarys.get()
    location=location_links.get()
    schoolName=schoolNames.get()
    schoolYear=schoolYears.get()
    schoolJourney=schoolJourneys.get()
    collegeName=collegeNames.get()
    education_year=education_years.get()
    education_journey=education_journeys.get()
    facebook_link=facebook_links.get()
    instagram_link=instagram_links.get()
    linkedin_link=linkedin_links.get()
    github_link=github_links.get()
    projectss=[pro1names.get(),pro2names.get(),pro3names.get()]
    projects=[item for item in projectss if item]
    num_projectss=len(projects)
    num_projects=len(projects)

    print("Name:", name)
    print("Age:", age)
    print("Date of Birth:", dob)
    print("Address:", address)
    print("Email:", email)
    print("Mobile Number:", mobile_num)
    print("Degree:", degree)
    print("Role:", role)
    print("Period of Professional Experience 1:", periodProf1)
    print("Bullet Point 1 of Prof Experience 1:", bulletProf11)
    print("Bullet Point 2 of Prof Experience 1:", bulletProf12)
    print("Bullet Point 3 of Prof Experience 1:", bulletProf13)
    print("Bullet Point 4 of Prof Experience 1:", bulletProf14)
    print("Period of Professional Experience 2:", periodProf2)
    print("Bullet Point 1 of Prof Experience 2:", bulletProf21)
    print("Bullet Point 2 of Prof Experience 2:", bulletProf22)
    print("Bullet Point 3 of Prof Experience 2:", bulletProf23)
    print("Bullet Point 4 of Prof Experience 2:", bulletProf24)
    print("First Skill from Role:", commaSepSkill1)
    print("Second Skill from Role:", commaSepSkill2)
    print("Certificate Name:", cert_name)
    print("Number of Certificates:", num_certificates)
    print("Number of Coding Languages Known:", num_coding_langs)
    print("One Line About:", one_line_about)
    print("Summary:", summary)
    print("Location:", location)
    print("School Name:", schoolName)
    print("School Year:", schoolYear)
    print("School Journey:", schoolJourney)
    print("College Name:", collegeName)
    print("Education Year:", education_year)
    print("git:", github_link)
    print("fb:", facebook_link)
    print("ll:", linkedin_link)
    print("in:", instagram_link)
    skillNexp=[s1names.get(),s2names.get(),s3names.get(),s4names.get(),s5names.get(),s6names.get(),s7names.get(),s8names.get()]
    skills=[item for item in skillNexp if item]
    skillLexp=[s1vals.get(),s2vals.get(),s3vals.get(),s4vals.get(),s5vals.get(),s6vals.get(),s7vals.get(),s8vals.get()]
    levels=[item for item in skillLexp if item]
    print("x:", skills)
    print("y:", levels)
    print("z:", projects)
    with open("updated_index.html", "r") as file:
        html_content = file.read()

    def replace_social_media_placeholder(html_content, platform, placeholder, class_name, icon_class, link):
        if link and link.lower() != 'no':
            return html_content.replace(f'<!-- {placeholder} -->', f'<a href="{link}" class="{class_name}"><i class="bi {icon_class}"></i></a>')
        return html_content

    placeholders1 = ['<!-- 1prop -->', '<!-- 2prop -->', '<!-- 3prop -->']
    filter_classes = ['filter-app', 'filter-product', 'filter-books']
    for i in range(3):
        if i < num_projects:
            html_content = html_content.replace(placeholders1[i], f'<li data-filter=".{filter_classes[i]}">{projects[i]}</li>')
        else:
            html_content = html_content.replace(placeholders1[i], '')

    
    placeholders2 = ['<!-- 11pro -->', '<!-- 12pro -->', '<!-- 13pro -->',
                 '<!-- 21pro -->', '<!-- 22pro -->', '<!-- 23pro -->',
                 '<!-- 31pro -->', '<!-- 32pro -->', '<!-- 33pro -->']
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
        
    html_content = html_content.replace("<title>yourTitle</title>", f"<title>{name}'s Portfolio</title>")
    html_content = html_content.replace('<h1 class="sitename">yourName</h1>', f'<h1 class="sitename">{name}</h1>')
    html_content = html_content.replace('<h2>yourName</h2>', f'<h2>{name}</h2>')
    html_content = html_content.replace('commaSepSkills', role)
    html_content = html_content.replace('oneLineAbout', one_line_about)
    # html_content = html_content.replace('headingForAbout', heading_about)
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
    # html_content = html_content.replace('totalNum4', str(num_grp_work))



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

    for placeholder, replacement in zip(placeholders2, replacements2):
        html_content = html_content.replace(placeholder, replacement)




    file_name = f"{name.lower()}'s portfolio.html"

      # Writing the modified content to the new file
    with open(file_name, "w") as new_file:
        new_file.write(html_content)
    print(f"{name} portfolio created succesfully") 


 







#___________________________________________________________________________________________
btn=tk.Button(scrollable_container.scrollable_frame,text="Genrate",bg="grey",command=gen)
btn.grid(row=29, column=0,columnspan=7,sticky="nsew",pady=10)

root.mainloop()
