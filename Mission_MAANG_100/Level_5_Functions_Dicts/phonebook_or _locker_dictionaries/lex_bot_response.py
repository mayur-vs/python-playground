'''
2. Dictionaries ({key: value}) - APIs aur Amazon Lex ka Foundation
Concept: Dictionary bilkul ek Phonebook ki tarah hoti hai. Aapko kisi ka number chahiye, toh aap uska naam (Key) dhundhte ho, aur aapko uska number (Value) mil jata hai.
Kyun seekhna hai? Jab aap APIs create karoge ya Amazon Lex (Bot) se response bhejoge/mangaoge, toh saara data hamesha ek Dictionary (JSON format) mein hi travel karta hai!
'''

# Chalo ek phonebook banate hain iska matlab ek dictionary banate hain
# phonebook mein/dictionary mein hamesha key ka value string mein rahta tha

lex_bot_response = {
    "intent_name" : "BookHotel",
    "status" : "Success",
    "confidence_score" : 90 
}

# Phonebook se number nikalna matlab dicionary se value nikalna
print("Bot ne ky bola?", lex_bot_response["status"])