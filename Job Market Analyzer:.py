import requests as rq
from bs4 import BeautifulSoup as bs

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import sqlite3 as sq

import pandas as pd


class Job_Market_Analyzer():

    def __init__(self):
        self.job_dict = {
            "Title": [],
            "Company name": [],
            "location": [],
            "start_date": [],
            "Cost": []
        }
        self.job_data = []

    class Data_Collecation_Storing():

        @staticmethod
        def scrape_internshala():
            # Getting input like keyword and location;

            try:
                print("""
                        ╭───────────────────────────────────────╮
                        │  For all data, just press [Space] '_' │
                        ╰───────────────────────────────────────╯
                    """)

                profile_names = [
                    "NET Development", "3D Printing", "AI Agent Development", "Accounts", "Acting",
                    "Aerospace Engineering", "Agriculture and Food Engineering", "Analytics", "Android App Development",
                    "Angular-js Development", "Animation", "Architecture", "Artificial Intelligence AI",
                    "Audio Making/Editing", "Auditing", "Automobile Engineering", "Backend Development", "Bank",
                    "Bioinformatics", "Biology", "Biotechnology Engineering", "Blockchain Development", "Blogging",
                    "Brand Management", "Business Development", "Business/MBA", "CA Articleship", "CAD Design",
                    "Campus Ambassador", "Chartered Accountancy (CA)", "Cinematography", "Civil Engineering",
                    "Client Servicing", "Cloud Computing", "Commerce", "Company Secretary (CS)", "Computer Science",
                    "Computer Vision", "Content Writing", "Copywriting", "Creative Design", "Creative Writing",
                    "Culinary Arts", "Customer Service", "Cyber Security", "Data Entry", "Data Science",
                    "Database Building", "Design", "Digital Marketing", "E-commerce", "Editorial", "Electric Vehicle",
                    "Electrical Engineering", "Electronics Engineering", "Embedded Systems", "Engineering",
                    "Engineering Design", "Event Management", "Fashion Design", "Film Making", "Finance",
                    "Flutter Development", "Front End Development", "Full Stack Development", "Fundraising",
                    "General Management", "Graphic Design", "Hospitality", "Hotel Management",
                    "Human Resources (HR)", "Humanities", "Image Processing", "Industrial & Production Engineering",
                    "Industrial Design", "Information Technology", "Interior Design", "International",
                    "Internet of Things (IoT)", "Java Development", "Javascript Development", "Journalism", "Law",
                    "Legal Research", "MLOps Engineering", "Machine Learning", "Manufacturing Engineering",
                    "Market/Business Research", "Marketing", "Material Science", "Mechanical Engineering",
                    "Mechatronics", "Media", "Medicine", "Merchandise Design", "Mobile App Development",
                    "Motion Graphics", "NGO", "Natural Language Processing (NLP)", "Network Engineering",
                    "Node.js Development", "Operations", "PHP Development", "Photography",
                    "Political/Economics/Policy Research", "Product Management", "Programming", "Project Management",
                    "Prompt Engineering", "Proofreading", "Psychology", "Public Relations (PR)",
                    "Python-Django", "Quality Analyst", "Recruitment", "Ruby on Rails", "Sales", "Science",
                    "Search Engine Optimization (SEO)", "Social Media Marketing", "Social Work", "Software Development",
                    "Software Testing", "Sports", "Stock/Market Trading", "Strategy",
                    "Subject Matter Expert (SME)", "Supply Chain Management (SCM)", "Talent Acquisition", "Teaching",
                    "Telecalling", "Travel & Tourism", "UI/UX Design", "Video Making/Editing", "Videography",
                    "Volunteering", "Web Development", "Wordpress Development", "iOS App Development"
                ]

                locations = [
                    "Ahmedabad", "Alappuzha", "Amreli", "Amroha", "Anand", "Andhra Pradesh", "Annur", "Assam",
                    "Aurangabad", "Avinashi",
                    "Balotra", "Bangalore", "Bangarapet", "Barmer", "Belagavi", "Belpahar", "Bharuch", "Bharuch INA",
                    "Bhavnagar", "Bhilai",
                    "Bhilwara", "Bhopal", "Bhubaneswar", "Bihar", "Bikaner", "Bilimora", "Botad", "Brahmapur",
                    "Buldhana", "Chaibasa",
                    "Chandigarh", "Chennai", "Chhattisgarh", "Chikballapur", "Chikkaballapura", "Chinchwad", "Chittoor",
                    "Churu",
                    "Coimbatore", "Dahisar", "Dakshina Kannada", "Dehradun", "Delhi", "Dhanbad", "Dharmapuri",
                    "Dindigul", "Dungarpur",
                    "Durg", "Ernakulam", "Erode", "Etawah", "Faridabad", "Firozabad", "Gandhinagar", "Ganjam",
                    "Gautam Buddh Nagar",
                    "Gautam Buddha Nagar", "Ghaziabad", "Goa", "Goa Velha", "Gobichettipalayam", "Godhra", "Gokak",
                    "Gopichettipalayam",
                    "Greater Noida", "Gujarat", "Gurgaon", "Gurgaon Division", "Guwahati", "Hansi", "Hardoi",
                    "Haridwar", "Haryana",
                    "Hathras", "Himachal Pradesh", "Hisar", "Hosur", "Hyderabad", "Indore", "Jabalpur", "Jaipur",
                    "Jammu", "Jammu And Kashmir",
                    "Jhansi", "Jharkhand", "Jharsuguda", "Jodhpur", "Jowai", "Junagadh", "Kadi", "Kalol", "Kalyan",
                    "Kamrup", "Kandukur",
                    "Kannur", "Kanpur", "Kanpur Dehat", "Karimnagar", "Karnakuppe", "Karnal", "Karnataka", "Kayamkulam",
                    "Kerala",
                    "Khandwa", "Khordha", "Kochi", "Kodagu", "Kolar", "Kolkata", "Kollam", "Koramangala", "Kozhikode",
                    "Krishna",
                    "Krishnagiri", "Kurnool", "Lucknow", "Madhya Pradesh", "Madikeri", "Madurai", "Maharashtra",
                    "Malappuram", "Malkapur",
                    "Mandi", "Mangalore", "Margao", "Meerut", "Meghalaya", "Mehsana", "Mettupalayam", "Modinagar",
                    "Mohali", "Mumbai",
                    "Muradnagar", "Mysuru", "N T R", "Nagpur", "Namakkal", "Nashik", "Navi Mumbai", "Navsari",
                    "New Delhi", "Nilgiris",
                    "Noida", "North Goa", "Odisha", "Ooty", "Osmanabad", "Pakala", "Palani", "Palladam", "Panaji",
                    "Panchkula",
                    "Panchmahal", "Panipat", "Pashchim Champaran", "Patna", "Perundurai", "Pimpri-Chinchwad",
                    "Pollachi", "Pondicherry",
                    "Prakasam", "Punalur", "Pune", "Punjab", "Purnea", "Purnia", "Raigad", "Raigarh", "Raipur",
                    "Rajasthan", "Rajkot",
                    "Rajula", "Ranchi", "Ranga Reddy", "Rayachoti", "Renukoot", "Rewa", "Sahibzada Ajit Singh Nagar",
                    "Salem", "Sardarshahar",
                    "Secunderabad", "Shahabad", "Shimoga", "Sonbhadra", "Sonepat", "Sonipat", "Srikakulam", "Sulur",
                    "Surat", "Tamil Nadu",
                    "Tandur", "Telangana", "Thane", "Thanjavur", "Thiruvananthapuram", "Thrissur", "Tinsukia",
                    "Tiruchengode",
                    "Tirunelveli", "Tirupati", "Tiruppur", "Tiruvannamalai", "Tumakuru", "Tumkur", "Tundla", "Tura",
                    "Turbhe", "Udaipur",
                    "Udumalpet", "Udupi", "Una", "Uppal", "Uttar Pradesh", "Uttarakhand", "Vadodara", "Vagator",
                    "Varanasi", "Vasai",
                    "Vasai-Virar", "Vellore", "Vijayawada", "Vijayawada (Rural) Sub-District", "Visakhapatnam",
                    "Vishakhapatnam",
                    "West Bengal", "West Garo Hills", "West Jaintia Hills", "West Singhbhum"
                ]

                keyword = input("Enter your job keyword like (python) : ")
                Location = input("Enter your location like (city) : ")

                # Collect matches
                matched_profiles = [k for k in profile_names if keyword.lower() in k.lower()]
                matched_locations = [l for l in locations if Location.lower() in l.lower()]

                # Validate matches
                if not matched_profiles:
                    print(f"No matching profile found for '{keyword}'.")
                    return job_dict, job_data


                # Show profile options and ask user to choose
                print("\nSelect one of the matching profiles:")
                for i, prof in enumerate(matched_profiles, 1):
                    print(f"[{i}] {prof}")
                prof_choice = int(input("Enter choice number: "))
                Exact_key = matched_profiles[prof_choice - 1].replace(" ", "-").lower()

                # Show location options and ask user to choose
                print("\nSelect one of the matching locations:")
                for i, loc in enumerate(matched_locations, 1):
                    print(f"[{i}] {loc}")
                loc_choice = int(input("Enter choice number: "))
                Exact_loc = matched_locations[loc_choice - 1].replace(" ", "-").lower()

            except:
                print(" Invalid Input ! ('_') ,Enter Again")

            # Adding header;
            header = {"User-Agent": "Mozilla/5.0"}

            # creating a list to store data;
            job_data = []

            # creating a dict to store data;
            job_dict = {
                "Title": [],
                "Company name": [],
                "location": [],
                "start_date": [],
                "Cost": []
            }

            # loop for 1,2....;
            page = 1
            while True:
                # printing number of pages for reference
                print(f"Scraping page {page}...")

                # inserting the input into your;
                url = f'https://internshala.com/internships/{Exact_key}-internship-in-{Exact_loc}/page-{page}/'

                """
                f"https://internshala.com/internships/{Exact_key}/{Exact_loc}-jobs/page-{page}/"
                url =f"https://internshala.com/internships/{Exact_key}-internship-in-{Exact_loc}/page-{page}/"
                f"https://internshala.com/internships/{keyword}/{Location}-jobs/page-{page}/"
                https://internshala.com/internships/{artificial-intelligence-ai}-internship-in-{coimbatore}/
                https://internshala.com/internships/{information-technology}-internship-in-{bangalore}/page-{2}/
                https://internshala.com/internships/{keyword}-internship-in-{Location}/page-{page}/
                """
                try:
                    # Going into your URl;
                    request = rq.get(url, headers=header)  # Sending request
                    soup = bs(request.content, 'html.parser')  # HTML body
                except:
                    print("Network error")

                # Finding the data;
                Find = soup.find_all("div", class_="individual_internship")
                print(f"Found {len(Find)} internship listings")  # how huch job we founded

                if not Find:  # when page is not found the code should end
                    if page == 1:
                        print("No internships found. Returning empty data.")
                        return job_dict, job_data
                    print("\nWe have been collected all the datas")
                    break

                for i in Find:  # when page is found,it add the data
                    try:
                        # Finding title
                        title = i.find("a", class_="job-title-href").get_text(strip=True) if i.find("a",
                                                                                                    class_="job-title-href") else "N/A"
                        # Finding company name
                        c_name = i.find("p", class_="company-name").get_text(strip=True) if i.find("p",
                                                                                                   class_="company-name") else "N/A"
                        # Finding location
                        loc_div = i.find('div', class_="row-1-item locations")
                        loc = loc_div.find('a').get_text(strip=True) if loc_div and loc_div.find('a') else "N/A"
                        # Find duration (calendar icon row)
                        duration = "N/A"
                        calendar_row = i.find("i", class_="ic-16-calendar")
                        if calendar_row:
                            span = calendar_row.find_next_sibling("span")
                            if span:
                                duration = span.get_text(strip=True) if span else "N/A"
                        # Amount of job
                        amot = i.find('span', class_="stipend").get_text(strip=True) if i.find('span',
                                                                                               class_="stipend") else "N/A"

                        # opening the data into the list
                        job_data.append({
                            "title": title,
                            "company": c_name,
                            "location": loc,
                            "start_date": duration,
                            "cost": amot
                        })
                        # storing the data into list
                        job_dict["Title"].append(title)
                        job_dict["Company name"].append(c_name)
                        job_dict["location"].append(loc)
                        job_dict["start_date"].append(duration)
                        job_dict["Cost"].append(amot)
                    except:
                        continue

                page += 1  # adding the page to go to next page
            print(f"\nTotal internships collected: {len(job_data)}\n")  # print the total number of job

            return job_dict, job_data

            '''for job in job_data:
                print(job)'''

        @staticmethod
        def Sql(job_data, conn):

            # storing the data into database;

            # creating the cursor;
            cursor = conn.cursor()

            # creating the table;
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS job(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT,
                Company TEXT,
                Location TEXT,
                Start_date TEXT,
                Cost TEXT
            )
            ''')

            cursor.execute("DELETE FROM job")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='job'")

            # inserting value into it;
            for job in job_data:
                try:
                    cursor.execute('''
                        INSERT INTO job (Title,Company,Location,Start_date,Cost)
                                VALUES(?,?,?,?,?)''',
                                   (job['title'], job['company'], job['location'], job['start_date'], job['cost']))
                except Exception as e:
                    print(f"Network error {e}")

            print(f"Total jobs saved to database: {len(job_data)}")
            '''for job in job_data:
                print(job)'''

            conn.commit()
            cursor.close()
            conn.close()

    class Virtualization():

        """with PdfPages('intenships.pdf') as pdf:
            df=pd.DataFrame(job_dict)     # using the dictionary storage"""

        @staticmethod
        def Csv():
            # reconnecting to database;
            conn = sq.connect("job.db")  # database before we created
            # database into panda data frame;
            df = pd.read_sql("SELECT * FROM job", conn)
            df.to_csv("internshala_jobs.csv", index=False)
            print("CSV file 'internshala_jobs.csv' has been created successfully.")

        @staticmethod
        def Job_Hiring_Companies(df, pdf):
            # job hiring companies
            hiring_com = df["Company name"].value_counts()
            '''print(haring_com)'''  # Count to call hiring companies
            top_hiring_com = hiring_com.head(20)
            g_top_haring_com = top_hiring_com.plot(kind='bar', color='lightblue', figsize=(16, 6))
            plt.xlabel("Number of Hiring Companies")
            plt.ylabel('Name of company')
            plt.title("Top Hiring Companies")
            plt.xticks(rotation=20, ha='right')
            plt.tight_layout()
            pdf.savefig()
            plt.close()

        @staticmethod
        def Top_Hiring_Location(job_dict, pdf):
            df = pd.DataFrame(job_dict)
            inten_loc = df["location"].value_counts()
            top_inten_loc = inten_loc.head(10)

            # Stem plot (aka lollipop chart)
            fig, ax = plt.subplots(figsize=(16, 6))

            # X and Y
            locations = top_inten_loc.index
            counts = top_inten_loc.values
            x = range(len(locations))

            # Plot the stem (vertical lines)
            ax.vlines(x=x, ymin=0, ymax=counts, color='mediumturquoise', linewidth=2)

            # Plot the "lollipop" head
            ax.plot(x, counts, 'o', color='lightseagreen', markersize=10)

            # Labels and layout
            ax.set_xticks(x)
            ax.set_xticklabels(locations, rotation=30, ha='right')
            ax.set_ylabel("Number of Internships")
            ax.set_title("Top Hiring Locations - Stem Plot")
            plt.tight_layout()

            # Save to PDF
            pdf.savefig()
            plt.close()

        @staticmethod
        def Internship_Durations(job_dict, pdf):
            conn = sq.connect("job.db")  # reconnect to database
            cursor = conn.cursor()  # create a new cursor
            df = pd.DataFrame(job_dict)
            inten_dur = df["start_date"]
            inten_dur_list = list(inten_dur)
            inten_dur_list_low = [i.lower() for i in inten_dur_list]
            inten_dur_list_spac = [i.replace(' ', '') for i in inten_dur_list_low]
            list_df = pd.DataFrame(inten_dur_list_spac, columns=["Cleaned_Duration"])

            # chart ;

            dur_c = list_df.value_counts().reset_index()
            g_dur_c = dur_c.plot(kind='line', color='skyblue', markerfacecolor='deepskyblue', figsize=(16, 6),
                                 marker='o', linestyle='--', )
            plt.xlabel("Internship Duration")
            plt.ylabel("Number of Internships")
            plt.title("Internship Durations Distribution")
            plt.xticks(rotation=20, ha='left')
            plt.tight_layout()
            pdf.savefig()
            plt.close()

        @staticmethod
        def Stipend_Range_Analysis(job_dict, pdf):
            # Step 1: Load data from the dictionary
            df = pd.DataFrame(job_dict)

            # Step 2: Filter out unpaid internships
            paid_df = df[df["Cost"].str.lower() != "unpaid"].copy()

            # Step 3: Clean 'Cost' column and extract lower stipend value
            paid_df["Cost"] = (
                paid_df["Cost"]
                .str.replace("₹", "", regex=False)
                .str.replace(",", "", regex=False)
                .str.replace("/month", "", regex=False)
                .str.replace("lump sum", "", regex=False)
                .str.replace("competitive stipend", "", regex=False)
                .str.strip()
                .str.split("-")
                .str[0]
                .str.strip()
            )

            # Drop any remaining non-numeric entries
            paid_df = paid_df[paid_df["Cost"].str.isnumeric()]

            # Step 4: Convert to integer (safe after cleaning)
            paid_df["Cost"] = paid_df["Cost"].astype(int)

            # Step 5: Define stipend ranges
            bins = [0, 5000, 10000, 15000, 20000, float('inf')]
            labels = ["0-5000", "5001-10000", "10001-15000", "15001-20000", "20001+"]

            # Step 6: Categorize into ranges
            paid_df["Stipend_Range"] = pd.cut(paid_df["Cost"], bins=bins, labels=labels)

            # Step 7: Count internships per range
            stipend_counts = paid_df["Stipend_Range"].value_counts().sort_index()

            # Step 8: Plot stipend distribution using a step plot
            plt.figure(figsize=(16, 6))
            plt.step(stipend_counts.index, stipend_counts.values, where='mid', color='greenyellow',
                     markerfacecolor='yellowgreen', linewidth=1, marker='o')

            plt.title("Internship Stipend Range Distribution (Step Plot)")
            plt.xlabel("Stipend Range (INR)")
            plt.ylabel("Number of Internships")
            plt.grid(axis='y', linestyle='--', alpha=0.6)
            plt.tight_layout()
            pdf.savefig()
            plt.close()

        def All_dil(n):
            print("""
                    ╔══════════════════════════════════════════════════════════════════════╗
                    ║ 📘 INTERNSHIP MARKET ANALYZER - DOCUMENTATION                        ║
                    ╠══════════════════════════════════════════════════════════════════════╣
                    ║                                                                      ║
                    ║ 📂 CONTENTS:                                                         ║
                    ║ ─────────────────────────────────────────────────────────────────────║
                    ║ 1. Overview                                                          ║
                    ║ 2. Module Structure                                                  ║
                    ║ 3. Step-by-Step Execution Flow                                       ║
                    ║ 4. Database Details                                                  ║
                    ║ 5. Output Files                                                      ║
                    ║ 6. Ideal Use Cases                                                   ║
                    ║                                                                      ║
                    ╠══════════════════════════════════════════════════════════════════════╣
                    ║ 📌 1. OVERVIEW:                                                      ║
                    ║ ─────────────────────────────────────────────────────────────────────║
                    ║ This program scrapes internship listings from Internshala based on   ║
                    ║ user-defined keywords and locations, stores the data in a local      ║
                    ║ SQLite database, and generates visual analysis in both CSV and PDF   ║
                    ║ formats.                                                             ║
                    ║                                                                      ║
                    ╠══════════════════════════════════════════════════════════════════════╣
                    ║ 🏗️ 2. MODULE STRUCTURE:                                               ║
                    ║ ─────────────────────────────────────────────────────────────────────║
                    ║ Job_Market_Analyzer                                                  ║
                    ║ ├── Data_Collecation_Storing                                         ║
                    ║ │   ├── scrape_internshala()      → Scrapes internship listings      ║
                    ║ │   └── Sql(data, conn)           → Saves data into SQLite database  ║
                    ║ └── Virtualization                                                   ║
                    ║     ├── Csv()                     → Exports internships to CSV       ║
                    ║     ├── Job_Hiring_Companies()   → Bar chart (Top Hiring Companies)  ║
                    ║     ├── Top_Hiring_Location()    → Lollipop chart (Locations)        ║
                    ║     ├── Internship_Durations()   → Line chart (Durations)            ║
                    ║     ├── Stipend_Range_Analysis() → Step chart (Stipend Buckets)      ║
                    ║     └── Generate_All_Charts()    → Calls all visualizations          ║
                    ║                                                                      ║
                    ╠══════════════════════════════════════════════════════════════════════╣
                    ║ 📊 3. STEP-BY-STEP EXECUTION FLOW:                                   ║
                    ║ ─────────────────────────────────────────────────────────────────────║
                    ║ ┌──────┬────────────────────────────────────────────────────────────┐║
                    ║ │ Step │ Task                                                       │║
                    ║ ├──────┼────────────────────────────────────────────────────────────┤║
                    ║ │  1   │ Prompt user for job keyword and location                   │║
                    ║ │      │ → Clean input for URL format (e.g., 'data science'         │║
                    ║ │      │     → 'data-science')                                      │║
                    ║ ├──────┼────────────────────────────────────────────────────────────┤║
                    ║ │  2   │ Scrape internship listings from Internshala                │║
                    ║ │      │ → Navigate pages until no more jobs found                  │║
                    ║ │      │ → Extract: Title, Company, Location, Start Date, Stipend   │║
                    ║ ├──────┼────────────────────────────────────────────────────────────┤║
                    ║ │  3   │ Save internship data into SQLite database                  │║
                    ║ │      │ → Database: job.db                                         │║
                    ║ │      │ → Table: job (cleared before every new insert)             │║
                    ║ ├──────┼────────────────────────────────────────────────────────────┤║
                    ║ │  4   │ Display interactive menu to user                           │║
                    ║ │      │ → Options: CSV, individual charts, or all charts           │║
                    ║ ├──────┼────────────────────────────────────────────────────────────┤║
                    ║ │  5   │ Execute chosen operation                                   │║
                    ║ │      │ → CSV: Save internships to 'internshala_jobs.csv'          │║
                    ║ │      │ → Charts: Generate and save to separate PDF files          │║
                    ║ ├──────┼────────────────────────────────────────────────────────────┤║
                    ║ │  6   │ Output result files                                        │║
                    ║ │      │ → CSV: internship table                                    │║
                    ║ │      │ → PDF(s): One per chart or combined, based on user choice  │║
                    ║ └──────┴────────────────────────────────────────────────────────────┘║
                    ║                                                                      ║
                    ╠══════════════════════════════════════════════════════════════════════╣
                    ║ 🗃️ 4. DATABASE DETAILS:                                               ║
                    ║ ─────────────────────────────────────────────────────────────────────║
                    ║ • File   : job.db                                                    ║
                    ║ • Table  : job                                                       ║
                    ║ • Fields : ID (auto), Title, Company, Location, Start_date, Cost     ║
                    ║                                                                      ║
                    ╠══════════════════════════════════════════════════════════════════════╣
                    ║ 📁 5. OUTPUT FILES:                                                  ║
                    ║ ─────────────────────────────────────────────────────────────────────║
                    ║ • internshala_jobs.csv        → Internship data (CSV format)         ║
                    ║ • hiring_companies.pdf        → Bar chart of top companies           ║
                    ║ • hiring_locations.pdf        → Lollipop chart of locations          ║
                    ║ • internship_durations.pdf    → Line chart of durations              ║
                    ║ • stipend_ranges.pdf          → Step chart of stipend brackets       ║
                    ║ • internships.pdf             → All charts combined in one PDF       ║
                    ║                                                                      ║
                    ╠══════════════════════════════════════════════════════════════════════╣
                    ║ 🎯 6. IDEAL USE CASES:                                               ║
                    ║ ─────────────────────────────────────────────────────────────────────║
                    ║ ✔️ Resume/portfolio project for data science roles                    ║
                    ║ ✔️ Practicing real-world scraping + visualization                     ║
                    ║ ✔️ Understanding pipelines (Scraping → Database → Charts)             ║
                    ║ ✔️ Practicing Python libraries: Requests, BS4, Pandas, SQLite,        ║
                    ║     Matpotlib                                                        ║
                    ║                                                                      ║
                    ╚══════════════════════════════════════════════════════════════════════╝

""")


# ------------------------ MAIN EXECUTION ------------------------

if __name__ == "__main__":
    analyzer = Job_Market_Analyzer()

    # Step 1: Scrape from Internshala
    job_dict, job_data = Job_Market_Analyzer.Data_Collecation_Storing.scrape_internshala()

    # Step 2: Save to database
    conn = sq.connect("job.db")
    Job_Market_Analyzer.Data_Collecation_Storing.Sql(job_data, conn)

    # Step 3: Create DataFrame from dict for plotting
    df = pd.DataFrame(job_dict)

    # Step 4: Menu
    print("""
╔═════════════════════════════════════════════╗
║         Internship Market Insights          ║
╠═════════════════════════════════════════════╣
║   [0]            Read me                    ║
║   [1]    View Internship Table (CSV)        ║
║   [2]   Analyze Top Hiring Companies        ║
║   [3]   Analyze Top Hiring Locations        ║
║   [4]   Analyze Internship Durations        ║
║   [5]     Analyze Stipend Ranges            ║
║   [6]      Generate All Reports             ║ 
╚═════════════════════════════════════════════╝
         ╭─────────────────────────╮
         │    Your choice (1-6):   │
         ╰─────────────────────────╯
""")

    try:
        n = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 6.")
        exit()

    if n not in [0, 1, 2, 3, 4, 5, 6]:
        print("Invalid choice. Please enter a number between 1 and 6.")
        exit()

    if n == 0:
        Job_Market_Analyzer.Virtualization.All_dil()
    elif n == 1:
        Job_Market_Analyzer.Virtualization.Csv()
    else:
        with PdfPages("internships.pdf") as pdf:
            if n == 2:
                Job_Market_Analyzer.Virtualization.Job_Hiring_Companies(df, pdf)
            elif n == 3:
                Job_Market_Analyzer.Virtualization.Top_Hiring_Location(job_dict, pdf)
            elif n == 4:
                Job_Market_Analyzer.Virtualization.Internship_Durations(job_dict, pdf)
            elif n == 5:
                Job_Market_Analyzer.Virtualization.Stipend_Range_Analysis(job_dict, pdf)
            elif n == 6:
                Job_Market_Analyzer.Virtualization.Csv()
                Job_Market_Analyzer.Virtualization.Job_Hiring_Companies(df, pdf)
                Job_Market_Analyzer.Virtualization.Top_Hiring_Location(job_dict, pdf)
                Job_Market_Analyzer.Virtualization.Internship_Durations(job_dict, pdf)
                Job_Market_Analyzer.Virtualization.Stipend_Range_Analysis(job_dict, pdf)

        print("PDF 'internships.pdf' created with selected charts.")

# analytics
# bangalore
