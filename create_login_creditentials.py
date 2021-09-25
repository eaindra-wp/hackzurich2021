import pandas as pd
from werkzeug.security import check_password_hash, generate_password_hash

# username_df = pd.DataFrame(columns = ['id','email', 'password', 'first_name', 'last_name', 'phone_number' ])

# username_df.loc[len(username_df.index)] = ["1", "test1@mail.com", generate_password_hash("test1"), "John", "Doe", "+41252533558"]
# username_df.index +=  1

# username_df.to_csv('user_signup_details.csv')
# print(username_df)

# open_username_csv = pd.read_csv('username_details.csv', index_col=0)
# new_row = {'id': len(open_username_csv.index) + 1, 'username':'stra', 'password':'ppp', 'date-of-birth': 'dsafsd'}
# open_username_csv = open_username_csv.append(new_row, ignore_index=True) 
# open_username_csv.to_csv("username_details.csv")

# open_username_csv = pd.read_csv('user_signup_details.csv')
# found_loggedin_user = open_username_csv.loc[(open_username_csv['email'].values == "test1@mail.com") & check_password_hash(open_username_csv['password'],"test1"), 'id'].values[0]
# print(found_loggedin_user)


username_df = pd.DataFrame(columns = ['id', 'user_id', 'insurance_id', 'date_of_birth', 'weight_in_kg', 'height_in_cm', 'blood_group','smoking','drinking','drinking_amount' ])

username_df.loc[len(username_df.index)] = ["1", "1", "025525663", "1996-10-03", "98", "192", "A", "Yes", "Yes", ]
username_df.index +=  1

username_df.to_csv('user_signup_details.csv')
print(username_df)