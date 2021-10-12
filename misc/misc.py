import random
import discord
from redbot.core import commands
from redbot.core.commands.context import Context

__version__ = "1.0.0"
__author__ = "Riggle"

BaseCog = getattr(commands, "Cog", object)


class Misc(BaseCog):
    def __init__(self, bot) -> None:
        self.bot = bot

        self.harmchoice = {
            10: '*{} pushes {} onto a table! Ouch!*',
            10: '*{} bends {} over their knee and smacks their bottom! Ouch!*',
            10: '*{} grabs {} by the neck and holds them in the air momentarily! Ouch!*',
            10: "*{} grapples onto {}'s tail, spins them around their head and throws them against a wall! Ouch!*",
            10: '*{} pulls {} into the bathroom and gives them a swirly! Ouch!*',
            10: '*{} equips a stunprod and repeatedly stuns {}! Ouch!*',
            10: '*{} pushes {} to the floor and holds them in place while they tickle their armpits! Ouch?*',
            10: '*{} sits on top of {} squishing them slightly! Ouch!*',
            10: "*{} yanks on {}'s hair! Ouch!*",
            10: '*{} writes a strongly worded insult directed at {}! Ouch?*',
            1: '*{} drags {} into their bedroom! Bystanders hear what sounds like "wrestling"!*'
        }

    @commands.command()
    async def harm(self, ctx: Context, *, name: str):
        """
        Harm someone
        """
        await ctx.send(
            random.choices(list(self.harmchoice.values()), list(self.harmchoice.keys()))[0].format(
                ctx.author.mention, name
            )
        )
