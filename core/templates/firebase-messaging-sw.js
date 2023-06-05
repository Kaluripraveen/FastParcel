importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-messaging.js");


firebase.initializeApp({
    apiKey: "AIzaSyBaVv-hizbvmYmfR59ZOGxTSup1SkgXvk0",
    authDomain: "fastparcel-c7202.firebaseapp.com",
    projectId: "fastparcel-c7202",
    storageBucket: "fastparcel-c7202.appspot.com",
    messagingSenderId: "551686917895",
    appId: "1:551686917895:web:5b1681ac54ef65807b3fa2"
})

const messaging = firebase.messaging();