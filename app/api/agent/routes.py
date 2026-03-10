from fastapi import APIRouter
from fastapi.responses import JSONResponse

from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from api.models import ChatRequest
from services.agent.agent import agent
from services.agent.utils import get_or_create_session


router = APIRouter(prefix="/agent")
session_service = InMemorySessionService()
runner = Runner(
    app_name="demo_app",
    agent=agent,
    session_service=session_service
)


@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        content = types.Content(role='user', parts=[types.Part(text=request.message)])
        
        _ = await get_or_create_session(session_service, "demo_app", "demo_user", "demo_session")

        async for event in runner.run_async(
            user_id="demo_user",
            session_id="demo_session",
            new_message=content,
        ):
            print(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")
            if event.is_final_response():

                if event.content and event.content.parts:
                    part = event.content.parts[0]

                    if part.text is not None:
                        final_response = part.text

                    elif hasattr(part, "data") and part.data is not None:
                        final_response = part.data

                elif event.actions and event.actions.escalate:
                    final_response = f"Agent escalated: {event.error_message or 'No message'}"

                break
    
        return {"response": final_response}

    except Exception as e:
        return {"response": f"ADK Agent Error: {str(e)}"}
    

@router.get("/tools")
async def list_tools():

    tools = []
    for toolset in agent.tools:
        toolset_tools = await toolset.get_tools()
        tools.extend(toolset_tools)

    return JSONResponse([
        {"name": t.name, "description": t.description}
        for t in tools
    ])
