def replace_placeholders_in_file(source_file_path, target_file_path, placeholders, replacements):
    # Read the content of the source file
    with open(source_file_path, 'r') as file:
        content = file.read()

    # Replace each placeholder with its corresponding replacement
    for placeholder, replacement in zip(placeholders, replacements):
        content = content.replace(placeholder, replacement)

    # Write the updated content to the new target file
    with open(target_file_path, 'w') as file:
        file.write(content)

# Ask the user for the number of projects
while True:
    try:
        num_projects = int(input("How many projects do you have (max 3)? "))
        if 1 <= num_projects <= 3:
            break
        else:
            print("Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Collect project names
projects = []
for i in range(num_projects):
    project_name = input(f"Enter the name of project {i + 1}: ")
    projects.append(project_name)

# Define the placeholders and replacements
placeholders = ['<!-- 1prop -->', '<!-- 2prop -->', '<!-- 3prop -->']
filter_classes = ['filter-app', 'filter-product', 'filter-books']
replacements = []

for i in range(3):
    if i < num_projects:
        replacements.append(f'<li data-filter=".{filter_classes[i]}">{projects[i]}</li>')
    else:
        replacements.append(placeholders[i])  # Keep the original placeholder if no project

# Define the source file and target file paths
source_file_path = 'propho.html'
target_file_path = f'{num_projects}projects.html'

# Replace placeholders in the new file
replace_placeholders_in_file(source_file_path, target_file_path, placeholders, replacements)

print(f"File '{target_file_path}' created successfully.")