# ScamShield AI — UPI Scam Early-Warning Prototype

A hackathon-ready educational MVP for the **AI-Driven Scam Pattern Recognition** challenge.

## What it demonstrates
- User-entered/synthetic transaction context
- Transparent risk scoring with an explanation for each signal
- Actionable safety advice for a UPI-style payment scenario
- Safe and suspicious demo presets
- Flask API endpoint (`POST /assess`) and health endpoint (`GET /health`)
- Responsive browser UI

## Important boundaries
This is a **rules-based prototype**, not a trained ML model, bank-grade detector, or live UPI integration. It does not block transactions, store submitted scenarios, or prove that a transaction is fraudulent or safe. Do not enter real customer or financial information. The thresholds are illustrative and require validation before real-world use.

## Run locally (macOS / Windows)
1. Install Python 3.10 or newer.
2. Open this folder in VS Code.
3. Create and activate a virtual environment:

   macOS:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   Windows:
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000`.

## Demo walkthrough
1. Click **Load lower-risk example**, then **Assess warning signals**.
2. Click **Load scam example**, then assess again.
3. Explain how the score is made up of observable signals and why the UI advises verification instead of blocking payment.

## Architecture
Browser UI -> Flask `/assess` endpoint -> transparent feature/rule scoring -> risk band + reasons + safety advice -> user decides whether to pause/verify/report.

## Proposed 48-hour expansion
- Hours 0–6: define synthetic schema, scenarios, and evaluation plan.
- Hours 6–18: build UI and API.
- Hours 18–28: create balanced synthetic scenarios and baseline evaluation.
- Hours 28–38: test false positives/negatives and refine rules.
- Hours 38–44: privacy/threat review and usability test.
- Hours 44–48: record demo, finalize pitch PDF, rehearse.

## Future production path
Only after institutional approval: evaluate on authorised, minimised data; compare rules with calibrated ML models; measure precision/recall and false-alert rate; run shadow mode; require user confirmation/human review for high-impact actions; conduct security and privacy reviews before any payment-provider integration.

## AI/data disclosure
- Initial implementation and documentation prepared with AI assistance.
- No real bank/UPI/customer data used.
- The app uses hand-authored rules; no external trained model or dataset is bundled.
# scamshieldai
