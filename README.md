# Internship Market Analyzer (Python)

A full-fledged Internship Market Analyzer that scrapes internships from [Internshala](https://internshala.com), stores the data in an SQLite database, and provides insightful visualizations in CSV and PDF format.

---

## Features

 Scrapes internships based on **user input**: job keyword and location  
 Filters **profile and location** suggestions with smart matching  
 Stores internship data in a local **SQLite database**  
 Converts internship data into **CSV** for further analysis  
 Generates **professional PDF reports** using `matplotlib`  
 Clear and **interactive CLI menu** for ease of use

---

## 📊 Visual Reports

Generated in `internships.pdf` or as individual PDFs:

-  **Top Hiring Companies** (Bar Chart)
-  **Top Hiring Locations** (Lollipop Chart)
-  **Internship Durations** (Line Chart)
-  **Stipend Range Analysis** (Step Plot)

---

##  Project Structure

  Job_Market_Analyzer/
    │
    ├── job.db                   ← SQLite Database
    ├── internships.pdf          ← Combined Visual Report
    ├── internshala_jobs.csv     ← Internship Data in CSV
    ├── test222.py               ← Main Script File
    ├── README.md                ← (You are here)
    └── requirements.txt         ← Python Dependencies

  ---

## ⚙️ Technologies Used

- **Python 3**
- `requests`, `bs4` (BeautifulSoup) → Web Scraping  
- `sqlite3` → Lightweight Local DB  
- `pandas` → Data Handling  
- `matplotlib` → Visualizations  
- `PdfPages` → Multi-page PDF Output  

---

## 🚀 How It Works

1. **Run the script** → Prompts you for job keyword & location  
2. **Scrapes multiple pages** from Internshala dynamically  
3. **Stores the data** into `job.db` using SQLite  
4. **Generates visuals** based on selected menu options  
5. **Exports** a CSV and/or PDF containing internship insights  

---

## 🧑‍💻 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/internship-market-analyzer.git
cd internship-market-analyzer
