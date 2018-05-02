#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PixivImagePicker import PixivImagePicker
from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import json
from slackclient import SlackClient
from errbot.plugin_wizard import ask


class Pixiv_bot(BotPlugin):
    """
    You choose tag, then you get image of the tag on Pixiv.
    """

    def activate(self):
        """
        Triggers on plugin activation

        You should delete it if you're not using it to override any default behaviour
        """
        super(Pixiv_bot, self).activate()

    def deactivate(self):
        """
        Triggers on plugin deactivation

        You should delete it if you're not using it to override any default behaviour
        """
        super(Pixiv_bot, self).deactivate()

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
        super(Pixiv_bot, self).check_configuration(configuration)

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
    @arg_botcmd('tag', type=str)
    @arg_botcmd('--n', dest='number', type=int, default=1)
    def pixiv(self, msg, tag=None, number=None):
        picker = PixivImagePicker("sato.egity.80@gmail.com", '@3348151@')
        tag_title = tag.replace('_', ' ')
        print(tag_title)
        urls = picker.get_image_urls_by_tag(tag_title, number)

        yield tag_title
        for url in urls:
            binary = picker.download_binary(url)
            self.send_stream_request(
                self.build_identifier("#slack_bot"),
                binary,
                name='image',
            )