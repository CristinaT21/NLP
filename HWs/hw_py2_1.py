import requests

API_KEY = "5388835749:AAG842MSsPIwephsraQHfiFRfwUKOr8o5Bw"
CHAT_ID = "745644608"
SEND_MESSAGE_URL_TEMPLATE = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHAT_ID}&text="

def evaluate_expression(expression):
    try:
        result = str(eval(expression))
    except SyntaxError:
        result = "Cannot evaluate expression.\n"
    return result

while True:
    user_input = input("Enter your expression:\n")
    print("The result is:\n")
    response = requests.get(SEND_MESSAGE_URL_TEMPLATE + evaluate_expression(user_input))
    print(response.json())
    