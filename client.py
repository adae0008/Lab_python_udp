from pathlib import Path

p = Path("data/message.txt")

s = p.read_text(encoding="utf-8")

print(type(s), len(s))
print(s)

b = p.read_bytes()

print(type(b), len(b))
print(b[:20])


b2 = s.encode("utf-8")
s2 = b.decode("utf-8")

print(len(b2), type(b2))
print(type(s2))
