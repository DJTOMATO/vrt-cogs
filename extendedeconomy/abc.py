import typing as t
from abc import ABCMeta, abstractmethod

import discord
from discord.ext.commands.cog import CogMeta
from redbot.core import commands
from redbot.core.bot import Red

from .common.models import DB


class CompositeMetaClass(CogMeta, ABCMeta):
    """Type detection"""


class MixinMeta(metaclass=ABCMeta):
    """Type hinting"""

    bot: Red
    db: DB
    checks: set
    charged: t.Dict[str, int]

    @abstractmethod
    async def save(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def cost_check(self, ctx: commands.Context):
        raise NotImplementedError()

    @abstractmethod
    async def slash_cost_check(self, interaction: discord.Interaction):
        raise NotImplementedError()

    @abstractmethod
    async def send_payloads(self):
        raise NotImplementedError()
