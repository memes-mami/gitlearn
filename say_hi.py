import random
import time

animals = [
    "dog 🐶", "cat 🐱", "lion 🦁", "tiger 🐯", "elephant 🐘",
    "giraffe 🦒", "monkey 🐒", "zebra 🦓", "panda 🐼", "penguin 🐧",
    "octopus 🐙", "dolphin 🐬", "shark 🦈", "parrot 🦜", "frog 🐸",
    "cow 🐄", "sheep 🐑", "chicken 🐔", "unicorn 🦄 (shhh, secret!)"
]

greetings = [
    "Yo", "Hey there", "Howdy", "What’s up", "Greetings",
    "Aloha", "Namaste", "Hola", "Bonjour", "Sup"
]

def say_hi_to_animals():
    print("🌍 Welcome to the Ultimate Animal Greeting Program 🐾\n")
    time.sleep(1)
    
    for animal in animals:
        greet = random.choice(greetings)
        print(f"{greet}, {animal}!")
        time.sleep(0.4)
    
    print("\n🎉 All animals have been greeted! Mission complete. 🐾")

if __name__ == "__main__":
    say_hi_to_animals()
