# Anti raid bot

Simple python bot to stop group raids.

# Deployment

* Create a new python virtual env and activate it

* Install dependencies  `pip install -r requirements.txt`

* Make a copy of `.env.example` and save it as `.env`. Modify it with your own bot token

* Run `python -m bot`

# Other

Modify `bot/perms.py` to what you would like your permissions to be during raid mode and normal mode.

Modify line `23` of `bot/handler.py` to whatever threshold of time you would like for users to be kicked for
