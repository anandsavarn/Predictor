<div align="center">
<img src="https://capsule-render.vercel.app/api?type=venom&color=0:0a0a0a,25:003300,60:006600,100:00ff88&height=160&section=header&text=PREDICTOR.COM&fontSize=60&fontColor=ffffff&fontAlignY=40&desc=AI-Powered%20Stock%20Price%20Prediction%20Engine&descAlignY=62&descColor=00ff88&animation=scaleIn" width="100%"/>
</div>

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=15&pause=900&color=00FF88&center=true&vCenter=true&width=700&lines=LSTM+Neural+Network+%C2%B7+Real-Time+Stock+Forecasting;Flask+%2B+TensorFlow+%2B+yfinance+%C2%B7+Full-Stack+ML+App;Interactive+EMA+Charts+%C2%B7+CSV+Export+%C2%B7+Live+Deploy)](https://predictor-65n3.onrender.com)

<br/>

[![Live Demo](https://img.shields.io/badge/◈_LIVE_DEMO-00C896?style=for-the-badge&logo=render&logoColor=white)](https://predictor-65n3.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.11+-0a0a0a?style=for-the-badge&logo=python&logoColor=00ff88)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=00ff88)](https://flask.palletsprojects.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-0a0a0a?style=for-the-badge&logo=tensorflow&logoColor=00ff88)](https://tensorflow.org)
[![License](https://img.shields.io/badge/LICENSE-MIT-00ff88?style=for-the-badge&labelColor=0a0a0a)](#license)

</div>

---

## ◈ OVERVIEW

> Predictor.com is a **Flask-based web application** that forecasts stock prices using a **deep learning LSTM (Long Short-Term Memory)** neural network. It pulls live OHLCV data from Yahoo Finance, computes exponential moving averages, renders interactive prediction charts, and lets users export the underlying dataset — all from a clean browser UI.

```python
class Predictor:
    model     = "4-Layer LSTM · Keras/TensorFlow"
    data      = "Yahoo Finance · yfinance · any global ticker"
    indicators = ["EMA-20", "EMA-50", "EMA-100", "EMA-200"]
    output    = ["Predicted vs Actual chart", "CSV export", "Trend statistics"]
    deployed  = "https://predictor-65n3.onrender.com"
    status    = "🟢 LIVE"
```

---

## ◈ FEATURES

<table>
<tr>
<td width="50%" valign="top">

```
📈  STOCK PRICE PREDICTION
    Deep LSTM model forecasts
    next-step closing price

📊  INTERACTIVE EMA CHARTS
    20 · 50 · 100 · 200-day
    exponential moving averages
```

</td>
<td width="50%" valign="top">

```
📉  PREDICTION COMPARISON
    Actual vs Predicted price
    overlay visualization

💾  DATA EXPORT
    One-click CSV download
    of full historical dataset
```

</td>
</tr>
<tr>
<td width="50%" valign="top">

```
🔍  MULTI-TICKER SUPPORT
    Works with any symbol
    available on Yahoo Finance
```

</td>
<td width="50%" valign="top">

```
⚡  FAST INFERENCE
    Pre-trained .keras model
    loaded once at startup
```

</td>
</tr>
</table>

---

## ◈ TECH STACK

<div align="center">

**Backend & ML**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

**Data & Visualization**

![yfinance](https://img.shields.io/badge/yfinance-720E9E?style=flat-square&logo=yahoo&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white)

**Deployment**

![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=black)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=gunicorn&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=flat-square&logo=heroku&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white)

</div>

---

## ◈ PROJECT STRUCTURE

```
Predictor.com/
├── Templet/
│   ├── app.py                 # Flask application entry point
│   ├── index.html             # Web interface
│   ├── Predictor.com.ipynb    # Model training notebook
│   ├── stock_model.keras      # Trained LSTM model (generate locally)
│   └── powergrid.csv          # Sample dataset
│
├── Static/                    # Auto-generated charts & datasets
│   ├── ema_20_50.png
│   ├── ema_100_200.png
│   └── *.csv
│
├── requirements.txt           # Python dependencies
├── Procfile                   # Deployment process config
├── wsgi.py                    # WSGI entry point
└── DEPLOYMENT.md              # Full deployment guide
```

---

## ◈ QUICK START

### 1 · Clone & Install

```bash
git clone https://github.com/Anandsavran/Predictor.com.git
cd Predictor.com
pip install -r requirements.txt
```

### 2 · Train the Model

```bash
# Open and run all cells in:
Templet/Predictor.com.ipynb
```
This generates `stock_model.keras` inside the `Templet/` folder — required before the app can serve predictions.

### 3 · Run Locally

```bash
cd Templet
python app.py
```

Open **`http://localhost:5000`** in your browser.

---

## ◈ USAGE

| Step | Action |
|------|--------|
| `01` | Enter a stock ticker symbol — e.g. `AAPL`, `MSFT`, `POWERGRID.NS` |
| `02` | Click **Submit** |
| `03` | View generated EMA charts, prediction overlay, and stats |
| `04` | Download the dataset as CSV if needed |

---

## ◈ DEPLOYMENT

Full step-by-step instructions live in **[DEPLOYMENT.md](DEPLOYMENT.md)**, covering:

<div align="center">

![Render](https://img.shields.io/badge/Render-Recommended-46E3B7?style=flat-square&logo=render&logoColor=black)
![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=flat-square&logo=heroku&logoColor=white)
![PythonAnywhere](https://img.shields.io/badge/PythonAnywhere-1D9FD7?style=flat-square&logo=python&logoColor=white)

</div>

This app is currently live at **[predictor-65n3.onrender.com](https://predictor-65n3.onrender.com)**.

---

## ◈ REQUIREMENTS

```
✓  Python 3.11+
✓  Trained model file → stock_model.keras
✓  Active internet connection (live Yahoo Finance data)
```

---

## ◈ NOTES

> ⚠️ The model **must be trained** before the app can generate predictions.
> ⏳ First request after deploy may be slow — model loads into memory on cold start.
> 💡 Free hosting tiers (Render/Heroku free dynos) may hit memory limits with larger models — consider a paid tier for production use.

---

## ◈ LICENSE

This project is open source and available for educational purposes under the **MIT License**.

---

<div align="center">

```
"Turning raw market data into deployable intelligence."
```

📡 [anandsavarn@gmail.com](mailto:anandsavarn@gmail.com) &nbsp;·&nbsp; [github.com/Anandsavran](https://github.com/Anandsavran) &nbsp;·&nbsp; [Live Demo ↗](https://predictor-65n3.onrender.com)

<img src="https://capsule-render.vercel.app/api?type=venom&color=0:00ff88,50:003300,100:0a0a0a&height=120&section=footer" width="100%"/>

</div>
