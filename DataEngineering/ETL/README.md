## ETL Pipleine Script ##

# 📦 Incremental ETL Pipeline using Python (PostgreSQL → PostgreSQL)

#### *Disclaimer: This is a sanitized version of a real-world ETL process. All schema names, table names, and business-specific logic have been generalized.* ####

## Overview and Problem Statement

This project demonstrates a production-style ETL pipeline was designed to solve a significant issue within the FP&A team in my companies finance organization.

For financial reporting, there was not a simple method to identify if there were new accounts that would come in each month and no method to notify the organization of new accounts that were added.

**To solve this issue, this script was bulilt to not only detect new accounts, but also insert those new records into a primary reference table so that all necessary tables within our SQL database are up to date with new accounts. This script also ensures data integrity and avoids duplication.**


---

## 🎯 Issues Script Solves

This pipeline solves that problem by:

* Identifying new records in a source table
* Inserting only missing values into target tables
* Preventing duplicate entries through conflict handling

---

## ⚙️ Key Features

* ✅ Incremental data loading (no full refresh required)
* ✅ Duplicate prevention using conflict handling
* ✅ Config-driven design for multiple tables
* ✅ Secure database connection via environment variables
* ✅ Idempotent execution (safe to run repeatedly)
* ✅ Cron job that runs three times per month

---

## 🧠 How It Works (Flow)

```
        ┌────────────────────┐
        │  Source Table      │
        │  (source_actuals)  │
        └─────────┬──────────┘
                  │
                  │ Extract distinct keys
                  ▼
        ┌────────────────────┐
        │ Compare with       │
        │ Target Table       │
        │ (LEFT JOIN)        │
        └─────────┬──────────┘
                  │
        Records NOT found in target
                  │
                  ▼
        ┌────────────────────┐
        │ Insert into Target │
        │ Table              │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Conflict Handling  │
        │ (DO NOTHING)       │
        └────────────────────┘
```

### Step-by-step logic

1. **Read configuration**

   * Defines source table and multiple target tables
   * Specifies keys for comparison

2. **Extract distinct keys**

   * Pulls unique identifiers from the source table

3. **Compare against target**

   * Uses a `LEFT JOIN` to find records not yet present

4. **Insert new records**

   * Inserts only missing values into the target table

5. **Handle duplicates safely**

   * Uses `ON CONFLICT DO NOTHING` to prevent failures

---

## 🧩 Code Structure

```
.
├── etl_script.py
├── .env
└── README.md
```

### Main Components

* **Configuration**

  * Database connection via environment variables
  * Table mappings defined in a structured config list

* **Core Function**

  * `insert_new_records()`
    Handles incremental insert logic for each table

* **Execution Layer**

  * Iterates through all table configurations
  * Executes ETL logic in a single transaction

---

## 🔐 Environment Setup

Create a `.env` file with your database credentials:

```
DB_HOST=your_host
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
```

---

## 🚀 Usage

Run the script:

```bash
python etl_script.py
```

The pipeline will:

* Connect to the database
* Process each configured table
* Insert only new records

---

## 🛠️ Technologies Used

* Python
* PostgreSQL
* psycopg2
* python-dotenv

---

## 💡 Design Highlights

### Config-Driven Architecture

Instead of hardcoding logic, the pipeline uses a configuration list:

* Easily extend to new tables
* Reduces code duplication
* Improves maintainability

---

### Idempotent Processing

The script can be run multiple times without:

* Creating duplicates
* Breaking existing data

---

### Safe SQL Construction

Uses `psycopg2.sql` for:

* Dynamic query generation
* Protection against SQL injection

---

## 📈 Real-World Application

This pipeline pattern is commonly used in:

* Data warehouse ingestion layers
* Master data synchronization
* Incremental dimension table updates
* Scheduled ETL jobs (Airflow, cron, etc.)

---


---

## 📊 Impact

**Before:**

* The FP&A team only found new accounts while working on their reporting and had to update hierarchy structure during important reporting deadlines
* Manually updating accourn records in excel, then updating in SQL
* Inefficient full reloads

**After:**

* Automated incremental updates
* Reliable and repeatable process
* Scalable design for multiple datasets

---



---

