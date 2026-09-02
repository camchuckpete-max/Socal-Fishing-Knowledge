import io
p = 'locations/bumps.md'
s = open(p, encoding='utf-8').read()
pairs = [
 ("[Lower Cross](lower-cross.md)).\n⚠ Fact-check (contradicted-internal): two further",
  "[Lower Cross](lower-cross.md)).\n\n⚠ Fact-check (contradicted-internal): two further"),
 ("this page's own backlinks block.\nThe zone exists on",
  "this page's own backlinks block.\n\nThe zone exists on"),
 ("no page on this ladder.\n⚠ Fact-check (contradicted-internal): [380](380.md)",
  "no page on this ladder.\n\n⚠ Fact-check (contradicted-internal): [380](380.md)"),
 ("points a different way and stops short.\n⚠ Fact-check (contradicted-by-source): `Ix0gG0-l3v0`",
  "points a different way and stops short.\n\n⚠ Fact-check (contradicted-by-source): `Ix0gG0-l3v0`"),
 ("this page's `distance_nm` field.\n⚠ Fact-check (contradicted-by-source): the ~180 mi",
  "this page's `distance_nm` field.\n\n⚠ Fact-check (contradicted-by-source): the ~180 mi"),
 ("calls day one of the event.\n⚠ Flagged gap",
  "calls day one of the event.\n\n⚠ Flagged gap"),
 ("water-temperature.md)).\n⚠ Fact-check (contradicted-by-source): \"chart-first\"",
  "water-temperature.md)).\n\n⚠ Fact-check (contradicted-by-source): \"chart-first\""),
 ("the region's doctrine.\n⚠ Flagged gap — no\ncorpus source: a wind or swell",
  "the region's doctrine.\n\n⚠ Flagged gap — no corpus source: a wind or swell"),
 ("not because the mark is shallow.\n⚠ Fact-check (contradicted-by-source): `Rf1HKJG-SDg`",
  "not because the mark is shallow.\n\n⚠ Fact-check (contradicted-by-source): `Rf1HKJG-SDg`"),
 ("pages.\n⚠ Flagged gap — no\ncorpus source says what shape",
  "pages.\n\n⚠ Flagged gap — no corpus source says what shape"),
 ("learned over repeat trips.\n⚠ Fact-check (contradicted-internal): \"no lee",
  "learned over repeat trips.\n\n⚠ Fact-check (contradicted-internal): \"no lee"),
 ("[Lower Cross](lower-cross.md).\n⚠ Flagged gap — no\ncorpus source: bottom composition",
  "[Lower Cross](lower-cross.md).\n\n⚠ Flagged gap — no corpus source: bottom composition"),
 ("\"outside\" reaches.\n⚠ Fact-check (contradicted-by-source): the direct quote",
  "\"outside\" reaches.\n\n⚠ Fact-check (contradicted-by-source): the direct quote"),
 ("2021-05-14 is the manifest upload date.\n⚠ Flagged gap",
  "2021-05-14 is the manifest upload date.\n\n⚠ Flagged gap"),
 ("a coastal island, not out here.\n⚠ Fact-check (contradicted-by-source): the temperature",
  "a coastal island, not out here.\n\n⚠ Fact-check (contradicted-by-source): the temperature"),
 ("anything near this water has.\n⚠ Fact-check (contradicted-by-source): the deep tier",
  "anything near this water has.\n\n⚠ Fact-check (contradicted-by-source): the deep tier"),
 ("you are looking at anything else.\n⚠ Fact-check (contradicted-by-source): `Blh2BA-7Ono`",
  "you are looking at anything else.\n\n⚠ Fact-check (contradicted-by-source): `Blh2BA-7Ono`"),
]
for old, new in pairs:
    n = s.count(old)
    if n != 1:
        raise SystemExit('MISS %d: %r' % (n, old[:60]))
    s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s)
print('ok', len(pairs))
