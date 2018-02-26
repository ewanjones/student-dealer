# THE APP
To start the app:

1. cd webapp/reactapp
2. npm start

3. source/env/bin/activate (from root)
4. python manage.py runserver
5. open http://localhost:8000/ in the browser


# PRODUCTION
To access the PostGreSQL database ssh in as root and login as postgre
(password from Ewan!)

```su - postgre
```
Then start postgre with

```
psql
```


# API
The backend api can be found at /api. This is where the backend interacts with the databases.

### /api/business
This endpoint returns a list of businesses in the form:

**Output**
*GET /api/business/*
```
{
    "status": "success"
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

*GET /api/business/?bid=<business_id>*
This won't be fully functioning until we have businesses
```
{
    "status": "success"
    "business": {
            "id":
            "name":
            "area":
            "address":
            "business_type":
            "description":
            "url":
    }
}
```

### /api/deal
This endpoint returns a list of deals in the form:

**Output**
*GET /api/deal/*
```
{
    "status": "success"
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

*GET /api/deal/?did=<deal_id>*
This won't be fully functioning until we have deals
```
{
    "status": "success"
    "business": {
            "id":
            "name":
            "area":
            "address":
            "business_type":
            "description":
            "url":
    }
}
```

### /user/auth
Users are only authenticated with email.
Please cache this user to allow them to continue to use the site/app

- *CSRF cookies will need to be implemented soon!*
- *Google reCAPTCHA?*

**Input**
```
{
    "email":
    "name":
}
```

**Output**
```
{
    "status": "success"
    "user": {
        "name":
        "email":
    }
}
```
