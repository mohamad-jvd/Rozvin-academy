/* =====================================================================
   Campus — main.js
   Vanilla JS only. Each feature is one guard-claused init function.
   ===================================================================== */
(function () {
  "use strict";

  var prefersReduced = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- sticky header shadow ---------- */
  function initHeaderScroll() {
    var header = document.getElementById("siteHeader");
    if (!header) return;
    var onScroll = function () {
      header.classList.toggle("is-stuck", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- mobile navigation ---------- */
  function initMobileNav() {
    var toggle = document.getElementById("navToggle");
    var nav = document.getElementById("mainNav");
    if (!toggle || !nav) return;

    var close = function () {
      nav.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", "Open menu");
    };
    var open = function () {
      nav.classList.add("is-open");
      toggle.setAttribute("aria-expanded", "true");
      toggle.setAttribute("aria-label", "Close menu");
    };

    toggle.addEventListener("click", function () {
      if (nav.classList.contains("is-open")) { close(); } else { open(); }
    });

    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) { close(); }
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { close(); }
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth > 860) { close(); }
    });
  }

  /* ---------- smooth scroll for in-page anchors ---------- */
  function initSmoothScroll() {
    var links = document.querySelectorAll('a[href^="#"]');
    if (!links.length) return;
    var header = document.getElementById("siteHeader");
    Array.prototype.forEach.call(links, function (link) {
      var id = link.getAttribute("href");
      if (id === "#" || id.length < 2) return;
      link.addEventListener("click", function (e) {
        var target = document.querySelector(id);
        if (!target) return;
        e.preventDefault();
        var offset = (header ? header.offsetHeight : 0) + 12;
        var top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top: top, behavior: prefersReduced ? "auto" : "smooth" });
        if (typeof target.focus === "function") {
          target.setAttribute("tabindex", "-1");
          target.focus({ preventScroll: true });
        }
      });
    });
  }

  /* ---------- hero search (front-end only) ---------- */
  function initSearch() {
    var form = document.getElementById("searchBar");
    var note = document.getElementById("searchNote");
    var input = document.getElementById("q");
    var select = document.getElementById("cat");
    var chips = document.querySelectorAll(".hero-chips .chip");
    if (!form || !note || !input) return;

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var term = input.value.trim();
      var cat = select ? select.value : "";
      if (!term && !cat) {
        note.style.color = "";
        note.textContent = "Type a topic or pick a category to see matching courses.";
        input.focus();
        return;
      }
      var label = term || cat;
      var scope = cat ? " in " + cat : "";
      note.textContent = "Great pick — showing courses for “" + label + "”" + (term && cat ? scope : "") + ".";
    });

    Array.prototype.forEach.call(chips, function (chip) {
      chip.addEventListener("click", function () {
        input.value = chip.textContent.trim();
        input.focus();
      });
    });
  }

  /* ---------- course category filter ---------- */
  function initCourseFilter() {
    var bar = document.querySelector(".filter-bar");
    var grid = document.getElementById("courseGrid");
    var empty = document.getElementById("gridEmpty");
    if (!bar || !grid) return;
    var pills = bar.querySelectorAll(".filter-pill");
    var cards = grid.querySelectorAll(".course-card");

    bar.addEventListener("click", function (e) {
      var pill = e.target.closest(".filter-pill");
      if (!pill) return;
      var filter = pill.getAttribute("data-filter");

      Array.prototype.forEach.call(pills, function (p) {
        var active = p === pill;
        p.classList.toggle("is-active", active);
        p.setAttribute("aria-pressed", active ? "true" : "false");
      });

      var shown = 0;
      Array.prototype.forEach.call(cards, function (card) {
        var match = filter === "all" || card.getAttribute("data-category") === filter;
        card.classList.toggle("is-hidden", !match);
        if (match) { shown++; }
      });
      if (empty) { empty.hidden = shown !== 0; }
    });
  }

  /* ---------- animated stat counters ---------- */
  function initCounters() {
    var nums = document.querySelectorAll(".stat-num[data-count]");
    if (!nums.length) return;

    var format = function (value, decimals) {
      if (decimals > 0) { return value.toFixed(decimals); }
      return Math.round(value).toLocaleString("en-US");
    };

    var run = function (el) {
      var target = parseFloat(el.getAttribute("data-count")) || 0;
      var suffix = el.getAttribute("data-suffix") || "";
      var decimals = parseInt(el.getAttribute("data-decimals"), 10) || 0;
      if (prefersReduced) { el.textContent = format(target, decimals) + suffix; return; }
      var dur = 1600, start = null;
      var tick = function (ts) {
        if (start === null) { start = ts; }
        var p = Math.min((ts - start) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = format(target * eased, decimals) + suffix;
        if (p < 1) { requestAnimationFrame(tick); }
      };
      requestAnimationFrame(tick);
    };

    if (!("IntersectionObserver" in window)) {
      Array.prototype.forEach.call(nums, function (el) { run(el); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          run(entry.target);
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });
    Array.prototype.forEach.call(nums, function (el) { io.observe(el); });
  }

  /* ---------- scroll reveal ---------- */
  function initReveal() {
    var els = document.querySelectorAll(".reveal");
    if (!els.length) return;
    if (prefersReduced || !("IntersectionObserver" in window)) {
      Array.prototype.forEach.call(els, function (el) { el.classList.add("is-visible"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
    Array.prototype.forEach.call(els, function (el) { io.observe(el); });
  }

  /* ---------- testimonials slider ---------- */
  function initTestimonials() {
    var track = document.getElementById("tstTrack");
    var prev = document.getElementById("tstPrev");
    var next = document.getElementById("tstNext");
    var dotsWrap = document.getElementById("tstDots");
    if (!track) return;
    var cards = track.querySelectorAll(".tst-card");
    if (!cards.length) return;

    var pageWidth = function () {
      var first = cards[0];
      var gap = parseFloat(getComputedStyle(track).columnGap) || 24;
      return first.offsetWidth + gap;
    };

    var updateButtons = function () {
      if (!prev || !next) return;
      var maxScroll = track.scrollWidth - track.clientWidth - 2;
      prev.disabled = track.scrollLeft <= 2;
      next.disabled = track.scrollLeft >= maxScroll;
    };

    if (prev) {
      prev.addEventListener("click", function () {
        track.scrollBy({ left: -pageWidth(), behavior: prefersReduced ? "auto" : "smooth" });
      });
    }
    if (next) {
      next.addEventListener("click", function () {
        track.scrollBy({ left: pageWidth(), behavior: prefersReduced ? "auto" : "smooth" });
      });
    }

    // build dots
    var dots = [];
    if (dotsWrap) {
      dotsWrap.removeAttribute("aria-hidden");
      Array.prototype.forEach.call(cards, function (card, i) {
        var dot = document.createElement("button");
        dot.type = "button";
        dot.className = "tst-dot" + (i === 0 ? " is-active" : "");
        dot.setAttribute("aria-label", "Go to testimonial " + (i + 1));
        dot.addEventListener("click", function () {
          track.scrollTo({ left: pageWidth() * i, behavior: prefersReduced ? "auto" : "smooth" });
        });
        dotsWrap.appendChild(dot);
        dots.push(dot);
      });
    }

    var syncActive = function () {
      var idx = Math.round(track.scrollLeft / pageWidth());
      if (idx > cards.length - 1) { idx = cards.length - 1; }
      dots.forEach(function (d, i) { d.classList.toggle("is-active", i === idx); });
    };

    var raf = null;
    track.addEventListener("scroll", function () {
      if (raf) { return; }
      raf = requestAnimationFrame(function () {
        updateButtons();
        syncActive();
        raf = null;
      });
    }, { passive: true });

    window.addEventListener("resize", updateButtons);
    updateButtons();
  }

  /* ---------- footer newsletter validation ---------- */
  function initSignup() {
    var form = document.getElementById("signupForm");
    var note = document.getElementById("signupNote");
    var email = document.getElementById("email");
    if (!form || !note || !email) return;
    var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var value = email.value.trim();
      if (!re.test(value)) {
        note.textContent = "Please enter a valid email address.";
        email.focus();
        return;
      }
      note.textContent = "You're in! Weekly course picks are on the way.";
      form.reset();
    });
  }

  /* ---------- boot ---------- */
  function init() {
    initHeaderScroll();
    initMobileNav();
    initSmoothScroll();
    initSearch();
    initCourseFilter();
    initCounters();
    initReveal();
    initTestimonials();
    initSignup();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
