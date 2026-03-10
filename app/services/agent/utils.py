import json

from pathlib import Path
from google.adk.sessions import InMemorySessionService


def load_asset(asset_name: str, extension: str) -> str:
    """
    Load a text asset from the assets directory.
    """
    # assets_dir = Path("assets")
    assets_dir = Path(__file__).resolve().parent / "assets"
    text = (assets_dir / f"{asset_name}.{extension}").read_text(encoding="utf-8")
    response = text.strip()
    if extension == "json":
        response = json.loads(text)

    return response


async def get_or_create_session(session_service: InMemorySessionService, app_name, user_id, session_id):
    session = await session_service.get_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id
    )
    if not session:
        session = await session_service.create_session(
            app_name=app_name,
            user_id=user_id,
            session_id=session_id
        )

    return session
