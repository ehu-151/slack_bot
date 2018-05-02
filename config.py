import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'  # Errbot will start in text mode (console only mode) and will answer commands from there.
# add
BOT_IDENTITY = {
    'token': 'xoxb-356299512438-Z7j5b0tZiza8I9LU866HJAz0',
}

BOT_DATA_DIR = r'C:\slack_bot\data'
BOT_EXTRA_PLUGIN_DIR = r'C:\slack_bot\plugins'

BOT_LOG_FILE = r'C:\slack_bot\errbot.log'
BOT_LOG_LEVEL = logging.DEBUG


BOT_ADMINS = ('@kd', )  # !! Don't leave that to "@CHANGE_ME" if you connect your errbot to a chat system !!