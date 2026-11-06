# ==========================================
# PROJECT: IDENTITY VERIFICATION SYSTEM
# DAY 01 - PYTHON FUNDAMENTALS
# ==========================================
#you can make a comment by click (cntrl+/)
print("="*45)
print("**Welcome to our Identity Verification System **")
print("="*45)
# ==========================================
# Store the user's personal information in variables.
gender=input("Please Enter your Gender(Mr/Ms) : \n")
first_name=input("Please Enter your first name: \n")
last_name=input("Please Enter your last name : \n")
# ==========================================
print("="*45)
print("             IDENTITY PROFILE")
print("="*45)
# ==========================================
# Use an f-string to insert variables directly into the output.
print (f"Hello {gender} {first_name} {last_name} ." )
print("\nIdentity profile created successfully.")
# ==========================================
print("=" * 45)
print("             END OF SESSION")
print("=" * 45)