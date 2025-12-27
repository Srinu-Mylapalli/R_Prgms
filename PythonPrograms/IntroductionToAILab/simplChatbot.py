import random as rd
def get_response(message):
    greetings=['hello','hi','hey','howdy']
    farewells=['bye','goodbye','see you','takecare']
    compliments=['nice','great','awesome','cool']
    message=message.lower()
    if any(word in message for word in greetings):
        return "hello! how can I help you today?"
    elif any(word in message for word in  farewells):
        return "good bye! have a nice day"
    elif any(word in message for word in compliments):
        return "thank you! I am here to assist you"
    else:
        return "I am sorry,I don't understand. Can you please rephrase"


def main():
    print("chatbot: hello I'm your simple chatbot.'bye' to exit")
    while True:
        user_input=input("you: ")

        if user_input.lower()=='bye':
            print("chatbot: good bye! have a great day!")
            break




        response=get_response(user_input)
        print("chatbot: ",response)


if __name__=="__main__":
    main()
