input_data = raw_input("Enter the string: ").lower()

print sum([(ord(c) - ord('a') + 1) for c in input_data])
