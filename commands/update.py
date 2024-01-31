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
    {"url":"https://www.salisbury.edu/admissions/international-students/","path":"../data/html/International Admissions | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/international-students/academics.aspx","path":"../data/html/Four Schools & Two Colleges – A Million Opportunities | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/international-students/about-su.aspx","path":"../data/html/About Salisbury University | International Students.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/center-for-international-education/english-language-institute/","path":"../data/html/English Language Institute | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/international-students/tuition-fees.aspx","path":"../data/html/International Admissions Tuition & Fees | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/international-students/immigration.aspx","path":"../data/html/Immigration | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/international-students/student-life.aspx","path":"../data/html/International Student Life | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/honors/", "path":"../data/html/Clark Honors College | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/honors/about-the-honors-college.aspx", "path":"../data/html/Honors Programs | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/honors/for-prospective-students.aspx", "path":"../data/html/Honors For Prospective Students | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/honors/current-honor-students/", "path":"../data/html/Honors For Current Students | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/honors/current-honor-students/apply-for-funding.aspx", "path":"../data/html/Honors Conferences and Research Funding | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/honors/current-honor-students/study-abroad-opportunities.aspx", "path":"../data/html/Honors Study Abroad Opportunities | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/honors/current-honor-students/honors-thesis-mentors.aspx", "path":"../data/html/Past Honors Thesis Mentors | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/honors/honors-application.aspx", "path":"../data/html/Honors Application - Online | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/honors/honors-housing.aspx", "path":"../data/html/Honors Housing | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/honors/honor-student-association.aspx", "path":"../data/html/Honors Student Association | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/honors/honors-student-ambassadors.aspx", "path":"../data/html/Honors Student Ambassadors | Salibsury University.html"},
    {"url":"https://www.salisbury.edu/explore-academics/study-abroad.aspx", "path":"../data/html/Study Abroad | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/financial-aid/", "path":"../data/html/Office of Financial Aid | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/financial-aid/fafsa-major-changes.aspx", "path":"../data/html/24-25 Major FAFSA Changes | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/financial-aid/how-to-apply.aspx", "path":"../data/html/How Do I Apply for Financial Aid? | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/financial-aid/types-of-aid/", "path":"../data/html/Types of Aid | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/financial-aid/types-of-aid/su-admission-scholarships.aspx", "path":"../data/html/SU Admission Scholarships | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/financial-aid/types-of-aid/grants.aspx", "path":"../data/html/Grants | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/financial-aid/types-of-aid/state-aid/", "path":"../data/html/State Aid | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/financial-aid/types-of-aid/loan/", "path":"../data/html/Loans | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/financial-aid/types-of-aid/federal-work-study.aspx", "path":"../data/html/Federal Work-Study | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/registrar/veterans/", "path":"../data/html/Veteran Services | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/financial-aid/cost-of-attendance/", "path":"../data/html/Cost of Attendance | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/discover-su/campus-map/building-info.aspx","path":"../data/html/Building Hours & Codes | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/experience-campus/athletics/","path":"../data/html/Athletics | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/experience-campus/athletics/campus-recreation/facilities/","path":"../data/html/Campus Recreation Facilities | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/experience-campus/athletics/discover-sammy.aspx","path":"../data/html/Sammy Sea Gull: Leader of Sea Gull Nation | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/student-affairs/student-health-services/","path":"../data/html/Student Health Services | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/coronavirus/","path":"../data/html/Coronavirus (COVID-19) Information | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/student-affairs/student-health-services/fees.aspx","path":"../data/html/Student Health Services Fees & Policies | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/student-affairs/counseling-center/","path":"../data/html/Counseling Center | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/advising-center/support-services.aspx","path":"../data/html/Additional Support Services | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/center-for-student-achievement/","path":"../data/html/Center For Student Achievement | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/police/","path":"../data/html/University Police | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/student-affairs/counseling-center/FAQs.aspx","path":"../data/html/FAQs | Counseling Center | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/student-affairs/disability-resource-center/","path":"../data/html/Disability Resource Center | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/student-affairs/disability-resource-center/requesting-accommodations.aspx","path":"../data/html/Requesting Academic & Housing Accommodations | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/discover-su/outcomes.aspx","path":"../data/html/Salisbury University Student Outcomes | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/discover-su/mission-values.aspx","path":"../data/html/Salisbury University Mission & Values | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/discover-su/campus-history/","path":"../data/html/Campus History | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/discover-su/campus-leadership.aspx","path":"../data/html/Campus Leadership | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/discover-su/offices-and-departments.aspx","path":"../data/html/Salisbury University Offices & Departments | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/discover-su/community-outreach/performing.aspx","path":"../data/html/Performing Ensembles: Experience the Arts | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/discover-su/community-outreach/galleries.aspx","path":"../data/html/Galleries & Museums | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/discover-su/community-outreach/institutes-and-centers.aspx","path":"../data/html/Institutes & Centers | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/events/","path":"../data/html/Events @ Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/registrar/","path":"../data/html/Office of the Registrar | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/registrar/registration.aspx","path":"../data/html/Registration | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/explore-academics/study-abroad.aspx","path":"../data/html/Study Abroad at Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/health-and-human-services/","path":"../data/html/College of Health & Human Services | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/business/","path":"../data/html/Perdue School of Business Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/liberal-arts/","path":"../data/html/Fulton School of Liberal Arts | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/education/","path":"../data/html/Education Major, Teaching college | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/academic-offices/honors/","path":"../data/html/Clarke Honors College at SU | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/explore-academics/research/undergraduate-student-research.aspx","path":"../data/html/Undergraduate Student Research | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/explore-academics/research/graduate-student-research.aspx","path":"../data/html/Graduate Student Research | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/explore-academics/research/faculty-research.aspx","path":"../data/html/Faculty Research | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/news/su-in-media.aspx","path":"../data/html/SU in the Media | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/news/","path":"../data/html/University News | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/discover-su/our-region.aspx","path":"../data/html/Our Region: Welcome to Salisbury! | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/libraries/hours.aspx","path":"../data/html/Library Hours | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/orientation/faq.aspx","path":"../data/html/FAQs | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/orientation/orientation-checklist.aspx","path":"../data/html/Orientation Checklist – Students Starting Fall 2023 | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/student-affairs/dining-services/meal-plans/dining-dollars.aspx","path":"../data/html/Dining Dollars | Salisbury Dining Services | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/admissions/admitted-students.aspx","path":"../data/html/For Admitted Students | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/administration/academic-affairs/university-writing-center/","path":"../data/html/University Writing Center | Salisbury University.html"},
    {"url":"https://www.salisbury.edu/explore-academics/internships.aspx","path":"../data/html/Internships for undergraduate students at Salisbury University.html"},

    ]
    #{"url":"", "path":"../data/html/| Salisbury University.html"}

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
    {"url":"https://www.salisbury.edu/administration/administration-and-finance-offices/financial-services/accounts-receivable-cashiers-office/_files/tuition-fee-schedule-2023-2024.pdf","path":"../data/pdf/tuition-fee-schedule-2023-2024.pdf"},
    {"url":"https://www.salisbury.edu/admissions/orientation/_docs/new-student-guide.pdf","path":"../data/pdf/new-student-guide.pdf"}
]

for pdf_url in pdf_urls:
    download_pdf(pdf_url["url"],pdf_url["path"])

print(datetime.now() - startTime)
