# Offline Dev

`virtualenv -p python3 venv`

`npm install`

`pip install -r requirements.txt`

`sls wsgi serve -p 8000`

Test queries in Graphi at http://localhost:8000/graphql

Example Response

```
{
  "data": {
    "getSong": {
      "composer": {
        "id": "c1",
        "name": "Jerome Kern"
      },
      "id": "1",
      "title": "All the Things You Are"
    }
  }
}
```

```
{
  "data": {
    "getComposer": {
      "id": "c1",
      "name": "Jerome Kern",
      "songs": [
        {
          "id": "1",
          "title": "All the Things You Are"
        }
      ]
    }
  }
}
```