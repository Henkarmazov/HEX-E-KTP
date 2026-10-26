from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import base64
import io
import json

# Root project
ROOT = Path(__file__).resolve().parent

FIELDS = [
    "ids", "nama", "bio", "jenis_kelamin", "hobi", "html", "css", "js",
    "gol_darah", "portfolio", "bahasa_favorit", "status", "project_fav",
    "tujuan", "dibuat",
]


def generate_card(data, photo_bytes):
    """Logika sama persis dengan create.py (posisi teks tidak diubah).
    Bedanya hanya: data dari request, foto dari upload, hasil dikembalikan sebagai bytes."""

    # font size list
    size = [25, 32, 16, 40]

    # open template
    tmp = Image.open(ROOT / "src" / "Template.png")

    # open second image for pas photo
    pas_photo = Image.open(io.BytesIO(photo_bytes)).convert("RGB")

    # Font list
    font = [str(ROOT / "font/Arrial.ttf"), str(ROOT / "font/Sign.ttf"), str(ROOT / "font/Ocr.ttf")]

    fprov = ImageFont.truetype(font[0], size[0])

    fnik = ImageFont.truetype(font[2], size[1])

    fdata = ImageFont.truetype(font[0], size[2])
    # Font for signature
    fsign = ImageFont.truetype(font[1], size[3])

    # Create condition if photo size not same 432
    if pas_photo.size[0] != 432:
        croped = pas_photo.crop((0, 0, 432, 450))
        csize = croped.resize((round(pas_photo.size[0] * 0.4), round(pas_photo.size[1] * 0.4)))
        tmp.paste(csize, (520, 140))
    else:
        csize = pas_photo.resize((round(pas_photo.size[0] * 0.4), round(pas_photo.size[1] * 0.4)))
        tmp.paste(csize, (520, 140))

    # sign
    s = data["nama"].split()
    sign = s[0]
    print("[XXX]GENERATE CARD PROGAMMER SUCCESS")
    print(data)

    # Draw in Image

    write = ImageDraw.Draw(tmp)

    write.text((380, 45), f"IDS : {data['ids']}", fill="black", font=fprov, anchor="ms")
    write.text((380, 70), f"{data['nama'].upper()}", fill="black", font=fprov, anchor="ms")

    write.text((170, 105), data["bio"], fill="black", font=fnik, anchor="lt")
    write.text((190, 145), data["jenis_kelamin"].upper(), fill="black", font=fdata, anchor="lt")
    write.text((190, 168), data["hobi"].upper(), fill="black", font=fdata, anchor="lt")
    write.text((190, 191), data["html"].upper(), fill="black", font=fdata, anchor="lt")
    write.text((463, 190), data["css"].upper(), fill="black", font=fdata, anchor="lt")
    write.text((190, 212), data["js"].upper(), fill="black", font=fdata, anchor="lt")
    write.text((190, 234), data["gol_darah"].upper(), fill="black", font=fdata, anchor="lt")
    write.text((190, 257), data["portfolio"].upper(), fill="black", font=fdata, anchor="lt")
    write.text((190, 279), data["bahasa_favorit"].upper(), fill="black", font=fdata, anchor="lt")
    write.text((190, 300), data["status"].upper(), fill="black", font=fdata, anchor="lt")
    write.text((190, 323), data["project_fav"].upper(), fill="black", font=fdata, anchor="lt")
    write.text((190, 346), data["tujuan"].upper(), fill="black", font=fdata, anchor="lt")

    write.text((553, 340), data["nama"].upper(), fill="black", font=fdata, anchor="lt")
    write.text((570, 360), data["dibuat"], fill="black", font=fdata, anchor="lt")
    write.text((540, 395), sign, fill="black", font=fsign, anchor="lt")

    out = io.BytesIO()
    tmp.save(out, format="PNG")
    return out.getvalue()
