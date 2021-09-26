# DigitalTwin for SWICA
In Switzerland, most of the medical records are still saved on the paper. This could lead us to delays in diagnosis and resource planning. Hence, a centralized data platform called DigitalTwin is created to overcome such problems and enable the users to share their data with health care providers.

-------
## Front-end

We used `JavaScript`, `HTML`, `CSS` as well as `Bootstrap` to create a graphical user interface. 

## Back-end
We set up a [`Flask`](https://flask.palletsprojects.com/en/2.0.x/) server to save the user input data and then output relevant information or predictions. We also integrated an OCR functionality to interpret handwritten or printed medical documents using `Python` and Google's `Pytesseract` library.


## ML/Data Science
We leveraged `Tensorflow`, `Keras`, and a LOT of research to build a predictive model that not only takes into account a user's health and daily habits, but also leverage the Switzerland's open data to generate and augment health data in order to build the best possible immediately available predictive model.

---------

## File Directory

* hackzurich2021
    * [flaskr](./tree-md) 
    * [model_training_testing](./model_training_testing)
    * [user_profile_details.csv](./user_profile_details.csv)  
    Here, the health-related details of each signed up user will be saved in this .csv file. 
    * [user_signup_details.csv](./user_signup_details.csv)
    Here, the sign-up and log-in credentials of the user will be saved. 
    