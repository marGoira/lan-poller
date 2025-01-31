# lan-poller
Implementation for garageLanParty

## Usage Hints

### Create a User

To create an admin user, run the following command:
```bash
python manage.py createsuperuser
```

### Create Models

After creating your models and adding them to admin.py, apply migrations with the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Start the Server
Start your development server with:
```bash
python manage.py runserver
```

### Admin Control
Access the admin interface at: http://localhost:port/admin
