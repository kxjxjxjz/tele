from .. import *


@sbb_b.ar_cmd(pattern="الاوامر")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\n**𖢿 هـذه هي قائمة اوامـر سـورس حيــاه **\n\n𖢿 `.الامر1` ◂ اوامر الأدمن\n𖢿 `.الامر2` ◂ اوامر المجموعة\n𖢿 `.م3` ◂ اوامر الترحيب\n𖢿 `.م4` ◂ اوامر الردود\n𖢿 `.م5` ◂ اوامر الترفيه\n𖢿 `.م6` ◂ اوامر حماية الخاص\n𖢿 `.م7` ◂ اوامر الاذاعه و الكشف \n𖢿 `.م8` ◂ اوامر البوت \n𖢿 `.م9` ◂ اوامر المنع والترجمه\n𖢿 `.م10` ◂ اوامر التلكراف و النطق\n𖢿 `.م11` ◂ اوامر التحميل\n𖢿 `.م12` ◂ اوامر التكرار\n𖢿 `.م13` ◂ اوامر الانتحال والتقليد\n𖢿 `.م14` ◂ اوامر الوقتي \n𖢿 `.م15` ◂ اوامر الذاتيه والاضافه\n𖢿 `.م16` ◂ اوامر البروفايل\n𖢿 `.م17` ◂ اوامر الأكسترا\n𖢿 `.م18` ◂ التاك و الملفات\n𖢿 `.م19` ◂ اوامر الصيغ\n𖢿 `.م20` ◂ اوامر التسلية\n𖢿 `.م21` ◂ اوامر التحكم\n𖢿 `.م22` ◂ اوامر حماية المجموعة\n𖢿 `.م23` ◂ اوامر لعبة البنك و الخطوط\n𖢿 `.م24` ◂ اوامر الرفع و النسب للتسلية\n𖢿 `.م25` ◂ اوامر تجميع النقاط \n𖢿 `.م26` ◂ اوامر الصيد و الالعاب\n𖢿 `.م27` ◂ اوامر الافتارات و البصمات\n𖢿 `.م28` ◂ اوامر تحديثات السورس \n\n**︙[┈┉━｢ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ｣━┅┈](t.me/HL_BG)**",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="الامر1")
async def hi(event):
    await edit_or_reply(
        event,
        "**قائـمه اوامر الادمن :**\n◂  `.حظر` \n❃ لحظر الشخص في مجموعه بالرد عليه\n\n ◂  `.الصورة -حذف`\n❃ اكتب الامر في المجموعة لحذف صورتها\n\n ◂  `.الصورة -وضع`\n❃ بالرد على الصورة في المجموعة لوضعها صورة للكروب\n\n ◂  `.الغاء الحظر`\n❃ لالغاء حظر الشخص من المجموعه بالرد عليه\n\n ◂  `.كتم` \n❃ لكتم الشخص بالرد عليه او وضع معرفه مع الامر\n\n ◂  `.الغاء كتم`\n❃ لالغاء كتم الشخص بالرد عليه بالامر\n\n ◂  `.تثبيت` \n❃ بالرد على الرسالة لتثبيتها في المجموعة\n\n ◂  `.الغاء تثبيت` \n❃ لألغاء تثبيت الرسالة في المجموعة , اذا اردت الغاء تثبيت جميع الرسائل اكتب مع الامر الكل\n\n ◂  `.رفع مشرف`  < لقب > \n❃ بالرد ؏ المستخدم لرفعه مشرف يمكنك وضع لقب\n\n ◂  `.تنزيل مشرف` \n❃ بالرد ؏ المستخدم لتنزيله من المشرفين\n\n ◂  `.ارفع`\n❃ بالرد ؏ المستخدم لرفعه مشرف في جميع المجموعات \n\n ◂  `.نزل`\n❃ بالرد ؏ المستخدم لتنزيله من جميع المجموعات\n\n ◂  `.الاحداث`\n❃ فقط ارسل الامر لعرض اخر احداث المجموعه \n\n ◂  `.الغاء المحظورين`\n❃ لالغاء جميع المحظورين في المجموعه فقط اكتب الامر\n\n ◂  `.المحذوفين`\n❃ لعرض الحسابات المحذوفة في المجموعه فقط اكتب الامر\n\n ◂  `.تفليش`\n❃ لحظر جميع المستخدمين من المجموعه فقط اكتب الامر\n\n ◂  `.تنزيل الكل`\n❃ لتنزيل جميع المشرفين من المجموعه فقط ارسل الامر في المجموعه\n\n ◂  `.المحظورين`\n❃ لعرض المستخدمين المحظورين في المجموعه اكتب الامر فقط\n\n ◂  `.تحذير`\n❃ بالرد على المستخدم لتحذيره في المجموعه \n\n ◂  `.حذف التحذيرات`\nلحذف تحذيرات المستخدم بالرد عليه او وضع معرفه مع الامر\n\n ◂  `.التحذيرات`\n❃ بالرد على المستخدم لعرض عدد تحذيراته",
    )


