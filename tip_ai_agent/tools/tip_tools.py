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

def writeHTML(htmlStr : str, fileName : str):
    print(f"Calling tool writeHTML on {fileName}")
    with open(fileName, "w") as f:
        f.write(htmlStr)
    return {
        "status": "success",
        "message": f"written html on {fileName}, don't display html in ouptut"
    }

def getTools():
    tools = []
    tools.append(searchProjects)
    tools.append(getProjectDetails)
    tools.append(findSimilarProjects)
    tools.append(writeHTML)
    return tools 

