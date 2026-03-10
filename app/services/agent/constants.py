import os


AGENT_NAME = os.getenv("AGENT_NAME", "custom_agent")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
POSTGRES_MCP_SERVER_URL = os.getenv("POSTGRES_MCP_SERVER_URL")
