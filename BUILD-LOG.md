# Build Log — Smart Security & Energy Home

A running log of what was done, tested, and decided during the build.

---

## Session 1 — September 2, 2026

**Setup**
- Installed Python 3 and Flask
- Created GitHub repository (`smart-home-project`), set up GitHub Desktop
- Created initial `app.py` with fake sensor data (motion, dark, light_on, locked) to build and test the backend before wiring real hardware

**Backend**
- Built `/status` route (GET) — returns current sensor/lock state as JSON
- Built `/unlock` and `/lock` routes (POST) — control the door lock state
- Added an API key check (`X-API-Key` header) so routes reject unauthorized requests

**Testing**
- Confirmed `/status` without a key returns `{"error": "unauthorized"}` (401)
- Confirmed `/status` with the correct key returns the real sensor data
- Confirmed `/unlock` without a key is rejected; with the key, it succeeds and returns `{"locked": false}`

**Security note**
- Initial API key was left as a placeholder default; replaced with a unique key and committed the change separately (see commit "update API key")

**Next steps**
- Build the dashboard webpage (login + status display + unlock button)
- Move to real sensor wiring (PIR, photocell, servo) once dashboard works against fake data
