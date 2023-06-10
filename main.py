from typing import Union
import asyncio
from slack import client
import sys
import os

def executestring(string) :
    commands = []
    start_index, end_index = 0, 0
    while start_index < len(string):
        start_index = string.find('<COMMAND>', end_index)
        if start_index == -1:
            break
        end_index = string.find('</COMMAND>', start_index)
        commands.append(string[start_index+9:end_index])
    for i in commands :
        os.system(i)

class ClaudeChatPrompt:
    def __init__(self, prompt):
        self.prompt = prompt

async def send_result_to_slack(result: str):
    await client.open_channel()
    await client.chat(result)
    async_gen = client.get_stream_reply()
    async for reply in async_gen:
        yield reply

async def mainfunc(string):
    stringrules = [[r'&lt;',r'<'],[r'&gt;',r'>'],[r'&amp;',r'&']]
    ret = ''
    try :
        async for response in send_result_to_slack(string):
            for i in stringrules :
                response = response.replace(i[0],i[1])
            print(response,end='')
            ret += response
    except :
        print('Error.')
    else :
        print('')
        return ret

while True :
    print("\033[34;1m->\033[0m ",end='')
    prompt = ''
    while True:
        line = input()
        if line:
            prompt += line + '\n'
        else:
            break
    if prompt == 'exit\n' :
        exit(0)
    print('Waiting for Claude...',end='\r')
    print('\033[31;1m->\033[0m',end='')
    result = asyncio.run(mainfunc(prompt))
    print('')
