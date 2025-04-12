# Repository for Playwright + Pytest Framework for demowebshop

This repository is a placeholder project implementing:
- **Page Object Model (POM)** for maintainability.
- **Pytest** as the test runner.
- **Test Parameterization** for testing multiple product combinations.
- **Logging** and **Screenshots on Failure**.
- **Allure Reports** generation.
- **Parallel Execution** on Chromium, Firefox, and WebKit.
- **Jenkinsfile** for CI/CD integration.

## Setup

1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   ```
   ```bash
   source venv/bin/activate
   ```
   
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Install playwright browsers
   ```bash
   python -m playwright install
   ```
4. Run tests
   ```bash
   pytest --alluredir=allure-results -n auto
   ```
5. Generate Allure report:
   ```bash
   allure generate allure-results --clean -o allure-report
   ```
6. Open the Allure report
   ```bash
   allure open allure-report
   ```
