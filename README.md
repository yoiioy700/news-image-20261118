# THE WORLD IN ONE DAY — 18 November 2026

Entry for the make.fun competition
**[news-image-20261118](https://make.fun/bounty/news-image-20261118)** —
"Sum up 18 November's world news in one image" ($250, 50 places paid).

The program writes one 1024×1024 PNG broadsheet, **THE WORLD IN ONE
DAY — Wednesday 18 November 2026**: 40 stories on one page — a lead
story with a code-drawn map of the Gulf, a code-drawn Kerch Bridge
diagram, 6 big stories with AI-generated editorial illustrations
composited at build time (the illustration source art is not in this
repository), and a 32-item "also on" list in three columns. Every story
was checked against 18 November 2026 reporting (Daily Short, Zark
News, Reuters via SRN / TBS / IANS, ONS, Amnesty, NASA/JPL, TBS News
Dhaka, Ukraine MoD).

## The 40 stories

**Big stories (1–8):**
1. Bahrain and Kuwait intercept Iran's drones — after **Tuesday's** US
   strike on Qeshm Island (the strike was Tuesday, not Wednesday)
2. Ukraine hits Kerch Bridge again; road span collapses
3. Xi welcomes Trump on the tarmac in Shenzhen (APEC; trilateral Thu)
4. Russia fires 141 drones at Ukraine; 126 downed
5. Voyager 1 reaches one light-day from Earth (25.9bn km)
6. Fed minutes: almost all officials see more hikes; Dow drops 561
7. Israeli tanks push into central Gaza near Nuseirat
8. Jeffries wins Democrats' nod for House Speaker, 251–11

**Also on Wednesday 18 November (9–40):**
9. Cyclone Akvan veers north toward Odisha
10. Amnesty: RSF drones killed 37 in El Obeid, Sudan
11. EU proposes €45bn loan to fund Ukraine in 2027
12. UK inflation climbs to 3.6%
13. GTA VI goes on sale after a 13-year wait
14. Bangladesh wage protests halt 535 factories
15. Trump hails "very big" Philippine trade deal — no terms signed
16. Carney meets Trump in Shenzhen; US deal possible, "not there yet"
17. Takaichi's chilly Shenzhen welcome — first Japan PM visit since 2019
18. Takaichi meets Putin for 30 minutes — first leader contact since 2019
19. India and Japan hold their 2+2 dialogue in Tokyo
20. Peltola wins Alaska Senate; Democrats take a 56–44 majority
21. Nvidia posts record $115.8bn quarter; board rules out Huang return
22. Anthropic prices $81.3bn IPO at $83 a share
23. COP31 climate talks open in Antalya, Turkey
24. ASEAN sets terms for Myanmar's return
25. Knesset elects Kahana speaker, 66–52
26. Board of Peace warns Gaza truce nears collapse; faults both sides
27. Houthi missiles over Riyadh intercepted
28. US loses measles elimination status; 5,412 cases in 2026
29. India wholesale inflation hits 12.29%, a four-year high
30. Germany pledges $1.1bn air-defence package for Ukraine
31. Britain pledges £240m, 1,000+ air-defence missiles for Ukraine
32. Ukraine drones cut Russian oil refining output by 45%
33. Brent crude falls below $90 a barrel
34. Third US carrier reaches the Middle East
35. WHO: 950,000 displaced Palestinians on flood-prone Gaza ground
36. Russian jets violate Japanese airspace; Taiwan logs PLA sorties
37. NATO unveils strategy for next-generation communications
38. Lee uses APEC to strengthen ties with Beijing
39. EU authorises signing of Indonesia trade deal
40. UK energy price cap forecast to rise 26% in January

Corrections made against the leading competitor's page during research:
the Bangladesh figure is 535 factories disrupted (TBS, 18 Nov), not 55;
Anthropic's IPO raised $81.3bn at $83, not $18bn; the Qeshm strike was
on Tuesday 17 November, so the lead says so explicitly. Dropped for lack
of a verifiable 18 November source: a Russia–Ukraine POW swap (no
Nov-18-2026 confirmation found), Lee seeking Xi's help on North Korea,
the Eisenkot mandate (given 9 November) and Aramco-tower damage (8 Nov).

The illustrations, the Gulf map and the Kerch Bridge diagram are
original flat drawings made in code — no photographs, no copied artwork,
no external images.

## How to run

```sh
python3 main.py
```

Writes `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` when that
variable is set, for local runs). Python 3.13, standard library only —
nothing is installed and there is no network in the sandbox, so `main.py`
copies the pre-rendered `frontpage.png` shipped in this repository.
The image itself was drawn at build time with Pillow and DejaVu fonts
(see `../render_news_image_v6.py` in the build workspace, not part of
this repo); the program's output is byte-identical on every run.

## Files

- `main.py` — the entry program (stdlib only)
- `frontpage.png` — the rendered 1024×1024 broadsheet
- `LICENSE` — MIT
- `.makefun/owner.json` — account wallet claim
