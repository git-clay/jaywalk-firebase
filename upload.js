var firebase = require("firebase")
import * as firebase from "firebase";

// Initialize Firebase
var config = {
  apiKey: "AIzaSyD5JZLxrwPRWO5Wq02GMo7V4Yxsc_pQsO8",
  authDomain: "jaywalk-8a738.firebaseapp.com",
  databaseURL: "https://jaywalk-8a738.firebaseio.com",
  storageBucket: "jaywalk-8a738.appspot.com",
  //   messagingSenderId: "1042841275273"
};
firebase.initializeApp(config);

// Cloud storage variables
// Docs: https://firebase.google.com/docs/storage/web/start
var storage     = firebase.storage(),
    storageRef  = storage.ref()
    // imagesRef  = storageRef.child('images')

/*
Once you've created an appropriate reference, 
you then call the put() method. 
put() takes files via the JavaScript 
File and Blob APIs and uploads them to Cloud Storage.
*/
var file = ... // use the Blob or File API
ref.put(file).then(function(snapshot) {
  console.log('Uploaded a blob or file!');
});

/*
In addition to the File and Blob types, 
put() can also upload a Uint8Array to Cloud Storage.
*/
// Uint8Array
var bytes = new Uint8Array([0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64, 0x21]);
ref.put(bytes).then(function(snapshot) {
  console.log('Uploaded an array!');
});

/*
If a Blob, File, or Uint8Array isn't available, 
you can use the putString() method to upload a raw, 
base64, base64url, or data_url encoded string to Cloud Storage.
*/
// Raw string is the default if no format is provided
var message = 'This is my message.';
ref.putString(message).then(function(snapshot) {
  console.log('Uploaded a raw string!');
});

// Base64 formatted string
var message = '5b6p5Y+344GX44G+44GX44Gf77yB44GK44KB44Gn44Go44GG77yB';
ref.putString(message, 'base64').then(function(snapshot) {
  console.log('Uploaded a base64 string!');
});

// Base64url formatted string
var message = '5b6p5Y-344GX44G-44GX44Gf77yB44GK44KB44Gn44Go44GG77yB';
ref.putString(message, 'base64url').then(function(snapshot) {
  console.log('Uploaded a base64url string!');
});

// Data URL string
var message = 'data:text/plain;base64,5b6p5Y+344GX44G+44GX44Gf77yB44GK44KB44Gn44Go44GG77yB';
ref.putString(message, 'data_url').then(function(snapshot) {
  console.log('Uploaded a data_url string!');
});

/*
Metadata (name, size, contentType)Cloud Storage automatically 
infers the content type from the file extension where the file 
is stored on disk, but if you specify a contentType in the 
metadata it will override the auto-detected type.
*/
// Create file metadata including the content type
var metadata = {
  contentType: 'image/jpeg',
};

// Upload the file and metadata
var uploadTask = storageRef.child('images/mountains.jpg').put(file, metadata);

/*
pause, resume, cancel uploads
*/
// Upload the file and metadata
var uploadTask = storageRef.child('images/mountains.jpg').put(file);
// Pause the upload
uploadTask.pause();
// Resume the upload
uploadTask.resume();
// Cancel the upload
uploadTask.cancel();
/*
observe upload
*/
var uploadTask = storageRef.child('images/rivers.jpg').put(file);

// Register three observers:
// 1. 'state_changed' observer, called any time the state changes
// 2. Error observer, called on failure
// 3. Completion observer, called on successful completion
uploadTask.on('state_changed', function(snapshot){
  // Observe state change events such as progress, pause, and resume
  // Get task progress, including the number of bytes uploaded and the total number of bytes to be uploaded
  var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
  console.log('Upload is ' + progress + '% done');
  switch (snapshot.state) {
    case firebase.storage.TaskState.PAUSED: // or 'paused'
      console.log('Upload is paused');
      break;
    case firebase.storage.TaskState.RUNNING: // or 'running'
      console.log('Upload is running');
      break;
  }
}, function(error) {
  // Handle unsuccessful uploads
}, function() {
  // Handle successful uploads on complete
  // For instance, get the download URL: https://firebasestorage.googleapis.com/...
  var downloadURL = uploadTask.snapshot.downloadURL;
});