@sbb_b.ar_cmd(pattern="الامر2")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائمـه اوامر المجموعة :\n\n ◂  `.المشرفين` \n❃ فقط اكتب الامر في المجموعه لعرض مشرفين المجموعه\n\n ◂  `.البوتات` \n❃ فقط اكتب الامر في الدردشة لعرض البوتات المضافة \n\n ◂  `.الاعضاء`\n❃ فقط اكتب الامر في المجموعه لعرض أعضاء الدردشة\n\n ◂  `.معلومات`\n❃ لعرض معلومات المجموعه اكتبه الامر في المجموعة\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
    )


@sbb_b.ar_cmd(pattern="م3")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائمـه اوامر الترحيب :\n\n ◂  `.ترحيب`\n❃ اكتب الامر مع الترحيب ليقوم بالترحيب في المستخدمين الجدد في المجموعة\n\n ◂  `.الترحيب`\n❃ لعرض رساله الترحيب الحاليه اكتب الامر فقط\n\n ◂  `.حذف الترحيب`\n❃ لالغاء الترحيب في المستخدمين فقط اكتب الامر\n\n⌔∮ متغيرات الترحيب [اضغط هنا](t.me/ZZZ7iZEE_74)\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="م4")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائمـه اوامر الردود :\n\n ◂  `.رد`\n❃ يستخدم الأمر بإضافة رد في المجموعه اكتب الامر والرد الخاص بك بالرد على الكلمه \n\n ◂  `.حذف الردود`\n❃ فقط اكتب الامر في الدردشه لحذف جميع الردود المضافه\n\n ◂  `.الردود`\n❃ لعرض الردود المصافه فقط اكتب الامر\n\n ◂  `.ايقاف`\n❃ اكتب الامر مع الرد لحذف الرد من الدردشه\n\n⌔∮ شرح توضيحي عن اوامر الردود  [اضغط هنا](https://graph.org/اوامر-حياه-04-24)\n⌔∮ شرح عن متغيرات الردود  [اضغط هنا](https://t.me/HL_BG)\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="م5")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\n**قائـمه اوامر الترفيه:**\n\n• جميع هذه الاوامر تستخدم بالرد على الشخص كترفيه\n ◂  `.رفع مطي`\n ◂  `.رفع كلب`\n ◂  `.رفع حيوان`\n ◂  `.رفع زاحف`\n ◂  `.رفع مرتي`\n ◂  `.رفع زوجي`\n ◂  `.رفع تاج`\n ◂  `.رفع بكلبي`\n ◂  `.رفع بزون`\n ◂  `.رفع قرد`\n\n ◂  `.نسبة الحب`\n ◂  `.نسبة الانوثة`\n ◂  `.نسبة الرجولة`\n ◂  `.نسبة الغباء`\n ◂  `.نسبة المثْلية`\n\n ◂  `.كت`\n ◂  `.اوصف`\n ◂  `.هينه`\n ◂  `.نزوج`\n ◂  `.طلاك`\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
    )


