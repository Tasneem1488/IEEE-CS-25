# Keyboard layout
keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"

# Read inputs
direction = input()
typed_message = input()

# Determine the shift based on the direction
shift = -1 if direction == "R" else 1

# Decode the original message
original_message = "".join(keyboard[keyboard.index(c) + shift] for c in typed_message)

# Output the result
print(original_message)
