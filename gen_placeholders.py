from PIL import Image, ImageDraw, ImageFont
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
FOREST = (15, 61, 46)
FOREST_DARK = (10, 42, 32)
GOLD = (194, 154, 66)
IVORY = (246, 243, 236)

def font(size):
    for path in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def make(path, w, h, label, sub=""):
    img = Image.new("RGB", (w, h), FOREST)
    d = ImageDraw.Draw(img)
    # diagonal texture
    step = max(24, w // 30)
    for x in range(-h, w, step):
        d.line([(x, 0), (x + h, h)], fill=FOREST_DARK, width=2)
    # gold corner frame
    m = min(w, h) * 0.045
    d.rectangle([m, m, w - m, h - m], outline=GOLD, width=2)
    f1 = font(int(min(w, h) * 0.09))
    f2 = font(int(min(w, h) * 0.045))
    bbox = d.textbbox((0, 0), label, font=f1)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((w - tw) / 2, (h - th) / 2 - (10 if sub else 0)), label, font=f1, fill=IVORY)
    if sub:
        bbox2 = d.textbbox((0, 0), sub, font=f2)
        tw2 = bbox2[2] - bbox2[0]
        d.text(((w - tw2) / 2, (h + th) / 2 + 8), sub, font=f2, fill=GOLD)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    img.save(full, quality=82)
    print("made", path)

make("img/hero/office-exterior.jpg", 1920, 1280, "M.A SALAWU & CO", "REPLACE WITH OFFICE / HERO PHOTOGRAPH")
make("img/general/office-interior.jpg", 1200, 1500, "OFFICE", "REPLACE WITH REAL PHOTOGRAPH")
make("img/general/og-cover.jpg", 1200, 630, "M.A SALAWU & CO", "BARRISTERS & SOLICITORS")

make("img/attorneys/founder-placeholder.jpg", 800, 1000, "M.A SALAWU", "FOUNDER PHOTO PLACEHOLDER")
for i in [2, 3, 4]:
    make(f"img/attorneys/placeholder-{i}.jpg", 800, 1000, "PHOTO", f"ATTORNEY {i} PLACEHOLDER")

article_labels = [
    "COMPLIANCE",
    "REAL ESTATE",
    "CONTRACTS",
    "TRADEMARKS",
    "EMPLOYMENT",
    "ARBITRATION",
]
for i, label in enumerate(article_labels, start=1):
    make(f"img/insights/article-{i}.jpg", 1000, 650, label, "ARTICLE IMAGE PLACEHOLDER")

print("ALL DONE")
