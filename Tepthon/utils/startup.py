# ZedThon - Tepthon
# Copyright (C) 2022 ZedThon . All Rights Reserved
#< https://t.me/ZThon >
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/master/LICENSE/>.

import time
import asyncio
import importlib
import logging
import glob
import os
import sys
import urllib.request
from datetime import timedelta
from pathlib import Path
from random import randint
from datetime import datetime as dt
from pytz import timezone
import requests
import heroku3

from telethon import Button, functions, types, utils
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.contacts import UnblockRequest

from Tepthon import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from ..Config import Config
from ..core.logger import logging
from ..core.session import zedub
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
LOGS = logging.getLogger("𝐬𝐨𝐮𝐫𝐜𝐞 الزعيم 🇵🇸")
cmdhr = Config.COMMAND_HAND_LER
Zed_Vip = (6723830547, 6583951825)
zchannel = {"@SSSTF2", "@EEEW2", "", "@EEEW2", "@SSSTF2"}
heroku_api = "https://api.heroku.com"
if Config.HEROKU_APP_NAME is not None and Config.HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
    app = Heroku.app(Config.HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


if ENV:
    VPS_NOLOAD = ["vps"]
elif os.path.exists("config.py"):
    VPS_NOLOAD = ["heroku"]

bot = zedub
DEV = 1260465030


async def autovars(): #Code by T.me/zzzzl1l
    if "ENV" in heroku_var:
        return
    LOGS.info("جـارِ إضافـة بقيـة الفـارات .. تلقائيًــا")
    zzenv = "ANYTHING"
    zzcom = "."
    zzztz = "Asia/Amman"
    heroku_var["ENV"] = zzenv
    heroku_var["COMMAND_HAND_LER"] = zzcom
    heroku_var["TZ"] = zzztz
    LOGS.info("تم إضافـة بقيـة الفـارات .. بنجـاح")


async def autoname(): #Code by T.me/zzzzl1l
    if Config.ALIVE_NAME:
        return
    await bot.start()
    await asyncio.sleep(15)
    LOGS.info("جـارِ إضافـة فـار الاسـم التلقـائـي .. انتظـر قليلًا")
    zelzal = await bot.get_me()
    zzname = f"{zelzal.first_name}"
    tz = Config.TZ
    tzDateTime = dt.now(timezone(tz))
    zdate = tzDateTime.strftime('%Y/%m/%d')
    militaryTime = tzDateTime.strftime('%H:%M')
    ztime = dt.strptime(militaryTime, "%H:%M").strftime("%I:%M %p")
    zzd = f"‹ {zdate} ›"
    zzt = f"‹ {ztime} ›"
    if gvarstatus("z_date") is None:
        zd = "z_date"
        zt = "z_time"
        addgvar(zd, zzd)
        addgvar(zt, zzt)
    LOGS.info(f"تم إضافـة اسـم المستخـدم {zzname} .. بنجـاح")
    heroku_var["ALIVE_NAME"] = zzname


async def setup_bot():
    """
    To set up bot for zthon
    """
    try:
        await zedub.connect()
        config = await zedub(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == zedub.session.server_address:
                if zedub.session.dc_id != option.id:
                    LOGS.warning(
                        f"أيـدي DC ثـابت فـي الجلسـة مـن {zedub.session.dc_id}"
                        f" إلـى {option.id}"
                    )
                zedub.session.set_dc(option.id, option.ip_address, option.port)
                zedub.session.save()
                break
        bot_details = await zedub.tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        # await zedub.start(bot_token=Config.TG_BOT_USERNAME)
        zedub.me = await zedub.get_me()
        zedub.uid = zedub.tgbot.uid = utils.get_peer_id(zedub.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(zedub.me)
    except Exception as e:
        LOGS.error(f"كـود تيرمكس - {str(e)}")
        sys.exit()


async def mybot(): #Code by T.me/zzzzl1l
    ZELZAL = bot.me.first_name
    Malath = bot.uid
    zel_zal = f"[{ZELZAL}](tg://user?id={Malath})"
    f"ـ {zel_zal}"
    f"•⎆┊هــذا البــوت خــاص بـ {zel_zal} يمكـنك التواصــل معـه هـنا 🧸♥️"
    zilbot = await zedub.tgbot.get_me()
    bot_name = zilbot.first_name
    botname = f"@{zilbot.username}"
    if bot_name.startswith("مسـاعـد"):
        print("تم تشغيل البوت بنجــاح")
    else:
        try:
            await bot.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "الزعيم")
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
            await bot.send_file("@BotFather", "Tepthon/zilzal/logozed.jpg")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setabouttext")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", f"- بـوت الزعيم المسـاعـد ♥️🦾 الخـاص بـ  {bot.me.first_name} ")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", f"•⎆┊انـا البــوت المسـاعـد الخــاص بـ {zel_zal} \n•⎆┊بـواسطـتـي يمكـنك التواصــل مـع مـالكـي 🧸♥️\n•⎆┊جروب الزعيم 🌐 @EEEW2 🌐")
        except Exception as e:
            print(e)


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    if gvarstatus("PMLOG") and gvarstatus("PMLOG") != "false":
        delgvar("PMLOG")
    if gvarstatus("GRPLOG") and gvarstatus("GRPLOG") != "false":
        delgvar("GRPLOG")
    try:
        if BOTLOG:
            Config.ZEDUBLOGO = await zedub.tgbot.send_file(
                BOTLOG_CHATID,
                "https://graph.org/file/e16eb92a2ca2a2651b96b.jpg",
                caption="**•⎆┊تـم بـدء تشغـيل سـورس الزعيم الخاص بك .. بنجاح 🧸♥️**",
                buttons=[(Button.url("سورس الزعيم 🇵🇸", "https://t.me/EEEW2"),)],
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
            await zedub.check_testcases()
            message = await zedub.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**•⎆┊تـم إعـادة تشغيـل السـورس بنجــاح 🧸♥️**"
            await zedub.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartupdate") is not None:
                await zedub.send_message(
                    msg_details[0],
                    f"{cmdhr}بنك",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await zedub.tgbot.get_me()
    try:
        await zedub(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=bot_details.username,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await zedub(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[bot_details.username],
                )
            )
        except Exception as e:
            LOGS.error(str(e))


async def saves():
   for Zcc in zchannel:
        try:
             await zedub(JoinChannelRequest(channel=Zcc))
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
        path = f"Tepthon/{folder}/*.py"
        plugin_path = f"Tepthon/{folder}"
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
        await zedub.tgbot.send_message(
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
            entity = await zedub.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "- الصلاحيات غير كافية لإرسال الرسائـل في مجموعة فار الـ PRIVATE_GROUP_BOT_API_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "لا تمتلك صلاحيات إضافة اعضاء في مجموعة فار الـ PRIVATE_GROUP_BOT_API_ID."
                    )
        except ValueError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID لم يتم العثور عليه . يجب التأكد من ان الفار صحيح."
            )
        except TypeError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID قيمة هذا الفار غير مدعومه. تأكد من انه صحيح."
            )
        except Exception as e:
            LOGS.error(
                "حدث خطأ عند محاولة التحقق من فار PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامة (وظيفتهـا تخزيـن كـل سجـلات وعمليـات البـوت.)"
        photozed = await zedub.upload_file(file="zedthon/malath/Tepthon.jpg")
        _, groupid = await create_supergroup(
            "مجموعـة السجـل الزعيم", zedub, Config.TG_BOT_USERNAME, descript, photozed
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print(
            "المجموعه الخاصه لفار الـ PRIVATE_GROUP_BOT_API_ID تم حفظه بنجاح و إضافة الفار إليـه."
        )
        flag = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await zedub.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        " الصلاحيات غير كافية لإرسال الرسائـل في مجموعة فار الـ PM_LOGGER_GROUP_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "لا تمتلك صلاحيات إضافة اعضاء في مجموعة فار الـ  PM_LOGGER_GROUP_ID."
                    )
        except ValueError:
            LOGS.error("PM_LOGGER_GROUP_ID لم يتم العثور على قيمة هذا الفار . تأكد من أنه صحيح .")
        except TypeError:
            LOGS.error("PM_LOGGER_GROUP_ID قيمة هذا الفار خطأ. تأكد من أنه صحيح.")
        except Exception as e:
            LOGS.error("حدث خطأ أثناء التعرف على فار PM_LOGGER_GROUP_ID.\n" + str(e))
    else:
        descript = "لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامة (وظيفتهـا تخزيـن رسـائل الخـاص.)"
        photozed = await zedub.upload_file(file="zedthon/malath/Tep.jpg")
        _, groupid = await create_supergroup(
            "مجموعـة التخـزين", zedub, Config.TG_BOT_USERNAME, descript, photozed
        )
        addgvar("PM_LOGGER_GROUP_ID", groupid)
        print("تم عمل الكروب التخزين بنجاح وإضافـة الفارات إليـه.")
        flag = True
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "Tepthon"]
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
        return await zedub.tgbot.send_message(BOTLOG_CHATID, errtext)
    await runcmd(gcmd)
    if not os.path.exists(cfolder):
        LOGS.error(
            "- حدث خطأ أثناء استدعاء رابط الملفات الإضافيـة .. قم بالتأكد من الرابط اولاً..."
        )
        return await zedub.tgbot.send_message(
            BOTLOG_CHATID,
            "**- حدث خطأ أثناء استدعاء رابط الملفات الإضافيـة .. قم بالتأكد من الرابط اولاً...**",
        )
    if os.path.exists(rpath):
        await runcmd(f"pip3 install --no-cache-dir -r {rpath}")
    await load_plugins(folder="Tepthon", extfolder=cfolder)
