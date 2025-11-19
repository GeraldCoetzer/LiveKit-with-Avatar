import logging
import os

from dotenv import load_dotenv

from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, WorkerType, cli
from livekit.plugins import openai, tavus

logger = logging.getLogger("tavus-avatar-example")
logger.setLevel(logging.INFO)

load_dotenv()


async def entrypoint(ctx: JobContext):
    # Connect to the LiveKit room before accessing local_participant-dependent features
    await ctx.connect()

    session = AgentSession(
        llm=openai.realtime.RealtimeModel(voice="alloy"),
    )

    persona_id = os.getenv("TAVUS_PERSONA_ID")
    replica_id = os.getenv("TAVUS_REPLICA_ID")
    tavus_avatar = tavus.AvatarSession(persona_id=persona_id, replica_id=replica_id)

    # start the agent first so it connects to the room
    await session.start(
        agent=Agent(
            instructions="Praat altyd Afrikaans, bly vriendelik en help die gebruiker."
        ),
        room=ctx.room,
    )

    # now start the avatar, room is connected and local_participant is available
    await tavus_avatar.start(session, room=ctx.room)

    session.generate_reply(instructions="Sê hallo aan die gebruiker in Afrikaans.")


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, worker_type=WorkerType.ROOM))