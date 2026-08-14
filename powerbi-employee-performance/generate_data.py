"""
Generates a synthetic employee performance dataset modeled on the
schema of the IBM HR Analytics Employee Attrition & Performance
dataset (https://www.kaggle.com/rhuebner/human-resources-data-set).

Kaggle requires authenticated download, which isn't reachable from
this environment, so this script builds a dataset with the same
column structure and realistic, non-random relationships:
- Attrition is driven by job satisfaction, overtime, work-life
  balance, income, and travel frequency (not pure noise)
- Performance rating is driven by satisfaction, involvement,
  training frequency, and time since last promotion
- Attrition rate calibrated to ~18-22%, in line with published
  real-world HR attrition benchmarks

Swap in the real Kaggle CSV and every downstream query/measure
works unchanged, provided column names match.
"""
import numpy as np, pandas as pd

rng = np.random.default_rng(21)
n = 800

departments = ['Sales','R&D','HR','Finance','Operations','Marketing','IT','Customer Support']
dept_weights = [0.22,0.20,0.06,0.10,0.14,0.10,0.12,0.06]
job_roles = {
    'Sales':['Sales Executive','Sales Manager','Account Manager'],
    'R&D':['Research Scientist','Lab Technician','R&D Manager'],
    'HR':['HR Specialist','HR Manager','Recruiter'],
    'Finance':['Financial Analyst','Accountant','Finance Manager'],
    'Operations':['Operations Analyst','Ops Manager','Supply Chain Coordinator'],
    'Marketing':['Marketing Specialist','Marketing Manager','Brand Manager'],
    'IT':['Software Engineer','IT Support','IT Manager'],
    'Customer Support':['Support Representative','Support Team Lead']
}
education_fields = ['Life Sciences','Medical','Marketing','Technical Degree','Business','Human Resources','Other']

dept = rng.choice(departments, size=n, p=dept_weights)
role = [rng.choice(job_roles[d]) for d in dept]

age = rng.integers(21,60,n)
gender = rng.choice(['Male','Female'], size=n, p=[0.6,0.4])
marital = rng.choice(['Single','Married','Divorced'], size=n, p=[0.32,0.48,0.20])
education = rng.integers(1,6,n)  # 1=Below College ... 5=Doctor
education_field = rng.choice(education_fields, size=n)

years_at_company = np.clip(rng.integers(0,25,n) - (age.max()-age)//4, 0, 25).clip(min=0)
years_at_company = np.minimum(years_at_company, age-18)
years_in_role = np.minimum(years_at_company, rng.integers(0,12,n))
years_since_promo = np.minimum(years_in_role, rng.integers(0,8,n))
total_working_years = np.clip(years_at_company + rng.integers(0,10,n), years_at_company, 40)

monthly_income = np.zeros(n)
dept_base = {'Sales':5200,'R&D':6100,'HR':4600,'Finance':5800,'Operations':4900,
             'Marketing':5300,'IT':6300,'Customer Support':4200}
for i in range(n):
    base = dept_base[dept[i]]
    seniority_mult = 1 + years_at_company[i]*0.035
    monthly_income[i] = round(base * seniority_mult * rng.uniform(0.85,1.2), 0)

job_satisfaction = rng.integers(1,5,n)             # 1-4 scale (IBM convention)
env_satisfaction = rng.integers(1,5,n)
worklife_balance = rng.integers(1,5,n)
job_involvement = rng.integers(1,5,n)
relationship_satisfaction = rng.integers(1,5,n)

overtime = rng.choice(['Yes','No'], size=n, p=[0.28,0.72])
business_travel = rng.choice(['Non-Travel','Travel_Rarely','Travel_Frequently'], size=n, p=[0.2,0.6,0.2])
distance_from_home = rng.integers(1,30,n)
training_times = rng.integers(0,7,n)

# Performance rating driven by satisfaction/involvement/training/promotion recency
perf_score = (
    0.35*job_satisfaction + 0.25*job_involvement + 0.15*(training_times/6*4) +
    0.15*(4 - np.clip(years_since_promo,0,4)) + 0.10*env_satisfaction + rng.normal(0,0.6,n)
)
performance_rating = np.clip(
    np.round(1 + (perf_score - perf_score.min())/(perf_score.max()-perf_score.min())*3), 1, 4
).astype(int)

# Attrition driven by satisfaction/overtime/income/travel/tenure, calibrated to ~20% base rate
attr_logit = (
    1.41
    -0.35*job_satisfaction - 0.30*worklife_balance - 0.20*env_satisfaction
    + 0.55*(overtime=='Yes') - 0.00012*monthly_income
    + 0.30*(business_travel=='Travel_Frequently') - 0.06*years_at_company
    + rng.normal(0,0.5,n)
)
attr_prob = 1/(1+np.exp(-attr_logit))
attrition = rng.binomial(1, attr_prob)
attrition_lbl = np.where(attrition==1,'Yes','No')

employee_id = [f'E{1000+i}' for i in range(n)]

df = pd.DataFrame({
    'EmployeeID': employee_id, 'Age': age, 'Gender': gender, 'MaritalStatus': marital,
    'Department': dept, 'JobRole': role, 'Education': education, 'EducationField': education_field,
    'BusinessTravel': business_travel, 'DistanceFromHome': distance_from_home,
    'MonthlyIncome': monthly_income.astype(int), 'YearsAtCompany': years_at_company,
    'YearsInCurrentRole': years_in_role, 'YearsSinceLastPromotion': years_since_promo,
    'TotalWorkingYears': total_working_years, 'TrainingTimesLastYear': training_times,
    'JobSatisfaction': job_satisfaction, 'EnvironmentSatisfaction': env_satisfaction,
    'WorkLifeBalance': worklife_balance, 'JobInvolvement': job_involvement,
    'RelationshipSatisfaction': relationship_satisfaction, 'OverTime': overtime,
    'PerformanceRating': performance_rating, 'Attrition': attrition_lbl,
})

df.to_csv('employee_performance.csv', index=False)
print(f"Generated {len(df)} employee records")
print(f"Attrition rate: {(df['Attrition']=='Yes').mean():.1%}")
