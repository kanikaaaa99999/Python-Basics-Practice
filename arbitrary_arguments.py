
# *args = allows you to pass multiple non-key arguements to a function
#         *args is a tuple of all the arguments passed to the function
#         **kwargs = allows you to pass multiple keyword arguments to a function
#                    **kwargs is a dictionary of all the keyword arguments passed to the function

#example:
#def add(*args): 
 # total = 0
  #for arg in args:
   # total += arg
 # return total
#print(add(2, 3, 3, 5 ))

# ----------------------------------------------------

#def display_name(*args):
#    for arg in args:
#        print(arg, end=" ")

#display_name("the", "kanika", "sharma", "III")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_address(street="123 Main St",
              apt="4B",
              city="Anytown",
              state="CA",
              zip="12345")

