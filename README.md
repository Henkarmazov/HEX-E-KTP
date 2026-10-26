# Hex E-DEV · Card Programmer (Vercel Serverless)

Struktur:
- `public/index.html`  → landing page + form input + hasil (frontend)
- `app.py` + `card.py`  → serverless function (Flask + Pillow); `card.py` berisi logika & posisi teks yang sama dengan `create.py`
- `create.py`, `data.json` → file asli, tidak diubah (tetap bisa dipakai lokal)
- `font/`, `src/Template.png` → aset kartu

Deploy:
1. `npm i -g vercel`
2. `vercel` (di folder ini), lalu `vercel --prod`
