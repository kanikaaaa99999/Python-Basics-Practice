#indexing = accessing elements of a sequence using [] 
# [start : end : step]
credit_number = "1234-5678-9101-1121"
#print(credit_number[0]) #1
#print(credit_number[-1]) #1
#print(credit_number[0:4]) #1234
#print(credit_number[5:9]) #5678
#print(credit_number[0:]) #1234-5678-9101-1121
#print(credit_number[:4]) #1234
#print(credit_number[::2]) #13579111
#print(credit_number[::-1]) #1211-1019-8765-4321

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")