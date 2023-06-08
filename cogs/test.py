# importing libs
import disnake
from disnake.ext import commands

# creating cog class
class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # logging about cog starting(optional)
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Test is enabled!")

    # creating slash command
    @commands.slash_command(name="test", description="Testing command")
    async def test(self, inter: disnake.CommandInteraction):
        await inter.response.send_message("Test completed")

# init cog
def setup(bot):
    bot.add_cog(test(bot))