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
        self.canvas.config(width=1200, height=600)  # Adjust dimensions as neededs
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





lab1 = tk.Label(scrollable_container.scrollable_frame, text="Name", padx=10, pady=15)
lab1.grid(row=2, column=0, sticky="w")
names = tk.Entry(scrollable_container.scrollable_frame)
names.grid(row=2, column=1, padx=10, pady=15)

lab2 = tk.Label(scrollable_container.scrollable_frame, text="Age", padx=10, pady=15)
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


#***********************************************************************************SKILL

h16 = tk.Label(scrollable_container.scrollable_frame, text="--------------------------Skills------------------------", padx=10, pady=15,font=("arial",15))
h16.grid(row=16, column=0,columnspan=7,sticky="nsew")

lab34=tk.Label(scrollable_container.scrollable_frame,text="Skill 1",padx=10,pady=15)
lab34.grid(row=17,column=0,sticky="w")
s1names=tk.Entry(scrollable_container.scrollable_frame)
s1names.grid(row=17,column=1,padx=10,pady=15)


lab35=tk.Label(scrollable_container.scrollable_frame,text="Skill 2",padx=10,pady=15)
lab35.grid(row=17,column=3,sticky="w")
s2names=tk.Entry(scrollable_container.scrollable_frame)
s2names.grid(row=17,column=4,padx=10,pady=15)

lab36=tk.Label(scrollable_container.scrollable_frame,text="Skill 3",padx=10,pady=15)
lab36.grid(row=17,column=5,sticky="w")
s3names=tk.Entry(scrollable_container.scrollable_frame)
s3names.grid(row=17,column=6,padx=10,pady=15)

lab37=tk.Label(scrollable_container.scrollable_frame,text="Skill 4",padx=10,pady=15)
lab37.grid(row=18,column=0,sticky="w")
s4names=tk.Entry(scrollable_container.scrollable_frame)
s4names.grid(row=18,column=1,padx=10,pady=15)

lab38=tk.Label(scrollable_container.scrollable_frame,text="Skill 5",padx=10,pady=15)
lab38.grid(row=18,column=3,sticky="w")
s5names=tk.Entry(scrollable_container.scrollable_frame)
s5names.grid(row=18,column=4,padx=10,pady=15)

lab39=tk.Label(scrollable_container.scrollable_frame,text="Skill 6",padx=10,pady=15)
lab39.grid(row=18,column=5,sticky="w")
s6names=tk.Entry(scrollable_container.scrollable_frame)
s6names.grid(row=18,column=6,padx=10,pady=15)

lab40=tk.Label(scrollable_container.scrollable_frame,text="Skill 7",padx=10,pady=15)
lab40.grid(row=19,column=0,sticky="w")
s7names=tk.Entry(scrollable_container.scrollable_frame)
s7names.grid(row=19,column=1,padx=10,pady=15)

lab41=tk.Label(scrollable_container.scrollable_frame,text="Skill 8",padx=10,pady=15)
lab41.grid(row=19,column=3,sticky="w")
s8names=tk.Entry(scrollable_container.scrollable_frame)
s8names.grid(row=19,column=4,padx=10,pady=15)


#_______________________________________________________________________________________
root.mainloop()
