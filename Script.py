class script(object):   
    HELP_TXT = """𝖧𝖤𝖸! {}\n𝖧𝖾𝗋𝖾 𝗂𝗌 𝗆𝗒 𝗁𝖾𝗅𝗉 𝖢𝖬𝖣𝗌."""

    ABOUT_TXT = """- 𝖬𝗒 𝖭𝖺𝗆𝖾 : {}
- 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href=https://t.me/k_ASTRA1>KevinASTRA</a>
- 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : Pyrogram
- 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : 𝖯𝗒𝗍𝗁𝗈𝗇 𝟥
- 𝖣𝖺𝗍𝖺𝖡𝖺𝗌𝖾 : 𝖬𝗈𝗇𝗀𝗈𝖣𝖡
- 𝖡𝖮𝖳 𝖲𝖾𝗋𝗏𝖾𝗋 : 𝖠𝗇𝗒𝖶𝗁𝖾𝗋𝖾
- 𝖡𝗎𝗂𝗅𝖽 𝖵𝖾𝗋𝗌𝗂𝗈𝗇 : 𝖯𝗋𝗈𝗃𝖾𝖼𝗍 𝖴𝗉𝗁𝗈𝗋𝗂𝖺 𝖵𝟢𝟣"""

    SOURCE_TXT = """<b>NOTE:</b>
- 𝖲𝗈𝗎𝗋𝖼𝖾 𝖢𝗈𝖽𝖾: 𝖳𝗁𝗂𝗌 𝗉𝗋𝗈𝗃𝖾𝖼𝗍 𝗂𝗌 𝗇𝗈𝗍 𝗈𝗉𝖾𝗇-𝗌𝗈𝗎𝗋𝖼𝖾, 𝖺𝗇𝖽 𝖨 𝖽𝗈 𝗇𝗈𝗍 𝗁𝖺𝗏𝖾 𝗈𝗐𝗇𝖾𝗋𝗌𝗁𝗂𝗉 𝗈𝖿 𝖺𝗅𝗅 𝗂𝗍𝗌 𝖼𝗈𝗆𝗉𝗈𝗇𝖾𝗇𝗍𝗌.

<b>𝖣𝖤𝖵:</b>
- 𝖢𝗋𝖾𝖺𝗍𝖾𝖽 𝖡𝗒<a href=https://t.me/k_ASTRA1>𝖪𝖾𝗏𝗂𝗇𝖠𝖲𝖳𝖱𝖠</a>
- 𝖢𝗋𝖾𝖽𝗂𝗍𝗌<a href=https://t.me/k_ASTRA1>𝖡𝖮𝖳 𝖮𝗐𝗇𝖾𝗋</a>"""

    FILE_TXT = """ 𝖧𝖾𝗅𝗉: 𝖥𝗂𝗅𝖾 𝖲𝗍𝗈𝗋𝖾 𝖬𝗈𝖽𝗎𝗅𝖾../

<b>𝖡𝗒 𝖳𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗌𝗍𝗈𝗋𝖾 𝖺𝗇𝖽 𝗆𝖺𝗇𝖺𝗀𝖾 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾 𝗐𝗂𝗍𝗁 𝖾𝖺𝗌𝖾. 𝖸𝗈𝗎 𝖼𝖺𝗇 𝖼𝗋𝖾𝖺𝗍𝖾 𝖿𝗈𝗅𝖽𝖾𝗋𝗌, 𝖺𝖽𝖽 𝗍𝖺𝗀𝗌, 𝗌𝖾𝗍 𝖺𝖼𝖼𝖾𝗌𝗌 𝗉𝖾𝗋𝗆𝗂𝗌𝗌𝗂𝗈𝗇𝗌, 𝖺𝗇𝖽 𝗍𝗋𝖺𝖼𝗄 𝖼𝗁𝖺𝗇𝗀𝖾𝗌. 𝖤𝗇𝗁𝖺𝗇𝖼𝖾 𝗒𝗈𝗎𝗋 𝗉𝗋𝗈𝖽𝗎𝖼𝗍𝗂𝗏𝗂𝗍𝗒 𝗐𝗂𝗍𝗁 𝗌𝗍𝗋𝖾𝖺𝗆𝗅𝗂𝗇𝖾𝖽 𝖿𝗂𝗅𝖾 𝗆𝖺𝗇𝖺𝗀𝖾𝗆𝖾𝗇𝗍...//</b>

◯ <b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝖭𝖣 𝖴𝗌𝖺𝗀𝖾:</b>

◯ /plink ›› <b>𝖱𝖾𝗉𝗅𝗒 𝖳𝖮 𝖺𝗇𝗒 𝗆𝖾𝖽𝗂𝖺 𝗍𝗈 𝗀𝖾𝗍 𝗅𝗂𝗇𝗄</b>
◯ /pbatch ›› <b>𝖴𝗌𝖾 𝗒𝗈𝗎𝗋 𝗆𝖾𝖽𝗂𝖺 𝗅𝗂𝗇𝗄 𝗐𝗂𝗍𝗁 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽</b>
◯ /batch ›› <b>𝖳𝗈 𝖼𝗋𝖾𝖺𝗍𝖾 𝗅𝗂𝗇𝗄 𝖿𝗈𝗋 𝗆𝗎𝗅𝗍𝗂𝗉𝗅𝖾</b>

◯ 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 -

<code>/batch https://t.me/k_ASTRA1 https://t.me/k_ASTRA1</code>

𝖣𝖾𝗏 • <a href=https://t.me/k_ASTRA1><b>𝖪𝖾𝗏𝗂𝗇𝖠𝖲𝖳𝖱𝖠</b></a>"""
    
    MANUELFILTER_TXT = """𝖧𝖾𝗅𝗉: <b>𝖥𝗂𝗅𝗍𝖾𝗋𝗌</b>

- 𝖥𝗂𝗅𝗍𝖾𝗋 𝗂𝗌 𝗍𝗁𝖾 𝖿𝖾𝖺𝗍𝗎𝗋𝖾 𝗐𝖾𝗋𝖾 𝗎𝗌𝖾𝗋𝗌 𝖼𝖺𝗇 𝗌𝖾𝗍 𝖺𝗎𝗍𝗈𝗆𝖺𝗍𝖾𝖽 𝗋𝖾𝗉𝗅𝗂𝖾𝗌 𝖿𝗈𝗋 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝗄𝖾𝗒𝗐𝗈𝗋𝖽 𝖺𝗇𝖽 𝖺𝗃𝖺𝗑 𝗐𝗂𝗅𝗅 𝗋𝖾𝗌𝗉𝗈𝗇𝖽 𝗐𝗁𝖾𝗇𝖾𝗏𝖾𝗋 𝖺 𝗄𝖾𝗒𝗐𝗈𝗋𝖽 𝗂𝗌 𝖿𝗈𝗎𝗇𝖽 𝗍𝗁𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾

<b>NOTE:</b>
𝟣. 𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗌𝗁𝗈𝗎𝗅𝖽 𝗁𝖺𝗏𝖾 𝖺𝖽𝗆𝗂𝗇 𝗉𝗋𝗂𝗏𝗂𝗅𝗅𝖺𝗀𝖾.
𝟤. 𝗈𝗇𝗅𝗒 𝖺𝖽𝗆𝗂𝗇𝗌 𝖼𝖺𝗇 𝖺𝖽𝖽 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍.
𝟥. 𝖺𝗅𝖾𝗋𝗍 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗁𝖺𝗏𝖾 𝖺 𝗅𝗂𝗆𝗂𝗍 𝗈𝖿 𝟨𝟦 𝖼𝗁𝖺𝗋𝖺𝖼𝗍𝖾𝗋𝗌.

◯ <b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝖭𝖣 𝖴𝗌𝖺𝗀𝖾:</b>
◯ <code>/filter</code> - <b>𝖺𝖽𝖽 𝖺 𝖿𝗂𝗅𝗍𝖾𝗋 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍</b>
◯ <code>/filters</code> - <b>𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗈𝖿 𝖺 𝖼𝗁𝖺𝗍</b>
◯ <code>/del</code> - <b>𝖽𝖾𝗅𝖾𝗍𝖾 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝖿𝗂𝗅𝗍𝖾𝗋 𝗂𝗇 𝖼𝗁𝖺𝗍</b>
◯ <code>/delall</code> - <b>𝖽𝖾𝗅𝖾𝗍𝖾 𝗍𝗁𝖾 𝗐𝗁𝗈𝗅𝖾 𝖿𝗂𝗅𝗍𝖾𝗋𝗌 𝗂𝗇 𝖺 𝖼𝗁𝖺𝗍 (𝖼𝗁𝖺𝗍 𝗈𝗐𝗇𝖾𝗋 𝗈𝗇𝗅𝗒)</b>

◯ <code>/g_filter off</code> 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 + 𝗈𝗇/𝗈𝖿𝖿 𝗂𝗇 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉 𝗍𝗈 𝖼𝗈𝗇𝗍𝗋𝗈𝗅 𝗀𝗅𝗈𝖻𝖺𝗅 𝖿𝗂𝗅𝗍𝖾𝗋 𝗂𝗇 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉"""
   
    BUTTON_TXT = """𝖧𝖾𝗅𝗉: <b>𝖡𝗎𝗍𝗍𝗈𝗇𝗌</b>

- 𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝖲𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗈𝗍𝗁 𝗎𝗋𝗅 𝖺𝗇𝖽 𝖺𝗅𝖾𝗋𝗍 𝗂𝗇𝗅𝗂𝗇𝖾 𝖻𝗎𝗍𝗍𝗈𝗇𝗌.

<b>𝖭𝖮𝖳𝖤:</b>
𝟣. 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗐𝗂𝗅𝗅 𝗇𝗈𝗍 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝗌𝖾𝗇𝖽 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁𝗈𝗎𝗍 𝖺𝗇𝗒 𝖼𝗈𝗇𝗍𝖾𝗇𝗍, 𝗌𝗈 𝖼𝗈𝗇𝗍𝖾𝗇𝗍 𝗂𝗌 𝗆𝖺𝗇𝖽𝖺𝗍𝗈𝗋𝗒.
𝟤. 𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗌𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗎𝗍𝗍𝗈𝗇𝗌 𝗐𝗂𝗍𝗁 𝖺𝗇𝗒 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗆𝖾𝖽𝗂𝖺 𝗍𝗒𝗉𝖾.
𝟥. 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝗌𝗁𝗈𝗎𝗅𝖽 𝖻𝖾 𝗉𝗋𝗈𝗉𝖾𝗋𝗅𝗒 𝗉𝖺𝗋𝗌𝖾𝖽 𝖺𝗌 𝗆𝖺𝗋𝗄𝖽𝗈𝗐𝗇 𝖿𝗈𝗋𝗆𝖺𝗍.

<b>𝖴𝗋𝗅 𝖡𝗎𝗍𝗍𝗈𝗇𝗌:</b>
<code>[Button Text](buttonurl:xxxxxxxxxxxx)</code>

<b>𝖠𝗅𝖾𝗋𝗍 𝖡𝗎𝗍𝗍𝗈𝗇𝗌:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """**𝖠𝗎𝗍𝗈 𝖥𝗂𝗅𝗍𝖾𝗋 𝖮𝗇/𝖮𝖥𝖥 𝖬𝗈𝖽𝗎𝗅𝖾..
𝖴𝖲𝖤 𝖳𝖧𝖨𝖲 𝖢𝖮𝖬𝖬𝖠𝖭𝖣 𝖮𝖭 𝖸𝖮𝖴𝖱 𝖦𝖱𝖮𝖴𝖯

