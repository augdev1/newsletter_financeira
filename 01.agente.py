from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agente = Agent(
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[TavilyTools()],
    debug_mode=True
)

agente.print_response("Use suas ferramentas para pesquisar possiveis oportunidades de investimento do dia 28/12/2025")