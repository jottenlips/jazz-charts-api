# Offline Dev
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