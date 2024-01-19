import os
import disnake
from disnake.ext import commands
from cfg.cfg import *


class ButtonView(disnake.ui.View):
    def __init__(self, user_id, bot):
        self.user_id = user_id
        self.bot = bot
        super().__init__(timeout=None)

    @disnake.ui.button(label='Закрыть тикет', style=disnake.ButtonStyle.red, emoji='📕')
    async def button(self, button: disnake.ui.Button, inter):
        await inter.response.send_message("Тикет скоро закроется...", ephemeral=False)
        channel_1 = self.bot.get_channel(1197178819845562390)
        user_1 = self.user_id
        user_2 = await self.bot.fetch_user(int(user_1))
        amount = 100
        f = open("logs/report.txt", "w+", encoding="UTF-8")
        async for message in inter.channel.history(limit=amount):
            try:
                f.write(f"({str(message.created_at).split('.')[0]}, {message.author}: {message.content} \n")
            except Exception as e:
                print(e)
        f.close()
        embed = disnake.Embed(title='📚 Server answer', description=f'@admin:~# Log report of <@{inter.user.id}>')
        await channel_1.send(embed=embed)
        await channel_1.send(file=disnake.File("logs/report.txt"))
        try:
            await user_2.send(embed=embed)
            await user_2.send(file=disnake.File("logs/report.txt"))
        except Exception as e:
            print(e)
        os.remove('logs/report.txt')
        await inter.channel.delete()


