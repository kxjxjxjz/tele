from telethon import events

from sbb_b import sbb_b

from ..sql_helper.globals import addgvar, delgvar, gvarstatus


@sbb_b.ar_cmd(pattern="تفعيل الزخرفة الانجليزية")
async def zakrafaon(event):
    if not gvarstatus("enzakrafa"):
        addgvar("enzakrafa", "on")
        await edit_delete(event, "𖢿 **تم تفعيل الزخرفة الانجليزية بنجاح ✅**")
        return
    if gvarstatus("enzakrafa"):
        await edit_delete(event, "𖢿 **الزخرفة الانجليزية مفعلة بالفعل ✅**")
        return


@sbb_b.ar_cmd(pattern="تعطيل الزخرفة الانجليزية")
async def zakrafaoff(event):
    if not gvarstatus("enzakrafa"):
        await edit_delete(event, "𖢿 **الزخرفة الانجليزية غير مفعلة بالفعل ❌**")
        return
    if gvarstatus("enzakrafa"):
        delgvar("enzakrafa")
        await edit_delete(event, "𖢿 **تم تعطيل الزخرفة الانجليزية بنجاح ❌**")
        return


@sbb_b.on(events.NewMessage(outgoing=True))
async def zakrafarun(event):
    if gvarstatus("enzakrafa"):
        text = event.message.message
        uppercase_text = (
            text.replace("a", "𝔸")
            .replace("b", "𝔹")
            .replace("c", "ℂ")
            .replace("d", "𝔻")
            .replace("e", "𝔼")
            .replace("f", "𝔽")
            .replace("g", "𝔾")
            .replace("h", "ℍ")
            .replace("i", "𝕀")
            .replace("j", "𝕁")
            .replace("k", "𝕂")
            .replace("l", "𝕃")
            .replace("m", "𝕄")
            .replace("n", "ℕ")
            .replace("o", "𝕆")
            .replace("p", "ℙ")
            .replace("q", "ℚ")
            .replace("r", "ℝ")
            .replace("s", "𝕊")
            .replace("t", "𝕋")
            .replace("u", "𝕌")
            .replace("v", "𝕍")
            .replace("w", "𝕎")
            .replace("x", "𝕏")
            .replace("y", "𝕐")
            .replace("z", "ℤ")
        )
        await event.edit(uppercase_text)
