# CS340-Portfolio
Portfolio repository for CS 340 featuring a MongoDB dashboard, CRUD module, and README documentation.
# CS 340 Portfolio Submission

This repository contains my Project Two artifacts for CS-340, including the dashboard notebook, CRUD Python module, and project documentation.

## Included Artifacts

- `ProjectTwoDashboard.ipynb`
- `animal_shelter.py`
- `CS340_ProjectTwo_README.docx`

## Reflection

### How do you write programs that are maintainable, readable, and adaptable?

I write maintainable, readable, and adaptable programs by separating responsibilities into clear parts, using descriptive variable and function names, and keeping related logic organized into reusable modules. A strong example from this course was the CRUD Python module from Project One. Instead of placing all database logic directly inside the dashboard notebook, I created a separate Python module to handle MongoDB operations. This made the dashboard code cleaner and easier to understand, and it allowed me to reuse the same database connection and query logic in Project Two. The advantage of working this way was that I could update or troubleshoot the database layer without rewriting the dashboard itself. In the future, I could reuse this CRUD module in other projects that need MongoDB access, such as inventory systems, personal databases, or analytics dashboards.

### How do you approach a problem as a computer scientist?

I approach a problem by first understanding the requirements, then breaking the larger task into smaller pieces that can be designed, tested, and improved step by step. For this project, I started by understanding Grazioso Salvare’s need to filter and categorize rescue dog candidates. Then I focused on the database structure, the MongoDB queries, the dashboard layout, and finally the interactive behavior through Dash callbacks. This approach differed from some earlier assignments because this project required me to connect multiple systems together instead of solving only one isolated programming problem. In the future, I would continue using this step-by-step design process by identifying the client’s needs first, designing a flexible schema, building reusable database access code, and testing each dashboard feature independently before combining everything.

### What do computer scientists do, and why does it matter?

Computer scientists design systems that organize data, automate tasks, solve problems, and support better decision-making. Their work matters because organizations often need software tools that make large amounts of information easier to use and understand. In this project, my work helped transform raw shelter data into a usable dashboard that allows Grazioso Salvare to quickly identify dogs that fit rescue-training profiles. This type of system improves efficiency, reduces manual effort, and helps users make better decisions based on data. For a company like Grazioso Salvare, a well-designed dashboard can make the process of finding suitable rescue candidates faster, more accurate, and more consistent.

## Repository Purpose

This repository serves as a portfolio artifact demonstrating my work with MongoDB, Python, CRUD design, Dash dashboards, and client/server development in CS-340.
