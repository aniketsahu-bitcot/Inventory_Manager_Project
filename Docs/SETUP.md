# Inventory Manager Project Weekly Installation and Setup guide

# Week1 Installation and Setup Guide

This guide explains how to install and set up the project step by step.

## Prerequisites

Make sure the following are installed on your system:

* Python 3.9 or above
* pip (Python package manager)
* Git (optional, but recommended)

## Step 1: Clone or Download the Project

If using Git:

```bash
git clone <repository-url>
cd <project-folder>
```

Or download the ZIP file and extract it, then open the project folder in terminal.

## Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

* On Linux / macOS:

```bash
source venv/bin/activate
```

* On Windows:

```bash
venv\Scripts\activate
```

## Step 3: Install Dependencies

Install required packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Step 4: Project Structure Overview

```
Docs/           # Documentation files
Week1/          # Python source files
  hello.py
  processor.py
  inventory.csv # Sample data file
README.md       # Project overview
```

## Step 5: Run the Project

Navigate to the `Week1` folder:

```bash
cd Week1
```

Run a Python file:

```bash
python hello.py
```

Or:

```bash
python processor.py
```

## Step 6: Documentation

Refer to the `Docs` folder for more details:

* `SETUP.md` – setup instructions
* `ARCHITECTURE.md` – project design

## Common Issues

* If `python` command fails, try `python3`
* If packages fail to install, update pip:

```bash
pip install --upgrade pip
```


# Week2 Installation and Setup Guide

This guide explains how to install and set up the project step by step.

## Prerequisites

Make sure the following are installed on your system:

* Python 3.9 or above
* pip (Python package manager)
* Git (optional, but recommended)

## Step 1: Clone or Download the Project

If using Git:

```bash
git clone <repository-url>
cd <project-folder>
```

Or download the ZIP file and extract it, then open the project folder in terminal.

## Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

* On Linux / macOS:

```bash
source venv/bin/activate
```

* On Windows:

```bash
venv\Scripts\activate
```

## Step 3: Install Dependencies

Install required packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Step 4: Week 2 Folder Structure

```
Week2/
├── Day1/
├── Day2/
├── Day3/
├── Day4/
│   └── inventory_manager/
└── Day5/
    └── inventory_manager/
```

* **Day 1–3**: Script-based learning
* **Day 4–5**: Proper Python package structure

---

## Step 5: Run Day 1 Code

```bash
cd Week2/Day1
python hello.py
```

Run processor:

```bash
python processor.py
```

---

## Step 6: Run Other Days

Example for Day 2:

```bash
cd Week2/Day2
python processor.py
```

Example for Day 3:

```bash
cd Week2/Day3
python processor.py
```

---

## Step 7: Day 4 & Day 5 (Package-based Code)

Navigate to Day 4 or Day 5 parent folder:

```bash
cd Week2/Day4
```

Run:

```bash
cd inventory_manager
```

Run:

```bash
python main.py
```

(Same steps apply for Day 5.)

---

## Common Issues

### `ModuleNotFoundError`

Make sure:

* Virtual environment is activated
* Dependencies are installed

Reinstall if needed:

```bash
pip install -r requirements.txt
```

### `python command not found`

Use:

```bash
python3
```

---




