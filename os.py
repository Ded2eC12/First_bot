# Импорт модулей

import disnake
from time import sleep
from random import choice
from disnake.ext import commands

# Создание самого бота

bot = commands.Bot(command_prefix="!",
                   help_command=None,
                   intents=disnake.Intents.all())
CENSORED_WORDS = ["/join", "/play", "/stop"]

# Первый ивент говорит об успешном запуске бота


@bot.event
# Метод on_ready говорит о начале работы бота
async def on_ready():
  print("Бот", bot.user.name, "запущен")


@bot.event
async def on_member_join(member):
  pic = [
    "https://i.pinimg.com/originals/3a/ad/23/3aad23e7c9ba44b7b0af27e7763b57ac.jpg",
    "https://i.pinimg.com/originals/24/9a/7a/249a7a5ddd354f8c0700d384dc18ee0f.jpg",
    "https://i.pinimg.com/originals/b3/79/83/b37983d24e44196c60a74bc3abf2bb1d.jpg",
    "https://i.pinimg.com/originals/ee/0a/38/ee0a386c576bfba3b0f96997efdba895.jpg",
    "https://i.pinimg.com/originals/47/25/dd/4725dd5b3b9a887bdcb5805893df8b34.jpg"
  ]
  picture = choice(pic)
  role = disnake.utils.get(member.guild.roles, id=1123563730010124379)
  channel = bot.get_channel(1124309330116739122)
  embed = disnake.Embed(title="Новый участник!!?",
                        description=f"{member.name}#{member.discriminator}",
                        color=0xFF00FF)
  embed.set_image(url=picture)
  await member.add_roles(role)
  await channel.send(embed=embed)


@bot.event
# Программа для удаления сообщений +p и тд в текстовом канале
async def on_message(message):
  await bot.process_commands(message)

  channel = bot.get_channel(1123913670154534912)
  if message.channel == channel:
    if message.author != bot.user and message.author.id == 184405311681986560:
        await message.delete()
        await channel.send(
          f"{message.author.mention} этот канал не для музыки!",
          delete_after=20)

# Программа для удаления сообщений в музыкальном канале
  channel = bot.get_channel(1123913721006264330)
  worst = ()
  time = 0
  if message.channel == channel:
    for i in message.content.split():
      time += 1
      word = i.lower()
      if word not in CENSORED_WORDS and message.author != bot.user and message.author.id != 184405311681986560:
        if time == 1:
          await message.delete()
          await channel.send(
            f"{message.author.mention} прости, но этот канал только для музыки!",
            delete_after=20)


# Программа для удаления человека с сервера


@bot.command()
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: disnake.Member, *, reason="Нарушение правил!"):
  channel = bot.get_channel(1124309330116739122)
  await ctx.channel.send(
    f"Один из гениев {ctx.author.mention} исключил пользователя {member.mention}",
    delete_after=20)
  await member.kick(reason=reason)
  await ctx.message.delete()



"""bot.run(Your token)"""
