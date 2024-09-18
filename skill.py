import re

# Read the existing HTML file
with open('skillsSection.html', 'r') as file:
    html_content = file.read()

# Ask user how many skills they want to include
N = int(input("How many skills do you want to include? "))

# List to store the new skill sections
new_skill_sections = []

# Loop to collect skill names and skill levels
for i in range(1, N+1):
    skill_name = input(f"Enter the name of skill {i}: ")
    skill_level = int(input(f"Enter the level of {skill_name} (0-100): "))

    # Create the new skill section using the placeholders
    skill_html = f'''
    <div class="progress">
        <span class="skill"><span>{skill_name}</span> <i class="val">{skill_level}%</i></span>
        <div class="progress-bar-wrap">
            <div class="progress-bar" role="progressbar" aria-valuenow="{skill_level}" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
    </div>
    '''

    # Append the generated HTML for the skill to the list
    new_skill_sections.append(skill_html)

# Create a copy of the original content to work with
new_html_content = html_content

# Replace all placeholders with the new skill sections
for i in range(1, N+1):
    placeholder = f"<!-- enter{i}skill -->"
    new_html_content = re.sub(placeholder, new_skill_sections[i-1], new_html_content, count=1)

# Write the modified content to a new file named based on the number of skills (e.g., skill5.html)
new_file_name = f"skill{N}.html"
with open(new_file_name, 'w') as file:
    file.write(new_html_content)

print(f"Skills added successfully to {new_file_name}!")
