from tools.tip_tools import getProjectDetails, searchProjects, findSimilarProjects 
from typing import Dict 
import json 

def writeFile(fileName : str, data : Dict):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))

if __name__ == "__main__":
    projects = searchProjects("concrete building")
    writeFile("test_projects.json", projects)
    if len(projects) > 0 and "slug" in projects[0]:
        writeFile("test_project_details.json", getProjectDetails(projectSlug=projects[0]["slug"]))
        writeFile("test_project_similar.json", findSimilarProjects(projectSlug=projects[0]["slug"]))

