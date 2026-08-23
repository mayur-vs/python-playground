def lex_response(user_intent) :
    bot_responses = {
        "greeting" : "Hello! How can I help you today?",
        "order_status" : "Your order is out for delivery.",
        "goodbye" : "Thank you for using our service. Have a great day!"
    }

    return bot_responses.get(user_intent, "Sorry, I didn't understand that.")

response_to_user_intent = lex_response("greeting")
print(response_to_user_intent)