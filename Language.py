from PY18N.extension import I18nExtension, Language
from nextcord.ext import commands

from SQL import Database_SQL
from config import STANDART_LANGUAGE_USER
i18n = I18nExtension([
    Language("English","en",{
        'member_join':'''Hi, {user_tag}, my name is {NAME_NOZOMI}! 
            On this server I'll' be your main assistant with everything,
            from help to contacting with {FATHER_NAME} to using all functionality of this server.
            All can see the entire list of my capabilities by using the /help command. Tag me if you need me😉
            You №{user_num} on this server.
            You joined on {datatime}''',
        'command_list':'''
/help marriage                  -  Marriage commands 
/help game                        -  Game commands
/help language                     -  Language changing command's
/anecdotes                        -  Random joke
/contact                             -  Dev contacts
/github                               -  Github''',
        'command_list_merriage':'''
/marriage <username> <username>   -  Marry
/divorce                                                       -  Divorce''',
        'command_list_game':'''
/dice                                       -  Dice
/More_less <more/less>  -  More/Less''',
        'Hello_Admine':', {FATHER_NAME} send you greetings',
        'FATHER_NAME_COMMAND':', this ',
        'HI':'Hi, ', 
        "Hey":"Hey there, I'm Nozomi_bot_Discord",
        'lang':'/language <<english> or <russian>>                      -  change language to English or Russian'}),

    Language("Russian","ru",{
        'member_join':'''Привет, {user_tag}, я {NAME_NOZOMI}! 
            На этом сервере я буду твоим главным помощником во всем, 
            начиная от помощи для обращения к {FATHER_NAME} до использования всех функций этого сервера. 
            Весь список моих возможностей ты найдёшь по команде "/help". Если понадоблюсь зови😉
            Ты №{user_num} на этом сервере
            Ты вошёл в {datatime}''',
        'command_list':'''
/help marriage                  -  Команды для свадьбы 
/help game                        -  Команды для игр
/help language                     -  Команды для смены языка
/anecdotes                        -  Случайный анекдот
/contact                             -  Контакты для связи
/github                               -  Github автора''',
        'command_list_merriage':'''
/marriage <username> <username>   -  Свадьба
/divorce                                                       -  Развод''',
        'command_list_game':'''
/dice                                       -  Игра в кости
/More_less <more/less>  -  Игра в больше меньше''',
        'Hello_Admine':', {FATHER_NAME} передает и тебе привет',
        'FATHER_NAME_COMMAND':', это ',
        'HI':'Привет, ', 
        "Hey":"Привет, я Nozomi_bot_Discord",
        'lang':'/language <<english> or <russian>>                      -  смена языка на Английский или Русский'})   
        ], fallback = STANDART_LANGUAGE_USER)
def get_locale(ctx: commands.Context):
    return Database_SQL.select('language', ctx.author.id)