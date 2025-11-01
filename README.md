# 🐍 Selenium Python Framework

This repository hosts a robust end-to-end (E2E) automation framework built using **Python**, **Selenium WebDriver**, and the **Pytest** testing framework. It follows SOLID principles, incorporating the Page Object Model (POM) design pattern for maintainability and scalability.

## 1. Environment Setup Instructions 🛠️

To get this project running locally and execute the automated tests, follow these steps.

### Prerequisites

* **Python:** Ensure you have Python (3.8+) installed.
* **Git:** Install Git to clone the repository.
* **Web Drivers:** Ensure the necessary browser drivers (like ChromeDriver, GeckoDriver, etc.) are installed and accessible in your system's PATH, or configure Pytest to download them automatically (often handled by libraries like `webdriver-manager` if included in `requirements.txt`).

### Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/skmen/selenium-python-framework.git](https://github.com/skmen/selenium-python-framework.git)
    cd selenium-python-framework
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    # Create the environment
    python -m venv venv
    
    # Activate the environment (macOS/Linux)
    source venv/bin/activate
    
    # Activate the environment (Windows)
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    Install all required packages listed in the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

---

## 2. Project Structure 📂

The framework is organized into a modular structure to separate tests, page objects, utilities, and configuration.

| Folder/File | Description |
| :--- | :--- |
| `tests/` | **Test Execution:** Contains all test files (`test_*.py`). Each file holds related test cases (functions prefixed with `test_`). |
| `main/` | **Page Objects & Utilities:** This is typically where the Page Object Model (POM) classes are defined, representing web pages, along with any common helper functions or fixtures. |
| `requirements.txt` | **Dependencies:** Lists all Python packages required for the project (e.g., `selenium`, `pytest`, etc.). |
| `conftest.py` | **Pytest Configuration:** Contains fixtures (like browser initialization/teardown) that are automatically discovered and shared across all test files in the project. |
| `.gitignore` | Specifies intentionally untracked files that Git should ignore (e.g., environment files, log files, cache). |

---

## 3. How to Run Automated Tests ▶️

Tests are executed using the **Pytest** command-line tool. Ensure your virtual environment is active before running tests.

### Basic Execution

To run all discovered tests in the `tests/` directory:

```bash
pytest
