# Simple frontend for SAND5G BRFB

This is a minimal static frontend using plain HTML, CSS, and JavaScript.

## Run locally

Open the file directly in a browser, or serve it with a simple local web server:

```bash
cd /home/ubuntu/papajohn/SAND5G/frontend
python3 -m http.server 8080
```

Then open:

- http://localhost:8080

The frontend sends requests to:

- http://localhost:8000/check-cve

Make sure the FastAPI backend is running first.
