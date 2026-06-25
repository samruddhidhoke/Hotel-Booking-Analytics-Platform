# 🏨 Hotel Booking Analytics Platform

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![SQL Server](https://img.shields.io/badge/SQL%20Server-Database-red?logo=microsoftsqlserver)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green)

> **Built as part of my Data Analytics Portfolio to demonstrate end-to-end data analysis, SQL integration, dashboard development, and business intelligence reporting.**


An end-to-end Hotel Booking Analytics platform built using **Python, SQL Server, and Streamlit** to automate exploratory data analysis, data quality assessment, business insight generation, and reporting.

The platform helps analysts identify data quality issues, discover booking patterns, detect anomalies, and generate actionable business insights through an interactive multi-page dashboard.

---

## 📌 Problem Statement

Hotel booking datasets often contain missing values, duplicate records, outliers, and hidden relationships that make analysis time-consuming and error-prone.

This project automates the complete exploratory data analysis (EDA) workflow, enabling faster and more reliable business decision-making.

---

## 🚀 Key Features

* 📊 Automated Dataset Profiling
* ⚠️ Missing Value Analysis
* 🔢 Numerical Feature Analysis
* 🔤 Categorical Feature Analysis
* 📈 Distribution Analysis
* 📉 Correlation Analysis
* 📦 Outlier Detection (IQR Method)
* 🧠 Automated Business Insights
* 📥 CSV Report Downloads
* 🖥️ Interactive Multi-Page Streamlit Dashboard

---

## 🛠️ Technology Stack

| Category              | Technologies         |
| --------------------- | -------------------- |
| Programming Language  | Python               |
| Database              | SQL Server           |
| Data Processing       | Pandas, NumPy        |
| Data Visualization    | Plotly               |
| Dashboard             | Streamlit            |
| Database Connectivity | SQLAlchemy           |
| Development Tools     | VS Code, Git, GitHub |

---

## 📊 Dataset Information

| Attribute | Value                 |
| --------- | --------------------- |
| Dataset   | Hotel Bookings        |
| Records   | 119,390               |
| Features  | 32                    |
| Database  | SQL Server            |
| Domain    | Hospitality Analytics |


---

## 🏗️ System Architecture

The project follows a modular architecture where data flows through multiple processing layers:

**Hotel Booking Dataset → SQL Server → Database Connection Layer → Data Preprocessing → Analytics Engine → Streamlit Multi-Page Dashboard → Business Insights & CSV Reports**

> 📌 *Refer to the architecture diagram below for the complete workflow.*

![System Architecture](assets/architecture.png)

---

## ⚙️ Project Workflow

1. Import the hotel booking dataset into SQL Server.
2. Establish a database connection using SQLAlchemy.
3. Preprocess and validate the dataset.
4. Perform automated exploratory data analysis (EDA).
5. Detect missing values, correlations, and outliers.
6. Generate automated business insights.
7. Present results through an interactive multi-page Streamlit dashboard.
8. Export analytical reports in CSV format.


---

## 📂 Project Structure

```text
hotel-booking-analytics-platform/
│
├── assets/
│   ├── architecture.png
│   └── screenshots/
│
├── config/
├── data/
├── docs/
├── modules/
├── pages/
├── reports/
├── sql/
├── tests/
├── utils/
│
├── app.py
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore
```

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project

```bash
cd hotel-booking-analytics-platform
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 📸 Application Screenshots

### 🏠 Home Page

![Home Page](assets/screenshots/home_page.png)

---

### 📊 Dataset Overview

![Dataset Overview](assets/screenshots/dataset_overview.png)

---

### ⚠️ Missing Value Analysis

![Missing Value Analysis](assets/screenshots/missing_value_analysis.png)

---

### 📉 Correlation Analysis

![Correlation Analysis](assets/screenshots/correlation_analysis.png)

---

### 🧠 Business Insights

![Business Insights](assets/screenshots/business_insights.png)

---


## 💡 Key Learnings

This project strengthened my understanding of:

* Building modular Python applications
* SQL Server integration using SQLAlchemy
* Data preprocessing and exploratory data analysis (EDA)
* Interactive dashboard development with Streamlit
* Data visualization using Plotly
* Rule-based business insight generation
* Git and GitHub project management

---

## 🔮 Future Enhancements

* AI-powered insights using Large Language Models (LLMs)
* PDF and Excel report generation
* Interactive dashboard filters
* Predictive analytics for booking cancellation
* Docker containerization
* Cloud database integration (Azure/AWS)
* User authentication and role-based access
* Interactive KPI dashboard with real-time database updates

---

## 👨‍💻 Author

**Samruddhi Dhoke**

Computer Engineering Graduate | Aspiring Data Analyst & Data Scientist

* GitHub: https://github.com/samruddhidhoke
* LinkedIn: https://linkedin.com/in/samruddhi--dhoke

If you found this project useful, feel free to ⭐ this repository.
