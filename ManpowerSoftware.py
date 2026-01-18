import math
doing=True
print("Hi, this is a manpower sorter, it will get your projects and manpower with their urgency to suggest the amount of manpower that is required for the project")

def formula(manpower, projects, noofprojects, max_per_project):
    base_allocation = 1

    manpower_left = manpower - noofprojects

    priorities = []
    for project in projects:
        deadline = project[1]

        weight = project[2] if len(project) > 2 else 1

        priority = (1 / deadline) * weight
        priorities.append(priority)

    totalpriority = sum(priorities)

    results = []
    allocatedsofar = 0

    for i in range(noofprojects):
        projectname, deadline = projects[i][0], projects[i][1]

        share = priorities[i] / totalpriority
        extra_workers = math.floor(share * manpower_left)

        extra_workers = min(extra_workers, max_per_project - base_allocation)

        allocatedsofar += extra_workers
        final_workers = base_allocation + extra_workers

        projectdetails2 = projectname, deadline, final_workers
        results.append(projectdetails2)

    leftover = manpower_left - allocatedsofar

    return results, leftover


while doing:
    projects = []
    usedprojectnames = []
    placeholderboolean = True
    noofprojects = int(input("How many projects are there?"))
    if noofprojects <= 0:
        doing = False
        print("Bye")
    while placeholderboolean:
        manpower = int(input("How much manpower do you have to complete these projects?"))
        if manpower<=0:
            print("Invalid manpower")
        else:
            placeholderboolean = False
    placeholderboolean = True
    while placeholderboolean:
        maxmanpower = int(input("How much manpower are you willing to put as the max manpower per project?"))
        if maxmanpower <= 0:
            print("Invalid")
        else:
            placeholderboolean = False
    placeholderboolean = True
    for i in range (noofprojects):
        while placeholderboolean:
            projectname=input(f"What is the name of project {i+1}?")
            if projectname in usedprojectnames:
                print("Name in use already")
            else:
                usedprojectnames.append(projectname)
                placeholderboolean = False
        placeholderboolean = True
        while placeholderboolean:
            projectdeadline=int(input("How many days to the deadline?"))
            if projectdeadline < 0:
                print("Invalid Deadline")
            else:
                placeholderboolean = False
        placeholderboolean=True
        while placeholderboolean:
            projectpriority = int(input("How urgent is this project on a scale of 1-100? The higher the number the more urgent it is"))
            if projectpriority <= 0:
                print("Invalid Priority")
            else:
                placeholderboolean = False
        placeholderboolean = True
        projectdetails = projectname, projectdeadline, projectpriority
        projects.append(projectdetails)
        print(projects)
            
    result, leftover = formula(manpower, projects, noofprojects, maxmanpower)
    for i in range(len(result)):
        projectname, projectdeadline, projectmp = result[i]
        print(f"For project {projectname}, you will need a recommended {projectmp} manpower to complete")
        if projectmp <= 0:
            print("This project has 0 manpower, it is recommended you either get more manpower or cancel the project")
        elif projectmp/projectdeadline >= manpower/projectdeadline - leftover:
            print("This project has very little manpower to complete it on time")

    print(f"You will have {leftover} leftover manpower")

    
