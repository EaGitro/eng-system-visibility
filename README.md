

## pip installs


```sh
pip install flask gunicorn flask-cors
```

## local debug 

```sh
> python .\app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5050
```

local server: `http://127.0.0.1:5050`


## url 

```env
NEXT_PUBLIC_USER_WATCHING_URL="http://127.0.0.1:5050/"
```

## endpoints

```
/post/visibility/
```


```
./
|
+- health       # health point
|
+- post/
    |
    +- visibility/
    |   |
    |   +- <uid>    # visibility point: POST
    |
    +- click/
        |
        +- <uid>    # click point: POST

```