◯ <code>/autofilter</code> 𝗈𝗇 - 𝖺𝗎𝗍𝗈𝖿𝗂𝗅𝗍𝖾𝗋 𝖾𝗇𝖺𝖻𝗅𝖾 𝗂𝗇 𝗒𝗈𝗋 𝖼𝗁𝖺𝗍
◯ <code>/autofilter</code> 𝗈𝖿𝖿 - 𝖺𝗎𝗍𝗈𝖿𝗂𝗅𝗍𝖾𝗋 𝖽𝗂𝗌𝖺𝖻𝗅𝖾 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗍 

𝖠𝖴𝖳𝖮 𝖥𝖨𝖫𝖳𝖤𝖱 𝖨𝖲 𝖳𝖧𝖤 𝖥𝖤𝖠𝖳𝖴𝖱𝖤 𝖳𝖮 𝖥𝖨𝖫𝖳𝖤𝖱 𝖠𝖭𝖣 𝖲𝖠𝖵𝖤  𝖳𝖧𝖤 𝖥𝖨𝖫𝖤𝖲 𝖠𝖴𝖳𝖮𝖬𝖠𝖳𝖨𝖢𝖠𝖫𝖫𝖸 𝖥𝖱𝖮𝖬 𝖢𝖧𝖠𝖭𝖭𝖤𝖫 𝖳𝖮 𝖦𝖱𝖮𝖴𝖯. 𝖸𝖮𝖴 𝖢𝖠𝖭 𝖴𝖲𝖤 𝖳𝖧𝖤 𝖥𝖮𝖫𝖫𝖮𝖶𝖨𝖭𝖦 𝖢𝖮𝖬𝖬𝖠𝖭𝖣𝖲 𝖳𝖮 𝖮𝖭 𝖠𝖭𝖣 𝖮𝖥𝖥 𝖳𝖧𝖤 𝖠𝖴𝖳𝖮𝖥𝖨𝖫𝖳𝖤𝖱 𝖨𝖭 𝖸𝖮𝖴𝖱 𝖦𝖱𝖮𝖴𝖯../

