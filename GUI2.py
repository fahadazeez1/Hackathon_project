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
        self.canvas.config(width=1000, height=600)  # Adjust dimensions as neededs
# Create the main application window
root = tk.Tk()
root.title("Form with Scrollbar using Grid")
root.geometry("900x600")  # Increased height for more space

# Add the scrollable frame
scrollable_container = ScrollableFrame(root)
scrollable_container.grid(row=0, column=0, sticky="nsew")

# Add your specified input fields to the scrollable frame using grid

lab1 = tk.Label(scrollable_container.scrollable_frame, text="Enter your name", padx=10, pady=5)
lab1.grid(row=0, column=0, sticky="w")
names = tk.Entry(scrollable_container.scrollable_frame)
names.grid(row=0, column=1, padx=10, pady=5)

lab2 = tk.Label(scrollable_container.scrollable_frame, text="Enter your Age", padx=10, pady=5)
lab2.grid(row=1, column=0, sticky="w")
ages = tk.Entry(scrollable_container.scrollable_frame)
ages.grid(row=1, column=1, padx=10, pady=5)

lab3 = tk.Label(scrollable_container.scrollable_frame, text="Enter your DOB", padx=10, pady=5)
lab3.grid(row=2, column=0, sticky="w")
dobs = tk.Entry(scrollable_container.scrollable_frame)
dobs.grid(row=2, column=1, padx=10, pady=5)

lab4 = tk.Label(scrollable_container.scrollable_frame, text="Enter your Address", padx=10, pady=5)
lab4.grid(row=3, column=0, sticky="w")
addresss = tk.Entry(scrollable_container.scrollable_frame)
addresss.grid(row=3, column=1, padx=10, pady=5)

lab5 = tk.Label(scrollable_container.scrollable_frame, text="Enter your Mobile number", padx=10, pady=5)
lab5.grid(row=4, column=0, sticky="w")
mobile_nums = tk.Entry(scrollable_container.scrollable_frame)
mobile_nums.grid(row=4, column=1, padx=10, pady=5)

lab6 = tk.Label(scrollable_container.scrollable_frame, text="Enter your mail", padx=10, pady=5)
lab6.grid(row=5, column=0, sticky="w")
emails = tk.Entry(scrollable_container.scrollable_frame)
emails.grid(row=5, column=1, padx=10, pady=5)

lab7 = tk.Label(scrollable_container.scrollable_frame, text="Enter your hobbies", padx=10, pady=5)
lab7.grid(row=6, column=0, sticky="w")
hobbiess = tk.Entry(scrollable_container.scrollable_frame)
hobbiess.grid(row=6, column=1, padx=10, pady=5)

lab8 = tk.Label(scrollable_container.scrollable_frame, text="Enter your school name", padx=10, pady=5)
lab8.grid(row=7, column=0, sticky="w")
schoolNames = tk.Entry(scrollable_container.scrollable_frame)
schoolNames.grid(row=7, column=1, padx=10, pady=5)

lab9 = tk.Label(scrollable_container.scrollable_frame, text="Enter your college name", padx=10, pady=5)
lab9.grid(row=8, column=0, sticky="w")
collegeNames = tk.Entry(scrollable_container.scrollable_frame)
collegeNames.grid(row=8, column=1, padx=10, pady=5)

lab10 = tk.Label(scrollable_container.scrollable_frame, text="Enter your Role (comma separated)", padx=10, pady=5)
lab10.grid(row=9, column=0, sticky="w")
roles = tk.Entry(scrollable_container.scrollable_frame)
roles.grid(row=9, column=1, padx=10, pady=5)

lab11 = tk.Label(scrollable_container.scrollable_frame, text="Enter the period of your first role", padx=10, pady=5)
lab11.grid(row=10, column=0, sticky="w")
periodProf1s = tk.Entry(scrollable_container.scrollable_frame)
periodProf1s.grid(row=10, column=1, padx=10, pady=5)

lab12 = tk.Label(scrollable_container.scrollable_frame, text="Enter the 1st bullet point for the first role", padx=10, pady=5)
lab12.grid(row=11, column=0, sticky="w")
bulletProf11s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf11s.grid(row=11, column=1, padx=10, pady=5)

