swapping current db with firebase
uses the pyrebase python3 library

$ npm install -g firebase-tools
$ firebase login   # login
$ firebase init    # Generate a firebase.json (REQUIRED)
$ firebase serve   # Start development server

Docs for cloud storage:
https://firebase.google.com/docs/storage/web/start

look into cloud functions
https://firebase.google.com/docs/functions/




## hidden variables
Do not forget to create .env file with
apiKey (for firebase)
authDomain (for firebase)
databaseURL (for firebase)
storageBucket (for firebase)
project_id (for kinetise)
token (for kinetise)

Also, you need a serviceAccount.json for firebase authentication