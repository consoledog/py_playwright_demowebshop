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
   Note: For activating the venv on Windows, use from cli: venv\Scripts\activate.bat
   
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Install playwright browsers
   ```bash
   python -m playwright install
   ```
4. Install allure on your computer
5. Run tests
   ```bash
   pytest --alluredir=allure-results -n auto
   ```
6. Generate Allure report:
   ```bash
   allure generate allure-results --clean -o allure-report
   ```
7. Open the Allure report
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

## About product_specification (IMPORTANT)

The purpose of this file is the existance of different configurations of products.

Let's say one product have configuration that is composed of: 
- Select processor
- Select RAM
- Select HDD
...
  
Let's say another product have configuration that is composed of:
- Select shoe color
- Select shoe size
...

So in this file are defined different types of configurations, and each of this
configurations is supported in the code by the function "def select_configuration"
So far you can find this function into comp_drop_page.py, comp_radio_page.py, gift_cart_page.py, product_page.py (Default one)

Note: If you want to support new configuration, add this code name into "product_specification.txt", then implement
the function "select_configuration" in your "*_page.py" file
