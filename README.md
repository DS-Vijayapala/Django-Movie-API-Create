# 🎬 Django Movie API

A **Django REST Framework (DRF) API** for managing movie data, including different categories such as action and cartoon movies. This API allows users to retrieve, create, update, and delete movie records using Django's ModelViewSet.

## 🚀 Features

- **Retrieve All Movies** – Get a list of all available movies.
- **Filter by Category** – Fetch action or cartoon movies separately.
- **CRUD Operations** – Create, update, and delete movie records.
- **Django REST Framework** – Uses DRF's ModelViewSet for easy API management.

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default)
- **API Documentation:** DRF Browsable API

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DS-Vijayapala/Django-Movie-API-Create.git
   cd django-movie-api
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. API Endpoints:
   ```
   GET /movies/  -> Fetch all movies
   GET /movies/?typ=action  -> Fetch only action movies
   GET /movies/?typ=cartoon -> Fetch only cartoon movies
   POST /movies/  -> Add a new movie
   PUT/PATCH /movies/{id}/  -> Update an existing movie
   DELETE /movies/{id}/  -> Delete a movie
   ```

## 🏗️ Future Improvements

- Implement **genre-based filtering**.
- Add **authentication and permissions** for managing movie records.
- Integrate **pagination** for large datasets.

## 🐝 License

This project is licensed under the **MIT License**.


