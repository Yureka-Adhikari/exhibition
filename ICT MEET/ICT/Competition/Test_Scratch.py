import scratchconnect

user = scratchconnect.ScratchConnect("exhibitionsmthg", "minigolf")
project = user.connect_project(project_id=1264096864)  # Replace with real project ID
print(project.title())  # Print the project title
print(project.author())  # Print the author