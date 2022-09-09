import emoji

input=input("Enter something: ")

def greet(name, input):
    print(emoji.emojize("Hi "+ input + ". "+ name +":green_heart:")) #% input))

if input=="you":
   greet(input, "- it's a reversed order")
else:
#   print("Hey %s" % input)
   greet("All is", input)
