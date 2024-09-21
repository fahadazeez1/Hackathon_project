import tkinter as tk
from tkinter import ttk

# class ScrollableFrame(ttk.Frame):
#     def __init__(self, container, *args, **kwargs):
#         super().__init__(container, *args, **kwargs)
        
#         # Create a canvas and attach a vertical scrollbar
#         # canvas = tk.Canvas(self, width=900, height=1000)  
#         self.canvas = tk.Canvas(self)
#         self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
#         self.scrollable_frame = ttk.Frame(self.canvas)
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
# fields = [
#     ("Enter your name", 0), ("Enter your Age", 1), ("Enter your DOB", 2),
#     ("Enter your Address", 3), ("Enter your Mobile number", 4), ("Enter your mail", 5),
#     ("Enter your hobbies", 6), ("Enter your school name", 7),
#     ("Enter your college name", 8), ("Enter your Role (comma separated)", 9),
#     ("Enter the period of your first role", 10), ("Enter the 1st bullet point for the first role", 11),
#     ("Enter the 2nd bullet point for the first role", 12), ("Enter the 3rd bullet point for the first role", 13),
#     ("Enter the 4th bullet point for the first role", 14), ("Enter the period of your second role", 15),
#     ("Enter the 1st bullet point for the second role", 16), ("Enter the 2nd bullet point for the second role", 17),
#     ("Enter the 3rd bullet for the second role", 18), ("Enter the 4th bullet point for the second role", 19),
#     ("Enter Facebook link (type no to skip)", 20),
#     ("Enter Github link (type no to skip)", 21), ("Enter Linkedin link (type no to skip)", 22),
#     ("Enter Instagram link (type no to skip)", 23),
#     ("Write the certificate name you have done the most", 24), ("Enter the number of these certificates", 24),
#     ("Number of projects you have created", 25), ("Number of languages you know", 26),
#     ("Enter your lower education passout year", 27), ("Enter your higher education passout year", 28),
#     ("Write about your lower education journey", 29),("explain the row 30",30)
# ]

# for label_text, row in fields:
#     label = ttk.Label(scrollable_container.scrollable_frame, text=label_text, padding=10)
#     label.grid(row=row, column=0, sticky="w")
#     entry = ttk.Entry(scrollable_container.scrollable_frame)
#     entry.grid(row=row, column=1, padx=10, pady=5)


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
facebookEntry = tk.Entry(scrollable_container.scrollable_frame)
facebookEntry.grid(row=20, column=1, padx=10, pady=5)

lab22 = tk.Label(scrollable_container.scrollable_frame, text="Enter Github link (type no to skip)", padx=10, pady=5)
lab22.grid(row=21, column=0, sticky="w")
githubEntry = tk.Entry(scrollable_container.scrollable_frame)
githubEntry.grid(row=21, column=1, padx=10, pady=5)

lab23 = tk.Label(scrollable_container.scrollable_frame, text="Enter Linkedin link (type no to skip)", padx=10, pady=5)
lab23.grid(row=22, column=0, sticky="w")
linkedinEntry = tk.Entry(scrollable_container.scrollable_frame)
linkedinEntry.grid(row=22, column=1, padx=10, pady=5)

lab24 = tk.Label(scrollable_container.scrollable_frame, text="Enter Instagram link (type no to skip)", padx=10, pady=5)
lab24.grid(row=23, column=0, sticky="w")
instagramEntry = tk.Entry(scrollable_container.scrollable_frame)
instagramEntry.grid(row=23, column=1, padx=10, pady=5)

lab25 = tk.Label(scrollable_container.scrollable_frame, text="Write the certificate name you have done the most", padx=10, pady=5)
lab25.grid(row=24, column=0, sticky="w")
certificateEntry = tk.Entry(scrollable_container.scrollable_frame)
certificateEntry.grid(row=24, column=1, padx=10, pady=5)

lab26 = tk.Label(scrollable_container.scrollable_frame, text="Enter the number of these certificates", padx=10, pady=5)
lab26.grid(row=25, column=0, sticky="w")
numCertificatesEntry = tk.Entry(scrollable_container.scrollable_frame)
numCertificatesEntry.grid(row=25, column=1, padx=10, pady=5)

lab27 = tk.Label(scrollable_container.scrollable_frame, text="Number of projectsyou have done", padx=10, pady=5)
lab27.grid(row=26, column=0, sticky="w")
numProjectsEntry = tk.Entry(scrollable_container.scrollable_frame)
numProjectsEntry.grid(row=26, column=1, padx=10, pady=5)

lab28 = tk.Label(scrollable_container.scrollable_frame, text="Any other skills you have", padx=10, pady=5)
lab28.grid(row=27, column=0, sticky="w")
otherSkillsEntry = tk.Entry(scrollable_container.scrollable_frame)
otherSkillsEntry.grid(row=27, column=1, padx=10, pady=5)

lab29 = tk.Label(scrollable_container.scrollable_frame, text="Any other achievements you have", padx=10, pady=5)
lab29.grid(row=28, column=0, sticky="w")
achievementsEntry = tk.Entry(scrollable_container.scrollable_frame)
achievementsEntry.grid(row=28, column=1, padx=10, pady=5)

lab30 = tk.Label(scrollable_container.scrollable_frame, text="Your profile image", padx=10, pady=5)
lab30.grid(row=0, column=4, sticky="w")
imageEntry = tk.Entry(scrollable_container.scrollable_frame)
imageEntry.grid(row=0, column=5, padx=10, pady=5)

lab31 = tk.Label(scrollable_container.scrollable_frame, text="Enter your portfolio title", padx=10, pady=5)
lab31.grid(row=0, column=2, sticky="w")
portfolioTitleEntry = tk.Entry(scrollable_container.scrollable_frame)
portfolioTitleEntry.grid(row=0, column=3, padx=10, pady=5)


# Start the main loop
def repl():
    e=names.get()
    r=ages.get()
    t=dobs.get()
    print(e)
    print(r)
    print(t)
btn=ttk.Button(scrollable_container.scrollable_frame,command=repl,text="click").grid(row=32,column=0)
root.mainloop()