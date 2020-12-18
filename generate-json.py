# [rights]  Copyright 2020 brianddk at github https://github.com/brianddk 
# [license] Apache 2.0 License https://www.apache.org/licenses/LICENSE-2.0
# [repo]    https://github.com/brianddk/bible-bip                         
# [btc]     BTC-b32: bc1qwc2203uym96u0nmq04pcgqfs9ldqz9l3mz8fpj           
# [tipjar]  github.com/brianddk/reddit/blob/master/tipjar/tipjar.txt      
# [ref]     https://www.sacred-texts.com/bib/osrc/                        

from mnemonic import Mnemonic
from json import dump
from sys import exit

wordlist = Mnemonic("english").wordlist
words = {}
verses = {}
for word in wordlist:
    words[word] = dict(hits = [], short = word[0:4])
    
with open("kjvdat.txt", "r") as f:
    lines = [l.lower().strip() for l in f.readlines()]
    for line in lines:
        i = line.find(" ")
        verse = line[0:(i-1)]
        verses[verse] = dict(hits = [], words = line[(i+1):].split(" "))

print(len(verses.keys()))        

hits = k = -1
m = 0
for key in words.keys():
    k += 1
    for verse in verses.keys():
        i = 0
        for word in verses[verse]['words']:
            i+=1
            if word.startswith(words[key]['short']):
                hits += 1
                hit = f"{i:04d}|{verse}"                
                words[key]['hits'] += [hit]
                hit = f"{i:04d}|{key}"                
                verses[verse]['hits'] += [hit]
                
    if not words[key]['hits']:
        m += 1
        miss_pct = m / (k+1)
        done_pct = (k+1) / 2048
        print(f"{100*done_pct:.2f} {100*miss_pct:.2f}")

with open("words.json", "w") as f:
    dump(words, f, indent=2)

for (k,d) in verses.items():
    del(d['words'])
with open("verses.json", "w") as f:
    dump(verses, f, indent=2)
    