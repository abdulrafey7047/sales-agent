from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams

from services.agent import utils
from services.agent import constants


agent = Agent(
    name=constants.AGENT_NAME,
    model=LiteLlm(model=constants.GEMINI_MODEL),
    description=utils.load_asset("system_description", "txt"),
    instruction=utils.load_asset("system_prompt", "txt"),
    tools=[McpToolset(
        connection_params=SseConnectionParams(
            url=constants.POSTGRES_MCP_SERVER_URL
        ),
    )],
)
