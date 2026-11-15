from agents.tip_ai_agent import analyseProjects
import sys 
import asyncio 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(analyseProjects(prompt=prompt))
