# Road Safety Dashboard API

This is a RESTful web application for analyzing global road traffic accident data. Built with Django and Django REST Framework, it supports structured querying, filtering, data entry, and a normalized SQLite3 database.

---

## Getting Started (Run from ZIP)

> These instructions assume you have already extracted the ZIP archive.

### 1. Open Terminal or Command Prompt

Navigate into the extracted folder:
```bash
cd path/to/unzipped/folder
````

---

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux/Ubuntu

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the custom API homepage.

---

### 5. (Optional) Run Unit Tests

```bash
python manage.py test
```

---

### 6. (Optional) Re-seed the Database

```bash
python manage.py shell
```

Then run:

```python
from dashboard.load_data import load_traffic_data
load_traffic_data()
exit()
```

---

## Django Admin Login

| Field    | Value                                                      |
| -------- | ---------------------------------------------------------- |
| URL      | [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) |
| Username | kimy                                                       |
| Password | kimy123                                                    |

---

## Development Environment

* OS: Ubuntu (via WSL on Windows)
* Python: 3.12.3
* SQLite3: Default Django database
* Django: 5.2.3
* DRF: 3.16.0

---

## Package Summary

Required packages from `requirements.txt`:

* Django==5.2.3
* djangorestframework==3.16.0
* gunicorn==23.0.0
* whitenoise==6.9.0
* black==25.1.0
  (others included for formatting and compatibility)

---

## API Features

* List all traffic accidents
* Filter accidents by city
* Filter accidents by cause (e.g. drunk driving)
* Filter accidents occurring on weekends
* Add a new accident via POST
* Apply multiple filters (e.g., city + cause)

All endpoints return paginated JSON and use nested serialization.

---

## Code Style

* Follows PEP8 standards
* Autoformatted using `black`
* Fully unit-tested (`tests.py`)
* Modular: views, models, serializers, and routes are separated

---

## File Highlights

* `load_data.py`: Data seeding script using relative paths
* `dashboard/`: All core app logic (views, models, tests, etc.)
* `templates/`: Custom styled homepage
* `static/`, `staticfiles/`: CSS for layout and DRF UI
* `db.sqlite3`: Pre-seeded database
* `requirements.txt`: All dependencies

---

## Deployed Live (Bonus)

[https://road-safety-dashboard.onrender.com/](https://road-safety-dashboard.onrender.com/)

are.
```
