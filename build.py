import markdown,re,json,sys
d=sys.argv[1]
T={1:("Introduction","פתיחה"),2:("Preparing for Shabbat","הכנות לשבת"),3:("Shabbat Times","זמני השבת"),4:("Lighting Shabbat Candles","הדלקת נרות שבת"),5:("Torah and Prayer on Shabbat","תורה ותפילה בשבת"),6:("Laws of Kiddush","הלכות קידוש"),7:("Shabbat Meals and Melaveh Malka","סעודות שבת ומלווה מלכה"),8:("Havdala and Motza'ei Shabbat","הבדלה ומוצאי שבת"),9:("Principles of the Melakhot","כללי המלאכות"),10:("Bishul (Cooking)","בישול"),
11:("Borer (Separating)","בורר"),12:("Food Preparation","הכנת מאכלים"),13:("Melakhot of Clothing","מלאכות הבגד"),
14:("Personal Grooming","הטיפול בגוף"),15:("Boneh and Soter","בונה וסותר"),16:("Mav'ir and Mekhabeh","מבעיר ומכבה"),
17:("Electricity","חשמל ומכשיריו"),18:("Kotev, Moḥek, Tzove'a","כותב, מוחק וצובע"),19:("Agricultural Melakhot","מלאכות שבצומח"),
20:("Animals","בעלי חיים"),21:("Hotza'ah (Carrying)","הוצאה"),22:("The Spirit of Shabbat","צביון השבת"),23:("Muktzeh","מוקצה")}
def conv(path,pre):
    h=markdown.markdown(open(path,encoding='utf-8').read(),extensions=['tables','sane_lists'],tab_length=4)
    parts=[p for p in re.split(r'(?=<h2>)',h) if p.strip()]
    h='\n'.join(f'<section id="{pre}{i}">{p}</section>' for i,p in enumerate(parts))
    h=re.sub(r'<td>✓',r'<td><span class="y">✓</span>',h); h=re.sub(r'<td>✗',r'<td><span class="n">✗</span>',h)
    h=h.replace('<li>✓','<li><span class="y">✓</span>').replace('<li>✗','<li><span class="n">✗</span>')
    return h
chaps=[];data={}
for n in T:
    for l in ('en','he'):
        chaps.append(f'<div class="chap" data-ch="{n}" data-lang="{l}" lang="{l}" dir="{"rtl" if l=="he" else "ltr"}" hidden><h3 class="ctag" hidden></h3>{conv(f"{d}/ch/{n}.{l}.md",f"{l}-{n}-")}</div>')
    data[n]={'t':{'en':T[n][0],'he':T[n][1]},'quiz':json.load(open(f'{d}/ch/{n}.quiz.json',encoding='utf-8'))}
js=json.dumps(data,ensure_ascii=False).replace('</','<\\/')
t=open(f'{d}/template.html',encoding='utf-8').read().replace('{{CHAPTERS}}','\n'.join(chaps)).replace('{{DATA}}',js)
open(f'{d}/index.html','w',encoding='utf-8').write(t)
print(len(t), sum(len(v['quiz']) for v in data.values()),'questions')
