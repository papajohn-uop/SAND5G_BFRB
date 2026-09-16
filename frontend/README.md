# Simple frontend for SAND5G BRFB

This is a minimal static frontend using plain HTML, CSS, and JavaScript.

## Run locally

Open the file directly in a browser, or serve it with a simple local web server:

```bash
cd /home/ubuntu/papajohn/SAND5G/frontend
python3 -m http.server 8080
```

```bash
cd /home/ubuntu/papajohn/SAND5G/frontend
python3 server.py
curl "http://172.16.100.128:8080/set?value=SOME_ID"

```


Then open:

- http://localhost:8080

The frontend sends requests to:

- `config.js` defines the API URL used by the page.
- The default config points to `http://172.16.100.128:8000/check-cve`.
- Update `frontend/config.js` if your backend runs on a different host.

Make sure the FastAPI backend is running first.
