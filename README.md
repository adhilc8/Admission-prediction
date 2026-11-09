# KEAM College Admission Predictor

A Flask website that compares a student's KEAM rank with official engineering course, college, and category closing ranks.

## Dataset

`keam_2025_cutoffs.csv` contains 5,010 category-level cutoff records parsed from CEE Kerala's KEAM 2025 Engineering First Phase Allotment – Last Rank Table (Final), dated 21 July 2025. It covers 51 courses and 139 colleges. The source PDF is included in this folder.

Dataset columns: year, allotment_phase, course, college_code, college_name, college_type, category, closing_rank.

## Run in VS Code on Windows

1. Open this folder in VS Code. Confirm `app.py`, `keam_2025_cutoffs.csv`, and `requirements.txt` are in the same folder.
2. Choose **Terminal → New Terminal**.
3. If the terminal is not already in this folder, run:

   `cd "C:\Users\adhil\OneDrive\Desktop\projects\mini project"`

4. Install dependencies:

   `python -m pip install -r requirements.txt`

5. Start the website:

   `python app.py`

6. Open `http://127.0.0.1:5000` in your browser. Keep the terminal running while you use the website. Press Ctrl+C in the terminal to stop it.

If `python` is not recognized, use `py` instead.

## Prediction method and limitations

The site uses a direct historical cutoff comparison, not a trained machine-learning model. It displays a match when `student_rank <= closing_rank` for the selected category. This is appropriate because the dataset contains closing ranks, not individual admitted and rejected student records with labels for training. The result is a guide only; future cutoffs can change with seat availability, preferences, rank distribution, policy, and allotment phase. The included data is for the first phase and is not the final cutoff across all phases.

Category codes follow the CEE table (SM, EZ, MU, LA, DV, VK, BH, BX, KN, KU, SC, ST, EW, and FW where printed). Rows with no published rank are omitted.
