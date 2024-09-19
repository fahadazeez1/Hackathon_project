def replace_placeholders_in_file(source_file_path, target_file_path, placeholders, replacements):
    with open(source_file_path, 'r') as file:
        content = file.read()
    for placeholder, replacement in zip(placeholders, replacements):
        content = content.replace(placeholder, replacement)
    with open(target_file_path, 'w') as file:
        file.write(content)

while True:
    try:
        num_projects = int(input("How many projects do you have (max 3)? "))
        if 1 <= num_projects <= 3:
            break
        print("Enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Enter a number.")

projects = [input(f"Enter project {i + 1} name: ") for i in range(num_projects)]
placeholders = ['<!-- 1prop -->', '<!-- 2prop -->', '<!-- 3prop -->']
filter_classes = ['filter-app', 'filter-product', 'filter-books']
replacements = [f'<li data-filter=".{filter_classes[i]}">{projects[i]}</li>' if i < num_projects else placeholders[i] for i in range(3)]

replace_placeholders_in_file('propho.html', f'{num_projects}projects.html', placeholders, replacements)

print(f"File '{num_projects}projects.html' created successfully.")