class Communication(disnake.ui.Modal):
    def __init__(self, bot):
        self.bot = bot
        components = [
            disnake.ui.TextInput(
                label="ВАШ ИГРОВОЙ НИКНЕЙМ",
                placeholder="Например: S1Non_",
                custom_id="Никнейм",
                max_length=25
            ),
            disnake.ui.TextInput(
                label="ТЕМА ВОПРОСА",
                placeholder="Например: Ситуация",
                custom_id="Тема",
                max_length=25
            ),
            disnake.ui.TextInput(
                label="ВОПРОС",
                placeholder="Например: В такой ситуации что можно сделать?",
                custom_id="Ситуация",
                style=disnake.TextInputStyle.paragraph,
                max_length=500
            ),
        ]
        super().__init__(title=" Связь с администрацией | Форма", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        try:
            await inter.response.send_message('ожидайте', ephemeral=True)
            embed = disnake.Embed(title="``Связь с администрацией``",
                                  description=f'<@&{staff}>'
                                              f'<@{inter.user.id}>',
                                  url='https://i.imgur.com/Du4qBr1.png',
                                  color=disnake.Color.blurple())
            for key, value in inter.text_values.items():
                embed.add_field(
                    name=key.capitalize(),
                    value=value[:1024],
                    inline=False,
                )
            channel = await inter.guild.create_text_channel(f'💇|{inter.user.name}',
                                                            category=disnake.utils.get(
                                                                inter.guild.categories,
                                                                id=1197211209037009006))
            await channel.set_permissions(inter.user,
                                          send_messages=True,
                                          read_message_history=True,
                                          read_messages=True)
            await channel.set_permissions(inter.guild.get_role(inter.guild.id),
                                          send_messages=False,
                                          read_messages=False)

            user_id = inter.user.id
            view = ButtonView(user_id, self.bot)
            await channel.send(embed=embed, view=view)
        except (Exception) as error:
            print(error)


class Application(disnake.ui.Modal):
    def __init__(self, bot):
        self.bot = bot
        components = [
            disnake.ui.TextInput(
                label="ВАШ ИГРОВОЙ НИКНЕЙМ",
                placeholder="Например: S1Non_",
                custom_id="Никнейм",
                max_length=25
            ),
            disnake.ui.TextInput(
                label="ССЫЛКА НА ВАШ STEAM-ПРОФИЛЬМ(ОТКРЫТЫЙ)",
                placeholder="Например: https://steamcommunity.com/id/Zifir72/",
                custom_id="Steam профиль",
                style=disnake.TextInputStyle.paragraph,
                max_length=500
            ),
            disnake.ui.TextInput(
                label="ВАШ ВОЗРАСТ",
                placeholder="Например: 18",
                custom_id="Возраст",
                max_length=25
            ),
            disnake.ui.TextInput(
                label="ВАШ ЧАСОВОЙ ПОЯС И СТРАНА ПРОЖИВАНИЯ",
                placeholder="Например: UTC+7 / Российская Федерация",
                custom_id="Часовой пояс и страна",
                max_length=25
            ),
            disnake.ui.TextInput(
                label="КОЛИЧЕСТВО ВАЙПОВ ОТЫГРАННЫХ",
                placeholder="Например: 1",
                custom_id="Кол-во вайпов",
                max_length=25
            ),
        ]
        super().__init__(title="Заявка на роль модератора | Форма", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        try:
            await inter.response.send_message('ожидайте', ephemeral=True)
            embed = disnake.Embed(title="``Заявка на роль модератора``",
                                  description=f'<@&{staff}>'
                                              f'<@{inter.user.id}>',
                                  url='https://i.imgur.com/Du4qBr1.png',
                                  color=disnake.Color.blurple())
            for key, value in inter.text_values.items():
                embed.add_field(
                    name=key.capitalize(),
                    value=value[:1024],
                    inline=False,
                )
            channel = await inter.guild.create_text_channel(f'💇|{inter.user.name}',
                                                            category=disnake.utils.get(
                                                                inter.guild.categories,
                                                                id=1197162346045517894))
            await channel.set_permissions(inter.user,
                                          send_messages=True,
                                          read_message_history=True,
                                          read_messages=True)
            await channel.set_permissions(inter.guild.get_role(inter.guild.id),
                                          send_messages=False,
                                          read_messages=False)

            user_id = inter.user.id
            view = ButtonView(user_id, self.bot)
            await channel.send(embed=embed, view=view)
        except (Exception) as error:
            print(error)


class Appeal(disnake.ui.Modal):
    def __init__(self, bot):
        self.bot = bot
        components = [
            disnake.ui.TextInput(
                label="ВАШ STEAM64ID | ССЫЛКА -- ОТКАЗ",
                placeholder="Например: 57895789697867989678",
                custom_id="Steamid64",
                max_length=25
            ),
            disnake.ui.TextInput(
                label="ДАТА И ПРИЧИНА БЛОКИРОВКИ",
                placeholder="Например: Например: 02.01.2024 / Читер",
                custom_id="Причина блокировки",
                max_length=25
            ),
            disnake.ui.TextInput(
                label="НИКНЕЙМ МОДЕРАТОРА,ВЫДАВШЕГО БЛОКИРОВКУ",
                placeholder="Например: S1Non_",
                custom_id="Ник модера",
                max_length=25
            ),
            disnake.ui.TextInput(
                label="НОМЕР СЕРВЕРА, НА КОТОРОМ БЛОКИРОВКА",
                placeholder="Например: #1",
                custom_id="Номер сервера",
                max_length=25
            ),
            disnake.ui.TextInput(
                label="ОПИШИТЕ СИТУАЦИЮ",
                placeholder="Например: предоставить видео,загруженное YouTube или Фото загруженное на imgur",
                custom_id="Ситуация",
                style=disnake.TextInputStyle.paragraph,
                max_length=500
            ),
        ]
        super().__init__(title="Апелляция на разбан | Форма", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        try:
            await inter.response.send_message('ожидайте', ephemeral=True)
            embed = disnake.Embed(title="``Апелляция на разбан:``",
                                  description=f'<@&{staff}>'
                                              f'<@{inter.user.id}>',
                                  url='https://i.imgur.com/Du4qBr1.png',)
            for key, value in inter.text_values.items():
                embed.add_field(
                    name=key.capitalize(),
                    value=value[:1024],
                    inline=False,
                )
            channel = await inter.guild.create_text_channel(f'💇|{inter.user.name}',
                                                                  category=disnake.utils.get(
                                                                      inter.guild.categories,
                                                                      id=1197162336688033853))
            await channel.set_permissions(inter.user,
                                          send_messages=True,
                                          read_message_history=True,
                                          read_messages=True)
            await channel.set_permissions(inter.guild.get_role(inter.guild.id),
                                          send_messages=False,
                                          read_messages=False)

            user_id = inter.user.id
            view = ButtonView(user_id, self.bot)
            await channel.send(embed=embed, view=view)
        except (Exception) as error:
            print(error)


class Reportonmoder(disnake.ui.Modal):
    def __init__(self, bot):
        self.bot = bot
        components = [
            disnake.ui.TextInput(
                label="НИКНЕЙМ МОДЕРАТОРА",
                placeholder="Например: S1Non_",
                custom_id="Никнейм",
                max_length=25
            ),
            disnake.ui.TextInput(
                label="НОМЕР СЕРВЕРА",
                placeholder="Например: #1",
                custom_id="Номер сервера",
                max_length=25
            ),
            disnake.ui.TextInput(
                label="НАРУШЕНИЕ МОДЕРАТОРА / ПРИЧИНА ЖАЛОБЫ",
                placeholder="Например: Данный модератор ведёт себя неадекватно в голосом чате сервера",
                custom_id="Причина",
                style=disnake.TextInputStyle.paragraph,
                max_length=500,
            ),
            disnake.ui.TextInput(
                label="ДОКАЗАТЕЛЬСТВО",
                placeholder="Например: предоставить видео,загруженное YouTube или Фото загруженное на imgur",
                custom_id="Доказательства",
                style=disnake.TextInputStyle.paragraph,
                max_length=500
            ),
            disnake.ui.TextInput(
                label="ВАШ STEAMID64 | НЕ ССЫЛКА",
                placeholder="Например: Для того чтобы получить Steam64ID, перейдите на steamid.xyz",
                custom_id="Steamid64",
                max_length=25
            )
        ]
        super().__init__(title="Жалоба на модератора | Форма", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        try:
            await inter.response.send_message('ожидайте', ephemeral=True)
            embed = disnake.Embed(title="``Жалоба на модератора:``",
                                  description=f'<@&{staff}>'
                                  f'<@{inter.user.id}>',
                                  color=disnake.Color.blurple())
            embed.set_thumbnail(url='https://i.imgur.com/Du4qBr1.png')
            for key, value in inter.text_values.items():
                embed.add_field(
                    name=key.capitalize(),
                    value=value[:1024],
                    inline=False,
                )
            channel = await inter.guild.create_text_channel(f'💇| {inter.user.name}',
                                                                  category=disnake.utils.get(
                                                                      inter.guild.categories,
                                                                      id=1197162327263424612))
            await channel.set_permissions(inter.user,
                                          send_messages=True,
                                          read_message_history=True,
                                          read_messages=True)
            await channel.set_permissions(inter.guild.get_role(inter.guild.id),
                                          send_messages=False,
                                          read_messages=False)

            user_id = inter.user.id
            view = ButtonView(user_id, self.bot)
            await channel.send(embed=embed, view=view)
        except (Exception) as error:
            print(error)


class Report(disnake.ui.Modal):
    def __init__(self, bot):
        self.bot = bot
        components = [
            disnake.ui.TextInput(
                label="ВАШ ИГРОВОЙ НИКНЕЙМ",
                placeholder="Например: S1Non_",
                custom_id="Никнейм",
                max_length=25
            ),
            disnake.ui.TextInput(
                label="НОМЕР СЕРВЕРА",
                placeholder="Например: #1",
                custom_id="Номер сервера",
                max_length=25
            ),
            disnake.ui.TextInput(
                label="НАРУШЕНИЕ ИГРОКА / ПРИЧИНА ЖАЛОБЫ",
                placeholder="Например: Читер,летает по воздуху",
                custom_id="Причина",
                style=disnake.TextInputStyle.paragraph,
                max_length=500,
            ),
            disnake.ui.TextInput(
                label="ДОКАЗАТЕЛЬСТВО",
                placeholder="Например: предоставить видео,загруженное YouTube или Фото загруженное на imgur",
                custom_id="Доказательства",
                style=disnake.TextInputStyle.paragraph,
                max_length=500
            )
        ]
        super().__init__(title="Жалоба на игрока | Форма", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        await inter.response.send_message('ожидайте', ephemeral=True)
        try:
            embed = disnake.Embed(title="``Жалоба на игрока:``",
                                  description=f'<@&{staff}>'
                                  f'<@{inter.user.id}>',
                                  color=disnake.Color.blurple())
            embed.set_thumbnail(url='https://i.imgur.com/Du4qBr1.png')
            for key, value in inter.text_values.items():
                embed.add_field(
                    name=key.capitalize(),
                    value=value[:1024],
                    inline=False,
                )
            channel = await inter.guild.create_text_channel(f'💇| {inter.user.name}',
                                                                  category=disnake.utils.get(
                                                                      inter.guild.categories,
                                                                      id=1197162316920262777))
            await channel.set_permissions(inter.user,
                                          send_messages=True,
                                          read_message_history=True,
                                          read_messages=True)
            await channel.set_permissions(inter.guild.get_role(inter.guild.id),
                                          send_messages=False,
                                          read_messages=False)
            user_id = inter.user.id
            view = ButtonView(user_id, self.bot)
            await channel.send(embed=embed, view=view)
        except (Exception) as error:
            print(error)


class select_ticket_dropdown(disnake.ui.StringSelect):
    def __init__(self,bot):
        self.bot = bot
        options = [
            disnake.SelectOption(
                label="Отправить жалобу на игра",
                description="Жалоба на игрока",
            ),
            disnake.SelectOption(
                label="Отправить жалобу на модератора",
                description="Жалоба на модератора/администратора "
            ),
            disnake.SelectOption(
                label="Подать апелляцию",
                description="Подать апелляцию на разбан"
            ),
            disnake.SelectOption(
                label="Написать заявку",
                description="Заявка на роль модератора проекта"
            ),
            disnake.SelectOption(
                label="Связь с администрацией",
                description="Задать любой интересующий вас вопрос"
            )
        ]
        super().__init__(
            placeholder="📃 Выберите категорию",
            min_values=1,
            max_values=1,
            options=options,
        )
    async def callback(self, inter: disnake.MessageInteraction):
        if self.values[0] == '1':
            modal = Report
            await inter.response.send_modal(modal=modal(self.bot))
        if self.values[0] == '2':
            modal = Reportonmoder
            await inter.response.send_modal(modal=modal(self.bot))
        if self.values[0] == '3':
            modal = Appeal
            await inter.response.send_modal(modal=modal(self.bot))
        if self.values[0] == '4':
            modal = Application
            await inter.response.send_modal(modal=modal(self.bot))
        if self.values[0] == '5':
            modal = Communication
            await inter.response.send_modal(modal=modal(self.bot))


class select_ticket_dropdown_view(disnake.ui.View):
    def __init__(self,bot):
        self.bot = bot
        super().__init__()
        self.add_item(select_ticket_dropdown(self.bot))


class Ticket(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('Ticket is Load')

    @commands.slash_command(guild_ids=[guild])
    @commands.has_permissions(administrator=True)
    async def ticket(self, inter: disnake.ApplicationCommandInteraction):
        view = select_ticket_dropdown_view(self.bot)
        emb = disnake.Embed(title='Добро пожаловать в систему тикетов! |  ',
                             description='', color=disnake.Color.gold())
        emb.set_image(url='https://i.imgur.com/ACTEE1W.jpeg')
        await inter.response.send_message(embed=emb, view=view)


def setup(bot: commands.Bot):
    bot.add_cog(Ticket(bot))