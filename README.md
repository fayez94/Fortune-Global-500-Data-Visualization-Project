# 📊 Fortune Global: A Tableau Journey

## 📝 Project Overview  
This project visualizes insights from the **Fortune Global 500 dataset**, highlighting key trends and financial performance of the world's top companies. 

## 📊 Interactive Dashboards  

### 🔹 Fortune Global 500: Key Insights on Top Companies  
[![Dashboard Preview](images/dashboard-1.png)](https://public.tableau.com/shared/HPK2HY9XF?:display_count=n&:origin=viz_share_link)  

### 🔹 Financial Performance Analysis: Revenue, Profit, Profit Margins  
[![Dashboard Preview](images/dashboard-2.png)](https://public.tableau.com/app/profile/mohammad.fayez.ullah/viz/FinancialPerformanceAnalysisRevenueProfitandProfitMargins/FinancialPerformanceAnalysisRevenueProfitandProfitMargins)  

🔗 **[Explore Full Dashboards on Tableau Public](https://public.tableau.com/app/profile/mohammad.fayez.ullah/viz/FortuneGlobal500KeyInsightsintoTopCompanies/FortuneGlobal500KeyInsightsintoTopCompanies)**  


## 📈 Key Insights from the Dashboards  

### 🔹 **1. The Most and Least Profitable Companies**
- **Highest Profit Margins:**  
  - **Apple, Oracle, L’Oréal, Iberdrola, Xiaomi**  
  - These companies maintain high-profit margins due to **strong brand positioning and efficient cost management**.
  
- **Lowest Profit Margins:**  
  - **Korea Gas, Metro, Walmart, Talanx, Samsung C&T**  
  - Some of these operate on **low-margin, high-volume models**, while others have high operational costs.

### 🔹 **2. Revenue vs. Profit Analysis**
- Companies with **high revenue do not always translate to high profit**.
- **Tech Giants** like **Apple, Microsoft, and Nvidia** maintain high profitability despite varied revenue levels.
- **Retail Giants** like **Walmart** generate **huge revenue** but operate on thin profit margins.


## 🔄 Project Workflow  
This project was completed in the following steps:  

1. **Data Scraping** 🕵️‍♂️  
   - Scraped the **Fortune Global 500 dataset** using **Selenium** to extract company details, revenue, profit, and other financial metrics.  

2. **Data Cleaning & Preprocessing** 🛠️  
   - Processed the scraped dataset using **Python** and libraries such as **Pandas** and **NumPy** to clean, structure, and prepare the data for visualization.  

3. **Data Visualization** 📊  
   - Used **Tableau** to create interactive dashboards with key insights from the cleaned dataset.  

4. **Publishing & Sharing** 🚀  
   - Uploaded dashboards to **Tableau Public** and pushed all files to **GitHub** for accessibility.  


## 📊 Dataset
- The dataset that is used in this project is the *[Fortune Global 500 dataset](https://fortune.com/ranking/global500/)*, which includes revenue, profit, and other key financial metrics of the top companies globally. It consists of the following columns:

```
Index(['Rank', 'Name', 'Revenue', 'Revenue in percentage', 'Profit',
       'Profit in percentage', 'Assets', 'Employees', 'Change in rank',
       'Years on global 500 list'],
      dtype='object')
```

- **Total Records:** 500
- **Main Features:** Revenue, Profit, Employee count, Rank changes, etc.

## 📂 Files in This Repository  
- `Fortune500_Company.py` - The Python script used for web scraping with Selenium.
- `visualization.ipynb` - The Python script for Data Processing, Transformation, Manipulation.
- `World_best_Company_details.csv` - The Dynamic dataset that  was scrapped by using selenium for tableau visualisation.
- `Cleaned_World_Best_Companies.csv` - The cleaned dataset after processing.
- `Fortune Global 500- Key insights on to top companies.twbx` - The Tableau Packaged Workbook containing dashboard of key insight on to top companies.
- `Financial Performance Analysis: Revenue, Profit, and Profit Margins.twbx` - The Tableau Packaged Workbook containing dashboard of Financial Performance Analysis.
- `README.md` - Documentation about the project.

## 🚀 Project Usage Guide

Follow these steps to set up and run the project on your local machine.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/fayez94/Fortune-Global-500-Data-Visualization-Project.git
cd Fortune-Global-500-Data-Visualization-Project
```

### 2️⃣ Create and Activate a Virtual Environment

#### 🔹 For Windows:
```bash
python -m venv myvenv
myvenv\Scripts\activate
```

#### 🔹 For macOS/Linux:
```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

### 3️⃣ Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Scraper Scripts

```bash
python Scraper.py
```

### 5️⃣ Deactivating the Virtual Environment
```bash
deactivate
```

## 📬 Contact
For any questions or suggestions, feel free to reach out!

📧 Email: mdfayezullah2624@gmail.com  
🐙 GitHub: [fayez94](https://github.com/fayez94)
 


