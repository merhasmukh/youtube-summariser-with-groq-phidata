from phi.agent import Agent
from phi.tools.youtube_tools import YouTubeTools
from phi.model.groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
agent = Agent(
    model=Groq(
        id="llama3-groq-70b-8192-tool-use-preview"
    ),
    tools=[YouTubeTools()],
    show_tool_calls=True,
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
)

agent.print_response("Summarize this video https://www.youtube.com/watch?v=Iv9dewmcFbs&t", markdown=True)
