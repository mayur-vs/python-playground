company = {"emp1": {"name": "Ravi", "role": "Dev"}, "emp2": {"name": "Pooja", "role": "HR"}}

# Dictionary Chain Indexing hum nested dictionary mein use karte hain
# Ek bada locker (Company) hai. Uske andar chhote lockers (Employee ID) hain. Aur un chhote lockers ke andar unka personal data (Name, Role) hai.
# Access kaise karein? Ek ke baad ek chabhi lagate jao! (Chain indexing).
# Agar data = {"user": {"address": "Pune"}} hai, 
# toh "Pune" tak pahunchne ke liye hum likhte hain: data["user"]["address"]. Pehle bahar wale locker ki chabhi, fir andar wale ki!

for employee_id in company :
    print(company[employee_id]["role"])