# Simple Discord Bot

Automatically respond to marking a package as updated.

This bot is a simple internal tool to tag packages as updated.  We use [Diun](https://github.com/crazy-max/diun) to notify us in a Discord channel when the image of a container gets updated, and then mark it with a checkmark ✅ emoji when someone performs the update.

This bot will then remove the embed, checkmark, add a custom emoji (Portainer) and reply with "Container Updated by [username].  This lets us know which ones are pending and which ones are done, as well as a timestamp of when it was marked.

## Usage
```
docker run -d \
  -e DISCORD_TOKEN=your_discord_token \
  -e DISCORD_CHANNEL=your_channel_id \
  thehedgefrog/discord-bot
```