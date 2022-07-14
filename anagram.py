string1=str(input("Enter first string"))
string2=str(input("ENter second string"))

lowered_String1 = string1.lower()
lowered_string2 = string2.lower()
if sorted(lowered_String1)==sorted(lowered_string2):
    print("The strings are anagram")
else:
    print("The strings are not anagram")
    

string1 = input("enter first string")
