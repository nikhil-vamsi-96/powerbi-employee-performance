# Employee Performance & Workforce Intelligence — Power BI

A portfolio-ready **Power BI HR analytics dashboard** focused on workforce size, employee attrition, compensation, performance, overtime, tenure, and employee satisfaction.

## 📊 Dashboard

The report contains four interactive pages:

| Page | Focus |
|---|---|
| **01 Executive Overview** | Executive KPIs, department workforce, attrition, performance, job-role exits, and overtime analysis |
| **02 Attrition Intelligence** | Attrition by department, job role, overtime, tenure, job satisfaction, and environment satisfaction |
| **03 Workforce Performance** | Workforce distribution, compensation, performance rating, and employee-experience analysis |
| **04 Employee Explorer** | Interactive slicers and employee-level detail |

## 🎯 Business Objective

HR teams need a clear view of workforce composition and the employee factors associated with attrition.

This dashboard turns employee-level data into an interactive reporting layer for exploring:

- Workforce distribution
- Attrition patterns
- Overtime and attrition
- Compensation
- Performance
- Tenure
- Employee satisfaction
- Department and job-role differences

## 🔢 Key Metrics

Based on the current 800-row dataset:

| KPI | Value |
|---|---:|
| Total Employees | **800** |
| Employees Left | **174** |
| Attrition Rate | **21.75%** |
| Average Age | **40.39** |
| Average Monthly Income | **$7,129.80** |
| Average Performance Rating | **2.57** |

## 📌 Key Analysis Areas

### Workforce
- Employees by department
- Average monthly income by department
- Average performance rating by department

### Attrition
- Attrition rate by department
- Employees left by job role
- Overtime vs. attrition rate
- Attrition by years at company
- Attrition by job satisfaction
- Attrition by environment satisfaction

### Employee Experience
- Job satisfaction
- Environment satisfaction
- Work-life balance
- Job involvement
- Relationship satisfaction

### Employee Explorer
Interactive filtering by:

`Department` • `JobRole` • `Gender` • `Education` • `OverTime` • `BusinessTravel` • `MaritalStatus` • `Attrition`

## 🧮 DAX Measures

The report uses these core measures:

```DAX
Total Employees
Employees Left
Attrition Rate
Average Age
Average Monthly Income
Average Performance Rating
```

## 🛠️ Tools & Technologies

- **Power BI Desktop**
- **Power BI Project (PBIP/PBIR)**
- **DAX**
- **Power BI Modeling MCP**
- **Power BI Report Authoring skill**
- **GitHub**

## 🎨 Dashboard Design

The report uses a dark executive-dashboard visual system with:

- KPI cards
- Large analytical chart panels
- Consistent accent colors
- Attrition-focused red/orange highlights
- Interactive slicers
- Employee-level exploration
- Consistent page structure and typography

## 📁 Project Structure

```text
powerbi-employee-performance/
├── README.md
├── .gitignore
├── data/
│   └── employee_performance.csv
├── images/
│   ├── 01 Executive Overview.png
│   ├── 02 Attrition Intelligence.png
│   ├── 03 Workforce Performance.png
│   └── 04 Employee Explorer.png
├── powerbi/
│   └── Employee Performance/
│       ├── Employee Performance.pbip
│       ├── Employee Performance.Report/
│       └── Employee Performance.SemanticModel/
└── documentation/
```

## ▶️ How to Use

1. Download or clone the repository.
2. Open the `powerbi/Employee Performance/Employee Performance.pbip` project in Power BI Desktop.
3. Review the Executive Overview.
4. Explore Attrition Intelligence and Workforce Performance.
5. Use the Employee Explorer slicers for employee-level analysis.

## 📝 Notes

The dashboard is an analytical reporting project. Attrition relationships shown in the visuals are descriptive and should be investigated alongside business context before making HR decisions.

## 👤 Author

**Nikhil Vamsi** — Data Analyst

- GitHub: https://github.com/nikhil-vamsi-96
- Data Portfolio: https://github.com/nikhil-vamsi-96/Data-Portfolio
