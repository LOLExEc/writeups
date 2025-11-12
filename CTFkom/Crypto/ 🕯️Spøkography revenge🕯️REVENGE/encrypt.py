#!/usr/bin/env python3
import hashlib, random, json, sys

EMOJIS = ['🎃','👻','🕷️','🦇','🪦','🧙‍♀️','🧛‍♂️','🧟‍♀️','🩸','🕯️','🍬','🍭','🧪','🦴','⚰️','🔮','🌕','🌑','🕸️','🏚️','🔔','📿','🗝️','🪄','😈','☠️']
ALPHABET = [chr(ord('A') + i) for i in range(26)]

def create_mapping(key: str):
    
    h = hashlib.sha256(key.encode('utf-8')).digest()
    seed = int.from_bytes(h[:8], 'big')
    rnd = random.Random(seed)
    emojis = EMOJIS[:]  
    rnd.shuffle(emojis)
    mapping = {ALPHABET[i]: emojis[i] for i in range(26)}
    return mapping

def encode(plaintext: str, mapping):
    out = []
    for ch in plaintext.upper():
        if ch in mapping:
            out.append(mapping[ch])
        else:
        
            out.append(ch)
    return ''.join(out)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("syntax error")
    key = sys.argv[1]
    flag = sys.argv[2]
    outprefix = sys.argv[3]

    mapping = create_mapping(key)
    ciphertext = encode(flag, mapping)

    with open(outprefix + "_mapping.json", "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)
    with open(outprefix + "_cipher.txt", "w", encoding="utf-8") as f:
        f.write(ciphertext + "\n")

    print("Generated:")
    print(" - mapping ->", outprefix + "_mapping.json")
    print(" - ciphertext ->", outprefix + "_cipher.txt")
    print("Ciphertext preview:", ciphertext)
