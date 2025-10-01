# 📊 CORD-19 Research Metadata Explorer

This project analyzes the **CORD-19 research metadata dataset** (COVID-19 Open Research Dataset Challenge) and provides an interactive dashboard using **Streamlit**.  
It focuses on exploring research papers, their publication trends, and journal distributions.

---

## 🎯 Objectives
- Load and clean the CORD-19 metadata dataset.
- Perform basic analysis (papers per year, top journals, keyword frequency).
- Create visualizations using **Matplotlib** and **Seaborn**.
- Build an interactive web app using **Streamlit**.

---

## 📂 Dataset
We use the **`metadata.csv`** file from the [CORD-19 Kaggle dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).  

Key columns:
- `title` – Paper title  
- `abstract` – Abstract of the paper  
- `publish_time` – Publication date  
- `authors` – Authors of the paper  
- `journal` – Journal name  

> ⚠️ Note: The full dataset is very large. You can use a smaller sample for testing.

---

## ⚙️ Installation
Clone this repo and install dependencies:

```bash
git clone https://github.com/your-username/Frameworks_Assignment.git
cd Frameworks_Assignment
pip install -r requirements.txt
