# Pytest Automation Framework

Welcome to your generated Pytest + Selenium 4 Automation Framework. 

## 🏗 Architecture
1. **Configuration (`config/config.yaml`)**: Centralized YAML file controlling browser types, timeouts, and environments.
2. **Page Object Model (`pages/`)**: Clean encapsulation of UI elements into logical pages.
3. **Execution (`tests/`)**: Pytest scripts utilizing powerful `@pytest.fixture` and native Selenium 4 WebDriver management.
4. **Visual Flow (`architecture_flow.html`)**: Open this included HTML file in your browser to view a sleek dashboard of how this framework operates.

## 🚀 Prerequisites
- Python 3.12+
- Google Chrome, Firefox, or Edge installed on your machine
- [Allure Commandline](https://docs.qameta.io/allure/#_installing_a_commandline) (Optional, for generating visual test reports)

## 🛠 Installation
Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## 🏃 Running Tests
Run all tests in Chrome (default):
```bash
pytest tests/
```

Run in Headless mode:
```bash
pytest tests/ --headless
```

Run on Firefox or Edge:
```bash
pytest tests/ --browser=firefox
pytest tests/ --browser=edge
```

Run multiple tests in parallel (xdist):
```bash
pytest tests/ -n auto
```

## 📊 Generating Reports
Generate a clean visual dashboard of your test runs using Allure:
```bash
allure serve allure-results
```