lab13 = tk.Label(scrollable_container.scrollable_frame, text="Enter the 2nd bullet point for the first role", padx=10, pady=5)
lab13.grid(row=12, column=0, sticky="w")
bulletProf12s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf12s.grid(row=12, column=1, padx=10, pady=5)

lab14 = tk.Label(scrollable_container.scrollable_frame, text="Enter the 3rd bullet point for the first role", padx=10, pady=5)
lab14.grid(row=13, column=0, sticky="w")
bulletProf13s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf13s.grid(row=13, column=1, padx=10, pady=5)

lab15 = tk.Label(scrollable_container.scrollable_frame, text="Enter the 4th bullet point for the first role", padx=10, pady=5)
lab15.grid(row=14, column=0, sticky="w")
bulletProf14s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf14s.grid(row=14, column=1, padx=10, pady=5)

lab16 = tk.Label(scrollable_container.scrollable_frame, text="Enter the period of your second role", padx=10, pady=5)
lab16.grid(row=15, column=0, sticky="w")
periodProf2s = tk.Entry(scrollable_container.scrollable_frame)
periodProf2s.grid(row=15, column=1, padx=10, pady=5)

lab17 = tk.Label(scrollable_container.scrollable_frame, text="Enter the 1st bullet point for the second role", padx=10, pady=5)
lab17.grid(row=16, column=0, sticky="w")
bulletProf21s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf21s.grid(row=16, column=1, padx=10, pady=5)

lab18 = tk.Label(scrollable_container.scrollable_frame, text="Enter the 2nd bullet point for the second role", padx=10, pady=5)
lab18.grid(row=17, column=0, sticky="w")
bulletProf22s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf22s.grid(row=17, column=1, padx=10, pady=5)

lab19 = tk.Label(scrollable_container.scrollable_frame, text="Enter the 3rd bullet for the second role", padx=10, pady=5)
lab19.grid(row=18, column=0, sticky="w")
bulletProf23s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf23s.grid(row=18, column=1, padx=10, pady=5)

lab20 = tk.Label(scrollable_container.scrollable_frame, text="Enter the 4th bullet point for the second role", padx=10, pady=5)
lab20.grid(row=19, column=0, sticky="w")
bulletProf24s = tk.Entry(scrollable_container.scrollable_frame)
bulletProf24s.grid(row=19, column=1, padx=10, pady=5)

lab21 = tk.Label(scrollable_container.scrollable_frame, text="Enter Facebook link (type no to skip)", padx=10, pady=5)
lab21.grid(row=20, column=0, sticky="w")
facebook_links = tk.Entry(scrollable_container.scrollable_frame)
facebook_links.grid(row=20, column=1, padx=10, pady=5)

lab22 = tk.Label(scrollable_container.scrollable_frame, text="Enter Github link (type no to skip)", padx=10, pady=5)
lab22.grid(row=21, column=0, sticky="w")
github_links = tk.Entry(scrollable_container.scrollable_frame)
github_links.grid(row=21, column=1, padx=10, pady=5)

lab23 = tk.Label(scrollable_container.scrollable_frame, text="Enter Linkedin link (type no to skip)", padx=10, pady=5)
lab23.grid(row=22, column=0, sticky="w")
linkedin_links = tk.Entry(scrollable_container.scrollable_frame)
linkedin_links.grid(row=22, column=1, padx=10, pady=5)

lab24 = tk.Label(scrollable_container.scrollable_frame, text="Enter Instagram link (type no to skip)", padx=10, pady=5)
lab24.grid(row=23, column=0, sticky="w")
instagram_links = tk.Entry(scrollable_container.scrollable_frame)
instagram_links.grid(row=23, column=1, padx=10, pady=5)

lab25 = tk.Label(scrollable_container.scrollable_frame, text="Write the certificate name you have done the most", padx=10, pady=5)
lab25.grid(row=24, column=0, sticky="w")
cert_names = tk.Entry(scrollable_container.scrollable_frame)
cert_names.grid(row=24, column=1, padx=10, pady=5)

