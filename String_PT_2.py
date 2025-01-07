# Accepting a string
st = input("Enter a string: ")

# Display each word and its length
x = st.split()
for w in x:
    l = len(w)
    print("Word:", w, "\tLength:", l)

# Reversing the case of each character using a while loop
st2 = ""  # Initialize the modified string
i = 0     # Initialize the index variable

while i < len(st):
    if st[i].isupper():
        st2 += st[i].lower()
    elif st[i].islower():
        st2 += st[i].upper()
    else:
        st2 += st[i]  # Preserve non-alphabetic characters as is
    i += 1  # Increment the index

print("Original String:", st)
print("String with Reversed Case:", st2)
