import pickle
var = input("Enter the news which is to be verified!")
print("You entered: " + str(var))


# function to run for prediction
def fakenews(var):    
# retrieving the best model for prediction call
    load_model = pickle.load(open('model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    return (print("The given statement is ",prediction[0]),
        print("The truth probability score is ",prob[0][1]))


if name == 'main':
    fakenews(var)
