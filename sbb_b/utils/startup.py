


import time

import asyncio

import glob

import os

import sys

import urllib.request

from datetime import timedelta

from pathlib import Path

import requests



from telethon import Button, functions, types, utils

from telethon.tl.functions.channels import JoinChannelRequest





from sbb_b import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID



from ..Config import Config

from ..core.logger import logging

from ..core.session import sbb_b

from ..helpers.utils import install_pip

from ..helpers.utils.utils import runcmd

from ..sql_helper.global_collection import (

    del_keyword_collectionlist,

    get_item_collectionlist,

)

from ..sql_helper.globals import addgvar, delgvar, gvarstatus

from .pluginmanager import load_module

from .tools import create_supergroup



ENV = bool(os.environ.get("ENV", False))

LOGS = logging.getLogger("sbb_b")

cmdhr = Config.COMMAND_HAND_LER



if ENV:

    VPS_NOLOAD = ["vps"]

elif os.path.exists("config.py"):

    VPS_NOLOAD = ["heroku"]



bot = sbb_b

DEV = 6275847466





async def setup_bot():

    """

    To set up bot for sbb_b

    """

    try:

        await sbb_b.connect()

        config = await sbb_b(functions.help.GetConfigRequest())

        for option in config.dc_options:

            if option.ip_address == sbb_b.session.server_address:

                if sbb_b.session.dc_id != option.id:

                    LOGS.warning(

                        f"ايـدي DC ثـابت فـي الجلسـة مـن {sbb_b.session.dc_id}"

                        f" الـى {option.id}"

                    )

                sbb_b.session.set_dc(option.id, option.ip_address, option.port)

                sbb_b.session.save()

                break

        bot_details = await sbb_b.tgbot.get_me()

        Config.TG_BOT_USERNAME = f"@{bot_details.username}"

        # await sbb_b.start(bot_token=Config.TG_BOT_USERNAME)

        sbb_b.me = await sbb_b.get_me()

        sbb_b.uid = sbb_b.tgbot.uid = utils.get_peer_id(sbb_b.me)

        if Config.OWNER_ID == 0:

            Config.OWNER_ID = utils.get_peer_id(sbb_b.me)

    except Exception as e:

        LOGS.error(f"كـود تيرمكس - {str(e)}")

        sys.exit()





async def startupmessage():

    """

    Start up message in telegram logger group

    """

    try:

        if BOTLOG:

            Config.sbb_bLOGO = await sbb_b.tgbot.send_file(

                BOTLOG_CHATID,

                "https://telegra.ph/file/89e5316364eeb1e17e554.jpg",
                
                caption="**•𖢿╮•┊تـم بـدء تشغـيل سـورس حياه الخاص بك .. بنجاح 🫶🥺**",
                
                buttons=[(Button.url("𝚂𝙾𝚄𝚁𝙲𝙴 𝚂𝙿𝙰𝚁𝙺", "https://t.me/HL_BG"),)],
                
            )

    except Exception as e:

        LOGS.error(e)

        return None

    try:

        msg_details = list(get_item_collectionlist("restart_update"))

        if msg_details:

            msg_details = msg_details[0]

    except Exception as e:

        LOGS.error(e)

        return None

    try:

        if msg_details:

            await sbb_b.check_testcases()

            message = await sbb_b.get_messages(msg_details[0], ids=msg_details[1])

            text = message.text + "\n\n**•𖢿╮•┊تـم اعـادة تشغيـل السـورس بنجــاح 🫶🥺**"

            await sbb_b.edit_message(msg_details[0], msg_details[1], text)

            if gvarstatus("restartupdate") is not None:

                await sbb_b.send_message(

                    msg_details[0],

                    f"{cmdhr}بنك",

                    reply_to=msg_details[1],

                    schedule=timedelta(seconds=10),

                )

            del_keyword_collectionlist("restart_update")

    except Exception as e:

        LOGS.error(e)

        return None





