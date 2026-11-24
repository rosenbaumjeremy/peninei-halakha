import markdown,re,json,sys
d=sys.argv[1]
T={1:("Introduction","פתיחה"),2:("Preparing for Shabbat","הכנות לשבת"),3:("Shabbat Times","זמני השבת"),4:("Lighting Shabbat Candles","הדלקת נרות שבת"),5:("Torah and Prayer on Shabbat","תורה ותפילה בשבת"),6:("Laws of Kiddush","הלכות קידוש"),7:("Shabbat Meals and Melaveh Malka","סעודות שבת ומלווה מלכה"),8:("Havdala and Motza'ei Shabbat","הבדלה ומוצאי שבת"),9:("Principles of the Melakhot","כללי המלאכות"),10:("Bishul (Cooking)","בישול"),
11:("Borer (Separating)","בורר"),12:("Food Preparation","הכנת מאכלים"),13:("Melakhot of Clothing","מלאכות הבגד"),
14:("Personal Grooming","הטיפול בגוף"),15:("Boneh and Soter","בונה וסותר"),16:("Mav'ir and Mekhabeh","מבעיר ומכבה"),
17:("Electricity","חשמל ומכשיריו"),18:("Kotev, Moḥek, Tzove'a","כותב, מוחק וצובע"),19:("Agricultural Melakhot","מלאכות שבצומח"),
20:("Animals","בעלי חיים"),21:("Hotza'ah (Carrying)","הוצאה"),22:("The Spirit of Shabbat","צביון השבת"),23:("Muktzeh","מוקצה"),
24:("Children","דיני קטן"),25:("A Non-Jew's Melakha","מלאכת גוי"),26:("Ma'aseh Shabbat and Lifnei Iver","מעשה שבת ולפני עיוור"),
27:("Pikuaḥ Nefesh and the Dangerously Ill","פיקוח נפש וחולה"),28:("Illness That Is Not Life-Threatening","חולה שאינו מסוכן"),29:("Eruvin","עירובין"),30:("Teḥum Shabbat","תחומי שבת")}
K={20:("Terefot","טריפות"),21:("Ḥelev and Gid Ha-nasheh","חלב וגיד הנשה"),22:("Blood and Kashering Meat","דם והכשרת הבשר"),
23:("Sheratzim (Insects)","שרצים"),24:("Food from Live Animals","מזון מהחי"),25:("Meat and Milk","בשר בחלב"),
26:("Waiting between Meat and Milk","דיני ההפסקה"),27:("Decrees on Gentiles' Food","הגזירות על מאכלי גויים"),28:("Pat and Bishul Akum","פת ובישולי גויים"),
29:("Gentiles' Wine and Drinks","יין ומשקאות גויים"),30:("Milk and Dairy Products","חלב ומוצריו"),31:("Tevilat Kelim","טבילת כלים"),
32:("Principles of Kashering Utensils","כללי הכשרת כלים"),33:("Kashering a Kitchen","הכשרת כלים ומטבח"),34:("Mixtures","דיני תערובות"),
35:("Types of Absorption","סוגי בליעות"),36:("Dangers","סכנות"),37:("The Food Industry","תעשיית המזון")}
Z={11:("Ḥanuka: History and Meaning","ימי החנוכה"),12:("Lighting the Ḥanuka Candles","הדלקת נרות חנוכה"),13:("Where and When to Light","מקום וזמן ההדלקה"),
14:("The Month of Adar","חודש אדר"),15:("Purim and Reading the Megilla","פורים ומקרא מגילה"),16:("The Mitzvot of Joy and Kindness","מצוות השמחה והחסד")}
# book code, source folder, chapter titles, section-id prefix
BOOKS=[('s','ch',T,''),('k','kashrut',K,'k'),('z','zemanim',Z,'z')]
def conv(path,pre):
    h=markdown.markdown(open(path,encoding='utf-8').read(),extensions=['tables','sane_lists'],tab_length=4)
    parts=[p for p in re.split(r'(?=<h2>)',h) if p.strip()]
    h='\n'.join(f'<section id="{pre}{i}">{p}</section>' for i,p in enumerate(parts))
    h=re.sub(r'<td>✓',r'<td><span class="y">✓</span>',h); h=re.sub(r'<td>✗',r'<td><span class="n">✗</span>',h)
    h=h.replace('<li>✓','<li><span class="y">✓</span>').replace('<li>✗','<li><span class="n">✗</span>')
    return h
chaps=[];data={}
for b,folder,titles,pre in BOOKS:
    data[b]={}
    for n in titles:
        for l in ('en','he'):
            chaps.append(f'<div class="chap" data-book="{b}" data-ch="{n}" data-lang="{l}" lang="{l}" dir="{"rtl" if l=="he" else "ltr"}" hidden><h3 class="ctag" hidden></h3>{conv(f"{d}/{folder}/{n}.{l}.md",f"{l}-{pre}{n}-")}</div>')
        data[b][n]={'t':{'en':titles[n][0],'he':titles[n][1]},'quiz':json.load(open(f'{d}/{folder}/{n}.quiz.json',encoding='utf-8'))}
js=lambda b:json.dumps(data[b],ensure_ascii=False).replace('</','<\\/')
t=open(f'{d}/template.html',encoding='utf-8').read().replace('{{CHAPTERS}}','\n'.join(chaps)).replace('{{DATAK}}',js('k')).replace('{{DATAZ}}',js('z')).replace('{{DATA}}',js('s'))
open(f'{d}/index.html','w',encoding='utf-8').write(t)
for b,_,_,_ in BOOKS: print(b, len(data[b]),'chapters,', sum(len(v['quiz']) for v in data[b].values()),'questions')
print(len(t),'bytes')
