Project: TournamentSchedule

Images
- Place event images under `data/image/<Month>/<day>/` (example: `data/image/Dec/13/1.jpeg`).
- You can add an `index.json` file inside the day folder listing filenames (e.g. `["1.jpg","2.jpg"]`). This is the preferred, fastest way for the gallery to discover images.

Quick commands
- Serve locally: `python3 -m http.server` (run from project root)
- Generate `index.json` files for all day folders: `python3 scripts/generate_index_json.py --root data/image --month Dec`

Gallery discovery order (used by client): `index.json` → directory listing parse → probe numbered files (1..20).

If you'd like I can also add image thumbnail generation or an admin UI to upload images.
