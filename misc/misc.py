# Godawful code below

# Standard Imports
import random

# Discord Imports
import discord

# Redbot Imports
from redbot.core import commands
from redbot.core.commands.context import Context

__version__ = "1.0.0"
__author__ = "Riggle"

BaseCog = getattr(commands, "Cog", object)


class Misc(BaseCog):
    def __init__(self, bot) -> None:
        self.bot = bot

        self.harmnormal = [
            "*{} pushes {} onto a table! Ouch!*",
            "*{} bends {} over their knee and smacks their bottom! Ouch!*",
            "*{} grabs {} by the neck and holds them in the air momentarily! Ouch!*",
            "*{} grapples onto {'s tail, spins them around their head and throws them against a wall! Ouch!*",
            "*{} pulls {} into the bathroom and gives them a swirly! Ouch!*",
            "*{} equips a stunprod and repeatedly stuns {}! Ouch!*",
            "*{} pushes {} to the floor and holds them in place while they tickle their armpits! Ouch?*",
            "*{} sits on top of {} squishing them slightly! Ouch!*",
            "*{} yanks on {}'s hair! Ouch!*",
            "*{} writes a strongly worded insult directed at {}! Ouch?*"
        ]
        self.harmchoice = {
            99: self.harmnormal,
            1: ["*{} drags {} into their bedroom! Bystanders hear what sounds like \"wrestling\"!*"]
        }

    @commands.command()
    async def harm(self, ctx: Context, *, name: str):
        """
        Harm someone
        """
        await ctx.send(
            random.choice(random.choices(list(self.harmchoice.values()), list(self.harmchoice.keys()))[0]).format(
                ctx.author.mention, name
            )
        )

    @commands.command()
    async def nibble(self, ctx: Context, name: str):
        """
        Nibble, nom
        """
        await ctx.send(
            "*{} nibbles {}!*".format(
                ctx.author.mention, name
            )
        )
