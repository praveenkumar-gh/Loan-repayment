Step 1: Understand the Relationship Between Schemas
Borrower_table: Contains information about each customer (one customer, one record). This serves as the main dimension for borrowers.
Loan_table: Each borrower may have multiple loans. This is a fact table that details the loans.
Payment_Schedule: Lists expected payment dates and amounts for each loan.
Loan_payment: Logs actual payments made by customers for each loan.
Missed_payment: Tracks times customers have missed payments (not directly provided but assumed to exist for alerting).

These tables are connected by ‘borrower_id’ and  ‘loan_id’  with ‘borrower_table’ being the core table linking the others.

Step 2: Dimensional Design
We’ll use a ‘star schema’ approach since it simplifies queries and is efficient for aggregating reports. Here’s the outline:

1. Fact Table: Loans – Central table that contains information about the loans.
   Primary Key: loan_id
   Foreign Key: borrower_id
   Attributes: LoanAmount, InterestRate, Term, Maturity_date, etc.

2. Dimension Table: Borrowers – Contains borrower details.
   Primary Key: borrower_id
   Attributes: State, City, ZipCode, Created_at

3.Fact Table: Loan Payments – Captures actual payment data.
   Primary Key: payment_id
   Foreign Key: loan_id
   Attributes: Amount_paid, Date_paid

4. Fact Table: Payment Schedule – Details expected payments.
   Primary Key: schedule_id
   Foreign Key: loan_id
   Attributes: Expected_payment_date, Expected_payment_amount

This model allows us to easily calculate missed payments (join Loan Payments and Payment Schedule) and overdue loans (calculate PAR Days).

Step 3: ELT Pipeline
Creating an ETL pipeline:

1. Extraction: Pull the data from source databases (PostgreSQL/MariaDB/BigQuery, etc.) into the staging area.
2. Loading : Load raw data into staging tables without transformations.(Temporary storage where the datasets will get stored before we push them into our first layer)
3. Transformation : Perform the necessary transformations to clean and format the data, and load it into the target dimensional model
For this, we use Azure data factory to orchestrate and automate the process. And Azure Databricks to do data analytics on a large scale dataset for efficiency

Step 4: PAR Days Calculation (Python & SQL)
1. Joining the Loan Payment and Payment Schedule tables based on loan_id.
2. Comparing the Expected_payment_date with Date_paid to find how many days late each payment was.
3. Calculating the Amount_at_risk by summing up the outstanding payments when a payment is overdue.

Step 5: Monitoring & Alerting System
- Implementing logging to capture errors during the ETL process using logging module in Python
- Use Slack Alerts or Email to notify when an issue occurs, e.g., when data fails to load or transformations result in inconsistencies.
- For detecting errors, capture the number of rows loaded at each stage and compare with expected counts.
Step 6: Deployment Workflow
We can additionally implement a deployment workflow:

- Use GitHub Actions or Jenkins to automate the pipeline deployment.
- Set up CI/CD pipelines that trigger a new deployment when all unit tests pass and data integrity checks succeed.
- Ensuring Schema consistency before deployment. creating tests to ensure the integrity of your models. For example, you can validate primary and foreign key relationships, ensure non-null values, and check that a column contains unique values.

Step 7: Documentation

Documenting each part of the pipeline and model.

- The source of each dataset and schema structure.
- The transformation logic.
- How to run the pipeline (commands, environment setup).
- How monitoring is configured.
