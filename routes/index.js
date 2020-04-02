var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var mongo = require('mongodb').MongoClient;
var objectId = require('mongodb').ObjectID;
var url = require('url');
const { exec } = require("child_process");
var assert = require('assert');

//mongoose.connect('localhost:27017/test');
var url = 'mongodb://localhost:27017/test';

router.get('/', function(req, res, next) {

        res.render('index', {title: "Main project Page"});

});


router.get('/get-data', function(req, res, next) {
  var resultArray = [];
  
  mongo.connect(url, function(err, db) {
    assert.equal(null, err);
    var cursor = db.collection('user-data').find();
    cursor.forEach(function(doc, err) {
      assert.equal(null, err);
      resultArray.push(doc);
    }, function() {
      db.close();
      res.render('admin', {items: resultArray});

    });
  });
});


router.get('/admin-data', function(req, res, next) {
  
    const fs = require('fs');
    var filename = fs.readFile('./users.json', 'utf8', (err, jsonString) => {
    if (err) {
        console.log("File read failed:", err)
        return
    }
    
    
   
    console.log('File data:', jsonString) 
    res.redirect('/pages/admin.html');
})
  
  
});

    
router.post('/login', function(req, res, next) {

    mongo.connect(url, function(err, db) {
    
    var cursor = db.collection('user-data');
    var adminU = "stevemc";
    var adminP = "stevemc";
   cursor.findOne({ 
      'username': req.body.usernameLog,
      'password':req.body.passwordLog }, function(err, user) {
      
      if (user) {
          console.log(req.body.usernameLog);
          if(req.body.usernameLog == adminU && req.body.passwordLog == adminP ){
          res.render('admin');
          }
          else{
          res.redirect('/pages/streamPage.html');
          }
      }else {
       res.redirect('/');
         
        }
        
   })   
        
   });
   
});


  router.post('/delete', function(req, res, next) {
  var id = req.body.id;

  mongo.connect(url, function(err, db) {
    assert.equal(null, err);
    db.collection('user-data').deleteOne({"_id": objectId(id)}, function(err, result) {
      assert.equal(null, err);
      console.log('Item deleted');
      res.render('admin')
      db.close();
    });
  });
});

router.post('/register', function(req, res, next) {
  var fs = require('fs')
  var util = require('util')
  
  var myFormObject = {
      
    username: req.body.username,
    email: req.body.email,
    password: req.body.password  
  };

  fs.appendFileSync('./users.json', 'var obj = ' + util.inspect(myFormObject) , 'utf-8')
  mongo.connect(url, function(err, db) {
    assert.equal(null, err);
    db.collection('user-data').insertOne(myFormObject, function(err, result) {
      assert.equal(null, err);
      console.log('Item inserted');
      console.log(myFormObject);
      db.close();
    });
  });

  res.redirect('/');
});


module.exports = router;
