from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PITCH_HTML = ROOT / "docs" / "pitch" / "index.html"


class PitchParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = []
        self.navs = []
        self.canvases = []
        self.anchors = []
        self.metas = []
        self._text_parts = []
        self._script_parts = []
        self._in_script = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "section":
            self.sections.append(attrs)
        elif tag == "nav":
            self.navs.append(attrs)
        elif tag == "canvas":
            self.canvases.append(attrs)
        elif tag == "a":
            self.anchors.append(attrs)
        elif tag == "meta":
            self.metas.append(attrs)
        elif tag == "script":
            self._in_script = True

    def handle_endtag(self, tag):
        if tag == "script":
            self._in_script = False

    def handle_data(self, data):
        if self._in_script:
            self._script_parts.append(data)
        else:
            self._text_parts.append(data)

    @property
    def text(self):
        return " ".join(" ".join(self._text_parts).split())

    @property
    def script(self):
        return "\n".join(self._script_parts)


def load_pitch():
    parser = PitchParser()
    parser.feed(PITCH_HTML.read_text(encoding="utf-8"))
    return parser


def class_names(attrs):
    return set((attrs.get("class") or "").split())


class PitchArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pitch = load_pitch()

    def test_sections_are_complete_and_ordered_for_generated_navigation(self):
        expected_ids = [
            "hero",
            "problem",
            "solution",
            "features",
            "architecture",
            "positioning",
            "cta",
        ]

        self.assertEqual([section.get("id") for section in self.pitch.sections], expected_ids)
        self.assertEqual(
            [section.get("data-section") for section in self.pitch.sections],
            [str(index) for index in range(len(expected_ids))],
        )

        nav = next(nav for nav in self.pitch.navs if nav.get("id") == "nav-dots")
        self.assertEqual(nav.get("aria-label"), "Section navigation")

        canvas = next(canvas for canvas in self.pitch.canvases if canvas.get("id") == "hero-canvas")
        self.assertEqual(canvas.get("aria-hidden"), "true")

    def test_positioning_section_preserves_organvm_pipeline_contract(self):
        text = self.pitch.text

        for expected in [
            "Part of ORGANVM",
            "Poiesis",
            "produces",
            "creative-artifact",
            "organvm-iii-ergon/peer-audited--behavioral-blockchain",
            "consumes",
            "theory",
            "organvm-i-theoria/styx-behavioral-economics-theory",
        ]:
            with self.subTest(expected=expected):
                self.assertIn(expected, text)

    def test_cta_links_to_canonical_repo_with_safe_new_tab_attributes(self):
        cta_links = [anchor for anchor in self.pitch.anchors if "cta-btn" in class_names(anchor)]

        self.assertEqual(len(cta_links), 1)
        cta = cta_links[0]
        self.assertEqual(
            cta.get("href"),
            "https://github.com/organvm-ii-poiesis/styx-behavioral-art",
        )
        self.assertEqual(cta.get("target"), "_blank")
        self.assertIn("noopener", (cta.get("rel") or "").split())

    def test_inline_script_keeps_reveals_nav_and_motion_guard_wired(self):
        script = self.pitch.script

        for expected in [
            "document.querySelectorAll('.card, .feature-card')",
            "document.querySelectorAll('section[data-section]')",
            "document.getElementById('nav-dots')",
            "document.createElement('a')",
            "a.href = '#' + s.id",
            "nav.appendChild(a)",
            "if (dots[idx]) dots[idx].classList.add('active')",
            "window.matchMedia('(prefers-reduced-motion: reduce)').matches",
            "if (prefersReduced) { return; }",
            "window.addEventListener('resize', resize)",
            "requestAnimationFrame(draw)",
        ]:
            with self.subTest(expected=expected):
                self.assertIn(expected, script)
