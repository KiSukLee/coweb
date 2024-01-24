
//use callbacks to attach handlers to dynamically generated elements
//can achieve this by restating the code for the new content after its creation
//or by creating functions and calling on them to avoid redundancy

//AJAX (Asynchronous JavaScript and XML) - front-end JavaScript that allows page
//to interact with database without freshing the page (useful for forms)

    //Fetch method - makes a GET request to API server, and "get" data sent back
    //can achieve this via Promise or Async/Await

    //Promise - looks similar to a chain reaction; uses arrow functions

    fetch("https://api.github.com/users/adion81")
        .then(response => response.json())
        .then(coderData => console.log(coderData))
        .catch(err => console.log(err))
    
    //POST Requests w/ Fetch

        var myForm = document.getElementById('myForm');
        myForm.onsubmit = function(e){
            e.preventDefault();
            var form = new FormData(myForm);
            //use fetch to send form data to server
            fetch('http://localhost:5000/create/user',{method:'POST', body:form})
                .then(response => response.json())
                .then(data => console.log(data))
        }
        //controller file/views.py file
        //request.form
    
    //Async/Await - wait for data to come back 

    async function getCoderData(){
        //await keyword lets js know that it need to wait for a response before continuing
        var response = await fetch("https://api.github.com/users/adion81");
        //need to convert data into JSON format
        var coderData = await response.json();
        return getCoderData;
    }
    console.log(getCoderData());

    //JSON - JavaScript Object Notation is a lightweight format for storing and transporting data
    //data is stored in key:value pairs and can be accessed using either square or dot notation
    
    //API - Application Programming Interface
    //Hiding APIs - install pipenv install python-dotenv and create .env file with server.py
    //declare variables in .env - FLASK_APP_API_KEY = ...
    //access variables with os module anywhere in project - print(os.environ.get("FLASK_APP_API_KEY"))

    //controller/views.py file
    //import request
    //import os
    //r = request.get(f"https:api.information.com/{os.environ.get('FLASK_API_KEY')}")
    //return jsonify(r.json())

    //From Front-End to Back-End
    
    //index.html
    //<form id="searchForm" onsubmit="search(event)">
    //  <input type='text' name='query'>

    //script.js
    //same as example code under POST requests w/ FLASK

    //controller/views.py file

    //import requests, os
    //from flask import jsonify, requests
    //app_route/view_function(methods=["POST"]):
    //  r = request.get(f"https:api.information.com/{os.environ.get('FLASK_API_KEY')/search?={request.form['query']}"})
    //  return jsonify(r.json())



//jQuery for Forms
    //.submit() - can be used as an event handler or as an eventof a form being submitted

    $('form').submit(function(){
        alert("you submitted me!");
    })

    //return false
    //can prevent form from being submitted by just returning false

    $('form').submit(function(){
        return false;
    })

    //.serialize() - encodes a set of form elements into computer-friendly array
    //transforms data that user inputs into format that can easily be passed to a back-end process
