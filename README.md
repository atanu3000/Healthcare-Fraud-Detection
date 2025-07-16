<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Healthcare Provider Fraud Detection</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      line-height: 1.6;
      margin: 2rem;
      color: #333;
    }
    h1, h2 {
      color: #2c3e50;
    }
    ul {
      margin-left: 1.5rem;
    }
    .section {
      margin-bottom: 2rem;
    }
    code {
      background-color: #f4f4f4;
      padding: 2px 6px;
      border-radius: 4px;
    }
    .emoji {
      font-size: 1.2rem;
    }
  </style>
</head>
<body>

  <h1 class="emoji">🏥 Healthcare Provider Fraud Detection 🕵️‍♂️</h1>
  <p>A complete data analysis and feature engineering pipeline for detecting fraudulent healthcare providers using real-world insurance claim datasets.</p>

  <div class="section">
    <h2 class="emoji">🔍 Project Overview</h2>
    <p>This project aims to identify <strong>potential fraud</strong> among healthcare providers using medical claims data. Leveraging structured datasets, we integrate, clean, and transform raw information from multiple sources to prepare it for modeling.</p>
    <p><strong>Key Components:</strong></p>
    <ul>
      <li>Data cleaning & preprocessing</li>
      <li>Handling missing values</li>
      <li>Feature engineering</li>
      <li>Exploratory Data Analysis (EDA)</li>
      <li>Merging inpatient, outpatient, and beneficiary data</li>
      <li>Preparing data for machine learning models</li>
    </ul>
  </div>

  <div class="section">
    <h2 class="emoji">📁 Dataset Structure</h2>
    <p>The project uses the following datasets:</p>
    <ul>
      <li><code>Train.csv</code> & <code>Test.csv</code>: Core label data</li>
      <li><code>Train_Beneficiarydata.csv</code> / <code>Test_Beneficiarydata.csv</code>: Patient-level data</li>
      <li><code>Train_Inpatientdata.csv</code> / <code>Train_Outpatientdata.csv</code>: Medical claim details</li>
    </ul>
    <p>These datasets were merged and cleaned to form a robust base for fraud detection.</p>
  </div>

  <div class="section">
    <h2 class="emoji">🛠️ Technologies Used</h2>
    <ul>
      <li><strong>Python</strong> (Pandas, NumPy, Seaborn, Matplotlib)</li>
      <li><strong>Jupyter Notebook</strong></li>
      <li><strong>Power BI</strong> (for optional visualization)</li>
      <li><strong>SQL / DAX / Excel</strong> (supporting tools)</li>
    </ul>
  </div>

  <div class="section">
    <h2 class="emoji">🚀 Features & Work Done</h2>
    <ul>
      <li>✅ Merged and aligned multi-source datasets</li>
      <li>✅ Created new features for provider-level fraud analysis</li>
      <li>✅ Engineered time-based and code-based variables</li>
      <li>✅ Visualized fraud patterns and claim distribution</li>
      <li>✅ Prepared dataset for supervised learning</li>
    </ul>
  </div>

  <div class="section">
    <h2 class="emoji">📊 Visualization & Insights</h2>
    <ul>
      <li>Age group and gender patterns in fraud</li>
      <li>Frequency of diagnosis/procedure codes</li>
      <li>Hospital stay trends and anomalies</li>
    </ul>
    <p><em>All transformations were designed with modeling readiness and business interpretability in mind.</em></p>
  </div>

  <div class="section">
    <h2 class="emoji">📌 How to Run</h2>
    <ol>
      <li>Clone the repo</li>
      <li>Place the dataset files in the same directory</li>
      <li>Open <code>Recent_Merge_Train_Test.ipynb</code> in Jupyter</li>
      <li>Run each cell step-by-step</li>
    </ol>
  </div>

  <div class="section">
    <h2 class="emoji">💡 Future Scope</h2>
    <ul>
      <li>Model training using classification algorithms</li>
      <li>SHAP-based model interpretation</li>
      <li>Deployment via Flask or Streamlit</li>
    </ul>
  </div>

  <div class="section">
    <h2 class="emoji">📚 Author</h2>
    <p><strong>Ankit Ghosal</strong><br>MCA Candidate @ SVU (2026)<br>Passionate about data, business insights, ML and ethical AI.</p>

    <h3 class="emoji">🤝 Co-Contributor</h3>
    <p><strong>Atanu Paul</strong><br>MCA Candidate @ SVU (2026)<br>Passionate about data, web development, and business insights.</p>
  </div>

  <div class="section">
    <p>⭐️ <strong>Star this repository</strong> if you found it helpful!<br>
    📬 <strong>Feel free to contribute or open issues!</strong></p>
  </div>

</body>
</html>