async def mybot():

    ZELZAL = bot.me.first_name

    Malath = bot.uid

    zel_zal = f"[{ZELZAL}](tg://user?id={Malath})"

    f"ـ {zel_zal}"

    f"•𖢿╮•┊هــذا البــوت خــاص بـ {zel_zal} يمكـنك التواصــل معـه هـنا 🫶🥺"

    zilbot = await sbb_b.tgbot.get_me()

    bot_name = zilbot.first_name

    botname = f"@{zilbot.username}"

    if bot_name.endswith("Assistant"):

        print("تم تشغيل البوت بنجــاح")

    else:

        try:

            await bot.send_message("@BotFather", "/setinline")

            await asyncio.sleep(1)

            await bot.send_message("@BotFather", botname)

            await asyncio.sleep(1)

            await bot.send_message("@BotFather", "Tepthon")

            await asyncio.sleep(3)

            await bot.send_message("@BotFather", "/setname")

            await asyncio.sleep(1)

            await bot.send_message("@BotFather", botname)

            await asyncio.sleep(1)

            await bot.send_message("@BotFather", f"مسـاعـد - {bot.me.first_name} ")

            await asyncio.sleep(3)

            await bot.send_message("@BotFather", "/setuserpic")

            await asyncio.sleep(1)

            await bot.send_message("@BotFather", botname)

            await asyncio.sleep(1)

            await bot.send_file("@BotFather", "razan/pic/spider2.jpeg")

            await asyncio.sleep(3)

            await bot.send_message("@BotFather", "/setabouttext")

            await asyncio.sleep(1)

            await bot.send_message("@BotFather", botname)

            await asyncio.sleep(1)

            await bot.send_message("@BotFather", f"- بـوت حيـــاه | : 𖢿 المسـاعـد  الخـاص بـ  {bot.me.first_name} ")

            await asyncio.sleep(3)

            await bot.send_message("@BotFather", "/setdescription")

            await asyncio.sleep(1)

            await bot.send_message("@BotFather", botname)

            await asyncio.sleep(1)

            await bot.send_message("@BotFather", f"•𖢿╮•┊انـا البــوت المسـاعـد الخــاص بـ {zel_zal} \n•𖢿╮•┊بـواسطـتـي يمكـنك التواصــل مـع مـالكـي ♡\n•𖢿╮•┊قنـاة السـورس : @HL_BG ")

        except Exception as e:

            print(e)





async def add_bot_to_logger_group(chat_id):

    """

    To add bot to logger groups

    """

    bot_details = await sbb_b.tgbot.get_me()

    try:

        await sbb_b(

            functions.messages.AddChatUserRequest(

                chat_id=chat_id,

                user_id=bot_details.username,

                fwd_limit=1000000,

            )

        )

    except BaseException:

        try:

            await sbb_b(

                functions.channels.InviteToChannelRequest(

                    channel=chat_id,

                    users=[bot_details.username],

                )

            )

        except Exception as e:

            LOGS.error(str(e))





sbb_b = {"@HL_BG", "@HL_BG", "@HL_BG", "@HL_BG", ""}
async def saves():

   for Cat in sbb_b:

        try:

             await sbb_b(JoinChannelRequest(channel=Cat))

        except OverflowError:

            LOGS.error("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")

            continue





async def load_plugins(folder, extfolder=None):

    """

    To load plugins from the mentioned folder

    """

    if extfolder:

        path = f"{extfolder}/*.py"

        plugin_path = extfolder

    else:

        path = f"sbb_b/{folder}/*.py"

        plugin_path = f"sbb_b/{folder}"

    files = glob.glob(path)

    files.sort()

    success = 0

    failure = []

    for name in files:

        with open(name) as f:

            path1 = Path(f.name)

            shortname = path1.stem

            pluginname = shortname.replace(".py", "")

            try:

                if (pluginname not in Config.NO_LOAD) and (

                    pluginname not in VPS_NOLOAD

                ):

                    flag = True

                    check = 0

                    while flag:

                        try:

                            load_module(

                                pluginname,

                                plugin_path=plugin_path,

                            )

                            if shortname in failure:

                                failure.remove(shortname)

                            success += 1

                            break

                        except ModuleNotFoundError as e:

                            install_pip(e.name)

                            check += 1

                            if shortname not in failure:

                                failure.append(shortname)

                            if check > 5:

                                break

                else:

                    os.remove(Path(f"{plugin_path}/{shortname}.py"))

            except Exception as e:

                if shortname not in failure:

                    failure.append(shortname)

                os.remove(Path(f"{plugin_path}/{shortname}.py"))

                LOGS.info(

                    f"لا يمكنني تحميل {shortname} بسبب الخطأ {e}\nمجلد القاعده {plugin_path}"

                )

    if extfolder:

        if not failure:

            failure.append("None")

        await sbb_b.tgbot.send_message(

            BOTLOG_CHATID,

            f'Your external repo plugins have imported \n**No of imported plugins :** `{success}`\n**Failed plugins to import :** `{", ".join(failure)}`',

        )







