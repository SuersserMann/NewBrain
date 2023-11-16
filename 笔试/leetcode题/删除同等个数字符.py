text = "zaabbbj"
aa = []
bb = []
for i in range(len(text)):
    if text[i] == "a":
        aa.append(i)
    if text[i] == "b":
        bb.append(i)
a = 0
for i in range(min(len(aa), len(bb))):
    text = text[:aa[i]-a] + text[(aa[i] + 1-a):]
    a += 1
for i in range(min(len(aa), len(bb))):
    text = text[:bb[i]-a] + text[(bb[i] + 1-a):]
    a += 1
print(text)
