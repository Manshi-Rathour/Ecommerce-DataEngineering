# Ecommerce-DataEngineering  

## 🚀 Overview  
This project demonstrates the creation of an end-to-end, cloud-based big data pipeline leveraging industry-standard data engineering concepts. The pipeline integrates multiple data sources, processes, and transforms the data using Azure services, and prepares it for downstream tasks like AI/ML model training and data visualization.

> **Note:** This project focuses on preparing clean, structured, and enriched data for use in AI/ML workflows and visualization tools.  


## 🔧 Tools & Technologies  

### **Azure Services:**  
- **Azure Resource Group**: Centralized resource management.  
- **Azure Data Factory (ADF)**: Data orchestration and pipeline creation.  
- **Azure Data Lake Storage (ADLS)**: Secure and scalable storage.  
- **Azure Databricks**: Data transformation and analysis.  
- **Azure Synapse Analytics**: Advanced data querying and aggregation.  

### **Databases:**  
- **MySQL**: Relational database hosted via Filess.io.  
- **MongoDB**: NoSQL database hosted via Filess.io.  

### **Languages & Libraries:**  
- **Python**: For data ingestion and integration scripting.  


## 🔑 Prerequisites  
To run this project, you’ll need the following:  
1. An **Azure subscription** with access to:  
   - Azure Data Factory (ADF)  
   - Azure Data Lake Storage (ADLS)  
   - Azure Databricks  
   - Azure Synapse Analytics  
2. Accounts on **Filess.io** to set up cloud-based MySQL and MongoDB databases.  
3. A **Python environment** for running ingestion scripts.  


## 📂 Project Workflow  

### 1️⃣ **Resource Setup**  
- Created an **Azure Resource Group** to manage and organize all cloud resources.  
- Used **Filess.io** to provision:  
  - A **MySQL database** for structured data storage.  
  - A **MongoDB database** for unstructured data storage.  

### 2️⃣ **Data Ingestion**  
- Built **Python scripts** to ingest data into MySQL and MongoDB.  
- Configured **Azure Data Factory** to create pipelines for retrieving data from:  
  - GitHub (via HTTP).  
  - SQL Databases.  
- Stored raw data in **Azure Data Lake Storage (ADLS)** under the **Bronze Folder**.  

### 3️⃣ **Medallion Architecture Implementation**  
Designed the Data Lake using the **Medallion Architecture**, with three tiers:  
- **Bronze Folder**: Stores raw, unprocessed data directly from source systems.  
- **Silver Folder**: Contains cleaned and transformed data.  
- **Gold Folder**: Finalized, aggregated data ready for downstream applications.  

### 4️⃣ **Data Transformation**  
- Configured **Azure Databricks** with the following steps:  
  - Set up IAM permissions to access ADLS.  
  - Registered Databricks app for authentication with Azure.  
- Performed data transformations in Databricks notebooks:  
  - Loaded raw data from the **Bronze Folder**.  
  - Conducted **Exploratory Data Analysis (EDA)**, data cleaning, and joining datasets.  
  - Integrated enriched data from **MongoDB**.  
- Stored the processed data in the **Silver Folder**.  

### 5️⃣ **Data Aggregation & Preparation**  
- Utilized **Azure Synapse Analytics** to:  
  - Query data from the **Silver Folder**.  
  - Apply SQL queries for advanced data analysis and aggregation.  
- Saved the final aggregated data into the **Gold Folder**.  

### 6️⃣ **Use Cases**  
- The **Gold Data** is now ready for various downstream applications, such as:  
  - **AI/ML Model Training** by Data Scientists.  
  - **Data Visualization** in tools like Power BI, Tableau, and Fabric.  

## 🌟 Key Highlights  
- Integrated data from diverse sources, including:  
  - GitHub (HTTP-based ingestion).  
  - SQL databases.  
  - MongoDB (NoSQL).  
- Followed **industry-standard Medallion Architecture** for a structured and efficient data lake.  
- Built a robust data pipeline using a comprehensive suite of **Azure services**: ADF, ADLS, Databricks, and Synapse Analytics.  


## 📊 Data Readiness  
The **Gold Folder** contains:  
- Cleaned, transformed, and enriched data.  
- Structured datasets optimized for:  
  - Training AI/ML models.  
  - Visualization workflows (e.g., Power BI, Tableau).  