lab26 = tk.Label(scrollable_container.scrollable_frame, text="Enter the number of these certificates", padx=10, pady=5)
lab26.grid(row=25, column=0, sticky="w")
num_certificatess = tk.Entry(scrollable_container.scrollable_frame)
num_certificatess.grid(row=25, column=1, padx=10, pady=5)

lab27 = tk.Label(scrollable_container.scrollable_frame, text="Number of projectsyou have done", padx=10, pady=5)
lab27.grid(row=26, column=0, sticky="w")
num_projectss = tk.Entry(scrollable_container.scrollable_frame)
num_projectss.grid(row=26, column=1, padx=10, pady=5)

lab28=tk.Label(scrollable_container.scrollable_frame,text="enter the umber of coding ",padx=10,pady=5).grid(row=27,column=0)
num_coding_langss=tk.Entry(scrollable_container.scrollable_frame)
num_coding_langss.grid(row=27,column=1,padx=10,pady=5)



lab29=tk.Label(scrollable_container.scrollable_frame,text="entr the year of lower edu passyear",padx=10,pady=5).grid(row=28,column=0)
schoolYears=tk.Entry(scrollable_container.scrollable_frame)
schoolYears.grid(row=28,column=1,padx=10,pady=5)

lab30=tk.Label(scrollable_container.scrollable_frame,text="entr the year of higher edu passyear",padx=10,pady=5).grid(row=29,column=0)
education_years=tk.Entry(scrollable_container.scrollable_frame)
education_years.grid(row=29,column=1,padx=10,pady=5)

lab31=tk.Label(scrollable_container.scrollable_frame,text="entr lower sch journey",padx=10,pady=5).grid(row=30,column=0)
schoolJourneys=tk.Entry(scrollable_container.scrollable_frame)
schoolJourneys.grid(row=30,column=1,padx=10,pady=5)

lab32=tk.Label(scrollable_container.scrollable_frame,text="entr lower higher journey",padx=10,pady=5).grid(row=31,column=0)
education_journeys=tk.Entry(scrollable_container.scrollable_frame)
education_journeys.grid(row=31,column=1,padx=10,pady=5)


lab33=tk.Label(scrollable_container.scrollable_frame,text="entr num of skill",padx=10,pady=5).grid(row=32,column=0)
num_skillss=tk.Entry(scrollable_container.scrollable_frame)
num_skillss.grid(row=32,column=1,padx=10,pady=5)


lab34=tk.Label(scrollable_container.scrollable_frame,text="entr name of skill 1",padx=10,pady=5).grid(row=33,column=0)
s1names=tk.Entry(scrollable_container.scrollable_frame)
s1names.grid(row=33,column=1,padx=10,pady=5)
lab35=tk.Label(scrollable_container.scrollable_frame,text="entr level of skill 1",padx=10,pady=5).grid(row=34,column=0)
s1vals=tk.Entry(scrollable_container.scrollable_frame)
s1vals.grid(row=34,column=1,padx=10,pady=5)

lab36=tk.Label(scrollable_container.scrollable_frame,text="entr name of skill 2",padx=10,pady=5).grid(row=35,column=0)
s2names=tk.Entry(scrollable_container.scrollable_frame)
s2names.grid(row=35,column=1,padx=10,pady=5)
lab37=tk.Label(scrollable_container.scrollable_frame,text="entr level of skill 2",padx=10,pady=5).grid(row=36,column=0)
s2vals=tk.Entry(scrollable_container.scrollable_frame)
s2vals.grid(row=36,column=1,padx=10,pady=5)

lab38=tk.Label(scrollable_container.scrollable_frame,text="entr name of skill 3",padx=10,pady=5).grid(row=37,column=0)
s3names=tk.Entry(scrollable_container.scrollable_frame)
s3names.grid(row=37,column=1,padx=10,pady=5)
lab39=tk.Label(scrollable_container.scrollable_frame,text="entr level of skill 3",padx=10,pady=5).grid(row=38,column=0)
s3vals=tk.Entry(scrollable_container.scrollable_frame)
s3vals.grid(row=38,column=1,padx=10,pady=5)