<𝖻>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</𝖻>
◯ <code>/set_template</code> - 𝖲𝖤𝖳 𝖢𝖴𝖲𝖳𝖮𝖬 𝖨𝖬𝖣𝖡 𝖳𝖤𝖬𝖯𝖫𝖠𝖳𝖤 𝖥𝖮𝖱 𝖠𝖴𝖳𝖮 𝖥𝖨𝖫𝖳𝖤𝖱.
◯ <code>/get_template</code> - 𝖦𝖤𝖳 𝖢𝖴𝖱𝖱𝖤𝖭𝖳 𝖨𝖬𝖣𝖡 𝖳𝖤𝖬𝖯𝖫𝖠𝖳𝖤 𝖮𝖥 𝖠𝖴𝖳𝖮 𝖥𝖨𝖫𝖳𝖤𝖱.

𝖢𝗋𝖾𝖽𝗂𝗍𝗌 :- <a href=https://t.me/k_ASTRA1>𝖬𝖺𝗌𝗍𝖾𝗋𝖪𝖤𝖵</a>**"""

    CONNECTION_TXT = """Help: <b>𝖢𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌</b>

◯ 𝖴𝗌𝖾𝖽 𝗍𝗈 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖡𝖮𝖳 𝗍𝗈 𝖯𝖬 𝖿𝗈𝗋 𝗆𝖺𝗇𝖺𝗀𝗂𝗇𝗀 𝖿𝗂𝗅𝖾𝗌
◯ 𝖨𝗍 𝗁𝖾𝗅𝗉𝗌 𝗍𝗈 𝖺𝗏𝗈𝗂𝖽 𝗌𝗉𝖺𝗆𝗆𝗂𝗇𝗀 𝗂𝗇 𝗀𝗋𝗈𝗎𝗉𝗌

<b>𝖭𝖮𝖳𝖤:</b>
𝟣. 𝖮𝗇𝗅𝗒 𝖺𝖽𝗆𝗂𝗇𝗌 𝖼𝖺𝗇 𝖺𝖽𝖽 𝖺 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇.
𝟤. 𝖲𝖾𝗇𝖽 <code>/connect</code> 𝖿𝗈𝗋 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗇𝗀 𝗆𝖾 𝗍𝗈 𝗎𝗋 𝖯𝖬

<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝖭𝖣 𝖴𝗌𝖺𝗀𝖾:</b>
◯ <code>/connect</code>  - 𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝖼𝗁𝖺𝗍 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖯𝖬
◯ <code>/disconnect</code>  - 𝖽𝗂𝗌𝖼𝗈𝗇𝗇𝖾𝖼𝗍 𝖿𝗋𝗈𝗆 𝖺 𝖼𝗁𝖺𝗍
◯ <code>/connections</code> - 𝗅𝗂𝗌𝗍 𝖺𝗅𝗅 𝗒𝗈𝗎𝗋 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>𝖭𝖮𝖳𝖤:</b>
- 𝖳𝗁𝖾𝗌𝖾 𝖺𝗋𝖾 𝗍𝗁𝖾 𝖾𝗑𝗍𝗋𝖺 𝖿𝖾𝖺𝗍𝗎𝗋𝖾𝗌 𝗈𝖿 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍

<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝖭𝖣 𝖴𝗌𝖺𝗀𝖾:</b>
◯ <code>/id</code> - 𝗀𝖾𝗍 𝗂𝖽 𝗈𝖿 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖾𝖽 𝗎𝗌𝖾𝗋.
◯ <code>/info</code>  - 𝗀𝖾𝗍 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖺𝖻𝗈𝗎𝗍 𝖺 𝗎𝗌𝖾𝗋.
◯ <code>/imdb</code> - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝖿𝗂𝗅𝗆 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝖨𝖬𝖣𝖻 𝗌𝗈𝗎𝗋𝖼𝖾.
◯ <code>/search</code> - 𝗀𝖾𝗍 𝗍𝗁𝖾 𝖿𝗂𝗅𝗆 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖿𝗋𝗈𝗆 𝗏𝖺𝗋𝗂𝗈𝗎𝗌 𝗌𝗈𝗎𝗋𝖼𝖾𝗌."""

    ADMIN_TXT = """<b>𝖭𝖮𝖳𝖤:</b>
<b>𝖳𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝖮𝖭𝖫𝖸 𝗐𝗈𝗋𝗄𝗌 𝖿𝗈𝗋 𝗆𝗒 𝖬𝖠𝖲𝖳𝖤𝖱</b>

- <b>𝖡𝖺𝗌𝗂𝖼 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌</b>
◯ <code>/logs</code> - 𝖳𝗈 𝗀𝖾𝗍 𝗋𝖾𝖼𝖾𝗇𝗍 𝖾𝗋𝗋𝗈𝗋𝗌</code>
◯ <code>/stats</code> - 𝖳𝗈 𝗀𝖾𝗍 𝗌𝗍𝖺𝗍𝗎𝗌 𝗈𝖿 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇 𝖣𝖡.</code>

- <b>𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 & 𝖲𝖾𝗋𝗏𝖾𝗋 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌</b>
◯ <code>/status</code> - 𝖳𝗈 𝗀𝖾𝗍 𝗌𝗍𝖺𝗍𝗎𝗌 𝗈𝖿 𝖺 𝗌𝖾𝗋𝗏𝖾𝗋
◯ <code>/stats</code> - 𝖳𝗈 𝗀𝖾𝗍 𝖣𝖺𝗍𝖺𝖡𝖺𝗌𝖾 𝗌𝗍𝖺𝗍𝗎𝗌
◯ <code>/delete</code> - 𝖣𝖾𝗅𝖾𝗍𝖾 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝖿𝗂𝗅𝖾 𝖿𝗋𝗈𝗆 𝖣𝖡
◯ <code>/deleteall</code> - 𝖣𝖾𝗅𝖾𝗍𝖾 𝖺𝗅𝗅 𝖿𝗂𝗅𝖾𝗌 𝖿𝗋𝗈𝗆 𝖣𝖡
◯ <code>/users</code> - 𝖳𝗈 𝗀𝖾𝗍 𝖺 𝗅𝗂𝗌𝗍 𝗈𝖿 𝗆𝗒 𝗎𝗌𝖾𝗋𝗌 𝖺𝗇𝖽 𝖨𝖣𝗌
◯ <code>/chats</code> - 𝖳𝗈 𝗀𝖾𝗍 𝖺 𝗅𝗂𝗌𝗍 𝗈𝖿 𝗆𝗒 𝖼𝗁𝖺𝗍𝗌 𝖺𝗇𝖽 𝖨𝖣𝗌
◯ <code>/channel</code> - 𝖳𝗈 𝗀𝖾𝗍 𝖺 𝗅𝗂𝗌𝗍 𝗈𝖿 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝖾𝖽 𝖼𝗁𝖺𝗇𝗇𝖾𝗅𝗌"""

    US_CHAT_TXT = """<b>𝖭𝖮𝖳𝖤:</b>
<b>𝖳𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝖮𝖭𝖫𝖸 𝗐𝗈𝗋𝗄𝗌 𝖿𝗈𝗋 𝗆𝗒 𝖬𝖠𝖲𝖳𝖤𝖱</b>

- <b>𝖢𝗁𝖺𝗍 & 𝖴𝗌𝖾𝗋</b>
◯ <code>/broadcast</code> - 𝖳𝗈 𝖻𝗋𝗈𝖺𝖽𝖼𝖺𝗌𝗍 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝖺𝗅𝗅 𝗎𝗌𝖾𝗋𝗌
◯ <code>/group_broadcast</code> - 𝖳𝗈 𝖻𝗋𝗈𝖺𝖽𝖼𝖺𝗌𝗍 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝖿𝗈 𝖺𝗅𝗅 𝖼𝗈𝗇𝗇𝖾𝖼𝗍𝖾𝖽 𝗀𝗋𝗈𝗎𝗉𝗌
◯ <code>/leave</code>  - 𝖳𝗈 𝗅𝖾𝖺𝗏𝖾 𝖿𝗋𝗈𝗆 𝖺 𝖼𝗁𝖺𝗍
◯ <code>/disable</code>  - 𝖳𝗈 𝖽𝗂𝗌𝖺𝖻𝗅𝖾 𝖠 𝖢𝗁𝖺𝗍
◯ <code>/invite</code> - 𝖳𝗈 𝗀𝖾𝗍 𝗂𝗇𝗏𝗂𝗍𝖾 𝗅𝗂𝗇𝗄 𝗈𝖿 𝖺𝗇𝗒 𝖼𝗁𝖺𝗍 𝗐𝗁𝖾𝗋𝖾 𝖻𝗈𝗍 𝗂𝗌 𝖺𝖽𝗆𝗂𝗇 𝗂𝗇
◯ <code>/ban_user</code> - 𝖳𝗈 𝖡𝖠𝖭 𝖺 𝗎𝗌𝖾𝗋
◯ <code>/unban_user</code>  - 𝖳𝗈 𝖴𝖭𝖡𝖠𝖭 𝖺 𝗎𝗌𝖾𝗋
◯ <code>/restart</code> - 𝖳𝗈 𝖱𝖾𝗌𝗍𝖺𝗋𝗍 𝖠 𝖳𝗁𝖾 𝖡𝖮𝖳
◯ <code>/usend</code> - 𝖳𝗈 𝖲𝖾𝗇𝖽 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝗎𝗌𝖾𝗋
◯ <code>/gsend</code> - 𝖳𝗈 𝖲𝖾𝗇𝖽 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝖼𝗁𝖺𝗍

◯ <code>/clear_junk</code> - 𝖼𝗅𝖾𝖺𝗋 𝖺𝗅𝗅 𝖽𝖾𝗅𝖾𝗍𝖾 𝖺𝖼𝖼𝗈𝗎𝗇𝗍 & 𝖻𝗅𝗈𝖼𝗄𝖾𝖽 𝖺𝖼𝖼𝗈𝗎𝗇𝗍 𝗂𝗇 𝖽𝖺𝗍𝖺𝖻𝖺𝗌𝖾 
◯ <code>/clear_junk_group</code> - 𝖼𝗅𝖾𝖺𝗋 𝖺𝖽𝖽 𝗋𝖾𝗆𝗈𝗏𝖾𝖽 𝗀𝗋𝗈𝗎𝗉 𝗈𝗋 𝖽𝖾𝖺𝖼𝗍𝗂𝗏𝖺𝗍𝖾𝖽 𝗀𝗋𝗈𝗎𝗉𝗌 𝗈𝗇 𝖽𝖻"""

    G_FIL_TXT = """<b>𝖭𝖮𝖳𝖤:</b>
<b>𝖳𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝖮𝖭𝖫𝖸 𝗐𝗈𝗋𝗄𝗌 𝖿𝗈𝗋 𝗆𝗒 𝖬𝖠𝖲𝖳𝖤𝖱</b>

◯ <b>𝖠𝖣𝖵 𝖦𝗅𝗈𝖻𝖺𝗅 𝖥𝗂𝗅𝗍𝖾𝗋</b>
◯ <code>/gfilter</code> - 𝖳𝗈 𝖺𝖽𝖽 𝗀𝗅𝗈𝖻𝖺𝗅 𝖿𝗂𝗅𝗍𝖾𝗋𝗌
◯ <code>/gfilters</code> - 𝖳𝗈 𝗏𝗂𝖾𝗐 𝗅𝗂𝗌𝗍 𝖮𝖥 𝗀𝗅𝗈𝖻𝖺𝗅 𝖿𝗂𝗅𝗍𝖾𝗋𝗌
◯ <code>/delg</code> - 𝖳𝗈 𝖽𝖾𝗅𝖾𝗍𝖾 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝗂𝖼 𝗀𝗅𝗈𝖻𝖺𝗅 𝖿𝗂𝗅𝗍𝖾𝗋
◯ <code>/delallg</code> - 𝖳𝗈 𝖽𝖾𝗅𝖾𝗍𝖾 𝖺𝗅𝗅 𝗀𝗅𝗈𝖻𝖺𝗅 𝖿𝗂𝗅𝗍𝖾𝗋𝗌
"""

    STATUS_TXT = """<b>᚛› 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌: <code>{}</code></b>
<b>◯ 𝖳𝗈𝗍𝖺𝗅 𝖴𝗌𝖾𝗋𝗌: <code>{}</code></b>
<b>◯ 𝖳𝗈𝗍𝖺𝗅 𝖢𝗁𝖺𝗍𝗌: <code>{}</code></b>
<b>◯ 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code> 𝖬𝖡</b>
<b>◯ 𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code> 𝖬𝖡</b>"""
    LOG_TEXT_G = """𝖬𝖺𝗌𝗍𝖾𝗋!!!
    
<b>◯ 𝖦𝗋𝗈𝗎𝗉 ⪼ {a}(<code>{b}</code>)</b>
<b>◯ 𝖦𝗋𝗈𝗎𝗉 𝖨𝖣 ⪼ @{c}
<b>◯ 𝖳𝗈𝗍𝖺𝗅 𝖬𝖾𝗆𝖻𝖾𝗋𝖺 ⪼ {d}</b>
<b>◯ 𝖠𝖽𝖽𝖾𝖽 𝖡𝗒 ⪼ {e}</b>

By {f}
"""
    LOG_TEXT_P = """𝖬𝖺𝗌𝗍𝖾𝗋!!!
    
<b>◯ 𝖨𝖣 - <code>{}</code></b>
<b>◯ 𝖭𝖺𝗆𝖾 - {}</b>
<b>◯ 𝖴𝖭 - @{}</b>

By @{} """
   
    ZOMBIES_TXT = """𝖧𝖾𝗅𝗉𝗌 𝖸𝗈𝗎 𝖳𝖮 𝖪𝗂𝖼𝗄 𝖴𝗌𝖾𝗋𝗌

<b>𝖪𝗂𝖼𝗄 𝗂𝗇𝖼𝖺𝗍𝗂𝗏𝖾 𝗆𝖾𝗆𝖻𝖾𝗋𝗌 𝖿𝗋𝗈𝗆 𝗀𝗋𝗈𝗎𝗉. 𝖠𝖽𝖽 𝗆𝖾 𝖺𝗌 𝖺𝖽𝗆𝗂𝗇 𝗐𝗂𝗍𝗁 𝖻𝖺𝗇 𝗎𝗌𝖾𝗋𝗌 𝗉𝖾𝗋𝗆𝗂𝗌𝗌𝗂𝗈𝗇 𝗂𝗇 𝗀𝗋𝗈𝗎𝗉.</b>

<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝖭𝖣 𝖴𝗌𝖺𝗀𝖾:</b>
◯ <code>/inkick</code> - 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗋𝖾𝗊𝗎𝗂𝗋𝖾𝖽 𝖺𝗋𝗀𝗎𝗆𝖾𝗇𝗍𝗌 𝖺𝗇𝖽 𝗂 𝗐𝗂𝗅𝗅 𝗄𝗂𝖼𝗄 𝗆𝖾𝗆𝖻𝖾𝗋𝗌 𝖿𝗋𝗈𝗆 𝗀𝗋𝗈𝗎𝗉.
◯ <code>/instatus</code> - 𝗍𝗈 𝖼𝗁𝖾𝖼𝗄 𝖼𝗎𝗋𝗋𝖾𝗇𝗍 𝗌𝗍𝖺𝗍𝗎𝗌 𝗈𝖿 𝖼𝗁𝖺𝗍 𝗆𝖾𝗆𝖻𝖾𝗋 𝖿𝗋𝗈𝗆 𝗀𝗋𝗈𝗎𝗉.
◯ <code>/inkick</code> 𝗐𝗂𝗍𝗁𝗂𝗇_𝗆𝗈𝗇𝗍𝗁 𝗅𝗈𝗇𝗀_𝗍𝗂𝗆𝖾_𝖺𝗀𝗈 - 𝗍𝗈 𝗄𝗂𝖼𝗄 𝗎𝗌𝖾𝗋𝗌 𝗐𝗁𝗈 𝖺𝗋𝖾 𝗈𝖿𝖿𝗅𝗂𝗇𝖾 𝖿𝗈𝗋 𝗆𝗈𝗋𝖾 𝗍𝗁𝖺𝗇 𝟨-𝟩 𝖽𝖺𝗒𝗌.
◯ <code>/inkick</code> long_time_ago - 𝗍𝗈 𝗄𝗂𝖼𝗄 𝗆𝖾𝗆𝖻𝖾𝗋𝗌 𝗐𝗁𝗈 𝖺𝗋𝖾 𝗈𝖿𝖿𝗅𝗂𝗇𝖾 𝖿𝗈𝗋 𝗆𝗈𝗋𝖾 𝗍𝗁𝖺𝗇 𝖺 𝗆𝗈𝗇𝗍𝗁 𝖺𝗇𝖽 𝖣𝖾𝗅𝖾𝗍𝖾𝖽 𝖠𝖼𝖼𝗈𝗎𝗇𝗍𝗌.
• <code>/dkick</code> - to kick deleted accounts."""

    IMAGE_TXT = """𝖧𝖾𝗅𝗉: <b>𝖨𝖬𝖠𝖦𝖤</b>

- <b>𝖳𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗁𝖾𝗅𝗉𝗌 𝗒𝗈𝗎 𝖾𝖽𝗂𝗍 𝖺𝗇 𝗂𝗆𝖺𝗀𝖾 𝖾𝖺𝗌𝗂𝗅𝗒</b>

- <b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 & 𝖴𝗌𝖺𝗀𝖾:</b>

- <b>𝖴𝖭𝖣𝖤𝖱 𝖬𝖺𝗂𝗇𝗍𝖺𝗂𝗇𝖺𝗇𝖼𝖾!!!</b>

𝖬𝖺𝖽𝖾 𝖡𝖸 <a href=https://t.me/k_ASTRA1>𝖬𝖺𝗌𝗍𝖾𝗋𝖪𝖤𝖵</a>"""

    RESTRIC_TXT = """𝖧𝖾𝗅𝗉: 𝖬𝖴𝖳𝖤

- 𝖳𝗁𝖾𝗌𝖾 𝖺𝗋𝖾 𝗍𝗁𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺 𝗀𝗋𝗈𝗎𝗉 𝖺𝖽𝗆𝗂𝗇 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗍𝗈 𝗆𝖺𝗇𝖺𝗀𝖾 𝗍𝗁𝖾𝗂𝗋 𝗀𝗋𝗈𝗎𝗉 𝗆𝗈𝗋𝖾 𝖾𝖿𝖿𝗂𝖼𝗂𝖾𝗇𝗍𝗅𝗒.

◯ <code>/ban</code> - 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
◯ <code>/unban</code> - 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
◯ <code>/tban</code> - 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
◯ <code>/mute</code> - 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
◯ <code>/unmute</code> - 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
◯ <code>/tmute</code> - 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

◯ 𝖮𝖧𝖧 𝗃𝗎𝗌𝗍 𝖺 𝗋𝖾𝗆𝗂𝗇𝖽𝖾𝗋:
𝖶𝗁𝗂𝗅𝖾 𝖴𝗌𝗂𝗇𝗀 /tmute 𝖮𝖱 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍

𝖥𝗈𝗋 𝖺𝗇 𝖤𝗑𝖺𝗆𝗉𝗅𝖾: <code>/𝗍𝖻𝖺𝗇</code> 𝟤𝖽 𝗈𝗋 <code>/𝗍𝗆𝗎𝗍𝖾</code> 𝟤𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗍𝗁𝖾𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌 𝖬/𝖧/𝖣
 - 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 - 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 - 𝖽 = 𝖽𝖺𝗒𝗌"""


    PIN_TXT ="""<b>𝖯𝗂𝗇 𝖬𝖮𝖣𝖴𝖫𝖤</b>
- 𝗉𝗂𝗇𝗇𝗂𝗇𝗀 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾../

- 𝖯𝗂𝗇 𝖱𝖾𝗅𝖺𝗍𝖾𝖽 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗋𝖾 𝖿𝗈𝗎𝗇𝖽 𝗁𝖾𝗋𝖾

<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝖭𝖣 𝖴𝗌𝖺𝗀𝖾:</b>

◯ <code>/pin</code> - 𝖳𝗈 𝖯𝖨𝖭 𝗍𝗁𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗍𝗌
◯ <code>/unpin</code> - 𝖳𝗈 𝖴𝖭𝖯𝖨𝖭 𝗍𝗁𝖾 𝖯𝖨𝖭𝖭𝖤𝖣 𝗆𝖾𝗌𝗌𝖺𝗀𝖾"""

    PASTE_TXT = """Help: <b>𝖯𝖺𝗌𝗍𝖾</b>

- 𝖯𝖺𝗌𝗍𝖾 𝗌𝗈𝗆𝖾 𝗍𝖾𝗑𝗍𝗌 𝗈𝗋 𝖽𝗈𝖼𝗎𝗆𝖾𝗇𝗍𝗌 𝗈𝗇 𝖺 𝗐𝖾𝖻𝗌𝗂𝗍𝖾!

<b>Commands 𝖠𝖭𝖣 Usage:</b>

◯ <code>/paste [text]</code> - 𝗉𝖺𝗌𝗍𝖾 𝗍𝗁𝖾 𝗀𝗂𝗏𝖾𝗇 𝗍𝖾𝗑𝗍 𝗈𝗇 𝖯𝖺𝗌𝗍𝗒

<b>𝖭𝖮𝖳𝖤:</b>

- 𝖳𝗁𝖾𝗌𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝗐𝗈𝗋𝗄𝗌 𝗈𝗇 𝖻𝗈𝗍𝗁 𝗉𝗆 𝖺𝗇𝖽 𝗀𝗋𝗈𝗎𝗉.
- 𝖳𝗁𝖾𝗌𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖼𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝖻𝗒 𝖺𝗇𝗒 𝗀𝗋𝗈𝗎𝗉 𝗆𝖾𝗆𝖻𝖾𝗋."""

    TTS_TXT = """𝖧𝖾𝗅𝗉: 𝖳𝖳𝖲 𝖬𝗈𝖽𝗎𝗅𝖾

𝖳𝖳𝖲 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝖳𝖤𝖷𝖳-𝖲𝖯𝖤𝖤𝖢𝖧

<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝖭𝖣 𝖴𝗌𝖺𝗀𝖾</b>

◯ <code>/tts <text></code> : 𝖼𝗈𝗇𝗏𝖾𝗋𝗍 𝗍𝖾𝗑𝗍 𝗍𝗈 𝗌𝗉𝖾𝖾𝖼𝗁

<b>𝖭𝖮𝖳𝖤:</b>

◯ 𝖨𝖬𝖣𝖻 𝗌𝗁𝗈𝗎𝗅𝖽 𝗁𝖺𝗏𝖾 𝖺𝖽𝗆𝗂𝗇 𝗉𝗋𝗂𝗏𝗂𝗅𝗅𝖺𝗀𝖾.
◯ 𝖳𝗁𝖾𝗌𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝗐𝗈𝗋𝗄𝗌 𝗈𝗇 𝖻𝗈𝗍𝗁 𝗉𝗆 𝖺𝗇𝖽 𝗀𝗋𝗈𝗎𝗉.
◯ 𝖨𝖬𝖣𝖻 𝖼𝖺𝗇 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝟤𝟢𝟢+ 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾𝗌."""

    PINGS_TXT ="""𝖧𝖾𝗅𝗉: 𝖯𝖨𝖭𝖦 𝖬𝗈𝖽𝗎𝗅𝖾

- 𝖧𝖾𝗅𝗉𝗌 𝖸𝖮𝖴 𝖪𝗇𝗈𝗐 𝗆𝗒 𝖯𝖨𝖭𝖦

<b>Commands:</b>

◯ <code>/alive</code> - 𝖳𝗈 𝖼𝗁𝖾𝖼𝗄 𝗒𝗈𝗎 𝖺𝗋𝖾 𝖺𝗅𝗂𝗏𝖾.
◯ <code>/ping</code> - 𝖳𝗈 𝗀𝖾𝗍 𝗒𝗈𝗎𝗋 𝗉𝗂𝗇𝗀.
- <b>𝖴𝗌𝖺𝗀𝖾</b>

◯ 𝖳𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖼𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝗂𝗇 𝗉𝗆𝗌 𝖺𝗇𝖽 𝗀𝗋𝗈𝗎𝗉𝗌
◯ 𝖳𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖼𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝖻𝗎𝗒 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉𝗌 𝖺𝗇𝖽 𝖻𝗈𝗍𝗌 𝗉𝗆
◯ 𝖲𝖧𝖠𝖱𝖤 𝖴𝖲 𝖥𝖮𝖱 𝖬𝖮𝖱𝖤!!!"""

    TELE_TXT = """𝖧𝖾𝗅𝗉: 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗉𝗁 𝖬𝗈𝖽𝗎𝗅𝖾

- 𝖣𝗈 𝖺𝗌 𝗒𝗈𝗎 𝗐𝗂𝗌𝗁 𝗐𝗂𝗍𝗁 𝗍𝖾𝗅𝖾𝗀𝗋𝖺.𝗉𝗁 𝗆𝗈𝖽𝗎𝗅𝖾!

</b>𝖴𝗌𝖺𝗀𝖾:</b>

◯ <code>/telegraph</code> - 𝖲𝖾𝗇𝖽 𝗆𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗋𝖾𝗉𝗅𝗒 𝗐𝗂𝗍𝗁 𝖯𝗂𝖼𝗍𝗎𝗋𝖾 𝗈𝗋 𝖵𝗂𝖽𝖾 𝖴𝗇𝖽𝖾𝗋 (𝟧𝖬𝖡)

<b>𝖭𝖮𝖳𝖤:</b>

◯ 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖨𝗌 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝗂𝗇 𝗀𝗈𝗎𝗉𝗌 𝖺𝗇𝖽 𝗉𝗆
◯ 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖢𝖺𝗇 𝖻𝖾 𝗎𝗌𝖾𝖽 𝖻𝗒 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾"""

    JSON_TXT ="""<b>𝖧𝖾𝗅𝗉: 𝖩𝖲𝖮𝖭 𝖬𝗈𝖽𝗎𝗅𝖾</b>

- 𝖡𝗈𝗍 𝗋𝖾𝗍𝗎𝗋𝗇𝗌 𝗃𝗌𝗈𝗇 𝖿𝗈𝗋 𝖺𝗅𝗅 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝗐𝗂𝗍𝗁  <code>/json</code>

<b>𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌:</b>

◯ 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖤𝖽𝗂𝗍𝗍𝗂𝗇𝗀 𝖩𝖲𝖮𝖭
◯ 𝖯𝗆 𝖲𝗎𝗉𝗉𝗈𝗋𝗍
◯ 𝖦𝗋𝗈𝗎𝗉 𝖲𝗎𝗉𝗉𝗈𝗋𝗍

<b>𝖭𝖮𝖳𝖤:</b>

𝖤𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 , 𝗂𝖿 𝗌𝗉𝖺𝗆𝗂𝗇𝗀 𝗁𝖺𝗉𝗉𝖾𝗇𝗌 𝖻𝗈𝗍 𝗐𝗂𝗅𝗅 𝖺𝗎𝗍𝗈𝗆𝖺𝗍𝗂𝖼𝖺𝗅𝗅𝗒 𝖻𝖺𝗇 𝗒𝗈𝗎 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉."""

    PURGE_TXT = """𝖧𝖾𝗅𝗉: 𝖯𝖴𝖱𝖦𝖤 𝖬𝗈𝖽𝗎𝗅𝖾
    
- 𝖣𝖾𝗅𝖾𝗍𝖾 𝖠 𝖫𝗈𝗍 𝖮𝖿 𝖬𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖥𝗋𝗈𝗆 𝖦𝗋𝗈𝗎𝗉𝗌! 
    
 <b>𝖠𝖣𝖬𝖨𝖭</b> 

◯ <code>/purge</code> - 𝖣𝖾𝗅𝖾𝗍𝖾 𝖠𝗅𝗅 𝖬𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖥𝗋𝗈𝗆 𝖳𝗁𝖾 𝖱𝖾𝗉𝗅𝗂𝖾𝖽 𝖳𝗈 𝖬𝖾𝗌𝗌𝖺𝗀𝖾, 𝖳𝗈 𝖳𝗁𝖾 𝖢𝗎𝗋𝗋𝖾𝗇𝗍 𝖬𝖾𝗌𝗌𝖺𝗀𝖾"""

    CREATOR_REQUIRED = """<b>You Have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """❗<b>എന്നെ Admin ആക്കത്ത സ്ഥലത്ത് ഞാൻ നിക്കില്ല പോകുവാ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ഇപ്പൊ എല്ലാം അടിച്ചുമാറ്റി തരാം...</b>"""
      
    CARB_TXT = """𝖧𝖾𝗅𝗉: 𝖢𝖠𝖱𝖡𝖮𝖭 𝖬𝗈𝖽𝗎𝗅𝖾
