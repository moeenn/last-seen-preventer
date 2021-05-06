# Prevent "Last Seen" on Skype
If you use Skype then you know that Skype tracks keypresses and mouse movements to detect the last time user was active. If a user doesn't move their mouse or press any keys for a while, Skype changes the user's status to "Recently active, Last seen n minutes ago". This is a short script that prevent this from happening.

## How does it work?
Skype detects user activity by frequency of keypresses and move movement. The script manages to fool skype by randomly pressing keys every n second (default 20 seconds).

## Installation
```bash
$ pip3 install -r requirements.txt
```

## Usage
Simply Start the web browser on any search engine and search for something random. Next start the script with the following command and immediately focus the browser window. Prefer to use Google Chrome in Incognito Mode.

```bash
$ python3 main.py
```
