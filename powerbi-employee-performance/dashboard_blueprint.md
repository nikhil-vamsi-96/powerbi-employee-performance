# Dashboard Blueprint — Employee Performance Metrics

Build this as a 2-page Power BI report. Import `employee_performance.csv`,
name the table `EmployeeData`, then paste in the measures from
`dax_measures.txt` before building visuals.

## Page 1: Executive Overview

**Top row — KPI cards (4 cards, left to right):**
1. `[Total Employees]`
2. `[Attrition Rate]` — format as %, conditional color red if >20%
3. `[Avg Performance Rating]`
4. `[Avg Monthly Income]` — format as currency

**Middle row — two visuals side by side:**
- **Left:** Clustered bar chart — Attrition Rate by Department (Axis: Department, Values: `[Attrition Rate]`). Sort descending. This is your highest-impact chart — put it first.
- **Right:** Clustered column chart — Attrition Rate by OverTime (Axis: OverTime, Values: `[Attrition Rate]`)

**Bottom row:**
- Donut chart: Performance Rating distribution (Legend: PerformanceRating, Values: Count of EmployeeID)
- Table: Department | `[Avg Performance Rating]` | `[Attrition Rate]` | `[Avg Monthly Income]` — sortable, this becomes a manager-facing summary table

**Slicers (top of page, applies to whole page):** Department, Gender, JobRole

---

## Page 2: Flight Risk & Performance Drivers

**Top row:**
- Scatter chart: X = JobSatisfaction, Y = PerformanceRating, Size = Count, Legend = Attrition — shows visually that satisfaction correlates with both performance AND retention
- KPI card: `[High Flight Risk Count]` with conditional formatting (red background if count is high)

**Middle row:**
- Bar chart: Average `FlightRiskScore` by Department (requires the calculated column from dax_measures.txt)
- Bar chart: Attrition Rate by `YearsSinceLastPromotion` bucket (create a calculated column bucketing 0-1yr / 2-3yr / 4+yr first)

**Bottom row:**
- Table: Top 20 employees by `FlightRiskScore` descending — filtered to `Attrition = "No"` (these are your current at-risk retained employees, the actionable list for HR)
- Bar chart: Average Monthly Income by Department, sorted descending

**Slicers:** BusinessTravel, MaritalStatus

---

## Design Notes
- Use a consistent 2-3 color palette: red/orange for risk indicators, blue/green for positive/neutral. Don't rainbow the department bars.
- Put the single most important chart (Attrition by Department) top-left on Page 1 — that's where eyes land first.
- Add a text box under the KPI cards on Page 1 with 1-2 sentences summarizing the headline finding — reviewers skim dashboards, a text callout increases retention of the insight.
- Enable drill-through from the Page 1 department table to Page 2, filtered to that department, so a hiring manager can click "HR" and land on HR's specific flight-risk data.
