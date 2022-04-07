from nextcord import Colour, Embed, Intents, utils, Member
from nextcord.ext import commands
from datetime import datetime
from logging import DEBUG, basicConfig

from config import FATHER_NAME, FATHER_NAME_COMMAND, NAME_NOZOMI, SERVER_STARTER_CHANNEL, STARTER_ROLE, TOKEN, Hello, Hello_Admine
from SQL import Database_SQL
from PY18N.extension import _
from Language import i18n, get_locale

bot = commands.Bot(command_prefix="/", intents=Intents().all(), help_command=None)

basicConfig(level=DEBUG)
i18n.init_bot(bot, get_locale)

@bot.command(pass_context=True)
async def help(ctx, arg=None):
    if not arg:
        await ctx.channel.send(_('command_list'))
    if arg == 'language':
        await ctx.channel.send(_('lang'))
    if arg == 'marriage':
        await ctx.channel.send(_('command_list_merriage'))
    if arg == 'game':
        await ctx.channel.send(_('command_list_game'))

@bot.command(pass_context=True)
async def language(ctx, arg=None):
    user_id = ctx.message.author.id
    try:
        if arg.lower() == 'english':
            Database_SQL.update_lang('en', user_id)
            await ctx.channel.send('You changed your language')
        if arg.lower() == 'russian':
            Database_SQL.update_lang('ru', user_id)
            await ctx.channel.send('Вы сменили язык')
    except:
        pass
    if not arg:
        await ctx.channel.send(_('lang'))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content in Hello:
        await message.channel.send(_('HI') + f'{message.author.mention}')
    if message.content in Hello_Admine:
        await message.channel.send(f'{message.author.mention}'+_('Hello_Admine').format(FATHER_NAME=FATHER_NAME))
    if message.content in FATHER_NAME_COMMAND:
        await message.channel.send(f'{message.author.mention}'+_('FATHER_NAME_COMMAND') + f'{FATHER_NAME}')
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    user_num= len(list(member.guild.members))
    avatar = member.display_avatar
    name_channel = member.guild
    user_tag = member.mention
    user_id = member.id
    datatime= datetime.now()
    member_join = _('member_join').format(user_tag=user_tag, NAME_NOZOMI=NAME_NOZOMI, FATHER_NAME=FATHER_NAME, user_num=user_num, datatime=datatime)
    em = Embed(color= Colour.random(), description=member_join)
    em.set_footer(text=name_channel, icon_url=member.guild.icon)
    em.set_image(url=avatar)
    em.timestamp = datetime.utcnow()
    channel = bot.get_channel(SERVER_STARTER_CHANNEL)
    welcome_message = await channel.send(embed=em)
    await member.add_roles(utils.get(member.guild.roles, id=STARTER_ROLE))
    Database_SQL.insert(str(name_channel), int(user_id), str(user_tag), str(member), str(avatar), int(user_num), datatime, int(welcome_message.id))

@bot.event
async def on_member_remove(member):
    user_id = member.id
    message=Database_SQL.select('welcome_message', user_id)
    try:
        await bot.http.delete_message(SERVER_STARTER_CHANNEL, message)
    finally:
        Database_SQL.Del_user(user_id)

@bot.event
async def on_ready():
    Database_SQL.create_table()
    for guild in bot.guilds:
        for member in guild.members:
            if not Database_SQL.get_member(member):
                user_num= 0
                avatar = member.display_avatar
                name_channel = member.guild
                user_tag = member.mention
                user_id = member.id
                datatime= datetime.now()
                welcome_message= 0
                Database_SQL.insert(str(name_channel), int(user_id), str(user_tag), str(member), str(avatar), int(user_num), datatime, int(welcome_message))
    print('START')
bot.run(TOKEN)
#Author: IPOleksenko