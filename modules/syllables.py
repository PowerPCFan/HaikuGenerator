import re as regexp
import collections
import cmudict
from typing import IO, Any

pronunciations: list[Any] | None = None
lookup: collections.defaultdict[str, list[str]] | None = None
rhyme_lookup: collections.defaultdict[str, list[str]] | None = None


def _pcmu(cmufh: IO[bytes]) -> list:
    pronunciations = list()
    for line in cmufh:
        line = line.strip().decode('utf-8')
        if line.startswith(';'):
            continue
        word, phones = line.split(" ", 1)
        pronunciations.append((word.split('(', 1)[0].lower(), phones))
    return pronunciations


def _rhp(phones: str) -> str:
    phones_list: list[str] = phones.split()
    for i in range(len(phones_list) - 1, 0, -1):
        if phones_list[i][-1] in '12':
            return ' '.join(phones_list[i:])
    return phones


def _init_cmu(filehandle: IO[bytes] | None = None) -> None:
    global pronunciations, lookup, rhyme_lookup
    if pronunciations is None:
        if filehandle is None:
            filehandle = cmudict.dict_stream()
        pronunciations = _pcmu(filehandle)
        filehandle.close()
        lookup = collections.defaultdict(list)
        for word, phones in pronunciations:
            lookup[word].append(phones)
        rhyme_lookup = collections.defaultdict(list)
        for word, phones in pronunciations:
            rp: str = _rhp(phones)
            if rp is not None:
                rhyme_lookup[rp].append(word)


def phones_for_word(find: str) -> list:
    _init_cmu()

    if lookup is None:
        raise ValueError("CMU Pronouncing Dictionary not initialized.")
    return lookup.get(find.lower(), [])


def get_syllables(word: str) -> int:
    phones: list[str] = phones_for_word(word.lower())
    if phones:
        return len(regexp.sub(r"[^012]", "", phones[0]))
    return len(regexp.findall(r'[aeiouy]+', word.lower()))  # fallback


def get_line_syllables(line: str) -> int:
    return sum(get_syllables(w) for w in regexp.findall(r'\w+', line))
