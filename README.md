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

### /api/businesses
This endpoint returns a list of businesses in the form:

**Output**
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

### /auth/
Users are only authenticated with email.
Please cache this user to allow them to continue to use the site/app
**CSRF cookies will need be implemented soon!**

**Input**
```
{
    email:
    name:
}
```
