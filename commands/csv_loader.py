from langchain_community.document_loaders.csv_loader import CSVLoader

def get_csv_documents():
    csv_loader1 = CSVLoader(file_path='../data/csv/classes.csv',csv_args={
        'delimiter': ',',
        'quotechar': '"',
        'fieldnames': ["description","courseNumber","departmentCode","courseTitle","avg_gpa","A_rate","B_rate","C_rate","D_rate","F_rate","Withdraw_rate","total_enrollment"]
    })
    csv_loader2 = CSVLoader(file_path='../data/csv/ap.csv',csv_args={
        'delimiter': ',',
        'quotechar': '"',
        'fieldnames': ['AP course', 'minimum score on ap test', 'college credits awarded','coursed granted prior to fall 2024','courses grated after fall 2024']
    })
    csv_loader3 = CSVLoader(file_path='../data/csv/ib.csv',csv_args={
        'delimiter': ',',
        'quotechar': '"',
        'fieldnames': ['International Baccalaureate (IB)', 'credits granted', 'courses granted']
    })
    csv_loader4 = CSVLoader(file_path='../data/csv/professors.csv',csv_args={
        'delimiter': ',',
        'quotechar': '"',
        'fieldnames': ["firstName","lastName","avg_gpa","total_enrollment","Withdraw_rate","A_rate","B_rate","C_rate","D_rate","F_rate","courses_taught"
    ]
    })
    csv_loader5 = CSVLoader(file_path='../data/csv/costs.csv',csv_args={
        'delimiter': ',',
        'quotechar': '"',
        'fieldnames': ['Fee Type', 'Instate', 'out of state']
    })
    csv_loader6 = CSVLoader(file_path='../data/csv/total_cost.csv',csv_args={
        'delimiter': ',',
        'quotechar': '"',
        'fieldnames': ['Type of student', 'total costs']
    })
    csv_loader7 = CSVLoader(file_path='../data/csv/grad_costs.csv',csv_args={
        'delimiter': ',',
        'quotechar': '"',
        'fieldnames': ['Per credit hour fee', 'maryland residents','non-residents','Non-Residents (Regional Hagerstown)']
    })
    csv_loader8 = CSVLoader(file_path='../data/csv/student_budget.csv',csv_args={
        'delimiter': ',',
        'quotechar': '"',
        'fieldnames': ['Fee', 'maryland residents','non-residents','Non-Residents (Regional Hagerstown)']
    })
    csv_loader9 = CSVLoader(file_path='../data/csv/gened.csv',csv_args={
        'delimiter': '|',
        'quotechar': '"',
        'fieldnames': ['Gened Group', 'Category','Requirements']
    })

    csv_documents=[*csv_loader1.load(),
        *csv_loader2.load(),
        *csv_loader3.load(),
        *csv_loader4.load(),
        *csv_loader5.load(),
        *csv_loader6.load(),
        *csv_loader7.load(),
        *csv_loader8.load(),
        *csv_loader9.load()]
    return csv_documents