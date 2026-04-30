"""FastAPI example demonstrating sync vs async endpoints."""

import asyncio
import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/sleep/{seconds}")
def sleep_for(seconds: int):
    """Blocking sleep — server cannot handle other requests while sleeping."""
    time.sleep(seconds)  # ← BLOCKING — server frozen for `seconds` seconds
    return "Awake!"


# uv run uvicorn sleepy_api:app --reload
# http://127.0.0.1:8000/sleep/10


@app.get("/sleepio/{seconds}")
async def sleep_for_async(seconds: int):
    """Non-blocking sleep — server can handle other requests while sleeping."""
    print("Going to bed")
    for s in range(seconds + 1):
        await asyncio.sleep(1)
        print(f"zz {s}")
    return "Awake!"


# http://127.0.0.1:8000/sleepio/10
