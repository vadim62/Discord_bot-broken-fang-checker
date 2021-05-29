# Discord_Bot
The bot checks the price of the broken fang case, there is also a command to track price statistics for a day / 3 days / week
#
Technology stack
- Python + Discord_py

# Install
1. Clone a repository with a project:

```sh
github.com/vadim62/Discord_bot-broken-fang-checker.git
```

2. Add the .env file containing the data to the root folder of the project:

```sh
steamLoginToken=****

Discord_bot_token=****
```

3. Create virtual environment and install requirements:

```sh
python -m venv venv
source venv/Scripts/activate

pip install -r requirements.txt
```

Commands:

```sh
!case - broken fang case price at the moment

!history - Broken fang case price for a day / 3 days / 7 days
```
