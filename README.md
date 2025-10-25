# ⚡ Energy Consumption Data Cleaning

This project focuses on **data cleaning and preprocessing** of an **Energy Consumption dataset** using **Python (Pandas & NumPy)**.  
The goal is to transform raw data into a clean, structured format ready for analysis and visualization.

---

## 🧩 Project Overview
The dataset contains records of electricity usage across different **cities**, with columns such as:
- `Customer_ID`
- `City`
- `Units_Consumed`
- `Billing_Amount`
- `Date`
- `Meter_Type`, etc.

The raw data had several issues such as:
- Missing values  
- Duplicates  
- Inconsistent data types  
- Outliers and formatting errors  

This project focuses on identifying and fixing these issues to ensure data accuracy and reliability.

---

## 🧹 Steps Performed

### 1. Data Loading
- Imported the dataset using **pandas.read_csv()**.
- Inspected the first few rows using `df.head()`.

### 2. Handling Missing Values
- Checked missing data with `df.isnull().sum()`.
- Filled or dropped null values depending on context.

### 3. Removing Duplicates
- Used `df.drop_duplicates()` to remove repeated records.

### 4. Data Type Conversion
- Converted columns like `Date` to datetime format.  
- Changed numerical columns to appropriate data types.

### 5. Cleaning Text Columns
- Trimmed spaces and standardized capitalization in city names.  
- Removed unwanted characters or symbols.

### 6. Handling Outliers
- Identified extreme values in `Units_Consumed` and `Billing_Amount` using **IQR method** or **boxplots**.
- Treated or removed outliers as needed.

### 7. Derived Columns
- Created new columns such as **average consumption rate** or **cost per unit** using vectorized operations.

---

## 🧠 Libraries Used
- `pandas`  
- `numpy`  
- `matplotlib` (for quick visualization)  

---

## 📊 Results
- The cleaned dataset is free from missing or duplicate entries.
- Data is standardized and ready for analysis and visualization.
- Insights such as **average units consumed per city** and **billing distribution** can now be derived easily.

---

## 🚀 Next Steps
- Perform **Exploratory Data Analysis (EDA)**  
- Visualize patterns in consumption using **Matplotlib** or **Seaborn**  
- Apply **predictive models** for energy usage forecasting  

---

## 👨‍💻 Author
**Faiz Ali Khaskheli**  
📧 Email: faizhere477@gmail.com   
🔗 [GitHub Profile](https://github.com/Faizalik1)

---

