from flask import Flask, render_template, request, jsonify
from datetime import datetime
import re

app = Flask(__name__)

# Demo-only rules. This is NOT a bank-grade fraud detector and does not connect to UPI.
def assess_transaction(tx):
    score = 0
    reasons = []
    amount = float(tx.get("amount") or 0)
    new_payee = str(tx.get("new_payee", "no")).lower() in ("yes", "true", "1", "on")
    urgent = str(tx.get("urgent_request", "no")).lower() in ("yes", "true", "1", "on")
    collect = str(tx.get("collect_request", "no")).lower() in ("yes", "true", "1", "on")
    qr = str(tx.get("unknown_qr", "no")).lower() in ("yes", "true", "1", "on")
    unusual = str(tx.get("unusual_time", "no")).lower() in ("yes", "true", "1", "on")
    message = str(tx.get("message", ""))[:1000].lower()

    if amount >= 25000:
        score += 20; reasons.append("High-value transfer for this demo threshold")
    elif amount >= 10000:
        score += 10; reasons.append("Elevated transaction amount")
    if new_payee:
        score += 20; reasons.append("Recipient is new to the user")
    if urgent:
        score += 20; reasons.append("Urgency or pressure to act was reported")
    if collect:
        score += 25; reasons.append("Payment-collection request: verify whether money is being requested from you")
    if qr:
        score += 20; reasons.append("QR code or payment link is from an unverified source")
    if unusual:
        score += 10; reasons.append("Transaction time is unusual for the user")
    keywords = ["otp", "pin", "urgent", "refund", "kyc", "account blocked", "screen share", "remote access", "prize", "verify now"]
    hits = sorted(set(k for k in keywords if k in message))
    if hits:
        score += min(20, 5 * len(hits))
        reasons.append("Message contains pressure or credential-related terms: " + ", ".join(hits))

    score = min(score, 100)
    if score >= 60:
        level = "High"; color = "high"
        advice = "Pause before paying. Verify the recipient through an independently obtained official channel. Never share your UPI PIN or OTP."
    elif score >= 30:
        level = "Medium"; color = "medium"
        advice = "Double-check the recipient, amount, and request context. Contact the person or business using a known number."
    else:
        level = "Lower"; color = "low"
        advice = "No strong warning signals were entered, but this is not proof that the payment is safe. Review the details before confirming."
    if not reasons:
        reasons = ["No configured demo warning signals were detected."]
    return {"score": score, "level": level, "color": color, "reasons": reasons, "advice": advice,
            "disclaimer": "Educational prototype using user-entered signals; not connected to banks/UPI and not a guarantee of fraud or safety."}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/assess", methods=["POST"])
def assess():
    data = request.get_json(silent=True) or request.form.to_dict()
    try:
        result = assess_transaction(data)
        return jsonify(result)
    except (ValueError, TypeError):
        return jsonify({"error": "Please enter a valid transaction amount."}), 400

@app.route("/health")
def health():
    return jsonify({"status": "ok", "app": "ScamShield AI demo", "mode": "synthetic/manual input only"})

if __name__ == "__main__":
    app.run(debug=True)
