# Deploy

Setup .aws credentials.

```console
npm install -g serverless
sls deploy
```

# Offline Dev

Set up your .aws credentials, make a DynamoDB table named jazz-charts-dev

Install node (to run serverless-offline). I use nvm to manage my node versions.

Go to your jazz-charts-api folder: 

`npm install`

`virtualenv -p python3 venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`sls wsgi serve -p 8000`

Run queries in Graphi at http://localhost:8000/graphql

## Run Tests

`TABLE_NAME=jazz-charts-test python -m pytest`

*Composer*

* getComposer

* getComposers

* createComposer

* updateComposer
 

*Song*

* getSong

* getSongs

* createSong

* updateSong

Example Query: 

```
{
  getComposer(id: "c1") {
    id
    fullName
    songs {
      id
      title
      chordChart
    }
  }
}
```

Example Response:

```
{
  "data": {
    "getComposer": {
      "id": "c1",
      "fullName": "Jerome Kern",
      "songs": [
        {
          "id": "1",
          "title": "All the Things You Are"
          "chordChart": "Db7#9 | % | C7#9 | % | F-7 | Bb-7 | Eb7 | AbMaj7 | DbMaj7 | G7 | CMaj7 | % | C-7 | F-7 | Bb7 | Ab-6 | EbMaj7 | F-7b5 | Bb7b5 | Ab-6 | EbMaj7 | G-7 | C7 | AbMaj7 | A-7b5 D7b9 | G-7 |C7 | F-7 C7 | F-7 Bb7 | Eb6 | F-7"
        }
      ]
    }
  }
}
```