@sbb_b.ar_cmd(pattern="م6")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائمـه اوامر حماية الخاص :\n\n ◂  `.الحماية تشغيل`\n❃ لتشغيل امر الحمايه يستخدم لتحذير المستخدمين عند مراسلتك في الخاص من التكرار\n\n ◂  `.الحماية تعطيل`\n❃ لتعطيل امر الحمايه وعدم تحذير المستخدمين في الخاص\n\n ◂  `.سماح` او `.س`\n❃ يستخدم الامر لقبول الشخص في الخاص وعدم ارسال تحذيرات له بالرد على الشخص\n\n ◂  `.رفض` او `.ر`\n❃ يستخدم لرفض الشخص من الخاص وتحذيره اذا كرر الرسائل وبعدها حظره\n\n ◂  `.بلوك`\n❃ بالرد على المستخدم لحظره من الخاص\n\n ◂  `.انبلوك`\n❃ بالرد على المستخدم لالغاء حظره من الخاص\n\n ◂  `.المسموح لهم`\n❃ اكتب الامر فقط لعرض معلومات عن الاشخاص الذين قبلته في الخاص\n\n⌔∮ لعرض فارات الحماية ارسل `.الفارات`\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="م7")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائمـه اوامر الكشف والاذاعة  :\n\n ◂  `.ايدي`\n❃ بالرد على المستخدم او وضع معرفه مع الامر لعرض معلوماته\n\n ◂  `.كشف`\n❃ بالرد على المستخدم لعرض معلومات معينه عنه\n\n ◂  `.للخاص`\n❃ اكتب الامر بالرد على رساله او اي ميديا ليقوم بارساله لجميع المحادثات في الخاص\n\n ◂  `.للكروبات`\n❃ بالرد على نص او اي ميديا ليقوم بنشره في جمبع المجموعات\n\n⌔∮ متغيرات الايدي  [اضغط هنا](https://t.me/HL_BG)\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="م8")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائمـه اوامر البوت :\n\n ◂  `.فحص`\n❃ فقط اكتب الامر لعرض معلومات السورس\n\n ◂  `.بنك`\n❃ فقط اكتب الامر لعرض سرعه البوت\n\n ◂  `.الانترنت + الاضافه`\n❃ يستخدم الامر لقياس سرعه البوت اكتب الامر مع الاضافه  :  `.الانترنت صورة`  `.الانترنت نص`\n\n ◂  `.اعادة تشغيل`\n❃ لعمل اعادة تشغيل للسورس وتحديثه \n\n ◂  `.الاشعارات` + تشغيل/تعطيل\n❃ لتشغيل او تعطيل الاشعارات عند تحديث او اعادة تشغيل السورس\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
    )


@sbb_b.ar_cmd(pattern="م9")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائمـه اوامر المنع والترجمة :\n\n ◂  `.منع`\n𖢿 اكتب الاكر مع الكلمه لمنع ارساله في المجموعه او اي دردشه\n\n ◂  `.الغاء منع`\n𖢿 اكتب الامر مع الكلمه لالغاء منعها من الدردشه\n\n ◂  `.قائمة المنع`\n𖢿 اكتب الامر لعرض قائمه الكلمات التي منعتها في الدردشة\n\n𖢿 لتفعيل امر الترجمة التلقائية\n𖢿 اكتب ◂ `.تفعيل الترجمة التلقائية`\n𖢿 للتعطيل اكتب ◂ `.تعطيل الترجمة التلقائية`\n\n◂  `.ترجمة`\n𖢿 يستخدم الاكر لترجمه الكلمات اكتب الامر مع كود اللغه بالرد غلى النص لترجمته\n\n⌔∮ اكواد اللغات للترجمه  [اضغط هنا](https://t.me/HL_BG)\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
    )


