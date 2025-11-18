<p align="center">
  <img src="assets/logo.png" alt="Logo" width="140"/>
</p>

<h1 align="center">Outliers – BrainLytics Hackathon Power BI Dashboard</h1>

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

A professional Power BI dashboard analyzing **Sales**, **Profit**, and **Customer Behavior** using the BrainLytics dataset.  
This project was developed for a **Power BI Hackathon**, and includes Excel cleaning, Python-based data merging, custom Figma backgrounds, and business-focused insights.

---

## 📌 Project Overview

The goal of this project is to deliver a clean, interactive, and business-ready dashboard that provides:

- **Sales trends** across months and quarters  
- **Profit analysis** by category and time  
- **Customer insights** including VIP customers, customer types, and delivery preferences  
- **Category performance shifts** across quarters (special hackathon requirement)  
- **Regional and segment distributions**

All insights are documented in a dedicated analysis file.

📄 *Detailed insights:* `docs/Report_Insights_Analysis.md`

---

## 🗂 Project Structure

```md
BrainLytics-PowerBI-Dashboard/
│
├── assets/
│   ├── dashboard/
│   │   ├── 01_overview.png
│   │   ├── 02_sales_profit.png
│   │   └── 03_customer_insights.png
│   │
│   └── wallpapers/
│       ├── page 1.svg
│       ├── page 2.svg
│       └── page 3.svg
│
├── data/
│   ├── BrainLyticsData1.csv
│   ├── BrainLyticsData2.csv
│   └── BrainLytics_Final.csv
│
├── scripts/
│   └── python_append_code.py
│
├── docs/
│   ├── Main_Requirements.pdf
│   └── Report_Insights_Analysis.md
│
├── power-bi-hackthon.pbix
├── README.md
├── LICENSE
└── .gitignore
```


## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| **Power BI** | Data modeling, DAX, dashboards |
| **Python + Pandas** | Data cleaning and merging |
| **Excel** | Initial raw data cleaning |
| **Figma** | Dashboard backgrounds and UI assets |

---

## 🧹 Data Preparation Summary

### **Raw Data Issues Fixed**
- Mixed encodings  
- Inconsistent column names  
- Duplicate rows  
- Two separate source files needing merging  

### **Output**
- **Final cleaned dataset:** 9,997 rows  
- **Exported as:** `BrainLytics_Final.csv`  
- Full script available in: `scripts/python_append_code.py`

---

## 🎯 Hackathon Requirements

| Requirement | Status |
|------------|--------|
| 3+ KPIs | ✅ Completed |
| 4+ slicers | ✅ Completed |
| Sales analysis | ✅ Completed |
| Profit analysis | ✅ Completed |
| Customer insights | ✅ Completed |
| Top 10 customers | ✅ Completed |
| Quarterly category contribution visual | ✅ Completed |

---

## 🧠 Key Insights (Summary)

- **Digital Equipment** is the top-performing category across sales & profit  
- Profit margin is around **11%**, with mid-year softening  
- **Q4** shows the strongest seasonal performance  
- **West Zone** accounts for **32%** of total customers  
- **Regular Delivery** dominates with **59.7%** of all orders  
- VIP customers significantly impact total revenue  

📄 *For page-by-page details, see:*  
`docs/Report_Insights_Analysis.md`

---

## 📥 How to Use

### **Install Requirements**
- Power BI Desktop  
- Python 3+ (optional for reprocessing)

### **Clone the Repository**
```bash
git clone https://github.com/yourusername/BrainLytics-PowerBI-Dashboard.git
```
### **Open the Dashboard**
```bash
power-bi-hackthon.pbix
```

## 👤 About the Developer

**Reem Barqawi**  
📧 Email: reeembarqawi@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/reem-barqawi200
  

---

## 📄 License
This project is licensed under the **MIT License**.

---

<div align="center">

⭐ **If you found this project helpful, please give it a star!**  
Made with 💜 by **Reem Barqawi**

</div>
