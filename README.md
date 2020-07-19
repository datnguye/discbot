# discbot
Discord bot template in pythonic


#### Development or Installation:
1. Create discord bot user via [Developer Portal](https://discordpy.readthedocs.io/en/latest/discord.html)

2. Clone source code:
```
git clone https://github.com/datnguye/discbot.git
cd discbot
```

3. Create enviroment:
```
python -m venv env
.\env\Scripts\activate
OR source env/bin/activate (linux)

python -m pip install -r requirements.txt

```

4. Create dotenv file (sample level as bot.py): ~/discbot/.env
```
DISCORD_TOKEN=your_token
DISCORD_GUILD=your_discord_server_name
ERROR_PATH=/path/to/your_file.log
```

5. Run it!
```
.\env\Scripts\activate
python run.py
```

### Version used
```
Python 3.7.5
```

### USAGE - run.py

```
from discbot import bot
bot.start()
```

### Available Commands
Typing -help in discord to see available commands


![Sample](/resources/sample.png)