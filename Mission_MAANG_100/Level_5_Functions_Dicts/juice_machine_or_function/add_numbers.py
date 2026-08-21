'''
1. Functions (def) - AWS Lambda ka Foundation
Concept: Function ek "Juice Machine" ki tarah hota hai. Aap usme fruit daalte ho (Input/Parameters), machine apna kaam karti hai (Logic), aur aapko juice nikal kar de deti hai (Output/Return).
Kyun seekhna hai? Kyunki AWS Lambda mein code hamesha ek "Function" ke andar hi likha jata hai (jise lambda_handler kehte hain).
'''

# Ek Function Banate hain, iska matlab hee function ko define karna hota hain
def add_numbers(number_one, number_two) :
    total = number_one + number_two
    return total

# Ab juice machine ko use karte hain, iska matlab hee function ko call karte hain
result = add_numbers(223, 2)
print(result)

# So pro developer ek he code ko baar baar nhi likte hain, isliye vo function likte hain, so jab zarurat padega tab vo usse call karte hain
# Jaise code ko bar bar chalane keliye hum loop use karte hain, waisa