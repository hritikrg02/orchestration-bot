### Purpose
This bot was created as a part of RIT GSO's 2026 April Fools event. 

### Info
The main file assumes there is a file called `token.txt` present within the `bot_root` directory. The main file also uses an internal list of channel ids -- the bot will monitor these channels and no others.

#### Usage
You may run this bot in either a docker container or locally.

##### Docker Container
Assuming you have the latest version of docker installed, you can simply run `docker compose up --build` from the `orchestration-bot` directory.

##### Local
Assuming that you have some form of `conda` installed, use the `environment.yml` file to create a new environment. Once this is done, simply run `conda activate gso-april-fools-2026` followed by `python bot_root/main.py` run from the `orchestration-bot` directory. 