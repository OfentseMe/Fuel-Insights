@echo off
echo Installing required packages...
pip install -r requirements.txt

echo Starting Petrol Analytics Dashboard...
streamlit run app.py

pause