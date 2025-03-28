# LocalLens API

This is the backend API for LocalLens, a project designed to track and analyze sentiment from various sources for restaurants.

## Project Description

The LocalLens API provides endpoints to retrieve information about restaurants, reviews, category sentiments, and meal sentiments. It interacts with a MySQL database to fetch and serve data.

## Technologies Used

* Python 3
* Flask
* Flask-SQLAlchemy
* MySQL

## Setup Instructions

1.  **Clone the Repository:**

    ```bash
    git clone your_repository_url
    cd LocalLens
    ```

2.  **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**

    * **On Windows:**

        ```bash
        venv\Scripts\activate
        ```

    * **On macOS and Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up the MySQL Database:**

    * Ensure you have MySQL installed and running.
    * Create a database named `beryldb`.
    * Create the necessary tables (restaurants, reviews, categorysentiments, mealsentiments) using the SQL script provided in the database section of the project.
    * Update the database connection string in `app.py` with your MySQL credentials.

6.  **Run the API:**

    ```bash
    python app.py
    ```

    * The API will be accessible at `http://127.0.0.1:5001`.

## API Endpoints

### 1. Search Restaurants

* **Endpoint:** `/restaurants/search`
* **Method:** GET
* **Parameters:**
    * `query` (optional): Search term.
* **Response:** JSON array of restaurant objects.

    ```json
    [
      {
        "restaurant_id": 1,
        "name": "The Local Grill",
        "address": "123 Main St"
      },
      // ... more restaurants
    ]
    ```

### 2. Get Restaurant Reviews

* **Endpoint:** `/restaurants/<int:restaurant_id>/reviews`
* **Method:** GET
* **Response:** JSON array of review objects.

    ```json
    [
      {
        "review_id": 101,
        "review_text": "Great food!",
        "rating": 4.5,
        "platform": "Google Reviews"
      },
      // ... more reviews
    ]
    ```

### 3. Get Restaurant Categories

* **Endpoint:** `/restaurants/<int:restaurant_id>/categories`
* **Method:** GET
* **Response:** JSON array of category sentiment objects.

    ```json
    [
      {
        "category_name": "Food",
        "sentiment_score": 4.2
      },
      // ... more categories
    ]
    ```

### 4. Get Restaurant Meals

* **Endpoint:** `/restaurants/<int:restaurant_id>/meals`
* **Method:** GET
* **Response:** JSON array of meal sentiment objects.

    ```json
    [
      {
        "meal_name": "Steak",
        "sentiment_score": 4.5
      },
      // ... more meals
    ]
    ```

## Database Setup

* Create a database named `beryldb` in your MySQL server.

* Run the following SQL script to create the tables:

    ```sql
    -- Create tables here.
    ```
    (Paste the SQL code from previous response here)

## Dependencies

* Flask
* Flask-SQLAlchemy
* mysqlclient

## Author

* Tawana Msebele

