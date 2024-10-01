name = input("Hello there, what is your name?")
age = input(f"How old are you, {name}?") 
greeting = input(f"Hello there {name}! How can I help you today?")
print("1. Exit\n 2. N/A\n 3. N/A\n 4. N/A")
choice = input(f"Please choose one of the folliwng options, {name}!")
if choice == '1':
  print(f"Goodbye {name}, I hope I could help you to the best of my ability!")
  break
else:
  continue

