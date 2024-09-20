import tkinter as  tk
from tkinter import ttk
root=tk.Tk()
root.geometry("400x600")


lab1=ttk.Label(root,text="Enter your name",padding=10).grid(row=0,column=0)
names=ttk.Entry(root)
names.grid(row=0,column=1)

lab2=ttk.Label(root,text="Enter your Age",padding=10).grid(row=0,column=3)
ages=ttk.Entry(root)
ages.grid(row=0,column=4)

lab3=ttk.Label(root,text="Enter your dob",padding=10).grid(row=0,column=5)
dobs=ttk.Entry(root)
dobs.grid(row=0,column=6)



lab4=ttk.Label(root,text="Enter your Address",padding=10).grid(row=1,column=0)
addresss=ttk.Entry(root)
addresss.grid(row=1,column=1)

lab5=ttk.Label(root,text="Enter your Mobile number",padding=10).grid(row=1,column=3)
mobile_nums=ttk.Entry(root)
mobile_nums.grid(row=1,column=4)

lab6=ttk.Label(root,text="Enter your mail",padding=10).grid(row=1,column=5)
emails=ttk.Entry(root)
emails.grid(row=1,column=6)

lab7=ttk.Label(root,text="Enter your hobbies",padding=10).grid(row=2,column=0)
hobbiess=ttk.Entry(root)
hobbiess.grid(row=2,column=1)



lab19=ttk.Label(root,text="Enter your school name").grid(row=2,column=3)
schoolNames=ttk.Entry(root)
schoolNames.grid(row=2,column=4)

lab20=ttk.Label(root,text="Enter your college name").grid(row=2,column=5)
collegeNames=ttk.Entry(root)
collegeNames.grid(row=2,column=6)




lab8=ttk.Label(root,text="Enter your Role (comma seprated)",padding=10).grid(row=3,column=0)
roles=ttk.Entry(root)
roles.grid(row=3,column=1)

lab9=ttk.Label(root,text="Enter your period of your first role",padding=10).grid(row=3,column=3)
periodProf1s=ttk.Entry(root)
periodProf1s.grid(row=3,column=4)

lab10=ttk.Label(root,text="Enter the 1st bullet point for the first role",padding=11).grid(row=4,column=0)
bulletProf11s=ttk.Entry(root)
bulletProf11s.grid(row=4,column=1)

lab11=ttk.Label(root,text="Enter the 2nd bullet point for the first role",padding=10).grid(row=5,column=0)
bulletProf12s=ttk.Entry(root)
bulletProf12s.grid(row=5,column=1)

lab12=ttk.Label(root,text="Enter the 3rd bullet point for the first role",padding=10).grid(row=6,column=0)
bulletProf13s=ttk.Entry(root)
bulletProf13s.grid(row=6,column=1)

lab13=ttk.Label(root,text="Enter the 4rt bullet point for the first role",padding=10).grid(row=7,column=0)
bulletProf14s=ttk.Entry(root)
bulletProf14s.grid(row=7,column=1)

lab14=ttk.Label(root,text="Enter your period of your second role",padding=10).grid(row=3,column=5)
periodProf2s=ttk.Entry(root)
periodProf2s.grid(row=3,column=6)

lab15=ttk.Label(root,text="Enter the 1st bullet point for the second role",padding=11).grid(row=4,column=3)
bulletProf21s=ttk.Entry(root)
bulletProf21s.grid(row=4,column=4)

lab16=ttk.Label(root,text="Enter the 2nd bullet point for the second role",padding=10).grid(row=5,column=3)
bulletProf22s=ttk.Entry(root)
bulletProf22s.grid(row=5,column=4)

lab17=ttk.Label(root,text="Enter the 3rd bullet for the second role",padding=10).grid(row=6,column=3)
bulletProf23s=ttk.Entry(root)
bulletProf23s.grid(row=6,column=4)

lab18=ttk.Label(root,text="Enter the 4rt bullet point for the second role",padding=10).grid(row=7,column=3)
bulletProf24s=ttk.Entry(root)
bulletProf24s.grid(row=7,column=4)




