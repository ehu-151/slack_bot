from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import random
from time import sleep


class Dice(BotPlugin):
    """
    throw a dice.
    """

    def activate(self):
        """
        Triggers on plugin activation

        You should delete it if you're not using it to override any default behaviour
        """
        super(Dice, self).activate()

    def deactivate(self):
        """
        Triggers on plugin deactivation

        You should delete it if you're not using it to override any default behaviour
        """
        super(Dice, self).deactivate()

    def get_configuration_template(self):
        """
        Defines the configuration structure this plugin supports

        You should delete it if your plugin doesn't use any configuration like this
        """
        return {'EXAMPLE_KEY_1': "Example value",
                'EXAMPLE_KEY_2': ["Example", "Value"]
                }

    def check_configuration(self, configuration):
        """
        Triggers when the configuration is checked, shortly before activation

        Raise a errbot.utils.ValidationException in case of an error

        You should delete it if you're not using it to override any default behaviour
        """
        super(Dice, self).check_configuration(configuration)

    def callback_connect(self):
        """
        Triggers when bot is connected

        You should delete it if you're not using it to override any default behaviour
        """
        pass

    def callback_message(self, message):
        """
        Triggered for every received message that isn't coming from the bot itself

        You should delete it if you're not using it to override any default behaviour
        """
        pass

    def callback_botmessage(self, message):
        """
        Triggered for every message that comes from the bot itself

        You should delete it if you're not using it to override any default behaviour
        """
        pass

    @webhook
    def example_webhook(self, incoming_request):
        """A webhook which simply returns 'Example'"""
        return "Example"

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def example(self, message, args):
        """A command which simply returns 'Example'"""
        return "Example"

    @arg_botcmd('name', type=str)
    @arg_botcmd('--favorite-number', type=int, unpack_args=False)
    def hello(self, message, args):
        """
        A command which says hello to someone.

        If you include --favorite-number, it will also tell you their
        favorite number.
        """
        if args.favorite_number is None:
            return "Hello {name}".format(name=args.name)
        else:
            return "Hello {name}, I hear your favorite number is {number}".format(
                name=args.name,
                number=args.favorite_number,
            )

    @botcmd(split_args_with=None)
    @arg_botcmd('number_of_roll', type=int, default=6)
    def dice_throw(self, msg, number_of_roll=None):
        """Say hello to the world"""
        return random.randint(1, number_of_roll)

    @botcmd
    def hello_card(self, msg, args):
        """Say a card in the chatroom."""
        self.send_card(title='Title + Body',
                       body='text body to put in the card',
                       thumbnail='https://raw.githubusercontent.com/errbotio/errbot/master/docs/_static/errbot.png',
                       image='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                       link='http://www.google.com',
                       fields=(('First Key', 'Value1'), ('Second Key', 'Value2'), ('First Key', 'Value1'),
                               ('Second Key', 'Value2'), ('First Key', 'Value1'), ('Second Key', 'Value2'),
                               ('First Key', 'Value1'), ('Second Key', 'Value2')),
                       color='red',
                       in_reply_to=msg)