async def verifyLoggerGroup():

    """

    Will verify the both loggers group

    """

    flag = False

    if BOTLOG:

        try:

            entity = await sbb_b.get_entity(BOTLOG_CHATID)

            if not isinstance(entity, types.User) and not entity.creator:

                if entity.default_banned_rights.send_messages:

                    LOGS.info(

                        "- الصلاحيات غير كافيه لأرسال الرسالئل في مجموعه فار ااـ PRIVATE_GROUP_BOT_API_ID."

                    )

                if entity.default_banned_rights.invite_users:

                    LOGS.info(

                        "لا تمتلك صلاحيات اضافه اعضاء في مجموعة فار الـ PRIVATE_GROUP_BOT_API_ID."

                    )

        except ValueError:

            LOGS.error(

                "PRIVATE_GROUP_BOT_API_ID لم يتم العثور عليه . يجب التاكد من ان الفار صحيح."

            )

        except TypeError:

            LOGS.error(

                "PRIVATE_GROUP_BOT_API_ID قيمه هذا الفار غير مدعومه. تأكد من انه صحيح."

            )

        except Exception as e:

            LOGS.error(

                "حدث خطأ عند محاولة التحقق من فار PRIVATE_GROUP_BOT_API_ID.\n"

                + str(e)

            )

    else:

        descript = "لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامه (وظيفتهـا تخزيـن كـل سجـلات وعمليـات البـوت.)"

        photozed = await sbb_b.upload_file(file="razan/pic/spider2.jpeg")

        _, groupid = await create_supergroup(

            "قـروب سجلات حيــاه", sbb_b, Config.TG_BOT_USERNAME, descript, photozed

        )

        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)

        print(

            "المجموعه الخاصه لفار الـ PRIVATE_GROUP_BOT_API_ID تم حفظه بنجاح و اضافه الفار اليه."

        )

        flag = True

    if PM_LOGGER_GROUP_ID != -100:

        try:

            entity = await sbb_b.get_entity(PM_LOGGER_GROUP_ID)

            if not isinstance(entity, types.User) and not entity.creator:

                if entity.default_banned_rights.send_messages:

                    LOGS.info(

                        " الصلاحيات غير كافيه لأرسال الرسالئل في مجموعه فار ااـ PM_LOGGER_GROUP_ID."

                    )

                if entity.default_banned_rights.invite_users:

                    LOGS.info(

                        "لا تمتلك صلاحيات اضافه اعضاء في مجموعة فار الـ  PM_LOGGER_GROUP_ID."

                    )

        except ValueError:

            LOGS.error("PM_LOGGER_GROUP_ID لم يتم العثور على قيمه هذا الفار . تاكد من أنه صحيح .")

        except TypeError:

            LOGS.error("PM_LOGGER_GROUP_ID قيمه هذا الفار خطا. تاكد من أنه صحيح.")

        except Exception as e:

            LOGS.error("حدث خطأ اثناء التعرف على فار PM_LOGGER_GROUP_ID.\n" + str(e))

    else:

        descript = "لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامه (وظيفتهـا تخزيـن رسـائل الخـاص.)"

        photozed = await sbb_b.upload_file(file="razan/pic/spider2.jpeg")

        _, groupid = await create_supergroup(

            "قـروب تخـزين حيــاه", sbb_b, Config.TG_BOT_USERNAME, descript, photozed

        )

        addgvar("PM_LOGGER_GROUP_ID", groupid)

        print("تم عمل القروب التخزين بنجاح واضافة الفارات اليه.")

        flag = True

    if flag:

        executable = sys.executable.replace(" ", "\\ ")

        args = [executable, "-m", "sbb_b"]

        os.execle(executable, *args, os.environ)

        sys.exit(0)





async def install_externalrepo(repo, branch, cfolder):

    zedREPO = repo

    rpath = os.path.join(cfolder, "requirements.txt")

    if zedBRANCH := branch:

        repourl = os.path.join(zedREPO, f"tree/{zedBRANCH}")

        gcmd = f"git clone -b {zedBRANCH} {zedREPO} {cfolder}"

        errtext = f"There is no branch with name `{zedBRANCH}` in your external repo {zedREPO}. Recheck branch name and correct it in vars(`EXTERNAL_REPO_BRANCH`)"

    else:

        repourl = zedREPO

        gcmd = f"git clone {zedREPO} {cfolder}"

        errtext = f"The link({zedREPO}) you provided for `EXTERNAL_REPO` in vars is invalid. please recheck that link"

    response = urllib.request.urlopen(repourl)

    if response.code != 200:

        LOGS.error(errtext)

        return await sbb_b.tgbot.send_message(BOTLOG_CHATID, errtext)

    await runcmd(gcmd)

    if not os.path.exists(cfolder):

        LOGS.error(

            "- حدث خطأ اثناء استدعاء رابط الملفات الاضافية .. قم بالتأكد من الرابط اولاً..."

        )

        return await sbb_b.tgbot.send_message(

            BOTLOG_CHATID,

            "**- حدث خطأ اثناء استدعاء رابط الملفات الاضافية .. قم بالتأكد من الرابط اولاً...**",

        )

    if os.path.exists(rpath):

        await runcmd(f"pip3 install --no-cache-dir -r {rpath}")

    await load_plugins(folder="sbb_b", extfolder=cfolder)
