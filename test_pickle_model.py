import pickle

with open("my_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

def get_drug(value:float) -> str:
    match value:
        case 0.0: return "A"
        case 1.0: return "B"
        case 2.0: return "C"
        case 3.0: return "X"
        case 4.0: return "Y"
        case _: return ""

# Age	Sex	BP	Cholesterol	Na_to_K	Drug
# 0	23	0	2.0	1.0	25.355	4.0
# 1	47	1	0.0	1.0	13.093	2.0
# 2	47	1	0.0	1.0	10.114	2.0
# 3	28	0	1.0	1.0	7.798	3.0
# 4	61	0	0.0	1.0	18.043	4.0 
def predict():
    try:
        age = int(input("Enter age: "))
        sex = int(input("Enter sex (0 or 1): "))
        bp = float(input("Enter bp (1,2 or 3): "))
        chol = float(input("Enter cholestrol (0-30): "))
        Na_to_k = float(input("Enter na_to_k (0,1,2,3 or 4): "))

        pred = loaded_model.predict([[age,sex,bp,chol,Na_to_k]])
        print(f"Model predicts drug {get_drug(pred)}")
    
    except Exception as e:
        print(e)

while True:
    print("1. Make prediction?")
    print("2. Quit")

    user_choice = input("Enter choice: ")

    if user_choice == "1": predict()
    if user_choice == "2": break

# predictions = loaded_model.predict([[20, 0, 1.0, 18.234, 3.0]])
# print(predictions)



