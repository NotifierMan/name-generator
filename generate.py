import random
from dns.resolver import Resolver
import dns.rdatatype as dtype

VOCALS = 'aeiou'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
BANNED_TOUPLES = [
    ('t', 'b'),
    ('g', 'q'),
    ('g', 't'),
    ('z', 'c'),
    ('c', 'z'),
    ('h', 'h'),
]
TLD = 'de'

dig = Resolver()

def is_consonant(chr):
    return chr.lower() not in VOCALS

def is_vocal(chr):
    return chr.lower() in VOCALS

def is_valid_word(word, chr):
    if is_vocal(chr):
        return True

    # ban char touples
    if len(word) >= 1:
        for banned_touple in BANNED_TOUPLES:
            if word[-1] == banned_touple[0] and chr == banned_touple[1]:
                return False

    # max two consonants
    if len(word) >= 1 and is_consonant(word[-1]) and len(word) >= 2 and is_consonant(word[-2]):
        return False

    return True


for _ in range(20):
    found = False
    while not found:
        word = ''
        while len(word) < 4:
            chr = random.choice(ALPHABET)
            while not is_valid_word(word, chr):
                chr = random.choice(ALPHABET)
            word += chr
        word += ''

        domain = word + '.' + TLD

        try:
            dig.resolve(domain, rdtype=dtype.SOA)
        except:
            print(domain)
            found = True