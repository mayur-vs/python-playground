bill_amount = float(input("Enter the bill amount: "))

gst_amount = bill_amount * 0.18  # Calculating 18% GST

total_amount = bill_amount + gst_amount

print(f"The total amount including 18% GST is: {total_amount:.2f}")