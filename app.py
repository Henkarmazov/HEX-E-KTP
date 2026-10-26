import base64
from pathlib import Path

from flask import Flask, jsonify, request, Response, send_from_directory

from card import FIELDS, generate_card

ROOT = Path(__file__).resolve().parent
app = Flask(__name__)


@app.get("/")
def index():
    return send_from_directory(ROOT / "public", "index.html")


@app.post("/api/generate")
def generate():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify(error="Data tidak valid."), 400

    # Hasil hanya dibuat jika SEMUA data (termasuk foto) sudah diisi
    data, kosong = {}, []
    for k in FIELDS:
        v = str(payload.get(k, "")).strip()
        if not v:
            kosong.append(k)
        data[k] = v[:60]
    photo_b64 = str(payload.get("pas_photo", ""))
    if "," in photo_b64:
        photo_b64 = photo_b64.split(",", 1)[1]
    if not photo_b64:
        kosong.append("pas_photo")
    if kosong:
        return jsonify(error="Data belum lengkap.", kosong=kosong), 400

    try:
        png = generate_card(data, base64.b64decode(photo_b64))
    except Exception as e:
        return jsonify(error=f"Gagal membuat kartu: {e}"), 500

    return Response(png, mimetype="image/png", headers={"Cache-Control": "no-store"})
