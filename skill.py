# Collect skill names and their levels from the user
skills = []
levels = []

# for i in range(1, 9):  # Loop for 8 skills
#     skill_name = input(f"Enter skill {i} name: ")
#     skill_level = int(input(f"Enter {skill_name} level from 0 to 100: "))
    
#     skills.append(skill_name)
#     levels.append(skill_level)

# Open the existing HTML file and read its content
with open('index.html', 'r') as file:
    html_content = file.read()

# Replace placeholders for each skill
# for i in range(8):  # Loop through each skill
#     skill_name = skills[i]
#     skill_level = levels[i]
    
#     # Define placeholders
#     skill_placeholder = f'<span class="skill"><span>skill{i+1}</span> <i class="val">skill{i+1}ValPer</i></span>'
#     progress_bar_placeholder = f'<div class="progress-bar-wrap"><div class="progress-bar" role="progressbar" aria-valuenow="skill{i+1}Val" aria-valuemin="0" aria-valuemax="100"></div></div>'
    
#     # Replace placeholders with actual values
#     html_content = html_content.replace(skill_placeholder, 
#                                         f'<span class="skill"><span>{skill_name}</span> <i class="val">{skill_level}%</i></span>')
#     html_content = html_content.replace(progress_bar_placeholder, 
#                                         f'<div class="progress-bar-wrap"><div class="progress-bar" role="progressbar" aria-valuenow="{skill_level}" aria-valuemin="0" aria-valuemax="100"></div></div>')

# Write the updated HTML content to a new file
html_content=html_content.replace("skill1Val","34")
new_filename = 'sduped_index.html'
with open(new_filename, 'w') as file:
    file.write(html_content)

print(f"Updated HTML content has been saved to {new_filename}.")
