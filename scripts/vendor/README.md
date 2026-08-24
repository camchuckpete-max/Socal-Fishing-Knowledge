# Vendored third-party assets

## leaflet-1.9.4.js / leaflet-1.9.4.css

[Leaflet](https://leafletjs.com) 1.9.4, BSD-2-Clause, (c) 2010-2023 Volodymyr
Agafonkin / CloudMade. Unmodified, from `unpkg.com/leaflet@1.9.4/dist/`.

**Why vendored rather than loaded from a CDN.** `scripts/build-review-watch.py`
inlines these into the Review Watch page so the map has **no runtime external
dependency**. A CDN `<script>` tag was tried first and is a real availability
risk: the map is a GATE review surface, and a page that silently loses its
basemap when unpkg is slow or blocked is worse than one that carries 160 KB.
Inlining also means the page renders identically offline, which is how it gets
tested.

Map TILES are still fetched from OpenStreetMap at view time — those cannot be
inlined, and OSM attribution is rendered on the map as their licence requires.
This is why the map lives on GitHub Pages: a published Claude Artifact runs
under a CSP that blocks external tile hosts.

To upgrade: replace both files, bump the version in this README and in the
`VENDOR` paths in `scripts/build-review-watch.py`.
