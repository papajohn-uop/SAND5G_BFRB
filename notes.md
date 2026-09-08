# SAND 5G BRFB

This is the Big Red Fine Button (BRFB) project to be used for the common UC for SAND5G.

## Components

### Frontend

- A simple frontend comprising a large red button.
- It will also contain a text field and/or a dropdown list with known vulnerabilities.
- After selecting a vulnerability and pressing the button, an API will be called to check for that vulnerability in SBOMs.

### Backend - PROD

In production, an API for Incident Response will be used.

### Backend - PoC

A backend server will be developed.

- Single endpoint receiving the CVE to be checked.
- It will return random results, including:
  - How many operators were checked (2-5)
  - How many SBOMs were checked per operator (10-30)
  - How many SBOMs per operator were vulnerable (5% chance for each SBOM)
