import requests
import json
url = 'http://127.0.0.1:8088/claude/stream_chat'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json;charset=utf-8' 
}
data = {'prompt' : 'null'}

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
    data['prompt'] = prompt
    r = requests.post(url,headers=headers,data=json.dumps(data),stream=True)
    for chunk in r.iter_lines(delimiter=b'\n'):
        print(chunk.decode())
    print('')