𝖢𝖺𝗋𝖻𝗈𝗇 𝗂𝗌 𝖺 𝗍𝗈𝗈𝗅 𝗍𝗁𝖺𝗍 𝖼𝗋𝖾𝖺𝗍𝖾𝗌 𝗏𝗂𝗌𝗎𝖺𝗅𝗅𝗒 𝖺𝗉𝗉𝖾𝖺𝗅𝗂𝗇𝗀 𝗂𝗆𝖺𝗀𝖾𝗌 𝖿𝗋𝗈𝗆 𝗍𝖾𝗑𝗍. 𝖴𝗌𝖾 𝗍𝗁𝖾 /𝖼𝖺𝗋𝖻𝗈𝗇 𝖼𝗈𝗆𝗆𝖺𝗇𝖽, 𝖺𝗇𝖽 𝗍𝗁𝖾 𝖻𝗈𝗍 𝗐𝗂𝗅𝗅 𝗋𝖾𝗌𝗉𝗈𝗇𝖽 𝗐𝗂𝗍𝗁 𝖺𝗇 𝗂𝗆𝖺𝗀𝖾 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝖿𝗈𝗋 𝗌𝗈𝖼𝗂𝖺𝗅 𝗆𝖾𝖽𝗂𝖺, 𝗉𝗋𝖾𝗌𝖾𝗇𝗍𝖺𝗍𝗂𝗈𝗇𝗌, 𝖺𝗇𝖽 𝗆𝗈𝗋𝖾. 𝖨𝗍'𝗌 𝗉𝖾𝗋𝖿𝖾𝖼𝗍 𝖿𝗈𝗋 𝖼𝗋𝖾𝖺𝗍𝗂𝗇𝗀 𝖾𝗇𝗀𝖺𝗀𝗂𝗇𝗀 𝖼𝗈𝗇𝗍𝖾𝗇𝗍."""

    FOND_TXT = """𝖧𝖾𝗅𝗉: 𝖥𝖮𝖭𝖣 𝖬𝗈𝖽𝗎𝗅𝖾
- 𝖥𝗈𝗇𝗍 𝗂𝗌 𝖺 𝗆𝗈𝖽𝗎𝗅𝖾 𝗍𝗈 𝗆𝖺𝗄𝖾 𝗒𝗈𝗎𝗋 𝗍𝖾𝗑𝗍 𝗌𝗍𝗒𝗅𝗂𝗌𝗁
- 𝖳𝗈 𝗎𝗌𝖾 𝗍𝗁𝖾 𝖿𝖾𝖺𝗍𝗎𝗋𝖾 𝗍𝗒𝗉𝖾 <code>/font <your text></code> 𝗍𝗁𝖾𝗇 𝗒𝗈𝗎𝗋 𝗍𝖾𝗑𝗍 𝗂𝗌 𝗋𝖾𝖺𝖽𝗒."""

    SHARE_TXT = """𝖧𝖾𝗅𝗉: 𝖲𝖧𝖠𝖱𝖤 𝖬𝗈𝖽𝖾

- 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 & 𝖴𝗌𝖺𝗀𝖾
◯ <code>/share</code> - 𝖱𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺𝗇𝗒 𝗆𝖾𝖽𝗂𝖺"""

    YTDL = """<b>𝖧𝖾𝗅𝗉: 𝖸𝗈𝗎𝗍𝗎𝖻𝖾 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖬𝖮𝖣𝖴𝖫𝖤</b>

- 𝖴𝖲𝖠𝖦𝖤
- 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖻𝗈𝗍𝗁 𝖺𝗎𝖽𝗂𝗈/𝗏𝗂𝖽𝖾𝗈 𝖿𝗋𝗈𝗆 𝖸𝖳

- 𝖧𝗈𝗐 𝗍𝗈 𝗎𝗌𝖾:
◯ <code>/song song name</code> 
◯ <code>/video or /mp4 𝘈𝘯𝘥 https://youtu.be/*****</code>

- 𝖤𝗑𝖺𝗆𝗉𝗅𝖾
<code>/song kevin</code>
<code>/mp4 https://youtu.be/*******</code>
<code>/video https://youtu.be/*****</code>  """


    


    

