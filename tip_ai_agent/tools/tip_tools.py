from services.tip_service import TipService 

ts = TipService()

def searchProjects(query : str):
    print(f"Calling searchProjects tool {query}")
    return ts.searchProject(query=query)

def getProjectDetails(projectSlug : str):
    print(f"Calling getProjectDetails tool {projectSlug}")
    return ts.getProjectDetails(projectSlug = projectSlug)

def findSimilarProjects(projectSlug : str):
    print(f"Calling findSimilarProjects tool with {projectSlug}")
    return ts.getSimilarProjects(projectSlug = projectSlug)

def getTools():
    tools = []
    tools.append(searchProjects)
    tools.append(getProjectDetails)
    tools.append(findSimilarProjects)
    return tools 

