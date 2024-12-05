# Dashboard Bike Sharing Agustinasb ✨

This is the **Dashboard Bike Sharing Agustinasb**, an interactive application built using **Streamlit**, designed to visualize and analyze bike-sharing data. The dashboard provides insights into daily and hourly rental patterns, the impact of weather conditions, and more.

## Setup Environment

### Option 1: Using **Anaconda**

1. **Create a new environment**:

    ```bash
    conda create --name bike-sharing-ds python=3.9
    ```

2. **Activate the environment**:

    ```bash
    conda activate bike-sharing-ds
    ```

3. **Install the required dependencies**:

    Navigate to your project directory and install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

### Option 2: Using **Shell/Terminal**

1. **Create a new directory for your project**:

    ```bash
    mkdir bike-sharing-dashboard
    cd bike-sharing-dashboard
    ```

2. **Install pipenv** (if not already installed):

    ```bash
    pip install pipenv
    ```

3. **Install dependencies using pipenv**:

    ```bash
    pipenv install
    ```

4. **Activate the pipenv environment**:

    ```bash
    pipenv shell
    ```

5. **Install additional dependencies (if needed)**:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Streamlit App

After setting up the environment, navigate to the project folder containing the dashboard script (`dashboard.py`), and run the following command:

```bash
streamlit run dashboard.py
