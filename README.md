# sharebite
### This file describes how to download and use the application based on the specifications given in the Sharebite Challenge PDF
### An ER diagram can be found in the sharebite folder 

### Project Requirements/Specifications 
- The application has all the CRUD operations related to Section,Item and Modifiers 
- The specification to display the whole menu is taken care by /api/section 
- A modifer can be added/modified  to an item with either the POST/PUT/PATCH for an item and hence no additional end points is required to take care of all modifications 
- A swagger UI is provided to test out all the API endpoints and also for the API Specifications

### Installation and Usage 
- install all the packages mentioned in the requirements.txt 
- install postgresql 
- add a .env file for your database credentials
- then run the following commands 
  - python manage.py migrate
  - python manage.py runserver 8100
  - python manage.py createsuperuser and add the required credentials
- then you can go to http://127.0.0.1:8100/swagger/ and get the api-token from /api/api-token-auth
- use the api to authorize in the swagger UI and try out all the APIs

### Test and Examples 
- I have tested out a few happy paths and sad paths. Postman request-response collection has been added for the same

#### Note: Please contact me at ranjana.seshadri@tamu.edu/ranjana.seshadri@gmail.com if any additional details/clarifications is required


