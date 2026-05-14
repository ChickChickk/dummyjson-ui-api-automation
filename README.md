# DummyJSON UI API Automation

## Project Overview

This project is a UI + API automation testing framework built with Selenium, Pytest, and Requests.

The goal of the project is to validate that frontend product data displayed on the UI matches the backend API response from DummyJSON.

---

## Tech Stack

- Python
- Selenium
- Pytest
- Requests
- HTML / JavaScript

---

## Features

### API Testing
- Validate product API responses
- Verify product data structure
- Validate product count and fields

### UI Testing
- Open local frontend page using Selenium
- Read product titles and prices from UI
- Validate products are rendered correctly

### UI + API Validation
- Compare frontend product data against backend API data
- Validate title consistency
- Validate price consistency

---

## Project Structure

```text
dummyjson_ui_api_automation/
│
├── api/
│   └── products_api.py
│
├── pages/
│   └── products_page.py
│
├── tests/
│   ├── test_products_api.py
│   ├── test_products_ui.py
│   └── test_products_ui_api.py
│
├── ui/
│   └── index.html
│
├── conftest.py
└── requirements.txt
```

## What each layer does 

ui/index.html
- Displays products visually

products_api.py
- Gets backend data

products_page.py
- Reads product data from UI

---

## Setup

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/dummyjson-ui-api-automation.git
cd dummyjson-ui-api-automation
```

### Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Tests

### Run API Tests

```bash
pytest -s tests/test_products_api.py
```

### Run UI Tests

```bash
pytest -s tests/test_products_ui.py
```

### Run UI + API Integration Tests

```bash
pytest -s tests/test_products_ui_api.py
```

---

## Learning Goals

This project was created to practice:
- Selenium automation
- API testing
- Page Object Model (POM)
- UI and backend data validation
- Integration testing concepts



test_products_api.py
Checks backend works

test_products_api.py
Checks frontend displays products
