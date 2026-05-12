# Receipt AutoFill Web Form App
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
  ```python
  prompt = "Extract the following from the receipt:
    - merchant_name
    - date_time
    - currency: Convert symbols to codes (e.g., '$' to 'USD', 'RM' to 'MYR', 'S$' to 'SGD'). Use 'NA' if unknown.
    - amount: The total paid as a number."
  ```
* Automatically fill web form fields
* Save data to CSV

## Installation
1. Clone the repository
   ```bash
   git clone  https://github.com/liwei2463/Receipt-AutoFill-Form/
   cd "[file path to Receipt-AutoFill-Form]"
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Create .env file, Set environment variables
   ```env
   GEMINI_API_KEY=your_api_key
   ```

4. Run the app
   ```bash
   python app.py
   ```
