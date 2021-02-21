# Project details

The project is built in Django 3.1 and is a simple web app where the user enters some words and those words are shown in alphabetic order.

## The views.py

### **index view**

The HTML template 'index.html' is rendered. This is where all JavaScript runs.

### **api view**

This is the view of the **API** endpoint. Three main things happen here:

1. The view ensures only a POST method is valid, otherwise a _405 Method not allowed_ is returned.
2. Data validation. It ensures that an array of strings is provided as a payload, otrherwise a 400 status is returned.
3. The response, which is a Json response, returns a sorted array of strings. The sorting takes place using the _Quicksort_ algorithm without the use of libraries or built-in functions.

## The HTML template

### **index.html**

This is the home page template. It has a form with a textarea and a button and a div where the results are shown. The _tailwindcss_ framework is used for the styling.

### **main.js**

Most of the home page functionality is here:

- When the _Submit_ button is pressed it triggers an asyncronous function that takes the data from the textarea and cleans them up.
- Then it sends the data with a POST method to the API endpoint and gets the results.
- The fetching of the data is made by the _fetchData_ function.
- While the data is being fetched the Submit button is disabled (with the _disableButton_ function) and the text is updated to 'Loading...'.
- Also the list with the results is cleanded up in case it was populated from a previous use of the page (_clearLiElements_ function).
- After the data is received the list with the ordered words is populated with the _populateList_ function
- In the end the _Submit_ button is re-enabled in its original state.