lab21=ttk.Label(root,text="Enter Facebook link (type no to skip) ",padding=10).grid(row=4,column=5)
facebook_links=ttk.Entry(root)
facebook_links.grid(row=4,column=6)


lab22=ttk.Label(root,text="Enter Github link (type no to skip)",padding=10).grid(row=5,column=5)
github_links=ttk.Entry(root)
github_links.grid(row=5,column=6)

lab23=ttk.Label(root,text="Enter Linkedin link (type no to skip) ",padding=10).grid(row=6,column=5)
linked_links=ttk.Entry(root)
linked_links.grid(row=6,column=6)


lab24=ttk.Label(root,text="Enter Github link (type no to skip)",padding=10).grid(row=7,column=5)
instagram_links=ttk.Entry(root)
instagram_links.grid(row=7,column=6)

lab25=ttk.Label(root,text="Write the cirtificate name you have done the most",padding=10).grid(row=8,column=0)
cert_names=ttk.Entry(root)
cert_names.grid(row=8,column=1)
lab26=ttk.Label(root,text="Enter the number of these cirtificates",padding=10).grid(row=8,column=3)
num_certificatess=ttk.Entry(root)
num_certificatess.grid(row=8,column=4)
lab27=ttk.Label(root,text="Number of project you have create",padding=10).grid(row=8,column=5)
num_projectss=ttk.Entry(root)
num_projectss.grid(row=8,column=6)

lab28=ttk.Label(root,text="Number of languages you known").grid(row=9,column=0)
num_coding_langss=ttk.Entry(root)
num_coding_langss.grid(row=9,column=1)

lab29=ttk.Label(root,text="Enter your lower edu passout year",padding=10).grid(row=9,column=3)
schoolYears=ttk.Entry(root)
schoolYears.grid(row=9,column=4)

lab30=ttk.Label(root,text="enter your higher edu passout year",padding=10).grid(row=9,column=5)
education_years=ttk.Entry(root)
education_years.grid(row=9,column=6)

lab31=ttk.Label(root,text="write about your lower edu journey ",padding=10).grid(row=10,column=0)
schoolJourneys=ttk.Entry(root)
schoolJourneys.grid(row=10,column=1)

lab32=ttk.Label(root,text="write about your higher edu journey ",padding=10).grid(row=10,column=3)
education_journeys=ttk.Entry(root)
education_journeys.grid(row=10,column=4)


# lab18=ttk.Label(root,text="Enter your period of your second role",padding=10).grid(row=8,column=0)
# periodProf2=ttk.Entry(root).grid(row=8,column=1)
# def repl():
#     name=names.get()
#     role=roles.get()
#     age=ages.get()
#     address=addresss.get()
#     dob=dobs.get()
#     mobile_num=mobile_nums.get()
#     print(name)
#     with  open("index.html","r") as file:
#         html=file.read()
       
#         html= html.replace("<title>yourTitle</title>", f"<title>{name}'s Portfolio</title>")
#         html= html.replace('<h1 class="sitename">yourName</h1>', f'<h1 class="sitename">{name}</h1>')
#         html= html.replace('<h2>yourName</h2>', f'<h2>{name}</h2>')
#         html= html.replace('commaSepSkills', role)
        
#         html = html.replace('<span>yourName</span>', f'<span>{name}</span>')
#         html = html.replace('<span>dob</span>', f'<span>{dob}</span>')
#         html = html.replace('<span>mobNum</span>', f'<span>{mobile_num}</span>')
#         html = html.replace('<span>Add</span>', f'<span>{address}</span>')
#         html = html.replace('<span>yourAge</span>', f'<span>{age}</span>')
     
#     with open("succ.html","w") as nfile:
#         nfile.write(html)



# frame = tk.Frame(root)
# frame.grid(pady=20)
# # btn=ttk.Button(root,text="GENRATE",padding=10).grid(row=8,column=3)
# button = tk.Button(frame, text="Centered Button")
# button.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()