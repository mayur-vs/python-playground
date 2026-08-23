# Bhai ab hum us format mein enter kar rahe hain, jo puri duniya ke internet ko chalata hain
# Chahe AWS Lambda use karo, Amazon Lex or Kisi database se data nikalo
# Data hamesha hamesha "List of Dictionaries" - AP/JSON format mein travel karta hai
# Real-world API ka data exactly List of Dictionaries mein aata hain
# Data mangwa toh liya vo list of dictionaries mein hain, 
# par ab is list ke andar chhipe hue lockers (dictionaries) mein se specific data kaise nikalein?

employees = [{"name" : "bill", "salary" : 40000}, {"name" : "gates", "salary" : 50000}, {"name" : "wonder", "salary" : 30000}]

for employee in employees :
    print(employee["name"])