import re, random 
destinations = {
    "beaches": ["Lakshyadweep", "Mumbai", "Goa"],
    "mountains" : ["Himalayas","Rocky MAountains", "Sahyadri"],
    "cities": ["Delhi","Chennai","Patna"]
}
jokes = [
    "What don't programmer like nature ? Too many bugs",
    "Why did the computer don not go to Doctor ? because it had a virus "
    "Why do traveller always fell warm ? because of all their hot spots"
]
def normalize_input(text):
 return re.sub(r"\s +"," ",text.strip().lower())
def recommend():
 print("Travel Bot : beaches, mountains, cities")
 preference = input("you:")
 preference = normalize_input(preference)
 if preference in destinations:
  suggestion = random.choice(destinations[preference])
  print("Travel Bot : Do you like it Yes or No ?")
  answer = input("You :").lower()
  if answer == "yes":
   print("Travel bot : Awesome ! Enjoy !", suggestion)
  elif answer == "no":
   print("Travel bot :Let's try another. Enjoy !")
   recommend()
  else:
   print("Travel bot : I will suggest again")
   recommend()
 else:
  print("Travel Bot : Oh Sorry ! I don't have that type of destination !")
 show_help()
def packing_tips():
 print("Travel bot : Where to ?")
 location = normalize_input(input("You :"))
 print("Travel Bot : How many days ?")
 days = input("You : ")
 print("Travel Bot : Packing tips for", days,"days in ", location)
 print("Pack Versatile Clothes")
 print("Pack Cahrgers and Adapters")
 print("Keep your Official Document with you")
 print("CHeck weather forecat of your destination")
def tell_joke():
 print("Travel Bot : ", random.choice(jokes))
def show_help():
    print("\nI can:")
    print("- Suggest travel spots (say 'recommendation')")
    print("- Tell a joke (say 'joke')")
    print("Type 'exit' or 'bye' to end.\n")
def chat():
    print("Hello! I'm TravelBot.")
    name = input("Your name? ")
    print(f"Nice to meet you, {name}!")
    
    show_help()
    
    while True:
        user_input = input(f"{name}: ")
        user_input = normalize_input(user_input)
        
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print("TravelBot: Safe travels! Goodbye!")
            break
        else:
            print("TravelBot: Could you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chat()