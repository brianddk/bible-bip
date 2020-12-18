# [rights]  Copyright 2020 brianddk at github https://github.com/brianddk 
# [license] Apache 2.0 License https://www.apache.org/licenses/LICENSE-2.0
# [repo]    https://github.com/brianddk/bible-bip                         
# [btc]     BTC-b32: bc1qwc2203uym96u0nmq04pcgqfs9ldqz9l3mz8fpj           
# [tipjar]  github.com/brianddk/reddit/blob/master/tipjar/tipjar.txt      
# [ref]     https://www.sacred-texts.com/bib/osrc/                        

from mnemonic import Mnemonic
from json import dump, load
from sys import exit
from math import log

size   = 12
scalar = 1 + 1/32
bits   = int(size * 11 / scalar)

# degrade from 128 bit to 122 bit
nemo = Mnemonic("english")
with open("words.json", "r") as f:
    words = load(f)

with open("verses.json", "r") as f:
    verses = load(f)
    
# https://www.sacred-texts.com/bib/osrc/    
with open("decode.json", "r") as f:
    scratch = load(f)

decode = {}
for (k,d) in scratch.items():
    decode[d] = k

miss = []
for (k,d) in words.items():
    if not d['hits']:
        miss += [k]

# print(len(miss)) # 595 words missing, leaving 1453 words instead of 2048
# print(log(2048**size / 2**(size/3), 2)) # BIP39 is 128 / 256 bits
# print(log((2048-len(miss))**size / 2**(size/3), 2)) # Bible-bip is only  122 / 244 bits

t = f = 0
while True:
    t += 1
    seed = nemo.generate(strength=bits)
    broke = False
    for word in seed.split():
        if word in miss: 
            f += 1
            broke = True
            break
    if not broke:
        num = 0
        offsets = []
        for word in seed.split():
            num += 1
            hits = words[word]['hits']
            hits.sort()
            offset, abriv, chapter, verse = hits[0].split("|")
            book = decode[abriv]
            offsets += [str(int(offset))]
            print(f"{num}. KJV: {book} {chapter}:{verse}")             
        print(f"\nword offsets: {' '.join(offsets).strip()}\n")
        print("seed:", seed)
        break
    if not t % 1_000:
        print(f"{t:,} attempts... still trying")