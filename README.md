# Repository for Playwright + Pytest Framework for demowebshop

This repository is a placeholder project implementing:
- **Page Object Model (POM)** for maintainability.
- **Pytest** as the test runner.
- **Test Parameterization** for testing multiple product combinations.
- **Logging** and **Screenshots on Failure**.
- **Allure Reports** generation.
- **Parallel Execution** on Chromium, Firefox, and WebKit.
- **Jenkinsfile** for CI/CD integration.

## Local Setup

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

## Jenkins Setup
1. Install Jenkins server on a machine
2. Install Allure Jenkins plugin in Jenkins plugins
3. Create a new item from Jenkins UI:
   - New Item
   - Select an item name: Pipleline
   - In Pipline section, change definition to "Pipeline script from SCM"
      - Set SCM to Git
      - Set Repository URL to be: https://github.com/consoledog/py_playwright_demowebshop.git
      - Set Branch Specifier (blank for 'any') to be: */main
      - Script Path: Jenkinsfile
      Note: Jenkinsfile is in the root of the project
4. Click Save
5. Go to the job instance
6. Click "Build Now"

-  In Console Output you can see the result of the execution
-  In Allure Report tab  can see the graphic report