# Peninei Halakha Notes

Study notes on Shabbat ch. 1–23 and Kashrut ch. 20–37.

Bilingual (English / עברית) student notes and review quizzes on Rav Eliezer Melamed's *Peninei Halakha*:

- **Shabbat**, chapters 1–23 (from the meaning of Shabbat through Muktzeh)
- **Kashrut**, chapters 20–37 (from Terefot through the food industry), summarized from the Hebrew

These are a student's notes in my own words, not a psak. For practical questions, ask a rav. Full text on Sefaria: [Shabbat](https://www.sefaria.org/Peninei_Halakhah%2C_Shabbat.1.1?lang=bi) · [Kashrut](https://www.sefaria.org/Peninei_Halakhah%2C_Kashrut.20.1?lang=he).

The site opens on a home page with a card for each book. Inside a book, the chapters (and the current chapter's sections) are in a side toolbar: on the left in English, on the right in Hebrew. On phones it collapses to dropdowns.

## Layout

- `ch/NN.en.md`, `ch/NN.he.md`, `ch/NN.quiz.json` – Shabbat notes and quiz per chapter
- `kashrut/NN.en.md`, `kashrut/NN.he.md`, `kashrut/NN.quiz.json` – Kashrut notes and quiz per chapter
- `template.html` – page template
- `build.py` – builds `index.html` from both books: `pip install markdown && python3 build.py .`
- `index.html` – the built, self-contained site

To add a book, add a folder of chapter files and an entry in `BOOKS` in `build.py` (plus its title, card text and links in `template.html`).

Links: `#en` / `#he` open the home page; `#en-5` is Shabbat ch. 5; `#he-k25` is Kashrut ch. 25; add `-quiz` for the quiz.
