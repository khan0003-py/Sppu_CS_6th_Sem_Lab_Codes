const express = require('express');
const bodyParser = require('body-parser');
const MongoClient = require('mongodb').MongoClient;

const app = express();
app.use(bodyParser.json());

const url = 'mongodb://localhost:27017';
const dbName = 'myDatabase';

let db;
MongoClient.connect(url, { useNewUrlParser: true }, (err, client) => {
  if (err) return console.error(err);
  db = client.db(dbName);
  app.listen(3000, () => {
    console.log('Listening on port 3000');
  });
});

app.post('/register', (req, res) => {
  db.collection('users').insertOne(req.body, (err, result) => {
    if (err) return console.error(err);
    res.send({ message: 'User registered' });
  });
});

app.post('/login', (req, res) => {
  db.collection('users').findOne(req.body, (err, result) => {
    if (err) return console.error(err);
    res.send({ message: 'Welcome ' + result.username + '!' });
  });
});