def first_last_three(s):
    if len(s) < 6:
        return s
    return s[:3] + s[-3:]

print(first_last_three("Python"))    # Виведе: "Python"
print(first_last_three("Ostrovsky"))  # Виведе: "Ostsky"
print(first_last_three("Ruslan"))         # Виведе: "Ruslan"