lab40=tk.Label(scrollable_container.scrollable_frame,text="entr name of skill 4",padx=10,pady=5).grid(row=39,column=0)
s4names=tk.Entry(scrollable_container.scrollable_frame)
s4names.grid(row=39,column=1,padx=10,pady=5)
lab41=tk.Label(scrollable_container.scrollable_frame,text="entr level of skill 4",padx=10,pady=5).grid(row=40,column=0)
s4vals=tk.Entry(scrollable_container.scrollable_frame)
s4vals.grid(row=40,column=1,padx=10,pady=5)

lab42=tk.Label(scrollable_container.scrollable_frame,text="entr name of skill 5",padx=10,pady=5).grid(row=41,column=0)
s5names=tk.Entry(scrollable_container.scrollable_frame)
s5names.grid(row=41,column=1,padx=10,pady=5)
lab43=tk.Label(scrollable_container.scrollable_frame,text="entr level of skill 5",padx=10,pady=5).grid(row=42,column=0)
s5vals=tk.Entry(scrollable_container.scrollable_frame)
s5vals.grid(row=42,column=1,padx=10,pady=5)

lab44=tk.Label(scrollable_container.scrollable_frame,text="entr name of skill 6",padx=10,pady=5).grid(row=43,column=0)
s6names=tk.Entry(scrollable_container.scrollable_frame)
s6names.grid(row=43,column=1,padx=10,pady=5)
lab45=tk.Label(scrollable_container.scrollable_frame,text="entr level of skill 6",padx=10,pady=5).grid(row=44,column=0)
s6vals=tk.Entry(scrollable_container.scrollable_frame)
s6vals.grid(row=44,column=1,padx=10,pady=5)

lab46=tk.Label(scrollable_container.scrollable_frame,text="entr name of skill 7",padx=10,pady=5).grid(row=45,column=0)
s7names=tk.Entry(scrollable_container.scrollable_frame)
s7names.grid(row=45,column=1,padx=10,pady=5)
lab47=tk.Label(scrollable_container.scrollable_frame,text="entr level of skill 7",padx=10,pady=5).grid(row=46,column=0)
s7vals=tk.Entry(scrollable_container.scrollable_frame)
s7vals.grid(row=46,column=1,padx=10,pady=5)

lab48=tk.Label(scrollable_container.scrollable_frame,text="entr name of skill 8",padx=10,pady=5).grid(row=47,column=0)
s8names=tk.Entry(scrollable_container.scrollable_frame)
s8names.grid(row=47,column=1,padx=10,pady=5)
lab49=tk.Label(scrollable_container.scrollable_frame,text="entr level of skill 8",padx=10,pady=5).grid(row=48,column=0)
s8vals=tk.Entry(scrollable_container.scrollable_frame)
s8vals.grid(row=48,column=1,padx=10,pady=5)



lab50=tk.Label(scrollable_container.scrollable_frame,text="Enter the project name 1 (if any)",padx=10,pady=5).grid(row=49,column=0)
pro1names=tk.Entry(scrollable_container.scrollable_frame)
pro1names.grid(row=49,column=1,padx=10,pady=5)

lab51=tk.Label(scrollable_container.scrollable_frame,text="Enter the project name 2 (if any)",padx=10,pady=5).grid(row=50,column=0)
pro2names=tk.Entry(scrollable_container.scrollable_frame)
pro2names.grid(row=50,column=1,padx=10,pady=5)

lab52=tk.Label(scrollable_container.scrollable_frame,text="Enter the project name 3 (if any)",padx=10,pady=5).grid(row=51,column=0)
pro3names=tk.Entry(scrollable_container.scrollable_frame)
pro3names.grid(row=51,column=1,padx=10,pady=5)



def repl():
    e=names.get()
    r=ages.get()
    t=dobs.get()
    print(e)
    print(r)
    print(t)
btn=ttk.Button(scrollable_container.scrollable_frame,command=repl,text="click").grid(row=55,column=0)
root.mainloop()
facebook_link = input("Enter your Facebook link (or type 'n' to skip): ").strip()
if facebook_link.lower()=="n":
    facebook_link="no"
else:
    facebook_link=facebook_link    
print(facebook_link)    
# facebook_link = facebook_link if facebook_link.lower()!= "n" else 'no'