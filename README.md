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
