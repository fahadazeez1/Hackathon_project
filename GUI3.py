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
        self.canvas.config(width=700, height=600)  # Adjust dimensions as neededs
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

h12 = tk.Label(scrollable_container.scrollable_frame, text="Personal details", padx=10, pady=5,font=("arial",15))
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

lab71 = tk.Label(scrollable_container.scrollable_frame, text="Hobbies", padx=10, pady=15)
lab71.grid(row=4, column=3, sticky="w")
abouts = tk.Entry(scrollable_container.scrollable_frame)
abouts.grid(row=4, column=4, padx=10, pady=15)





#********************************************education
h13 = tk.Label(scrollable_container.scrollable_frame, text="Educational Details", padx=10, pady=5,font=("arial",15))
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


















#_______________________________________________________________________________________
root.mainloop()
