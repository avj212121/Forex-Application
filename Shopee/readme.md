# Forex application

This is a CRUD app based on MVC architecture to track exchange rates between country and uses Python , Mysql and Docker.

### Prerequisites

You only need Docker in your local machine to run this app.

```
For Windows - https://docs.docker.com/docker-for-windows/install/

For MAC - https://docs.docker.com/docker-for-mac/install/
```
### Running the app
```
1. Go to command line and cd to folder in which you have cloned the app.
2. Type docker-compose build to build the app. This will download all the requirements.
3. Type docker-compose up to run the app. 
```


### API documentation

```
Homepage - http://localhost/

Add the currencies - http://localhost/register
                          
Track the currencies - http://localhost/track
                       
Delete the currencies - http://localhost/delete
                        
```

### Assumptions

```
1. While registering, the app assumes current date when user adds two countries without date in the form.
2. User can update the rates for a particular date by going to the register link and re submitting the rate.
   The app will detect if it's a new request or an update request and respond accordingly. 
3. While registering it is mandatory to enter both countries but is not mandatory to enter date and rate.   
```

## Code walk through

```
webapp--
       |
       templates-- Contains all the html documents. (View in MVC)
       |
       __init__.py -- App and Db initialization
       |
       config.py - Contains configuration needed by app
       |
       controllers.py - Contains API routes. (Controller in MVC)  
       |
       forms.py - Defines forms used in app.
       |
       models.py - Contains db design. (Model in MVC)
       |
       requirements.txt - Contains requirements needed by app. Docker installs all these dependency. 
       |
       utils.py - Contains utility functions like calculating 7-day-average
|
docker-compose.yml - Defines how app and db image interact with one another
|
Dockerfile - Instructions to run the app.
|
run.py - Entrypoint of app.       
```

## Db design

```
App only contains one table i.e exchange_rates and it's structure can be found in models.py
```
