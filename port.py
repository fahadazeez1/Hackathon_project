# Read the content of the initial file
source_file_path = 'propho.html'
final_file_path = 'final_projects.html'

with open(source_file_path, 'r') as file:
    content = file.read()

# Get project details from the user
while True:
    try:
        num_projects = int(input("How many projects do you have (max 3)? "))
        if 1 <= num_projects <= 3:
            break
        else:
            print("Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

projects = [input(f"Enter the name of project {i + 1}: ") for i in range(num_projects)]

# First set of placeholders and replacements
placeholders1 = ['<!-- 1prop -->', '<!-- 2prop -->', '<!-- 3prop -->']
filter_classes = ['filter-app', 'filter-product', 'filter-books']

# Replace placeholders in the content for project names
for i in range(3):
    if i < num_projects:
        content = content.replace(placeholders1[i], f'<li data-filter=".{filter_classes[i]}">{projects[i]}</li>')
    else:
        content = content.replace(placeholders1[i], '')

# Second set of placeholders and replacements with specific HTML blocks for each project
placeholders2 = ['<!-- 11pro -->', '<!-- 12pro -->', '<!-- 13pro -->',
                 '<!-- 21pro -->', '<!-- 22pro -->', '<!-- 23pro -->',
                 '<!-- 31pro -->', '<!-- 32pro -->', '<!-- 33pro -->']

# Instead of a template, specific HTML code for each project
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
            </div>'''.format(projects[0])
    ]
    
    if num_projects > 1:
        replacements2 += [
            '''<div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-app">
                  <div class="portfolio-content h-100">
                    <img src="p22.png" class="img-fluid" alt="">
                    <div class="portfolio-info">
                      <h4>{}</h4>
                      <a href="p22.png" title="Project" data-gallery="portfolio-gallery-app" class="glightbox preview-link">
                        <i class="bi bi-zoom-in"></i></a>
                    </div>
                  </div>
                </div>'''.format(projects[0])
        ]
    
    if num_projects == 3:
        replacements2 += [
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
            </div>'''.format(projects[1])
    ]
    
    if num_projects > 1:
        replacements2 += [
            '''<div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-product">
                  <div class="portfolio-content h-100">
                    <img src="p12.png" class="img-fluid" alt="">
                    <div class="portfolio-info">
                      <h4>{}</h4>
                      <a href="p12.png" title="Project" data-gallery="portfolio-gallery-product" class="glightbox preview-link">
                        <i class="bi bi-zoom-in"></i></a>
                    </div>
                  </div>
                </div>'''.format(projects[1])
        ]
    
    if num_projects == 3:
        replacements2 += [
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

if num_projects == 3:
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

# Replace placeholders for project HTML blocks
for placeholder, replacement in zip(placeholders2, replacements2):
    content = content.replace(placeholder, replacement)

# Write the final content to the new file
with open(final_file_path, 'w') as new_file:
    new_file.write(content)

print(f"New file '{final_file_path}' created successfully.")
