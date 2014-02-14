import codecs, re

def search(c, q):
  out = []
  regex = re.compile(q, re.IGNORECASE)
  for k in c:
    linehits = regex.findall(c[k]["msg"])
    if linehits:
      out.append((str(k), c[k]["uname"], c[k]["msg"]))
  return out

def readCorpus():
  fin = codecs.open("moroccorp.txt", "r", "utf-8")
  lines = fin.readlines()
  fin.close()
  crp = {}
  i = 1
  for line in lines:
    uname = line.split("\t")[0]
    msg = " ".join(line.split("\t")[1:]).strip()
    crp[i] = {"uname": uname, "msg": msg}
    i += 1
  return crp

moroccorp = readCorpus()
hits = search(moroccorp, r"\been [^\s]+e \bmeisje\b")

for hit in hits:
  print "\t".join(hit)
