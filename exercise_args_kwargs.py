
def shipping_label(*args , **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()  # for a new line after printing args
    if "apt" in kwargs:
       print(f"{kwargs.get('street')} {kwargs.get('apt')}")  
    else:
         print(f"{kwargs.get('street')}")   
    print(f"{kwargs.get('city')} , {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("dr.", "kanika", "sharma", "III",
               street="123 Main St",
               apt="#4B",
               city="Anytown",
               state="CA",
               zip="12345")