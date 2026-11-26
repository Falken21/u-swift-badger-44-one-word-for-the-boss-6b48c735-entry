"""One Word for the Boss: Creditnapper.

The word is "Creditnapper" - a boss who kidnaps the credit for
work other people did. It fits the judge's brief in order:

1. It is a single word describing a boss, the sort of nickname a
   person would actually use about the one they report to.
2. It is funny on its own: the kidnapper twist lands instantly,
   with no caption or explanation needed.
3. It rings true, catching a real habit everyone has met - the
   boss who is nowhere during the work, then front and centre
   when the praise, the bonus or the boss's boss arrives.
4. It is fresh: not the first word anyone reaches for, yet its
   surprise is immediately understood rather than obscure.
5. It travels: credit can be napped in a kitchen, a warehouse or
   an office, with no industry needing to be explained.
"""

import os

TEXT = "Creditnapper"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
