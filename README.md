🏥 Healthcare Provider Fraud Detection 🕵️‍♂️
A complete data analysis and feature engineering pipeline for detecting fraudulent healthcare providers using real-world insurance claim datasets.

🔍 Project Overview
This project aims to identify potential fraud among healthcare providers using medical claims data. Leveraging structured datasets, we integrate, clean, and transform raw information from multiple sources to prepare it for modeling.

Key components:

Data cleaning & preprocessing

Handling missing values

Feature engineering

Exploratory Data Analysis (EDA)

Merging inpatient, outpatient, and beneficiary data

Preparing data for machine learning models

📁 Dataset Structure
The project uses the following datasets:

Train.csv & Test.csv: Core label data

Train_Beneficiarydata.csv / Test_Beneficiarydata.csv: Patient-level data

Train_Inpatientdata.csv / Train_Outpatientdata.csv: Medical claim details

These datasets were merged and cleaned to form a robust base for fraud detection.

🛠️ Technologies Used
Python (Pandas, NumPy, Seaborn, Matplotlib)

Jupyter Notebook

Power BI (for optional visualization)

SQL / DAX / Excel (supporting tools)

🚀 Features & Work Done
✅ Merged and aligned multi-source datasets

✅ Created new features for provider-level fraud analysis

✅ Engineered time-based and code-based variables

✅ Visualized fraud patterns and claim distribution

✅ Prepared dataset for supervised learning

📊 Visualization & Insights
Age group and gender patterns in fraud

Frequency of diagnosis/procedure codes

Hospital stay trends and anomalies

All transformations were designed with modeling readiness and business interpretability in mind.

📌 How to Run
Clone the repo

Place the dataset files in the same directory

Open Recent_Merge_Train_Test.ipynb in Jupyter

Run each cell step-by-step

💡 Future Scope
Model training using classification algorithms

SHAP-based model interpretation

Deployment via Flask or Streamlit

📚 Author
Ankit Ghosal
MCA Candidate @ SVU (2026) 
Passionate about data, business insights, ML and ethical AI.

📚 Co-Contributer:
Atanu Paul
MCA Candidate @ SVU (2026) 
Passionate about data, Web Development, business insights.

⭐️ Star this repository if you found it helpful!
📬 Feel free to contribute or open issues!


