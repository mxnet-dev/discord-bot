FROM python:3.11.2-slim-buster

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot

COPY . .

RUN python3 -m pip install discord.py

CMD [ "python3", "discord_bot.py" ]