# Data Engineering Assessment

Welcome!  
This exercise evaluates your core **data-engineering** skills:

| Competency | Focus                                                         |
| ---------- | ------------------------------------------------------------- |
| SQL        | relational modelling, normalisation, DDL/DML scripting        |
| Python ETL | data ingestion, cleaning, transformation, & loading (ELT/ETL) |

---

## 0 Prerequisites & Setup

> **Allowed technologies**

- **Python ≥ 3.8** – all ETL / data-processing code
- **MySQL 8** – the target relational database
- **Lightweight helper libraries only** (e.g. `pandas`, `mysql-connector-python`).  
  List every dependency in **`requirements.txt`** and justify anything unusual.
- **No ORMs / auto-migration tools** – write plain SQL by hand.

---

## 1 Clone the skeleton repo

```
git clone https://github.com/100x-Home-LLC/data_engineer_assessment.git
```

✏️ Note: Rename the repo after cloning and add your full name.

**Start the MySQL database in Docker:**

```
docker-compose -f docker-compose.initial.yml up --build -d
```

- Database is available on `localhost:3306`
- Credentials/configuration are in the Docker Compose file
- **Do not change** database name or credentials

For MySQL Docker image reference:
[MySQL Docker Hub](https://hub.docker.com/_/mysql)

---

### Problem

- You are provided with a raw JSON file containing property records is located in data/
- Each row relates to a property. Each row mixes many unrelated attributes (property details, HOA data, rehab estimates, valuations, etc.).
- There are multiple Columns related to this property.
- The database is not normalized and lacks relational structure.
- Use the supplied Field Config.xlsx (in data/) to understand business semantics.

### Task

- **Normalize the data:**

  - Develop a Python ETL script to read, clean, transform, and load data into your normalized MySQL tables.
  - Refer the field config document for the relation of business logic
  - Use primary keys and foreign keys to properly capture relationships

- **Deliverable:**
  - Write necessary python and sql scripts
  - Place your scripts in `sql/` and `scripts/`
  - The scripts should take the initial json to your final, normalized schema when executed
  - Clearly document how to run your script, dependencies, and how it integrates with your database.

**Tech Stack:**

- Python (include a `requirements.txt`)
  Use **MySQL** and SQL for all database work
- You may use any CLI or GUI for development, but the final changes must be submitted as python/ SQL scripts
- **Do not** use ORM migrations—write all SQL by hand

---

## Submission Guidelines

- Edit the section to the bottom of this README with your solutions and instructions for each section at the bottom.
- Place all scripts/code in their respective folders (`sql/`, `scripts/`, etc.)
- Ensure all steps are fully **reproducible** using your documentation
- Create a new private repo and invite the reviewer https://github.com/mantreshjain

---

**Good luck! We look forward to your submission.**

## Solutions and Instructions (Filed by Candidate)

**Document your database design and solution here:**

**Schema Explanation and Design Decisions:**
- The schema is normalized into six main tables according to the provided Field-Config:
    - `property`: Stores core details about each property (address, type, metrics).
    - `leads`: Tracks lead/review details for each property and links by `property_id`.
    - `valuation`: Stores pricing, rent, and estimated value metrics, linked by `property_id`.
    - `hoa`: Captures HOA info (flag, amount), linked by `property_id`.
    - `rehab`: Contains all rehabilitation-related flags and data, linked by `property_id`.
    - `taxes`: Records tax rate and amounts, linked by `property_id`.
- Foreign key constraints maintain referential integrity such that child tables always reference valid properties.
- Data types reflect expected max lengths and numeric ranges based on typical property datasets.

**Run and Test Instructions:**
1. Start the MySQL service via Docker Compose:
   ```
   docker-compose -f docker-compose.final.yml up --build -d
   ```
2. Create the schema:
   ```
   mysql -u db_user -p6equj5_db_user home_db < sql/create_tables.sql
   ```
3. Install dependencies:
   ```
   pip install -r scripts/requirements.txt
   ```
4. Run the ETL/data loader script:
   ```
   python3 scripts/load_data.py
   ```
5. Verify:
   - Connect to MySQL and check for row counts in each table:
     ```
     SELECT COUNT(*) FROM property;
     SELECT COUNT(*) FROM leads;
     SELECT COUNT(*) FROM valuation;
     SELECT COUNT(*) FROM hoa;
     SELECT COUNT(*) FROM rehab;
     SELECT COUNT(*) FROM taxes;
     ```

***

**Document your ETL logic here:**
**Approach and Design:**
- The ETL script reads the raw input JSON, iterating over each record.
- Each record is mapped to fields, grouped per target table according to the provided Field-Config rules.
- For every record, it first inserts into the `property` table, then uses its `property_id` (primary key) to insert related data into the child tables.
- Each `insert_*` function extracts the relevant fields or assigns None for missing data, ensuring relational linking.
- The process guarantees atomic data loading—if a property fails, related records are skipped.
- The script commits after loading all data to ensure performance and consistency.

**Instructions and Code:**
1. Place `load_data.py` inside `scripts/`, and `create_tables.sql` inside `sql/`.
2. Ensure the service is running and schema is loaded as per above.
3. Run:
   ```
   python3 scripts/load_data.py
   ```
   This uses credentials specified in your Docker Compose file.

**Requirements:**
- Python ≥ 3.8
- `mysql-connector-python` (see requirements.txt)
- (Optional): `pandas` for future enhancements or advanced preprocessing

***
