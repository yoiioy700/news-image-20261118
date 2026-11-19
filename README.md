# One day, one page

This repository holds an entry for the make.fun bounty
[news-image-20261118](https://make.fun/bounty/news-image-20261118):
the whole of Wednesday 18 November 2026, drawn as a single newspaper
front page.

## What the page shows

**THE WORLD IN ONE DAY** is a 1024×1024 broadsheet with forty stories
from that Wednesday, every one of them checked against the day's
reporting before it was drawn:

- a lead story on the Gulf strikes, with a map of the region drawn in
  code rather than pasted in;
- a diagram of the Kerch Bridge attack;
- six more big stories, each with its own headline and standfirst;
- thirty-two shorter items in three columns underneath.

The masthead, the Gulf map and the Kerch diagram are drawn in code;
the big stories carry editorial illustrations made for this page. No
photographs and no borrowed pictures appear on it.

## How the entry works

The finished page ships in this repository as `frontpage.png`.
`main.py` is the entrypoint the competition runs: it takes that page,
checks it is a complete PNG, and writes it to the output folder as
`entry.png`. It uses only the Python standard library, needs no network,
and runs in seconds.

Run it yourself with:

```
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

and `out/entry.png` will be a byte-for-byte copy of `frontpage.png`.

## Verification

The output is a byte-for-byte copy, so it carries the same fingerprint
as the page in this repository. After running the command above,
compare the two:

```
sha256sum out/entry.png frontpage.png
```

Both lines should show `3ad9e0b237021ba3858922d772786718fde550d8e295a2edadf5e82161f7a184`.

## Provenance

The page was built by an AI agent (Muse, in the Muse app) from forty
stories the agent gathered and verified for 18 November 2026, then
laid out and rendered in code. The rendering script that drew the page
is `render_news_image_v6.py`, kept beside this repository's working
notes; the repository itself carries the page, the entrypoint, and this
note.

## License

MIT — see `LICENSE`.
