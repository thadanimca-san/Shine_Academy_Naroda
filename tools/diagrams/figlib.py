"""Small drawing helper for textbook diagrams (Pillow only).

Figures are drawn in world units (like cm on graph paper) and saved as PNG.
Drawing happens at 3x size and is scaled down, which smooths the lines.
"""
import math
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SS = 3  # supersampling factor

BLACK, GREY, LIGHT = (30, 30, 30), (120, 120, 120), (200, 200, 200)
RED, BLUE, GREEN = (214, 48, 49), (9, 105, 218), (0, 150, 80)
ORANGE, PURPLE = (230, 126, 34), (142, 68, 173)
GLASS = (210, 232, 250)


class Fig:
    def __init__(self, xmin, xmax, ymin, ymax, width=1200, margin=40):
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.k = (width - 2 * margin) / (xmax - xmin)
        self.margin = margin
        self.w = width
        self.h = int(round((ymax - ymin) * self.k + 2 * margin))
        self.img = Image.new("RGB", (self.w * SS, self.h * SS), "white")
        self.d = ImageDraw.Draw(self.img)

    # ---- coordinates ----
    def px(self, p):
        x, y = p
        return ((self.margin + (x - self.xmin) * self.k) * SS, (self.margin + (self.ymax - y) * self.k) * SS)

    def _font(self, size, bold=False):
        return ImageFont.truetype(FONT_BOLD if bold else FONT, int(size * SS))

    # ---- primitives ----
    def line(self, p, q, color=BLACK, width=2.5, dash=None):
        a, b = self.px(p), self.px(q)
        if not dash:
            self.d.line([a, b], fill=color, width=int(width * SS))
            return
        on, off = dash[0] * SS, dash[1] * SS
        length = math.dist(a, b)
        if length == 0:
            return
        ux, uy = (b[0] - a[0]) / length, (b[1] - a[1]) / length
        s = 0.0
        while s < length:
            e = min(s + on, length)
            self.d.line([(a[0] + ux * s, a[1] + uy * s), (a[0] + ux * e, a[1] + uy * e)], fill=color, width=int(width * SS))
            s = e + off

    def polyline(self, pts, color=BLACK, width=2.5, dash=None):
        for p, q in zip(pts, pts[1:]):
            self.line(p, q, color, width, dash)

    def head(self, at, direction, color=BLACK, size=14):
        """Filled arrowhead with its tip at `at`, pointing along `direction` (world units)."""
        tip = self.px(at)
        dx, dy = direction[0], -direction[1]
        n = math.hypot(dx, dy) or 1
        ux, uy = dx / n, dy / n
        s = size * SS
        back = (tip[0] - ux * s, tip[1] - uy * s)
        left = (back[0] - uy * s * 0.45, back[1] + ux * s * 0.45)
        right = (back[0] + uy * s * 0.45, back[1] - ux * s * 0.45)
        self.d.polygon([tip, left, right], fill=color)

    def arrow(self, p, q, color=BLACK, width=2.5, dash=None, size=14):
        self.line(p, q, color, width, dash)
        self.head(q, (q[0] - p[0], q[1] - p[1]), color, size)

    def ray(self, p, q, color=RED, width=2.5, dash=None, at=0.55):
        """A light ray from p to q with an arrowhead part of the way along it."""
        self.line(p, q, color, width, dash)
        m = (p[0] + (q[0] - p[0]) * at, p[1] + (q[1] - p[1]) * at)
        self.head(m, (q[0] - p[0], q[1] - p[1]), color, 13)

    def text(self, p, s, size=22, color=BLACK, anchor="mm", bold=False, dx=0, dy=0):
        x, y = self.px(p)
        self.d.text((x + dx * SS, y + dy * SS), s, fill=color, font=self._font(size, bold), anchor=anchor)

    def dot(self, p, r=4, color=BLACK):
        x, y = self.px(p)
        r *= SS
        self.d.ellipse([x - r, y - r, x + r, y + r], fill=color)

    def circle(self, c, r, outline=BLACK, width=2.5, fill=None):
        x, y = self.px(c)
        r *= self.k * SS
        self.d.ellipse([x - r, y - r, x + r, y + r], outline=outline, width=int(width * SS), fill=fill)

    def ellipse(self, c, rx, ry, outline=BLACK, width=2.5, fill=None):
        x, y = self.px(c)
        rx, ry = rx * self.k * SS, ry * self.k * SS
        self.d.ellipse([x - rx, y - ry, x + rx, y + ry], outline=outline, width=int(width * SS), fill=fill)

    def arc(self, c, r, a0, a1, color=BLACK, width=2.5):
        """Arc of radius r about c from angle a0 to a1 (degrees, anticlockwise, world sense)."""
        x, y = self.px(c)
        rr = r * self.k * SS
        self.d.arc([x - rr, y - rr, x + rr, y + rr], -a1, -a0, fill=color, width=int(width * SS))

    def polygon(self, pts, fill=None, outline=BLACK, width=2.5):
        q = [self.px(p) for p in pts]
        self.d.polygon(q, fill=fill)
        if outline:
            self.d.line(q + [q[0]], fill=outline, width=int(width * SS), joint="curve")

    def rect(self, p, q, fill=None, outline=BLACK, width=2.5):
        self.polygon([p, (q[0], p[1]), q, (p[0], q[1])], fill, outline, width)

    def save(self, path):
        self.img.resize((self.w, self.h), Image.LANCZOS).save(path, optimize=True)


def lerp(p, q, t):
    return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)


def extend(p, q, x=None, t=None):
    """Point on line pq: at abscissa x, or at parameter t (0 = p, 1 = q)."""
    if x is not None:
        t = (x - p[0]) / (q[0] - p[0])
    return lerp(p, q, t)
