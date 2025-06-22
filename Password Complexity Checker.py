import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("🔸 Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("🔸 Add uppercase letters.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("🔸 Add lowercase letters.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("🔸 Include numbers.")

    if re.search(r"[@$!%*#?&]", password):
        strength += 1
    else:
        feedback.append("🔸 Add special characters (@, #, etc.).")

    # Result based on strength
    if strength == 5:
        result = "✅ Strong Password"
    elif 3 <= strength < 5:
        result = "⚠️ Moderate Password"
    else:
        result = "❌ Weak Password"

    return result, feedback

# Main program
password = input("Enter your password: ")
result, feedback = check_password_strength(password)

print("\nPassword Strength:", result)
if feedback:
    print("Suggestions:")
    for f in feedback:
        print(f)
