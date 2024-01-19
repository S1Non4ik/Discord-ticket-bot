import disnake
from cfg.cfg import guild
from disnake.ext import commands

from cfg.system import *
from datetime import datetime

start_time = datetime.now()

class System(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('System is Load')

    @commands.slash_command(guild_ids=[guild])
    @commands.has_permissions(administrator=True)
    async def system(self, inter: disnake.ApplicationCommandInteraction):
        emb = disnake.Embed(title="** Server load **  ",
                             description=f"🕛 Время ответа от сервера: =  {round(self.bot.latency * 1000)}ms\n "
                                         f"📗 Процессор: {cpu_per} % / 100% \n"
                                         f"📘 Память: {mem_info} % / 100% \n"
                                         f"📙 Время работы бота: {str(datetime.now() - start_time).split('.')[0]}",
                             color=disnake.Color.green())
        await inter.response.send_message(embed=emb)


def setup(bot: commands.Bot):
    bot.add_cog(System(bot))