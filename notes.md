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

## Architecture

The system will follow a simple request flow:

1. The user selects a vulnerability from the frontend and presses the red button.
2. The frontend sends the selected CVE to the backend API.
3. The backend evaluates the request and returns the relevant vulnerability data for the requested SBOM set.
4. In the PoC, the backend returns simulated results with randomized counts.
5. In production, the backend is replaced by the incident response API that provides the real data source.

### High-level components

- Frontend: User interface for selecting a CVE and triggering the check.
- Backend PoC: Lightweight service exposing one endpoint for testing and validation.
- Production backend: Real Incident Response API used in deployment.
- SBOM data source: Collection of SBOMs used to evaluate vulnerabilities across operators.
