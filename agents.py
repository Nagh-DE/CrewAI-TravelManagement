from crewai import Agent
from langchain_openai import AzureChatOpenAI
import os
from tools.search_tools import SearchTools
from dotenv import load_dotenv

load_dotenv()

azure_llm = AzureChatOpenAI(
    openai_api_version=os.environ.get(
        "AZURE_OPENAI_VERSION", "<xxx>-<x>-<x>-<x>"),
    azure_deployment=os.environ.get(
        "AZURE_OPENAI_DEPLOYMENT", "<deployment-name>"),
    azure_endpoint=os.environ.get(
        "AZURE_OPENAI_ENDPOINT", "https://<deployment>.openai.azure.com/"),
    api_key=os.environ.get("AZURE_OPENAI_KEY")
)

search_tools = SearchTools()

# travel agency manager
agency_manager = Agent(
    role='Travel Agency Manager',
    goal='To greet customers, and manage the customers travel requirements',
    verbose=True,
    backstory="A manager in a reputed travel agency, which helps users to recommend and resolve all the requirements of users",
    llm=azure_llm,
    tools=[
        search_tools.search_internet
    ]
)

# local agent
local_travel_agent = Agent(
    role='Local Tourist Guide',
    goal='To make travellers visit all the local tourist spots based on day itenary',
    verbose=True,
    backstory="A famous local tourist guide who can speak multiple languages and have very good idea about all the tourist spots and also the history about the spots",
    llm=azure_llm,
    tools=[
        search_tools.search_internet,
    ]
)

# transport and accomodation agent
transport_accomodation_agent = Agent(
    role='Transport & Accomodation Travel Agent',
    goal='to provide travel recommendations based on weather, and accomodation details',
    verbose=True,
    backstory="You've all details about travel options, accomodation options for user requirements which are not too expensive",
    llm=azure_llm,
    tools=[
        search_tools.search_internet,
    ]
)
