# edabasic
An Exploratory Data Analysis basics project
# 📄 Mobile Phone Dataset (`mobiles1.csv`)

## 📁 Overview

This dataset contains specifications and metadata for a collection of mobile phones. It is suitable for exploratory data analysis (EDA), regression modeling, and machine learning projects involving price prediction, feature correlation, and consumer rating analysis.

---

## 🧩 Dataset Structure

Each row represents a unique mobile phone model and its associated features.

| Column Name | Description |
|-------------|-------------|
| `brand` | Manufacturer name (e.g., Samsung, Xiaomi, Apple) |
| `model` | Mobile model name or number |
| `price` | Price of the phone (in INR or other currency) |
| `ram` | RAM capacity in GB |
| `storage` | Internal storage capacity in GB |
| `processor` | Processor model/chipset (e.g., Snapdragon 888, A15 Bionic) |
| `battery` | Battery capacity in mAh |
| `display` | Display size or resolution |
| `rating` | Average user rating (typically out of 5, e.g., "4.3/5") |
| `camera` | Rear/front camera configuration (e.g., "64MP + 12MP") |
| `os` | Operating system (e.g., Android, iOS) |

> Note: Some columns may contain missing or inconsistent values (e.g., NaN, "4.5/5"). Preprocessing may be required before applying ML models.

---

## 🔍 Sample Use Cases

- 📊 Exploratory Data Analysis (EDA)
- 📈 Price Prediction using Regression
- 🤖 Classification or Clustering of phones by specs
- 📉 Feature Extraction & Text Cleaning
- 🧠 Correlation analysis between features like price, RAM, and ratings

---

## 🛠️ Requirements (for analysis)

- Python 3.8+
- pandas, numpy
- seaborn, matplotlib
- scikit-learn
