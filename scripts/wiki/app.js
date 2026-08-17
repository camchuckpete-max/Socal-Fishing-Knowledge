/* Bight Fishing Wiki - router, navigation, and search over the whole KB. */
(function () {
  "use strict";

  var KB = JSON.parse(document.getElementById("kb-data").textContent);
  var NOTES = KB.notes;
  var BY_ID = Object.create(null);
  var BRANCH_OF = Object.create(null);
  var IN_BRANCH = Object.create(null);
  var i;

  for (i = 0; i < NOTES.length; i++) {
    var n = NOTES[i];
    BY_ID[n.id] = n;
    n.lc = (n.title + "   " + n.tags.join(" ") + "   " + n.text).toLowerCase();
    n.lcTitle = n.title.toLowerCase();
    n.headings = (n.toc || []).map(function (t) { return t.text.toLowerCase(); }).join(" | ");
  }
  for (i = 0; i < KB.branches.length; i++) {
    BRANCH_OF[KB.branches[i].id] = KB.branches[i];
    IN_BRANCH[KB.branches[i].id] = [];
  }
  for (i = 0; i < NOTES.length; i++) {
    if (IN_BRANCH[NOTES[i].branch] && !NOTES[i].isIndex) IN_BRANCH[NOTES[i].branch].push(NOTES[i]);
  }
  Object.keys(IN_BRANCH).forEach(function (k) {
    IN_BRANCH[k].sort(function (a, b) {
      if (a.subdir !== b.subdir) return a.subdir < b.subdir ? -1 : 1;
      return a.title.localeCompare(b.title);
    });
  });

  var $ = function (sel) { return document.querySelector(sel); };
  var app = $(".app");
  var main = $("#main");
  var sidebar = $("#sidebar");

  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function plural(count, word) { return count + " " + word + (count === 1 ? "" : "s"); }
  function commas(x) { return String(x).replace(/\B(?=(\d{3})+(?!\d))/g, ","); }

  function prettyDate(iso) {
    if (!iso) return "";
    var parts = iso.split("-");
    var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    return months[parseInt(parts[1], 10) - 1] + " " + parseInt(parts[2], 10) + ", " + parts[0];
  }

  /* ------------------------------------------------------------ theme -- */

  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  var savedTheme = store.get("bight-theme");
  if (savedTheme === "light" || savedTheme === "dark") {
    document.documentElement.setAttribute("data-theme", savedTheme);
  }

  $("#theme-toggle").addEventListener("click", function () {
    var explicit = document.documentElement.getAttribute("data-theme");
    var dark = explicit ? explicit === "dark"
      : window.matchMedia("(prefers-color-scheme: dark)").matches;
    var next = dark ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    store.set("bight-theme", next);
  });

  $("#repo-link").href = KB.repo;

  /* -------------------------------------------------------------- nav -- */

  var CHEV = '<svg class="navchev" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 3.5 10.5 8 6 12.5"/></svg>';

  function buildSidebar() {
    var html = "";
    html += '<div class="navtop"><a href="#/planning/day-plan-protocol">' +
      '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.8 2.6 5.4v5c0 4.3 3.1 7.2 7.4 7.8 4.3-.6 7.4-3.5 7.4-7.8v-5Z"/><path d="M7 10.1 9.2 12.3 13.3 8"/></svg>' +
      "Start: the day plan</a></div>";

    for (var g = 0; g < KB.groups.length; g++) {
      var group = KB.groups[g];
      var branches = KB.branches.filter(function (b) { return b.group === group.id; });
      var loose = group.id === "meta" ? NOTES.filter(function (x) { return x.branch === "meta"; }) : [];
      if (!branches.length && !loose.length) continue;

      html += '<div class="navgroup"><h2 class="navgroup-label">' + group.label + "</h2>";
      for (var b = 0; b < branches.length; b++) {
        var br = branches[b];
        var items = IN_BRANCH[br.id] || [];
        html += '<div class="navbranch" data-branch="' + br.id + '" data-open="false">' +
          '<button class="navbranch-head" data-toggle="' + br.id + '" aria-expanded="false">' +
          CHEV + '<span class="navcode">' + br.code + "</span>" + esc(br.label) +
          '<span class="navbranch-count">' + items.length + "</span></button>" +
          '<ul class="navlist">';
        if (br.index) {
          html += '<li><a href="#/' + br.id + '" data-note="' + br.id + '">Overview</a></li>';
        }
        var lastSub = "";
        for (var k = 0; k < items.length; k++) {
          var it = items[k];
          if (it.subdir !== lastSub) {
            lastSub = it.subdir;
            if (lastSub) html += '<li class="navsub">' + esc(lastSub.replace(/[-_/]/g, " ")) + "</li>";
          }
          html += '<li><a href="#/' + it.id + '" data-note="' + it.id + '">' + esc(it.nav || it.title) + "</a></li>";
        }
        html += "</ul></div>";
      }
      if (loose.length) {
        html += '<ul class="navlist" style="border-left:0;margin-left:0;padding-left:8px">';
        for (var m = 0; m < loose.length; m++) {
          html += '<li><a href="#/' + loose[m].id + '" data-note="' + loose[m].id + '">' + esc(loose[m].nav || loose[m].title) + "</a></li>";
        }
        html += "</ul>";
      }
      html += "</div>";
    }
    sidebar.innerHTML = html;
  }

  sidebar.addEventListener("click", function (ev) {
    var toggle = ev.target.closest("[data-toggle]");
    if (toggle) {
      var wrap = toggle.parentNode;
      var open = wrap.getAttribute("data-open") === "true";
      wrap.setAttribute("data-open", open ? "false" : "true");
      toggle.setAttribute("aria-expanded", open ? "false" : "true");
      return;
    }
    if (ev.target.closest("a") && window.matchMedia("(max-width: 900px)").matches) closeNav();
  });

  function markNav(noteId, branchId) {
    var links = sidebar.querySelectorAll("a[data-note]");
    for (var j = 0; j < links.length; j++) {
      if (links[j].getAttribute("data-note") === noteId) links[j].setAttribute("aria-current", "page");
      else links[j].removeAttribute("aria-current");
    }
    var wraps = sidebar.querySelectorAll(".navbranch");
    for (var w = 0; w < wraps.length; w++) {
      var isActive = wraps[w].getAttribute("data-branch") === branchId;
      wraps[w].setAttribute("data-active", isActive ? "true" : "false");
      if (isActive && wraps[w].getAttribute("data-open") !== "true") {
        wraps[w].setAttribute("data-open", "true");
        wraps[w].querySelector(".navbranch-head").setAttribute("aria-expanded", "true");
      }
    }
    var current = sidebar.querySelector('a[aria-current="page"]');
    if (current && current.getBoundingClientRect) {
      var box = current.getBoundingClientRect();
      if (box.top < 90 || box.bottom > window.innerHeight - 20) {
        current.scrollIntoView({ block: "center" });
      }
    }
  }

  function openNav() {
    app.setAttribute("data-nav", "open");
    $("#scrim").hidden = false;
    $("#nav-toggle").setAttribute("aria-expanded", "true");
  }
  function closeNav() {
    app.removeAttribute("data-nav");
    $("#scrim").hidden = true;
    $("#nav-toggle").setAttribute("aria-expanded", "false");
  }
  $("#nav-toggle").addEventListener("click", function () {
    if (app.getAttribute("data-nav") === "open") closeNav(); else openNav();
  });
  $("#scrim").addEventListener("click", closeNav);

  /* ------------------------------------------------------------ pages -- */

  function metaChips(note) {
    var out = "";
    if (note.type) out += '<span class="chip">' + esc(note.type) + "</span>";
    if (note.confidence) {
      out += '<span class="chip" data-conf="' + esc(note.confidence) + '">' +
        '<span class="chip-dot"></span>' + esc(note.confidence) + " confidence</span>";
    }
    if (note.sources && note.sources.length) {
      out += '<span class="chip"><span class="chip-num">' + note.sources.length + "</span> sources</span>";
    }
    out += '<span class="chip"><span class="chip-num">' + commas(note.words) + "</span> words</span>";
    if (note.updated) out += '<span class="chip">Updated ' + esc(prettyDate(note.updated)) + "</span>";
    out += '<a class="chip" href="' + KB.repo + "/blob/main/" + note.path + '" target="_blank" rel="noopener">Source &#8599;</a>';
    return out;
  }

  function tocMarkup(note) {
    if (!note.toc || note.toc.length < 2) return { rail: "", mobile: "" };
    var items = note.toc.map(function (t) {
      return '<li><a class="lvl' + t.level + '" href="#/' + note.id + "~" + t.id + '" data-jump="' + t.id + '">' + esc(t.text) + "</a></li>";
    }).join("");
    return {
      rail: '<nav class="toc" aria-label="On this page"><h2 class="toc-head">On this page</h2><ul>' + items + "</ul></nav>",
      mobile: '<details class="toc-mobile"><summary>On this page &mdash; ' + plural(note.toc.length, "section") + "</summary><ul>" + items + "</ul></details>"
    };
  }

  function neighbours(note) {
    var list = IN_BRANCH[note.branch];
    if (!list || note.isIndex) return "";
    var idx = list.indexOf(note);
    if (idx < 0) return "";
    var prev = list[idx - 1], next = list[idx + 1], out = "";
    out += prev ? '<a class="pn prev" href="#/' + prev.id + '"><span>Previous</span><b>' + esc(prev.title) + "</b></a>" : "<span></span>";
    out += next ? '<a class="pn next" href="#/' + next.id + '"><span>Next</span><b>' + esc(next.title) + "</b></a>" : "<span></span>";
    return '<div class="prevnext">' + out + "</div>";
  }

  function renderNote(note, anchor) {
    var branch = BRANCH_OF[note.branch];
    var body = note.html;
    var lead = "";
    if (body.indexOf("<p>") === 0) {
      var end = body.indexOf("</p>");
      if (end > 0 && end < 320) {
        lead = body.slice(3, end);
        body = body.slice(end + 4);
      }
    }
    var crumbs = '<a href="#/">Wiki</a><span class="sep">/</span>';
    if (branch) crumbs += '<a href="#/' + branch.id + '">' + esc(branch.label) + "</a>";
    else crumbs += "Behind the KB";
    if (note.subdir) crumbs += '<span class="sep">/</span>' + esc(note.subdir.replace(/[-_/]/g, " "));

    var toc = tocMarkup(note);
    var tags = (note.tags || []).length
      ? '<div class="tagrow">' + note.tags.map(function (t) {
          return '<a class="tag" href="#/" data-tag="' + esc(t) + '">' + esc(t) + "</a>";
        }).join("") + "</div>"
      : "";

    var foot = "";
    if (note.backlinks && note.backlinks.length) {
      foot += '<section class="docfoot"><h2 class="foothead">Linked from ' +
        plural(note.backlinks.length, "note") + '</h2><div class="linkchips">' +
        note.backlinks.map(function (l) {
          return '<a class="linkchip" href="#/' + l.note + '">' + esc(l.title) + "</a>";
        }).join("") + "</div></section>";
    }
    if (note.sources && note.sources.length) {
      foot += '<p class="sourceline"><b>Sources</b><br>' + note.sources.map(function (s) {
        return s === "cameron" ? "cameron"
          : '<a href="https://www.youtube.com/watch?v=' + encodeURIComponent(s) + '" target="_blank" rel="noopener">' + esc(s) + "</a>";
      }).join(" &middot; ") + "</p>";
    }

    main.innerHTML =
      '<div class="page"><div class="doc"><article class="doc-body">' +
      '<p class="eyebrow">' + crumbs + "</p>" +
      '<h1 class="doctitle">' + esc(note.title) + "</h1>" +
      (lead ? '<p class="doclead">' + lead + "</p>" : "") +
      '<div class="contour"></div>' +
      '<div class="metarow">' + metaChips(note) + "</div>" +
      tags +
      toc.mobile +
      '<div class="prose">' + body + "</div>" +
      foot +
      neighbours(note) +
      "</article>" + toc.rail + "</div></div>";

    decorate();
    markNav(note.id, note.branch);
    afterRender(anchor);
    spy();
  }

  function renderBranch(branch, note, anchor) {
    var items = IN_BRANCH[branch.id] || [];
    var blurbs = Object.create(null);
    if (note && note.children) {
      note.children.forEach(function (c) { blurbs[c.note] = c.blurb; });
    }
    var body = note ? note.html : "";
    // The generated index list is replaced by the note grid below it.
    var cards = items.map(function (it) {
      var blurb = blurbs[it.id] || it.summary || "";
      if (blurb.length > 150) blurb = blurb.slice(0, 150).replace(/\s+\S*$/, "") + "\u2026";
      return '<a class="notecard" href="#/' + it.id + '"><b>' + esc(it.title) + "</b>" +
        (blurb ? "<p>" + esc(blurb) + "</p>" : "") +
        '<span class="notecard-meta"><span class="dot" data-conf="' + esc(it.confidence || "") + '"></span>' +
        esc(it.confidence || "unrated") + " &middot; " + commas(it.words) + " words</span></a>";
    }).join("");

    var sub = items.length ? '<div class="sectionhead"><h2>' + plural(items.length, "note") + "</h2></div>" +
      '<div class="notegrid">' + cards + "</div>" : "";

    main.innerHTML =
      '<div class="page"><div class="doc solo"><article class="doc-body wide">' +
      '<p class="eyebrow"><a href="#/">Wiki</a><span class="sep">/</span>' + esc(branch.label) + "</p>" +
      '<h1 class="doctitle">' + esc(branch.label) + "</h1>" +
      '<p class="doclead">' + branch.blurb + "</p>" +
      '<div class="contour"></div>' +
      sub +
      (body ? '<div class="prose" style="margin-top:38px">' + body + "</div>" : "") +
      (note ? '<p class="sourceline" style="margin-top:30px"><a href="' + KB.repo + "/blob/main/" + note.path + '" target="_blank" rel="noopener">Read this index on GitHub &#8599;</a></p>' : "") +
      "</article></div></div>";

    decorate();
    markNav(branch.id, branch.id);
    afterRender(anchor);
  }

  function renderHome() {
    var s = KB.stats;
    var stats = [
      [commas(s.notes), "Notes"],
      [s.species, "Species"],
      [s.techniques, "Techniques"],
      [commas(s.sources), "Sources"],
      [commas(s.transcripts), "Transcripts"],
      [commas(Math.round(s.words / 1000)) + "k", "Words"]
    ].map(function (row) {
      return '<div class="stat"><b>' + row[0] + "</b><span>" + row[1] + "</span></div>";
    }).join("");

    var groupsHtml = KB.groups.map(function (group) {
      var branches = KB.branches.filter(function (b) { return b.group === group.id; });
      if (!branches.length) return "";
      var cards = branches.map(function (b) {
        return '<a class="card" href="#/' + b.id + '"><span class="card-top">' +
          '<span class="navcode">' + b.code + "</span>" +
          '<span class="card-title">' + esc(b.label) + "</span>" +
          '<span class="card-count">' + b.count + "</span></span><p>" + b.blurb + "</p></a>";
      }).join("");
      return '<div class="sectionhead"><h2>' + group.label + '</h2></div><div class="cardgrid">' + cards + "</div>";
    }).join("");

    main.innerHTML =
      '<div class="page home">' +
      '<header class="masthead">' +
      '<p class="eyebrow">Southern California Bight <span class="sep">&middot;</span> Baja <span class="sep">&middot;</span> updated ' + esc(prettyDate(KB.generated)) + "</p>" +
      '<h1 class="home-title">Everything the <i>Bight</i> will teach you,<br>in one searchable place.</h1>' +
      '<p class="home-lead">The system of record for fishing <strong>knowledge</strong> &mdash; where to go, when to go, how to find fish on the meter, which technique fits the situation, and what tackle it takes. Live <strong>conditions</strong> come from BightSST; everything else lives here.</p>' +
      "</header>" +
      '<div class="statstrip">' + stats + "</div>" +
      '<a class="startcard" href="#/planning/day-plan-protocol">' +
      '<svg class="startcard-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2 3.4 6.4v5.9c0 5 3.6 8.4 8.6 9.1 5-.7 8.6-4.1 8.6-9.1V6.4Z"/><path d="M8.3 12.1 11 14.8l4.9-5.2"/></svg>' +
      '<span><span class="startcard-kicker">Start here</span><b>The day-plan protocol</b>' +
      "<p>Pull conditions, apply the seasonal priors, route through the species notes, then resolve gear against your profile. The procedure every trip runs on.</p></span>" +
      '<span class="startcard-go">&rarr;</span></a>' +
      groupsHtml +
      '<footer class="homefoot">' +
      '<span>Built ' + esc(prettyDate(KB.generated)) + " from the knowledgebase</span>" +
      '<a href="' + KB.repo + '" target="_blank" rel="noopener">Repository &#8599;</a>' +
      '<a href="https://bightai-api.onrender.com" target="_blank" rel="noopener">BightSST conditions &#8599;</a>' +
      '<a href="#/spec">Repo conventions</a>' +
      "</footer></div>";

    markNav("", "");
    afterRender("");
  }

  /* Content-aware touches the Markdown itself can't carry. */
  function decorate() {
    var paras = main.querySelectorAll(".prose p");
    for (var p = 0; p < paras.length; p++) {
      var strong = paras[p].firstElementChild;
      if (strong && strong.tagName === "STRONG" && /^observed\b/i.test(strong.textContent)) {
        paras[p].classList.add("obs");
      }
    }
    var rows = main.querySelectorAll(".x-table tbody tr");
    for (var r = 0; r < rows.length; r++) {
      if (/flagged stub/i.test(rows[r].textContent)) rows[r].setAttribute("data-stub", "true");
    }
  }

  function afterRender(anchor) {
    if (anchor) {
      var target = document.getElementById(anchor);
      if (target) {
        var top = target.getBoundingClientRect().top + window.pageYOffset - 74;
        window.scrollTo(0, top);
        return;
      }
    }
    window.scrollTo(0, 0);
  }

  /* --------------------------------------------------------- scrollspy -- */

  var spyObserver = null;
  function spy() {
    if (spyObserver) spyObserver.disconnect();
    var links = main.querySelectorAll(".toc a[data-jump]");
    if (!links.length || !window.IntersectionObserver) return;
    var map = Object.create(null);
    for (var j = 0; j < links.length; j++) map[links[j].getAttribute("data-jump")] = links[j];
    var heads = main.querySelectorAll(".prose .x-h[id]");
    var visible = [];
    spyObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var id = entry.target.id;
        var at = visible.indexOf(id);
        if (entry.isIntersecting && at < 0) visible.push(id);
        if (!entry.isIntersecting && at >= 0) visible.splice(at, 1);
      });
      var active = visible.length ? visible[0] : null;
      if (!active) return;
      for (var key in map) map[key].classList.toggle("on", key === active);
    }, { rootMargin: "-76px 0px -68% 0px" });
    for (var h = 0; h < heads.length; h++) spyObserver.observe(heads[h]);
  }

  /* ------------------------------------------------------------ router -- */

  function route() {
    var hash = location.hash.replace(/^#\/?/, "");
    var anchor = "";
    var tilde = hash.indexOf("~");
    if (tilde >= 0) { anchor = hash.slice(tilde + 1); hash = hash.slice(0, tilde); }
    hash = decodeURIComponent(hash).replace(/\/$/, "");

    if (!hash) { renderHome(); return; }
    var branch = BRANCH_OF[hash];
    if (branch) { renderBranch(branch, BY_ID[hash], anchor); return; }
    var note = BY_ID[hash];
    if (note) { renderNote(note, anchor); return; }

    main.innerHTML = '<div class="page"><div class="doc"><article class="doc-body">' +
      '<p class="eyebrow"><a href="#/">Wiki</a></p><h1 class="doctitle">No such note</h1>' +
      '<p class="doclead">Nothing is filed at <code>' + esc(hash) + "</code>. Try the search, or head back to the " +
      '<a href="#/">index</a>.</p></article></div></div>';
    markNav("", "");
  }

  window.addEventListener("hashchange", route);

  document.addEventListener("click", function (ev) {
    var tagLink = ev.target.closest("[data-tag]");
    if (tagLink) {
      ev.preventDefault();
      openSearch("tag:" + tagLink.getAttribute("data-tag"));
      return;
    }
    var anchorLink = ev.target.closest(".x-anchor, .x-anchorlink");
    if (anchorLink) {
      ev.preventDefault();
      var id = anchorLink.getAttribute("data-anchor") || anchorLink.getAttribute("href").slice(1);
      var current = location.hash.replace(/^#\/?/, "").split("~")[0];
      history.replaceState(null, "", "#/" + current + "~" + id);
      var el = document.getElementById(id);
      if (el) window.scrollTo(0, el.getBoundingClientRect().top + window.pageYOffset - 74);
      return;
    }
    var jump = ev.target.closest("[data-jump]");
    if (jump) {
      ev.preventDefault();
      var jid = jump.getAttribute("data-jump");
      var jel = document.getElementById(jid);
      if (jel) {
        window.scrollTo({ top: jel.getBoundingClientRect().top + window.pageYOffset - 74, behavior: "smooth" });
        var base = location.hash.replace(/^#\/?/, "").split("~")[0];
        history.replaceState(null, "", "#/" + base + "~" + jid);
      }
    }
  });

  /* ------------------------------------------------------------ search -- */

  var layer = $("#search-layer");
  var input = $("#search-input");
  var results = $("#search-results");
  var metaLine = $("#search-meta");
  var selected = 0;
  var current = [];

  function parseQuery(raw) {
    var filters = { tag: [], type: [], branch: [] };
    var terms = [];
    raw.trim().split(/\s+/).forEach(function (part) {
      if (!part) return;
      var m = /^(tag|type|in|branch):(.+)$/i.exec(part);
      if (m) {
        var key = m[1].toLowerCase();
        if (key === "in") key = "branch";
        filters[key].push(m[2].toLowerCase());
      } else {
        terms.push(part.toLowerCase());
      }
    });
    return { terms: terms, filters: filters };
  }

  function countOf(haystack, needle) {
    var total = 0, at = haystack.indexOf(needle);
    while (at >= 0 && total < 40) { total++; at = haystack.indexOf(needle, at + needle.length); }
    return total;
  }

  function search(raw) {
    var q = parseQuery(raw);
    var hits = [];
    for (var j = 0; j < NOTES.length; j++) {
      var note = NOTES[j];
      var f = q.filters;
      if (f.tag.length && !f.tag.every(function (t) {
        return note.tags.some(function (x) { return x.toLowerCase().indexOf(t) >= 0; });
      })) continue;
      if (f.type.length && !f.type.some(function (t) { return (note.type || "").toLowerCase().indexOf(t) === 0; })) continue;
      if (f.branch.length && !f.branch.some(function (t) { return note.branch.indexOf(t) === 0; })) continue;

      var score = note.isIndex ? -30 : 0;
      var ok = true;
      for (var t = 0; t < q.terms.length; t++) {
        var term = q.terms[t];
        if (note.lc.indexOf(term) < 0) { ok = false; break; }
        if (note.lcTitle === term) score += 1200;
        else if (note.lcTitle.indexOf(term) === 0) score += 520;
        else if (note.lcTitle.indexOf(term) >= 0) score += 300;
        if (note.tags.some(function (x) { return x.toLowerCase().indexOf(term) >= 0; })) score += 170;
        if (note.headings.indexOf(term) >= 0) score += 95;
        if ((note.summary || "").toLowerCase().indexOf(term) >= 0) score += 55;
        score += Math.min(countOf(note.text.toLowerCase(), term), 12) * 7;
      }
      if (!ok) continue;
      if (!q.terms.length && !(q.filters.tag.length || q.filters.type.length || q.filters.branch.length)) continue;
      hits.push({ note: note, score: score });
    }
    hits.sort(function (a, b) { return b.score - a.score || a.note.title.localeCompare(b.note.title); });
    return { hits: hits.slice(0, 60), terms: q.terms, total: hits.length };
  }

  function highlight(text, terms) {
    var out = esc(text);
    if (!terms.length) return out;
    var pattern = terms.map(function (t) { return t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }).join("|");
    return out.replace(new RegExp("(" + pattern + ")", "gi"), '<span class="hit">$1</span>');
  }

  function snippet(note, terms) {
    if (!terms.length) return note.summary || "";
    var lc = note.text.toLowerCase();
    var best = -1, longest = "";
    terms.forEach(function (t) {
      var at = lc.indexOf(t);
      if (at >= 0 && (best < 0 || t.length > longest.length)) { best = at; longest = t; }
    });
    if (best < 0) return note.summary || "";
    var from = Math.max(0, best - 85);
    var slice = note.text.slice(from, from + 230);
    if (from > 0) slice = "\u2026" + slice.replace(/^\S*\s/, "");
    return slice + "\u2026";
  }

  function renderResults(raw) {
    var found = search(raw);
    current = found.hits;
    selected = 0;

    if (!raw.trim()) {
      metaLine.innerHTML = "Jump to";
      var picks = ["planning/day-plan-protocol", "species/yellowtail", "species/bluefin-tuna",
        "species/calico-bass", "conditions/water-regimes", "planning/electronics-and-sounder"];
      results.innerHTML = picks.filter(function (id) { return BY_ID[id]; }).map(function (id, k) {
        var note = BY_ID[id];
        return '<a class="sr" href="#/' + id + '" data-sel="' + (k === 0) + '"><span class="sr-top">' +
          '<span class="sr-title">' + esc(note.title) + '</span><span class="sr-branch">' +
          esc((BRANCH_OF[note.branch] || {}).label || note.branch) + "</span></span>" +
          '<p class="sr-snip">' + esc(note.summary || "") + "</p></a>";
      }).join("");
      current = picks.filter(function (id) { return BY_ID[id]; }).map(function (id) { return { note: BY_ID[id] }; });
      return;
    }

    if (!found.hits.length) {
      metaLine.innerHTML = "No matches";
      results.innerHTML = '<div class="sr-empty"><b>Nothing found</b>Try a shorter term, or filter with ' +
        "<code>tag:</code>, <code>type:</code> or <code>in:</code>.</div>";
      return;
    }

    metaLine.innerHTML = "<em>" + found.total + "</em> " + (found.total === 1 ? "note" : "notes") +
      (found.total > found.hits.length ? " &mdash; showing top " + found.hits.length : "");
    results.innerHTML = found.hits.map(function (hit, k) {
      var note = hit.note;
      return '<a class="sr" href="#/' + note.id + '" data-sel="' + (k === 0) + '"><span class="sr-top">' +
        '<span class="sr-title">' + highlight(note.title, found.terms) + "</span>" +
        '<span class="sr-branch">' + esc((BRANCH_OF[note.branch] || {}).label || "Meta") + "</span></span>" +
        '<p class="sr-snip">' + highlight(snippet(note, found.terms), found.terms) + "</p></a>";
    }).join("");
  }

  function moveSelection(delta) {
    var nodes = results.querySelectorAll(".sr");
    if (!nodes.length) return;
    nodes[selected] && nodes[selected].setAttribute("data-sel", "false");
    selected = (selected + delta + nodes.length) % nodes.length;
    nodes[selected].setAttribute("data-sel", "true");
    nodes[selected].scrollIntoView({ block: "nearest" });
  }

  function openSearch(prefill) {
    layer.hidden = false;
    document.body.style.overflow = "hidden";
    input.value = prefill || "";
    renderResults(input.value);
    input.focus();
    input.setSelectionRange(input.value.length, input.value.length);
  }
  function closeSearch() {
    layer.hidden = true;
    document.body.style.overflow = "";
  }

  $("#search-open").addEventListener("click", function () { openSearch(""); });
  $("#search-close").addEventListener("click", closeSearch);
  layer.addEventListener("mousedown", function (ev) { if (ev.target === layer) closeSearch(); });

  var typing = null;
  input.addEventListener("input", function () {
    clearTimeout(typing);
    typing = setTimeout(function () { renderResults(input.value); }, 60);
  });

  input.addEventListener("keydown", function (ev) {
    if (ev.key === "ArrowDown") { ev.preventDefault(); moveSelection(1); }
    else if (ev.key === "ArrowUp") { ev.preventDefault(); moveSelection(-1); }
    else if (ev.key === "Enter") {
      var node = results.querySelectorAll(".sr")[selected];
      if (node) { ev.preventDefault(); location.hash = node.getAttribute("href"); closeSearch(); }
    }
  });

  results.addEventListener("click", function (ev) { if (ev.target.closest(".sr")) closeSearch(); });

  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape") {
      if (!layer.hidden) { closeSearch(); return; }
      if (app.getAttribute("data-nav") === "open") closeNav();
      return;
    }
    var typingHere = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName) ||
      document.activeElement.isContentEditable;
    if ((ev.key === "k" || ev.key === "K") && (ev.metaKey || ev.ctrlKey)) {
      ev.preventDefault();
      layer.hidden ? openSearch("") : closeSearch();
      return;
    }
    if (ev.key === "/" && !typingHere && layer.hidden) { ev.preventDefault(); openSearch(""); }
  });

  /* -------------------------------------------------------------- boot -- */

  input.placeholder = "Search " + KB.notes.length + " notes \u2014 species, technique, tag, depth\u2026";
  buildSidebar();
  route();
})();
