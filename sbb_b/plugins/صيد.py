#تثبيت`t.me/Dar4k  ~ t.me/R0R77

import random

import requests
import telethon
from telethon.sync import functions
from user_agent import generate_user_agent

from sbb_b import sbb_b

a = "qwertyuiopassdfghjklzxcvbnm"
b = "1234567890"
e = "qwertyuiopassdfghjklzxcvbnm1234567890"

trys, trys2, trys3 = [0], [0], [0]
isclaim = ["off"]
isauto = ["off"]


def check_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False


def gen_user(choice):
    if choice == "ثلاثي":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "خماسي":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "خماسي حرفين":
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسي":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسي حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سباعي":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "بوت":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        username = "".join(f)
        username = username + "bot"

    elif choice == "تيست":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], d[0], c[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    else:
        raise ValueError("Invalid choice for username generation.")
    return username


@sbb_b.ar_cmd(pattern="2الصيد")
async def _(event):
    await event.edit(
        """
** هذه هي قائـمه الصيد الاصدار الثاني الخاصه بسورس الخليفه : **

ٴ— — — — — — — — — —

** الانـواع : ( `ثلاثي` ) - ( `خماسي` ) - ( `سداسي` ) - ( `بوت` ) - ( `سباعي` )**

** ارسل : `سحب` + الـنوع **
** الشـرح : يـقوم بصـيد معـرفات حـسب النـوع **

** الامـر :  `تثبيت` + معرف **
** وظيفة الامـر : يقوم بالتثبيت على المعرف عندما يصبح متاح يأخذه **

 — — — — — — — — — — 
** الامـر:   `.الحاله` **
** • لمعرفة عدد المحاولات للصيد **

 — — — — — — — — — — 
** الامـر:  `.تثبيت` **
** • لمعرفة عدد المحاولات للسحب **

@ZZZ7iZ  - **Source Al-Khalif **

"""
    )


@sbb_b.ar_cmd(pattern="سحب بوت")
async def huntbot(event):
    await event.edit(f"- بدء السحب الان")
    isclaim.clear()
    isclaim.append("on")
    botmod = True
    while botmod:
        username = gen_user("بوت")
        isav = check_user(username)
        if isav == True:
            try:
                await sbb_b.send_message("@botfather", "/newbot")
                await sbb_b.send_message("@botfather", "@ZZZ7iZ - @H_M_Dr 🐊")
                await sbb_b.send_message("@botfather", username)
                await event.client.send_file(
                    event.chat_id,
                    "https://t.me/JZIXl/109",
                    caption="🐊 Khalifa The best  🐊\n- - - - - - - - - - - - - - - - - - - - - - - -\n-  المعرف : ❲ @{} ❳\n- اضغط: ❲ {} ❳\n-  تم حفظ : ❲ bot ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @ZZZ7iZ - @H_M_Dr ❳ ".format(
                        username, trys3
                    ),
                )
                await event.client.send_message(
                    "@H_M_Dr", f"-  انتـهى  : @{username} !\n- By : @ZZZ7iZ - @H_M_Dr !"
                )
                botmod = False
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except telethon.errors.FloodError as e:
                await sbb_b.send_message(
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند-  ({e.seconds}) ثانية .",
                )
                botmod = False
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                if "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    pass
                else:
                    await sbb_b.send_message(
                        event.chat_id,
                        f"""- فشل مع @{username} , الخطأ :{str(eee)}""",
                    )
                    botmod = False
                    break
        else:
            pass
        trys3[0] += 1
    isclaim.clear()
    isclaim.append("off")


@sbb_b.ar_cmd(pattern="سحب (.*)")
async def hunterusername(event):
    if event.text[1:].startswith("سحب بوت"):
        return
    choice = str(event.pattern_match.group(1))
    await event.edit(f"- بدء السحب الان")
    try:
        ch = await sbb_b(
            functions.channels.CreateChannelRequest(
                title="- صـيد الخليفه ",
                about="تم انشاء هذه القناة لصيد المعرفات بواسطة : - @ZZZ7iZ ",
            )
        )
        ch = ch.updates[1].channel_id
    except Exception as e:
        await sbb_b.send_message(
            event.chat_id, f"فشل في انشاء القناة : {str(e)}"
        )
        sedmod = False

    isclaim.clear()
    isclaim.append("on")
    sedmod = True
    while sedmod:
        username = gen_user(choice)
        if username == "error":
            await event.edit("- يرجى وضع النوع بشكل صحيح")
            break
        isav = check_user(username)
        if isav == True:
            try:
                await sbb_b(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_file(
                    event.chat_id,
                    "https://t.me/JZIXl/109",
                    caption="🏆 Khalifa The best 🏆\n- - - - - - - - - - - - - - - - - - - - - - - -\n-  المعرف : ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Type: {}\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @ZZZ7iZ - @H_M_Dr ❳ ".format(
                        username, trys, choice
                    ),
                )
                await event.client.send_file(
                    ch,
                    "https://t.me/JZIXl/109",
                    caption="🏆 Khalifa The best 🏆\n- - - - - - - - - - - - - - - - - - - - - - - -\n-  المعرف: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Type: {}\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @ZZZ7iZ - @H_M_Dr ❳ ".format(
                        username, trys, choice
                    ),
                )
                await event.client.send_message(
                    "@H_M_Dr", f"-  انتـهى  : @{username} !\n- By : @ZZZ7iZ - @H_M_Dr !"
                )
                sedmod = False
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except Exception as baned:
                if "(caused by UpdateUsernameRequest)" in str(baned):
                    pass
            except telethon.errors.FloodError as e:
                await sbb_b.send_message(
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند-  ({e.seconds}) ثانية .",
                )
                sedmod = False
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                if "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    pass
                else:
                    await sbb_b.send_message(
                        event.chat_id,
                        f"""- فشل مع @{username} , الخطا :{str(eee)}""",
                    )
                    sedmod = False
                    break
        else:
            pass
        trys[0] += 1
    isclaim.clear()
    isclaim.append("off")


@sbb_b.ar_cmd(pattern="تثبيت (.*)")
async def _(event):
    msg = event.text.split()
    try:
        ch = str(msg[2])
        ch = ch.replace("@", "")
        await event.edit(f" حسناً سيتم بدء التثبيت في :: @{ch} .")
    except:
        try:
            ch = await sbb_b(
                functions.channels.CreateChannelRequest(
                    title="- صـيد الخليفه",
                    about="- تم انشاء هذه القناة لصيد المعرفات بواسطة @ZZZ7iZ ",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"- تم بنجاح بدأ التثبيت")
        except Exception as e:
            await sbb_b.send_message(
                event.chat_id, f"** فشل في انشاء القناة : {str(e)}"
            )
    isauto.clear()
    isauto.append("on")
    username = str(msg[1])

    swapmod = True
    while swapmod:
        isav = check_user(username)
        if isav == True:
            try:
                await sbb_b(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_file(
                    ch,
                    "https://t.me/JZIXl/109",
                    caption="🏆 Khalifa The best 🏆\n- - - - - - - - - - - - - - - - - - - - - - - -\n-  المعرف : ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @ZZZ7iZ - @H_M_Dr ❳ ".format(
                        username, trys2
                    ),
                )
                await event.client.send_file(
                    event.chat_id,
                    "https://t.me/JZIXl/109",
                    caption="🏆 Khalifa The best 🏆\n- - - - - - - - - - - - - - - - - - - - - - - -\n- * المعرف **: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Save: ❲ Chaneel ❳\n- - - - - - - - - - - - - - - - - - - - - - - -\nThE KiNgS ❲ @ZZZ7iZ - @H_M_Dr ❳ ".format(
                        username, trys2
                    ),
                )
                await event.client.send_message(
                    "@H_M_Dr",
                    f"- منتهي : @{username} !\n- By : @ZZZ7iZ - @H_M_Dr !\n-  سجل السحب  {trys2}",
                )
                swapmod = False
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(
                    event.chat_id, f"المعرف : @{username} غير صالح "
                )
                swapmod = False
                break
            except telethon.errors.FloodError as e:
                await sbb_b.send_message(
                    event.chat_id, f"للاسف تبندت : مدة الباند ({e.seconds}) ثانية "
                )
                swapmod = False
                break
            except Exception as eee:
                await sbb_b.send_message(
                    event.chat_id,
                    f"""فشل مع {username} ، الخطأ :{str(eee)}""",
                )
                swapmod = False
                break
        else:
            pass
        trys2[0] += 1

    isclaim.clear()
    isclaim.append("off")


@sbb_b.ar_cmd(pattern="الحاله")
async def _(event):
    if "on" in isclaim:
        await event.edit(f"- السحب وصل لـ({trys[0]}) من المحاولات")
    elif "off" in isclaim:
        await event.edit("- السحب بالاصل لا يعمل .")
    else:
        await event.edit("- لقد حدث خطأ ما وتوقف الامر لديك")


@sbb_b.ar_cmd(pattern="تثبيت")
async def _(event):
    if "on" in isauto:
        await event.edit(f"- التثبيت وصل لـ({trys2[0]}) من المحاولات")
    elif "off" in isauto:
        await event.edit("- التثبيت بالاصل لا يعمل .")
    else:
        await event.edit("-لقد حدث خطأ ما وتوقف الامر لديك")