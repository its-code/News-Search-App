# News Search Engine

## Setting Up

### Clone the Repository

1. Before proceeding with the setup, ensure you have cloned the repository:
   ```bash
    git clone https://github.com/its-code/News-Search-App.git
    cd News-Search-App
    ```
   
### First RUN Backend before running Frontend

1. Navigate to the backend directory:
    ```bash
    cd backend
    ```

2. Setup a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask app:
    ```bash
    python app.py
    ```

### Frontend

1. Open the new Terminal and navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2. Install required dependencies:
    ```bash
    npm install
    ```

3. Serve the Vue app:
    ```bash
    npm run serve
    ```

### API Keys

### Obtaining NewsAPI Key

1. Register for an API key at [NewsAPI](https://newsapi.org/register) .
2. After registration, you'll receive an API key.
3. Store the API in backend\app.py 
    ```bash
    NEWS_API_KEY = "HERE"    
    ```
    




    
