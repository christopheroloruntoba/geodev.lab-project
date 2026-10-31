
# <My GeoDev Lab Africa project>

Which settlements in Ibadan North local government area sit in low-lying land within 200 metres of a watercourse?

**GeoDev Lab Africa, Cohort One.** <Oloruntoba Christopher Eyitayo>

---

## The question
Which settlements in Ibadan North local government area sit in low-lying land within 200 metres of a watercourse?

## What's in here

```
<project-name>/
├── docs/
│   ├── 01-project-brief.md      Week 1
│   ├── 02-data-notes.md         Week 2
│   └── 03-data-preparation.md   Week 3
├── data/
│   ├── raw/                     downloads, not committed
│   └── processed/               outputs, not committed
├── scripts/
└── requirements.txt
```

## How to run it

```bash
git clone https://github.com/christopheroloruntoba/geodev.lab-project/.git
cd <geodev.lab-project> 

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

The data is not in this repository. Every source is linked in
[the project brief](docs/01-project-brief.md), so anyone can fetch it.

## Progress

Week 1, project brief with a source link for every dataset

Week 2, data downloaded, opened and described

Week 3, reprojected, clipped and quality checked

Week 4, first spatial analysis, checked four ways

---
## Month 2: development environment and early Python

Week 5: set up Python, VS Code and the terminal. hello.py runs.

Week 6: set up the project with uv and added pandas. check.py prints the pandas version.

Week 7: analyse.py reads wards.csv, converts each area and classifies each ward.

Week8: inspect_data.py summarises depth and yield in my Oyo boreholes data.

Week 9: Python data analysis capstone: Built a reusable Python data analysis script using functions to read CSV files, clean data, calculate summary statistics, and generate reports.

### Month 2 Reflection

One idea that finally clicked for me this month is how to use Python functions to break a programme into smaller, reusable tasks. I now understand how to read CSV files, clean data, and calculate descriptive statistics using Python. I am still working on understanding how to handle different data types and combine functions effectively when analysing datasets. My capstone project has shown me that my Month 1 data can be organised, cleaned, and analysed to produce meaningful information that supports geospatial analysis and decision-making.


<Oloruntoba Christopher Eyitayo> · GeoDev Lab Africa
Learn. Build. Collaborate. Transform.
