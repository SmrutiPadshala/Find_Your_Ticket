
# Find Your Ticket 🎟️

This is a Django-based web application named **Find Your Ticket** (or **Movie Booking**), designed for movie ticket bookings. It allows users to explore movies and book tickets easily.

## Features

- User-friendly interface for movie ticket booking
- Admin panel to manage movies and bookings
- MySQL database integration
- Organized codebase with templates and static files

## Tech Stack

- Python
- Django
- MySQL
- HTML, CSS (static files)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/SmrutiPadshala/Find_Your_Ticket.git
   cd sp_project
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**
   - Ensure MySQL is running.
   - Create a database named `movie_booking`.
   - Update `settings.py` with your DB credentials:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'movie_booking',
             'USER': 'root',
             'PASSWORD': '',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

5. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the App**
   Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Admin Panel

To access the Django admin panel:
```bash
python manage.py createsuperuser
```
Then log in at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## License

This project is for educational purposes.
