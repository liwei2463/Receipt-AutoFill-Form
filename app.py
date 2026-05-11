# %pip install google-generativeai -q
# %pip install flask -q
# %pip install flask_cors -q
import os, io, json, csv
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
from pydantic import BaseModel
import PIL.Image

# Define data structure
class ReceiptData(BaseModel):
  merchant_name: str
  date_time: str
  currency: str
  amount_paid: float

app = Flask(__name__)
CORS(app)
# Configure AI model
genai.configure(api_key="AIzaSyBXk_W8sA3yWMG4VzQJ1LNGf1nMQ2N6uNk") # Enter Gemini API key
client = genai.GenerativeModel(
  model_name="gemini-3-flash-preview",
  generation_config={
    "response_mime_type": "application/json",
    "response_schema": ReceiptData
  }
)

# First, load HTML Web UI
@app.route("/")
def home():
  return render_template("receipt-form.html")

# Extract receipt data from image
@app.route("/upload", methods=["POST"])
def extract_receipt():
  if "receiptFile" not in request.files:
    return jsonify({"error": "No file uploaded"}), 400
  
  file = request.files["receiptFile"]
  img = PIL.Image.open(file.stream) # Load receipt image
  # Craft prompt
  prompt = """ Extract the following from the receipt:
    - merchant_name
    - date_time
    - currency: Convert symbols to codes (e.g., '$' to 'USD', 'RM' to 'MYR', 'S$' to 'SGD').
    Use 'NA' if unknown.
    - amount: The total paid as a number.
    """
  # return jsonify({ "merchant_name": "Whole Foods Market", "date_time": "2026-05-11T12:30:00", "currency": "USD", "amount": 42.15 })
  response = client.generate_content([prompt, img]) # Generate content
  print(response.usage_metadata)
  response= json.loads(response.text)
  return jsonify({ # Output [JSON format]
    "merchant_name": response.get("merchant_name"),
    "date_time": response.get("date_time"),
    "currency": response.get("currency"),
    "amount": response.get("amount_paid")
  })

# Save receipt data in CSV
@app.route("/save", methods=["POST"])
def save():
  data = request.json
  with open("receipts-record.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
      data.get("merchant_name"),
      data.get("receipt_date"),
      data.get("currency"),
      data.get("amount")
    ])
  return {"status": "saved"}

if __name__ == "__main__":
  # use_reloader=False -> prevents Flask trying to kill the interactive session
  app.run(port=5000, debug=True, use_reloader=False)