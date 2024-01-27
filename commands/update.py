import requests
import os
from datetime import datetime
startTime = datetime.now()

def download_html(url, path):
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        os.remove(path)
        print("removed old file")

        # Write the HTML content to a file
        with open(path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"HTML downloaded successfully and saved as {path}")
    else:
        print("Failed to download HTML")

html_urls=[
    {"url":"https://www.salisbury.edu/admissions/transfer-students/academic-requirements.aspx", "path":"../data/html/Academic Requirements For Transfer Applicants | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/transfer-students/admissions-requirements.aspx","path":"../data/html/Admissions Requirements For Transfer Applicants | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/admissions-team.aspx","path":"../data/html/Admissions Team | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/liberal-arts/for-students/student-grants.aspx","path":"../data/html/Announcement of Fulton Student Research Grants | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/ourca/conferences/susrc/","path":"../data/html/Annual Student Research Conference (SUSRC) | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/freshman-students/application-evaluation-criteria.aspx","path":"../data/html/Application Evaluation Criteria | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/freshman-students/","path":"../data/html/Applying for Freshman Students | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/transfer-students/","path":"../data/html/Applying for Transfer Students | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/transfer-students/articulation-agreements.aspx","path":"../data/html/Articulation Agreements | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/freshman-students/credit-by-exam.aspx","path":"../data/html/Credit by Exam (AP & IB) | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/transfer-students/credit-policies-artsys.aspx","path":"../data/html/Credit Policies:ARTSYS | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/enrollment-management/","path":"../data/html/Enrollment Management | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/transfer-students/transfer-faqs.aspx","path":"../data/html/FAQs for Transfer Applicants | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/freshman-students/freshman-faqs.aspx","path":"../data/html/Freshman Admissions FAQs | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/freshman-students/freshman-application.aspx","path":"../data/html/Freshman Application Process | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/graduate-admissions.aspx","path":"../data/html/Graduate Admissions | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/assistantships.aspx","path":"../data/html/Graduate Assistantships | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/graduate-council.aspx","path":"../data/html/Graduate Council | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/graduate-academic-policies-committee.aspx","path":"../data/html/Graduate Council Academic Policies Committee | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/graduate-curriculum-committee.aspx","path":"../data/html/Graduate Curriculum Committee | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/faculty.aspx","path":"../data/html/Graduate Faculty | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/rap.aspx","path":"../data/html/Graduate Research & Presentation Grant (RAP) | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/research.aspx","path":"../data/html/Graduate Research | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/scholarship.aspx","path":"../data/html/Graduate Scholarships | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/campus-governance/graduate-student-council/","path":"../data/html/Graduate Student Council | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/transfer-students/transfer-housing.aspx","path":"../data/html/Housing for Transfer Students | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/interdisciplinary-graduate-courses.aspx","path":"../data/html/Interdisciplinary Graduate Courses | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/staff.aspx","path":"../data/html/Office of Graduate Studies Staff | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/transfer-students/ptk-scholarship.aspx","path":"../data/html/Phi Theta Kappa (PTK) | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/sponsored-programs/pre-award/funding.aspx","path":"../data/html/Pre-Award | Find Funding | Salisbury University.html"},
    {"url":"https://en.wikipedia.org/wiki/Salisbury_University","path":"../data/html/Salisbury University - Wikipedia.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/scholarly-project.aspx","path":"../data/html/Scholarly Project Information | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/freshman-students/test-optional-policy.aspx","path":"../data/html/Test Optional Policy | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/transfer-students/transfer-portal.aspx","path":"../data/html/Transfer Portal | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/transfer-students/transfer-tuesday.aspx","path":"../data/html/Transfer Tuesdays | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/international-students/","path":"../data/html/International Admissions | Salisbury University.html"}
    {"url":"https://www.salisbury.edu/admissions/international-students/academics.aspx","path":"../data/html/Four Schools & Two Colleges – A Million Opportunities | Salisbury University.html"}
    {"url":"https://www.salisbury.edu/admissions/international-students/about-su.aspx","path":"../data/html/About Salisbury University | International Students.html"}
    {"url":"https://www.salisbury.edu/administration/academic-affairs/center-for-international-education/english-language-institute/","path":"../data/html/English Language Institute | Salisbury University.html"}
    {"url":"https://www.salisbury.edu/admissions/international-students/tuition-fees.aspx","path":"../data/html/International Admissions Tuition & Fees | Salisbury University.html"}
    {"url":"https://www.salisbury.edu/admissions/international-students/immigration.aspx","path":"../data/html/Immigration | Salisbury University.html"}
    {"url":"https://www.salisbury.edu/admissions/international-students/student-life.aspx","path":"../data/html/International Student Life | Salisbury University.html"}
    ]

for html_url in html_urls:
    download_html(html_url["url"],html_url["path"])

def download_pdf(url, path):
    response = requests.get(url)

    if response.status_code == 200:
        os.remove(path)
        print("removed old file")

        with open(path, 'wb') as pdf_file:
            pdf_file.write(response.content)
        print(f"PDF downloaded successfully and saved to: {path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")
        
pdf_urls=[
    {"url":"https://www.salisbury.edu/administration/administration-and-finance-offices/financial-services/accounts-receivable-cashiers-office/_files/course-fee-schedule-fy24.pdf","path":"../data/pdf/course-fee-Schedule-fy24.pdf"},
    {"url":"https://www.salisbury.edu/administration//academic-affairs/graduate-studies-and-research/_files/DeferralofApplication2015TEST.pdf","path":"../data/pdf/DeferralofApplication2015TEST.pdf"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/_files/GA-Credit-Waiver-9-25-14.pdf","path":"../data/pdf/GA-Credit-Waiver-9-25-14.pdf"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/_files/graduate-student-handbook/2023-2024/Graduate-Student-Handbook-2023-24.pdf","path":"../data/pdf/Graduate-Student-Handbook-2023-24.pdf"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/_files/Request-to-Transfer-to-Another-Program.pdf","path":"../data/pdf/Request-to-Transfer-to-Another-Program.pdf"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/_files/Scholarly-Project-Completion-defense-Submission-Form.pdf","path":"../data/pdf/Scholarly-Project-completion-defense-Submission-Form.pdf"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/_files/Scholarly-Project-Manual.pdf","path":"../data/pdf/Scholarly-Project-manual.pdf"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/graduate-studies-and-research/graduate-studies/_files/seven-year-waiver-2021.pdf","path":"../data/pdf/seven-year-waiver-2021.pdf"},
    {"url":"https://www.salisbury.edu/administration/administration-and-finance-offices/financial-services/accounts-receivable-cashiers-office/_files/tuition-fee-schedule-2023-2024.pdf","path":"../data/pdf/tuition-fee-schedule-2023-2024.pdf"}

]

for pdf_url in pdf_urls:
    download_pdf(pdf_url["url"],pdf_url["path"])

print(datetime.now() - startTime)
