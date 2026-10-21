import random


def play_mad_libs():
    print("\n--- NEW MAD LIBS STORY ---")

    templates = [
        # Hospital Template 
        "It was about {0} {1} ago when I arrived at the hospital in a {2}. "
        "The hospital is a/an {3} place, there are a lot of {4} {5} here. "
        "There are nurses here who have {6} {7}. "
        "If someone wants to come into my room I told them that they have to {8} first. "
        "I’ve decorated my room with {9} {10}. "
        "Today I talked to a doctor and they were wearing a {11} on their {12}. "
        "I heard that all doctors {13} {14} every day for breakfast. "
        "The most {15} thing about being in the hospital is the {16} {17}!",

        # Camping Template 
        "This weekend I am going camping with {0}. "
        "I packed my lantern, sleeping bag, and {1}. "
        "I am so {2} to {3} in a tent. "
        "I am {4} we might see a(n) {5}, I hear they’re kind of dangerous. "
        "While we’re camping, we are going to hike, fish, and {6}. "
        "I have heard that the {7} lake is great for {8}. "
        "Then we will {9} hike through the forest for {10} {11}. "
        "If I see a {12} {13} while hiking, I am going to bring it home as a pet! "
        "At night we will tell {14} {15} stories and roast {16} around the campfire!!",

        # Castle Template 
        "Dear {0}, I am writing to you from a {1} castle in an enchanted forest. "
        "I found myself here one day after going for a ride on a {2} {3} in {4}. "
        "There are {5} {6} and {7} {8} here! "
        "In the {9} there is a pool full of {10}. "
        "I fall asleep each night on a {11} of {12} and dream of {13} {14}. "
        "It feels as though I have lived here for {15} {16}. "
        "I hope one day you can visit, although the only way to get here now is {17} on a {18} {19}!!",
    ]

    #Prompts in each template
    hospital_prompts = [
        "Number",
        "Measure of time",
        "Mode of Transportation",
        "Adjective",
        "Adjective2",
        "Noun",
        "Color",
        "Part of the Body",
        "Verb",
        "Number2",
        "Noun2",
        "Noun3",
        "Part of the Body 2",
        "Verb2",
        "Noun4",
        "Adjective3",
        "Silly Word",
        "Noun5",
    ]

    camping_prompts = [
        "Proper Noun (Person's Name)",
        "Noun",
        "Adjective (Feeling)",
        "Verb",
        "Adjective (Feeling) 2",
        "Animal",
        "Verb2",
        "Color",
        "Verb (ending in ing)",
        "Adverb (ending in ly)",
        "Number",
        "Measure of Time",
        "Color2",
        "Animal2",
        "Number2",
        "Silly Word",
        "Noun2",
    ]

    castle_prompts = [
        "Proper Noun (Person's Name)",
        "Adjective",
        "Color",
        "Animal",
        "Place",
        "Adjective2",
        "Magical Creature (Plural)",
        "Adjective3",
        "Magical Creature (Plural) 2",
        "Room in a House",
        "Noun",
        "Noun2",
        "Noun (Plural) 3",
        "Adjective4",
        "Noun (Plural) 4",
        "Number",
        "Measure of time",
        "Verb (ending in ing)",
        "Adjective5",
        "Noun5",
    ]

    #Use random library to select a template 
    choice = random.randint(0, 2)
    selected_template = templates[choice]

    #Match the selected index to its prompt list
    if choice == 0:
        current_prompts = hospital_prompts
    elif choice == 1:
        current_prompts = camping_prompts
    else:
        current_prompts = castle_prompts

    #Collecting  inputs,,
    user_words = []
    for prompt in current_prompts:
        word = input(f"Type a/an {prompt}: ")
        user_words.append(word)

    #Format and print the full story
    story = selected_template.format(*user_words)

    print("\n" + "=" * 50)
    print("HERE IS YOUR FULL STORY:")
    print("=" * 50)
    print(story)
    print("=" * 50 + "\n")


# Main game loop
print("Welcome to the Mad Libs Game!")

keep_playing = True
while keep_playing:
    play_mad_libs()

    user_choice = input("Do you want to play again? (yes/no): ").lower()
    if user_choice != "yes" and user_choice != "y":
        keep_playing = False
        print("Thanks for playing! Goodbye.")