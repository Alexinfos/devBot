# DevBot

A basic discord bot using python.

Lastest update (v0.4.1): *June 27th, 2019*

**WARNING: This project is no longer maintained**


# Quick start

Here is a quick guide to help you setup DevBot.

## Dependencies

 - [discord.py](https://github.com/Rapptz/discord.py) (tested with v1.2.3)
 - [emoji](https://pypi.org/project/emoji/) (tested with v0.5.2)

## Setting environment up

 1. Install [python](https://wiki.python.org/moin/BeginnersGuide/Download)
 
 2. Install dependencies:
>     pip install discord.py
>     pip install emoji

 3. Clone repository:

>     git clone https://github.com/Alexinfos/devBot.git
 4. Go to the [Discord Developper Portal](https://discordapp.com/developers/applications/) and create a new app.

 5. Select the "Bot" option on the left menu.

 6. Click "Add Bot" and validate.

 7. Under "Token", click "Copy".

 8. Open the "main.py" file with your prefered code editor/IDE and edit line 138 `client.run("BOT-TOKEN")` where "BOT-TOKEN" is your freshly-generated Discord Bot Token.
 
 9. Create a debug channel on your discord test server, where the bot will print debug messages.
 
 10. Enable "Developper Mode" in your Discord Client (Settings > Appearance >  Advanced > Developper Mode), right-click on your newly-created debug channel to open the context menu and click "Copy ID".
 
 11. Go back to the "main.py" file and edit line 16 `test_channel = 0000` where "0000" is replaced with the channel id you just copied.
 
 12. Go back to the [Discord Developper Portal](https://discordapp.com/developers/applications/) and click the "OAuth2" option on the left menu, then under "SCOPES" check the "bot" option.
 
 13. You can then choose which permissions you want to give to your bot under "BOT PERMISSIONS" (I recommend you at least check all "TEXT PERMISSIONS").
 
 14. Copy the generated link and open it in your browser. Select a server that the bot should join and run the main.py file with python !

# License

Copyright (C) Alexis Brandner 2018/2019

>    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the  License, or (at your option) any later version.
>     
>    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
>     
>    You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
