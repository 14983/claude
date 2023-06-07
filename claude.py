from os import getenv
from typing import Union
from fastapi import FastAPI, Depends, Header, HTTPException, status
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from slack import client

app = FastAPI()
server_token = getenv("SERVER_TOKEN")

async def must_token(x_token: Union[str, None] = Header(None)):
    if server_token and x_token != server_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "msg": "must token",
            }
        )

class ClaudeChatPrompt(BaseModel):
    prompt: str

@app.post("/claude/stream_chat", dependencies=[Depends(must_token)])
async def chat(body: ClaudeChatPrompt):
    await client.open_channel()
    await client.chat(body.prompt)
    sr = client.get_stream_reply()
    return StreamingResponse(sr, media_type="text/plain")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8088)
