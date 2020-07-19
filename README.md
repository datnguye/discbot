# discbot
Discord bot template

#### Development or Installation:
Clone source code:
```
git clone https://github.com/datnguye/discbot.git
cd discbot
```

Create enviroment:
```
python -m venv env
.\env\Scripts\activate
OR source env/bin/activate (linux)

python -m pip install -r requirements.txt

```

Create dotenv file (sample level as bot.py): ~/discbot/.env
```
DISCORD_TOKEN=your_token
DISCORD_GUILD=your_discord_server_name
ERROR_PATH=/path/to/your_file.log
```

#### Run test cases:
```
.\env\Scripts\activate
python run.py
```

### Version used
```
Python 3.7.5
```

## USAGE - run.py

```
from discbot import bot
bot.start()
```

## COMMAND LISTING
Typing -help in discord to see available commands