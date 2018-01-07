# THE APP
To start the app:

1. cd webapp/reactapp
2. npm start
3. source/env/bin/activate (from root)
4. python manage.py runserver
5. navigate to http://localhost:8000/



# API
The backend api can be found at /api

## /api/businesses
This endpoint returns a list of businesses in the form:
```
{
    "items": [
        {
            "id":
            "name":
            "area":
            "address":
            "business_type":
            "description":
            "url":
        }
    ]
}
```
