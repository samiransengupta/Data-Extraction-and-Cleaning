#  Data Extraction from Election Commission of India (ECI) Website and Cleaning

📌 **Priject Overview**

The Election Commission of India (ECI) publishes election results online before making structured Excel files available, causing delays in accessing crucial data. My client needed election data immediately after the result day for initial analysis. This project automates the extraction and delivering an analysis-ready dataset within 24 hours of result declaration.

🚨 **The Problem** 

-ECI releases structured election data in Excel format after a delay. 

-Intially , Results are available only on the website, requiring manual extraction. 

-My client needed the data immediately after the result day for early trend analysis.

⚡ **The Solution** 

I developed a web scraping solution to extract election results directly from the ECI website. After retrieving the raw data, I cleaned, structured, and validated it to ensure accuracy before delivering it in Excel format for seamless analysis.

🚧 **The Challenges & How I Solved Them** 
 
 1. Dynamic Website Handling
    - The ECI website auto-refreshes after a certain minutes, causing the script to break.
    - I used error handling and adaptive scraping techniques to stabilize data extraction.
    - I refined my approach through ChatGPT prompt engineering, leveraging it to debug issues efficiently.
 
 2. Data Cleaning & Validation
    - Loaded the raw dataset into Jupyter Notebook for cleaning and  transformation.
    - Performed data validation by cross-checking key metrics
        - Total votes polled
        - Seats won by each party
        - Vote share percentage
 
 **Ensured that the final dataset was accurate, structured, and analysis-ready.**

📊 **Business Impact**

✅Faster Insights – Client received clean, structured data within 24 hours of results.

✅Automation & Efficiency – Eliminated manual data extraction, saving time & effort while maintaining accuracy.

✅ Enhanced Decision-Making – Enabled early trend analysis.

🛠️ **Technical Approach**

Web Scraping: Used VS Code for development.

Data Cleaning & Validation: Processed in Jupyter Notebook using Pandas.

Output Format: Delivered in Excel for direct analysis.

ECI - https://www.eci.gov.in/

**Data Structure of raw excel file**

<img width="668" alt="image" src="https://github.com/user-attachments/assets/e6476c33-c044-46ba-80ef-176522e8545c" />

🎓 **Key Learnings** 

Advanced Web Scraping Techniques – Handling auto-refreshing pages dynamically. 

Prompt Engineering – Improved problem-solving efficiency using ChatGPT.

**All relevant files are available in this repository.**
