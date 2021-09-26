import numpy as np
import tensorflow
from tensorflow import keras

# columns (almost all are one hot encoded, see this example for details)
dummy_user = [75.2, # weight in kg
              167.5, # height in cm
              0, 1, # isFemale, isMale (only one should be 1)
              0, 0, 0, 1, 0, 0, 0, # Diet_Carnivore, Diet_Intermittent Fasting, Diet_Keto, Diet_Mediterranean, Diet_Paleo, Diet_Vegan/Plant-Based, Diet_Vegetarian (again, only one should be 1),
              0, 1, # 'Daily water intake_Less than recommended', 'Daily water intake_Normal'  (only one should be 1)
              1, 0, 0, # 'Smoking Frequency_Ex-smoker', 'Smoking Frequency_Never smoked', 'Smoking Frequency_Regular smoker' (only one 1, rest 0s)
              0, 0, 0, 0, 1, # 'Alcohol_<15g alcohol per day', 'Alcohol_>50g alcohol per day', 'Alcohol_Abstainer/rare drinker', 'Alcohol_Between 15g and 50g alcohol per day', 'Alcohol_Weekly drinker', (only one 1, rest 0s)
              1, 0, 0, 0, # 'Hours of Sleep_6 to 8 hours per night', 'Hours of Sleep_8 to 10 hours per night', 'Hours of Sleep_Less 6 hours per night', 'Hours of Sleep_More than 10 hours per night' (only one 1, rest 0s)
             ]
# if needed, writing a function to do this is not hard, just a bunch of if/elses

health_model = keras.models.load_model("health_outcome_model")
predicted_lifespan_years = health_model.predict(np.array(dummy_user).reshape((1, -1)))[0][0]

print(predicted_lifespan_years)