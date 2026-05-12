# Receipt AutoFill Web App
A web application that extracts receipt image data using Gemini API and automatically fills a form.

## Demo
<img width="1917" height="968" alt="image" src="https://github.com/user-attachments/assets/4ce425b5-96fd-483d-8821-193969976d32" />

## Features
* Upload receipt image
* Extract data using Gemini API
  - Merchant Name
  - Date Time
  - Currency
  - Amount
* Automatically fill form fields
* Save data to CSV

## Installation
1. Clone the repository
  git clone  https://github.com/liwei2463/Receipt-AutoFill-Form/
  cd Receipt-AutoFill-Form
   
2. Install dependencies
  pip install -r requirements.txt

3. Set environment variables
  GEMINI_API_KEY=your_api_key

4. Run the app
  python app.py
