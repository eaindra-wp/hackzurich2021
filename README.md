# HealthYou
In Switzerland, many medical records are saved on paper, so delays in diagnosis and resource planning happen. Our centralized data platform enables users to share their data with health care providers.

-------
## Front-end

We used `JavaScript`, `HTML`, `CSS` as well as `Bootstrap` to create a graphical user interface fo the user to sign up, login, show health-related updates and other interesting features. 

## Back-end
We set up a [`Flask`](https://flask.palletsprojects.com/en/2.0.x/) server to save the user input data and then output relevant information or predictions. We also integrated an OCR functionality to interpret handwritten or printed medical documents using `Python` and Google's `Pytesseract` library.


## ML/Data Science
We leveraged `Tensorflow`, `Keras`, and a LOT of research to build a predictive model that not only takes into account a user's health and daily habits, but also leverage the Switzerland's open data to generate and augment health data in order to build the best possible immediately available predictive model.

---------

### File Directory
Below is a short summary of the folders in this repository.
* hackzurich2021
    * [flaskr](./flask) --> main folder for this web application built by Flask. 
        * [static](./flask/static) -->
        Here, the CSS files, local files required to render on the view are saved under this folder.
            * [css](./flask/static/css)
            * [fonts](./flask/static/fonts)
            * [img](./flask/static/img)
            * [js](./flask/static/js)
     
        * [templates](./flask/templates) --> The HTML source codes for the views are placed here
            * [auth](./flask/templates/auth)
            * [home](./flask/templates/home)
            * [ocr](./flask/templates/ocr)
    * [model_training_testing](./model_training_testing) --> Contains all training and testing algorithms to build a neural model, which will predict the life expectation of the user in the long run.
    * [user_profile_details.csv](./user_profile_details.csv)  --> Here, the health-related details of each signed up user will be saved in this .csv file. 
    * [user_signup_details.csv](./user_signup_details.csv) --> Here, the sign-up and log-in credentials of the user will be saved. 
    
### Pre-requisites
You will need to install python packages like `Tensorflow`, `Flask` via `pip` to run this application successfully. More information to host and run this Flask application can be found here: https://flask.palletsprojects.com/en/2.0.x/