@sbb_b.ar_cmd(pattern="م10")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائمـه اوامر التلكراف و النطق :\n\n ◂  `.انطق`\n❃ بالرد على الكلام لتسجيله ببصمه و ارساله لك\n\n ◂  `.تلكراف ميديا ◂  \n❃ بالرد على الميديا لصنع رابط تلكراف منها\n\n ◂  `.تلكراف نص`\n❃ بالرد على النص لعمل رابط تلكراف\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
    )


@sbb_b.ar_cmd(pattern="م11")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائمـه اوامر التحميل :\n\n ◂  `.متحركات`\n❃ بكتابة عنوان مع الامر لجلب متحركة لك من العنوان\n\n ◂  `.فلم`\n❃ بكتابة اسم الفلم باللغة الانجليزية مع الامر لعرض معلومات الفلم\n\n ◂  `.تحميل فيديو`\n❃ بالرد على رابط من يوتيوب او اي موقع ثاني لتحميل الفيديو وارساله لك\n\n ◂  `.تحميل صوتي`\n❃ اكتب الامر بالرد على الرابط من اليوتيوب لتكميل مقطع الصوتي و ارساله لك\n\n ◂  `.انستا`\n❃ اكتب الامر بالرد على الرابط التحميل من الانستا \n\n ◂  `.بينترست`\n❃ بالرد على رابط من بينتسرت للتحميل لك\n\n ◂  `.صور`\n❃ اكتب الامر مع عنوان للبحث عنه وارسال لك الصور،  اذا بحثت عن اباحي سيتم تعطيل حسابك\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
    )


@sbb_b.ar_cmd(pattern="م12")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\n** قائـمه اوامر التكرار**:\n\n◂ `.كرر`\n❃ اكتب الامر مع عدد التكرار بالرد ؏ النص او او صورة ملصق ليقوم بتكراره مع العدد الذي وضعته\n\n ◂  `.تكرار الملصق` \n❃ بالرد على الملصق ليقوم باستخراج جميع ملصقات الحزمه وارسالها في الدردشة\n\n ◂ `.مكرر`\n❃ اكتب الامر مع وقت بالثواني و مع عدد التكرار وبالرد على صورة او نص  (  تكرار وقتي  )\n\n ◂  `.التكرار`\n❃ بالرد على الرسالة بالامر فقط سيقوم بعمل تكرار سريع ويصل عدده الى 10 الاف تكرار  ! \n\n ◂  `.ايقاف التكرار`\n❃ يقوم هذا الامر بأيقاف التكرار فقط اكتبه\n\n** تنبيه اوامر التكرار قد تؤدي الى حظر حسابك على التلي اذا استخدمتها بشكل غير صحيح**\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
    )


@sbb_b.ar_cmd(pattern="م13")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\n** قائـمه اوامر الأنتحال و التقليد :**\n\n ◂  `.انتحال`\n❃ بالرد على المستخدم لأنتحال حسابه  من اسم وصورة وبايو  . \n\n ◂  `.اعادة الحساب`\n❃ لأعادة حسابك الى وضعه السابق  .\n\n ◂ `.تقليد`\n❃ بالرد على الشخص لتقليد جميع رسائله في الدردشه \n\n ◂ `.الغاء تقليد`\n❃ بالرد على الشخص لايقاف التقليد\n\n ◂ `.المقلدهم `\n❃ لاظهار قائمه الاشخاص الذي فعلت عليهم امر التقليد ولمسحهم ارسل  `.حذف المقلدهم`\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
    )


@sbb_b.ar_cmd(pattern="م14")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائـمه اوامر الوقتي:**\n\n◂ `.اسم وقتي`\n❃ بكتابة الامر لاضافة اسم وقتي حسب منطقة التي وضعتها \n\n ◂ `.انهاء اسم وقتي`\n❃ لانهاء الاسم الوقتي و ارجاع الاسم الطبيعي .\n\n ◂ `.بايو وقتي`\n❃ بكتابة الامر لاضافة ساعه يتحرك مع النبذة الخاصة بك  \n\n ◂ `.انهاء بايو وقتي`\n❃ لانهاء البايو الوقتي و ارجاع البايو الطبيعي\n\n ◂  `.الصورة الوقتية`\n❃ لبدء تشغيل وقت على الصورة الخاصة بحسابك\n\n ◂  `.انهاء الصورة الوقتية`\n❃ لألغاء امر الصورة الوقتية\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
    )


@sbb_b.ar_cmd(pattern="م15")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nاوامر جلب الذاتية وامر الاضافة**:\n\n ◂  `.ضيف`\n❃ اكتب الامر مع رابط مجموعه التي تريد سحب اعضائها وارسل الامر في مجموعتك لسحبهم الى مجموعتك\n\n ◂ `.ذاتيه` او `.ذاتية`\n❃ بالرد على صورة او فيديو ذاتية التدمير لحفظها وارسالها في الرسائل المحفوظة بسرية تامة الامر ل حيــاه حصريا!\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
    )


@sbb_b.ar_cmd(pattern="م16")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائـمه اوامر البروفايل: \n\n ◂  `.تغيير اسم`\n𖢿 لتغيير اسم حسابك اكتب الاسم مع الامر\n\n ◂  `.تغيير بايو`\n𖢿 لتغيير بايو حسابك اكتب البايو مع الامر \n\n ◂  `.تغيير صورة`\n𖢿 لتغيير صورة حسابك بالرد على الصورة بالامر\n\n ◂  `.تغيير معرف`\n𖢿 لتغيير معرف حسابك اكتب المعرف مع الامر\n\n ◂  `.ازالة الصورة`\n𖢿 اكبت الامر لحذف صورة حسابك\n\n ◂  `.معرفاتي`\n𖢿 لعرض معرفات حسابك التي صنعتها\n\n ◂  `.معلوماتي`\n𖢿 لعرض معلومات و احصائيات حسابك\n\n◂ `.قائمه قنواتي`\n𖢿 لعرض قائمة القنوات التى انت مالكها\n\n◂ `.قائمه كروباتي`\n𖢿 لعرض قائمة الكروبات التي انت مالكها\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
    )


@sbb_b.ar_cmd(pattern="م17")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائـمه اوامر الأكسترا: \n\n ◂  `.فك المحظورين`\n❃ قم بكتابة الامر لفك جميع المستخدمين الذي حظرتهم من الخاص\n\n ◂  `.وهمي كتابه`\n❃ لبدء وضع كتابة بشكل وهمي جربه بنفسك\n\n ◂  `.وهمي فيديو`\n❃ لبدء وضع ارسال فيديو بشكل وهمي جربه بنفسك\n\n ◂  `.وهمي لعبه`\n❃ لبدء وضع ارسال لعبة بشكل وهمي جربه بنفسك\n\n ◂  `.وهمي صوتي`\n❃ لبدء وضع ارسال بصمة صوتية بشكل وهمي جربه بنفسك\n\n ◂  `.الحاسبة`\n❃ لعرض حاسبه علميه جربه بنفسك\n\n ◂  `.حالتي`\n❃ لعرض حاله حسابك الحاليه اذا كان محظور او لا\n\n ◂  `.صلاة`❃ اكتب الامر مع اسم محافظتك او مدينتك بالانكليزي لعرض اوقات الصلاة والامساك\n\n ◂  `.تغميق`\n❃ بالرد على الكلام لجعله بشكل غامق\n\n ◂  `.نسخ`\n❃ بالرد على الكلام لجعله بشكل للنسخ\n\n ◂  `.مائل`\n❃ بالرد على الكلام لجعله بشكل مائل\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
    )


@sbb_b.ar_cmd(pattern="م18")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائـمه اوامر التاك والملفات:\n\n ◂  او  `.تاك للكل`\n❃ لعمل تاك لاخر 100 عضو في المجموعه اكتب الامر مع اي نص تريد\n\n ◂  `.تبليغ`\n❃ لتبليغ المشرفين اذا حصل شيء ما فقط اكتب الامر\n\n ◂  `.منشن`\n❃ بالرد على المستخدم وكتابه شيء مع الامر لعمل تاك داخل الكلمه للمستخدم\n\n ◂  `.تنصيب`\n❃ لتنصيب ملفات خارجيه للسورس \n\n ◂  `.الغاء تنصيب`\n❃ بكتابه الامر مع اسم الملف لحذف تنصيبه من السورس\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
    )


@sbb_b.ar_cmd(pattern="م19")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\nقائـمه اوامر الصيغ:\n\n ◂  `.فاس`\n❃ بالرد على متحركو او فيديو لتحويله الى ملصق متحرك\n\n ◂  `.تحويل صورة`\n❃ بالرد على ملصق اتحويله الى صورة\n\n ◂  `.تحويل ملصق`\n❃ بالرد على الصورة لتحويلها الى ملصق\n\n ◂  `.تحويل متحركة `\n❃ بالرد على الفيديو لتحويله الى متحركة \n\n◂  `.لملف`\n❃ بكتابة اسم الملف والرد على كتابة لتحويلها الى ملف\n\n ◂  `.لكتابة`\n❃ بالرد على الملف لاستخراج النص الذي بداخله وارساله لك\n\n ◂  `.الملف لصورة`\n❃ بالرد على الصورة التي تكون بشكل ملف لتحويلها لصورة عادية\n\n ◂  `.تحويل بصمة`\n❃ بالرد على المقطع الوصتي لتحويله الى بصمة\n\n ◂  `.تحويل صوتي`\n❃ بالرد على البصمة لتحويلها على شكل مقطع صوتي\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="م20")
async def hi(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\n**⌔∮ قائـمة اوامر التسلية**: \n\n`.غبي`  `.القنابل`  `.اتصل`   `.قتل`    `.طوبة`\n\n`.مربعات`   `.حلويات`     `.نار`     `.شحن`\n\n`.افكر`    `.متت`    `.ضايج`    `.ساعة`\n\n`.مح`    `.قلب`     `.جيم`     `.الارض`\n\n`.قمر`      `.اقمار`     `.قمور `    `.نجمه`\n\n`.مكعبات`   `.مطر `     `.تفريغ`      `.فليم`\n\n`.احبك`    `.طائره`        `.شرطه `\n\n`.النضام الشمسي`    `.قاتل`       `.عين`\n\n`.افكرر`      `.افعى`         `.رج`      `.مايكرو`\n\n`.فايروس`    `.قطار`      `.موسيقى `\n\n`.رسم`   `.تحميل`     `.مربع`       `.دائره`\n\n`.انيم`    `.بشره`      `.قرد`      `.يد`\n\n`.العد التنازلي`        `.قلوب`\n\n`.فصخ + الكلام`\n\n`.تهكير`     `.تهكير2`   `.تهكير3`\n\nٴ╼──────────────────╾\n • جميع الاوامر تستخدم بالضغط على الامر راح ينسخ وحده وارسله فقط\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="م21")
async def we(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\n• اوامر التحكم تتيح لمستخدم اخر ان يستخدم اوامر تنصيبك وهو غير منصب حيــاه حيث سيصبح متحكم في اوامر تنصيبك يرجى الانتباه من انه سيحصل على صلاحيات الاوامر وقد يسبب خطورة لك اذا كنت لا تثق في المستخدم الذي اضفته. \n\n\n`.التحكم` تفعيل/تعطيل\n• تستخدم هذه الميزة لتفعيل/لتعطيل خاصية التحكم بأوامر تنصيبك للمستخدمين الذين أضفتهم في قائمة المتحكمين\n\n`.المتحكمين`\n• لعرض المستخدمين الذين اضفتهم الى قائمة المستخدمين المتحكمين\n\n`.اضف متحكم`\n• بالرد على المستخدم لأضافته متحكم في تنصيب حيــاه الخاص بك\n\n`.ازالة متحكم`\n• بالرد على المستخدم لازالته من قائمة المتحكمين\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n**⌯︙ [┈┉━｢ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ｣━┅┈](https://t.me/HL_BG)**",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="م22")
async def ae(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\n• اوامر حماية المجموعات بالمسح والتحذير\n\n ◂  `.قفل/فتح`\nالسب\nالفارسية\nالميديا\nالبوتات\nالدخول\nالاضافة\nالتوجيه\nالروابط\nالمعرفات\nالكل\n\n• فقط عليك كتابة قفل او فتح مع الاضافة لقفلها ولأظهار الصلاحيات ارسل `.الاعدادات`\n\n ◂  `.البوتات`\n•لمعرفة البوتات في المجموعة ولطردهم\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n**⌯︙ [┈┉━｢ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ｣━┅┈](https://t.me/HL_BG)",
        link_preview=False,
    )

@sbb_b.ar_cmd(pattern="م23")
async def ae(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\n𖢿 اوامر لعبة البنك و الخطوط\n\n𖢿 قائمة اوامر بنك سورس حيــاه\n\n𖢿 لأنشاء حساب بنكي\n𖢿 اكتب(`.انشاء حساب بنك حيــاه`)\n\n① (`.استثمار` + المبلغ) \n◂ مثال :(`.استثمار 100`)\n② (`.حظ` + المبلغ)\n◂ مثال : (`.حظ 100`)\n③ (`.راتب`)\n④ (`.كنز`)\n⑤ (`.بخشيش`)\n⑥ (`.فلوسي`) | لرؤية فلوسك\n⑦ (`.بنكي` او `.مصرفي`) | برؤية حسابك\n⑧ (`.مسح حسابي`) | لحذف حسابك البنكي\n\n𖢿 قائمة اوامر خطوط سورس حيــاه\n\n𖢿 لتفعيل الخط الغامق\n𖢿 اكتب (`.خط الغامق`)\n𖢿 لألغاء الخط الغامق اكتب الامر مرة ثانية\n\n𖢿 لتفعيل خط الرمز\n𖢿 اكتب (`.خط الرمز`)\n𖢿 لألغاء خط الرمز اكتب الامر مرة ثانية\n\n𖢿 لتفعيل الزخرفة العربية\n𖢿 اكتب ◂ `.تفعيل الزخرفة الانجليزية`\n𖢿 للتعطيل اكتب ◂ `.تعطيل الزخرفة الانجليزية`\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="م24")
async def ae(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\n**𖢿 اوامر الرفع و النسب للتسلية**\n\n𖢿 جميع الاوامر تستخدم بالرد على الشخص\n𖢿 اوامر الرفع للتسلية\n𖢿 .رفع بقلبي .رفع زوجي .رفع مرتي .طلاك\n𖢿 .رفع تاج .رفع مطي .رفع بزون .نزوج\n𖢿 .رفع قرد .رفع كلب .رفع زاحف\n𖢿 .رفع حيوان .رفع حمار\n\n𖢿 اوامر النسب للتسلية \n𖢿 .نسبة الرجولة & .نسبة الانوثة\n𖢿 .نسبة الحب & .نسبة الجمال\n𖢿 .نسبة الغباء & .نسبة الذكاء \n \n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="م25")
async def ae(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\n𖢿 اوامر تجميع النقاط في بوتات التمويل\n\n𖢿 لتجميع نقاط بوت تمويل المليار\n𖢿 اكتب(`.تجميع المليار`)\n➥ @KBKBoT \n\n𖢿 لتجميع نقاط بوت تمويل العرب\n𖢿 اكتب (`.تجميع العرب`)\n ➥ @xnsex21bot\n\n𖢿 لتجميع نقاط بوت تمويل الجوكر\n𖢿 اكتب(`.تجميع الجوكر`)\n➥ @A_MAN9300BOT \n\n𖢿 لتجميع نقاط بوت تمويل الملوك\n𖢿 اكتب (`.تجميع الملوك`) \n➥ @BotTMOEL10M_bot \n\n𖢿 لتجميع نقاط بوت تمويل العملاق\n𖢿 اكتب (`.تجميع العملاق`)\n➥ @TMWEL10M_BOT\n\n𖢿 لتجميع نقاط بوت تمويل العقاب\n𖢿 اكتب (`.تجميع العقاب`)\n➥ @MARKTEBOT\n\n𖢿 لتجميع نقاط بوت تمويل تيربو\n𖢿 اكتب (`.تجميع تيربو`)\n➥ @TURBO7xbot \n\n𖢿 اذا كنت تريد اضافة تجميع نقاط لبوت اخر\n𖢿 تواصل مع ◂ @H_M_Dr \n\n\n**︙ [┈┉━｢ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ｣━┅┈](https://t.me/HL_BG)",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="م26")
async def ae(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\n𖢿 قائمة اوامر الصيد و الالعاب\n\n𖢿 لعرض اوامر صيد اليوزرات\n𖢿 اكتب (`.الصيد`) \n\n𖢿 لعرض العاب الاونلاين لسورس حيــاه\n𖢿 اكتب (`.الالعاب`) & (`.الالعاب2`) \n𖢿 لبدأ لعبة XO ◂ اكتب (`.اكس او`) \n𖢿 لبدأ لعبة الشطرنج ◂ اكتب (`.شطرنج`)\n𖢿 لعرض اوامر الهمسة اكتب ◂ (`.الهمسة`)\n𖢿 العاب الاسئلة (`.كت` ~ `.خيروك`)\n𖢿 للأذكار اكتب ◂ (`.اذكار`)\n\n𖢿 لعمل تاك لأعضاء الجروب او القناة\n𖢿 اكتب (`.تاك`)\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="م27")
async def ae(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\n**𖢿 اوامر الافتارات و البصمات**\n\n𖢿 اوامر الافتارات\n𖢿 `.حالات` & `.حب` & `.بنات` & `.ميمز`\n𖢿 `.ستوري انمي` & `.بنت انمي` & `.ولد انمي`     \n𖢿 `.رياكشن` & `.ري اكشن` & `.رماديه` & `.رمادي`\n𖢿 `.خيرني` & `.تويت` & `.شعر` & `.ادت` & `.معلومه`\n\n𖢿 اوامر بصمات الانمي\n𖢿 `.انمي1`  `.انمي2`  `.انمي3`  `.انمي4`   `.انمي5`\n𖢿 `.انمي6`  `.انمي7`   `.انمي8`  `.انمي9`  `.انمي10`\n\n𖢿 اوامر القرآن الكريم و غنيلي\n𖢿 `.قران` & `.غنيلي` & `.غنيلي2` & `.ريمكس`\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
        link_preview=False,
    )


@sbb_b.ar_cmd(pattern="م28")
async def ae(event):
    await edit_or_reply(
        event,
        "⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺\n\n𖢿 قائمة تحديثات سورس حيــاه\n\n𖢿اوامر عمل حساب gmail وهمي\n𖢿 اكتب ◂ `.ايميل وهمي` \n\n𖢿 تيلثون حيــاه الذكاء الاصطناعي\n𖢿 اكتب (`.os` + اي شئ تريدة)\n𖢿 مثال ◂ `.os كم عدد سكان العراق`\n\n𖢿 سورس حيــاه اختراق كود تيرمكس\n𖢿 اكتب (`.هاك`)\n\n𖢿 سورس حيــاه فحص فيزات\n𖢿 لجلب فيز اكتب ◂ (`.فيزا`)\n𖢿 لفحص فيزا اعمل ريب على الفيزا\n𖢿 واكتب (`.cc`)\n\n𖢿 لجلب معلومات عن حساب github\n𖢿 اكتب ( `.كيثهاب` + يوزر الحساب ) \n\n𖢿 اوامر ارسال رسالة موقوتة\n𖢿 اكتب ( `.مؤقت` + الرسالة + عدد الثواني ) \n𖢿 مثال (`.مؤقت اهلا `10) \n\n𖢿 اوامر الكتم ◂ لكتم شخص في الخاص\n𖢿 للتفعيل اكتب ◂ `.كتم`\n𖢿 للتعطيل اكتب ◂ `.الغاء كتم`\n\n𖢿 اوامر تمبلر\n𖢿 `.تمبلريه` `.البايو` `.الزغرفة` `.الاختصارات` \n\n𖢿 لعرض اخر تحديثات السورس \n𖢿 اكتب ◂ `.التحديثات`\n⩹⌯⊷━♢ ⦓ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 ⦔ ♢━⊶⌯⩺",
        link_preview=False,
    )
    
    
@sbb_b.ar_cmd(pattern="م29")

async def ae(event):

    await edit_or_reply(

        event,

        " سور القرآن الكريم 🌺\n\n1 `.سوره الفاتحة` \n2 `.سوره البقرة` \n3 `.سوره آل عمران` \n4 `.سوره النساء` \n5 `.سوره المائدة` \n6 `.سوره الأنعام` \n7 `.سوره الأعراف` \n8 `.سوره الأنفال` \n9 `.سوره التوبة` \n10 `.سوره يونس` \n11 `.سوره هود` \n12 `.سوره يوسف` \n13 `.سوره الرعد` \n14 `.سوره إبراهيم` \n15 `.سوره الحجر` \n16 `.سوره النحل` \n17 `.سوره الإسراء`\n18 `.سوره الكهف` \n19 `.سوره مريم` \n20 `.سوره طه` \n21 `.سوره الأنبياء` \n22 `.سوره الحج` \n23 `.سوره المؤمنون` \n24 `.سوره النور` \n25 `.سوره الفرقان` \n26 `.سوره الشعراء`\n27 `.سوره النمل` \n28 `.سوره القصص` \n29 `.سوره العنكبوت` \n30 `.سوره الروم` \n31 `.سوره لقمان` \n32 `.سوره السجدة` \n33 `.سوره الأحزاب` \n34 `.سوره سبأ` \n35 `.سوره فاطر` \n36 `.سوره يس` \n37 `.سوره الصافات` \n38 `.سوره ص` \n39 `.سوره الزمر` \n40 `.سوره غافر` \n41 `.سوره فصلت` \n42 `.سوره الشورى`\n43 `.سوره الزخرف`\n44 `.سوره الدخان`\n45 `.سوره الجاثية`\n46 `.سوره الأحقاف`\n47 `.سوره محمد`\n48 `.سوره الفتح` \n49 `.سوره الحجرات` \n50 `.سوره ق` \n51 `.سوره الذاريات` \n52 `.سوره الطور`\n53 `.سوره النجم` \n54 `.سوره القمر` \n55 `.سوره الرحمن` \n56 `.سوره الواقعة` \n57 `.سوره الحديد`\n58 `.سوره المجادلة`\n59 `.سوره الحشر` \n60 `.سوره الممتحنة` \n61 `.سوره الصف` \n62 `.سوره الجمعة` \n63 `.سوره المنافقون` \n64 `.سوره التغابن` \n65 `.سوره الطلاق` \n66 `.سوره التحريم` \n67 `.سوره الملك` \n68 `.سوره القلم` \n69 `.سوره الحاقة` \n70 `.سوره المعارج` \n71 `.سوره نوح` \n72 `.سوره الجن` \n73 `.سوره المزمل` \n74 `.سوره المدثر` \n75 `.سوره القيامة` \n76 `.سوره الإنسان` \n77 `.سوره المرسلات` \n78 `.سوره النبأ` \n79 `.سوره النازعات` \n80 `.سوره عبس` \n81 `.سوره التكوير` \n82 `.سوره الإنفطار` \n83 `.سوره المطففين` \n84 `.سوره الإنشقاق` \n85 `.سوره البروج`\n86 `.سوره الطارق` \n87 `.سوره الأعلى` \n88 `.سوره الغاشية`\n89 `.سوره الفجر`\n90 `.سوره البلد`\n91 `.سوره الشمس`\n92 `.سوره الليل`\n93 `.سوره الضحى`\n94 `.سوره الشرح`\n95 `.سوره التين`\n96 `.سوره العلق`\n97 `.سوره القدر`\n98 `.سوره البينة`\n99 `.سوره الزلزلة`\n100 `.سوره العاديات`\n101 `.سوره القارعة`\n102 `.سوره التكاثر`\n103 `.سوره العصر`\n104 `.سوره الهمزة`\n105 `.سوره الفيل`\n106 `.سوره قريش`\n107 `.سوره الماعون`\n108 `.سوره الكوثر`\n109 `.سوره الكافرون`\n110 `.سوره النصر`\n111 `.سوره المسد`\n112 `.سوره الإخلاص`\n113 `.سوره الفلق`\n114 `.سوره الناس`",

        link_preview=False,

    )
