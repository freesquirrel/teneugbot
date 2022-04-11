import discord #모듈 불러오기
token = "OTYyNzkxODI4MDE1NDE5NDUy.YlMrww.mE7OCpMN6w0NTDia8LJ8lbBU7WE" #봇 토큰 설정하기
client = discord.Client() #cLient 설정하기

@client.event
async def on_ready(): #봇이 준비되었을때 
    print("봇 준비 완료!")
    print(client.user)
    print("============================")

@client.event
async def on_message(message): #사용자가 메세지를 입력했을때
    if message.content == "야": #만일 사용자가 "야" 라고 입력했을때 
        await message.channel.send("왜 불러") #봇이 "왜 불러" 라고 답한다.
    if message.content == "ㅎㅇ": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("잘가") #봇이 "잘가" 라고 답한다.
    if message.content == "너두잘가": #만일 사용자가 "너두잘가" 라고 입력했을때
        await message.channel.send("?") #봇이 "?" 라고 답한다.
    if message.content == ".": #만일 사용자가 "." 라고 입력했을때
        await message.channel.send("!재난문자 전국") #봇이 "!재난문자 전국" 라고 답한다.
    if message.content == "안녕하세요": #만일 사용자가 "안녕하세요" 라고 입력했을때
        await message.channel.send("네 안녕하세요") #봇이 "네 안녕하세요" 라고 답한다.
    if message.content == "방장한테 개인메세지": #만일 사용자가 "방장한테 개인메세지" 라고 입력했을때
        await message.channel.send("스늑𝓽𝓮𝓷𝓮𝓾𝓰#1555 친추보내주세요") #봇이 "스늑𝓽𝓮𝓷𝓮𝓾𝓰#1555 친추보내주세요" 라고 답한다.
    if message.content == "봇친구왔네": #만일 사용자가 "봇친구왔네" 라고 입력했을때
        await message.channel.send("와우") #봇이 "와우" 라고 답한다.

    if message.content.startswith("!청소해"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제 완료!")
    
from discord.ext import tasks
from itertools import cycle

status = cycle(["개발자가 직접 12시간 지원", ])    # 본인이 원하는 만큼 추가 가능

@client.event
async def on_ready():
    print(f"[!] 다음으로 로그인에 성공했습니다.")
    print(f"[!] 다음 : {client.user.name}")
    print(f"[!] 다음 : {client.user.id}")
    print(f"[!] 참가 중인 서버 : {len(client.guilds)}개의 서버에 참여 중\n")    # 참여 중인 서버 수

    change_status.start()    # 봇이 on_ready 상태라면, change_message 함수 실행

@tasks.loop(seconds=5)    # n초마다 다음 메시지 출력
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
client.run(token)