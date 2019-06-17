# Model Deployment

Install packages with

```
source venv/bin/activate
pip install -r requirements.txt
```

Start flask with

```
python app.py
```

`POST` number to API with

```
curl --header "Content-Type: application/json" --request POST --data '{"number": 4}' 127.0.0.1:5000/predict
```

Alternatively, serve the flask module with gunicorn (as would done be done in production)

```
gunicorn -w 1 -b :5000 wsgi:application
```

NB: gunicorn isn't supported on windows, you will need to run this on linux or MacOS.

Finally, to run with docker

```
docker-compose build
docker-compose up -d
curl --header "Content-Type: application/json" --request POST --data '{"X": 5}' 0.0.0.0:5000/api/predict
docker-compose down --remove-orphans
```

