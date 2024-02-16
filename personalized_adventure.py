def generate_story(name, setting):
    story_templates = {
        "forest": f"One sunny day, {name} decided to explore a mysterious forest nearby. As they wandered deeper, they stumbled upon a hidden glade, shimmering with magical light. Suddenly, a wise old owl appeared, offering {name} a quest to find the lost treasure of the ancient elves.",
        "mountain": f"Under the light of a full moon, {name} set out to conquer the daunting peaks of the Dragon's Spine Mountains. Halfway up, they discovered a cave etched with ancient runes. Inside, a dragon lay sleeping on a pile of gold. With cunning and bravery, {name} navigated the cave, finding a mystical sword that belonged to the legendary hero of the lands.",
        "sea": f"{name} embarked on a journey across the high seas aboard the ship, The Marauder's Destiny. A storm brought them to an uncharted island, where they found a pirate's map leading to buried treasure. With the help of their crew, {name} braved the dangers of the island, uncovering the hoard of the infamous pirate Blackbeard."
    }

    return story_templates.get(setting, "The adventure awaits, but the path is yet unclear. Choose your setting wisely.")

def main():
    print("Welcome to your personalized adventure story!")
    name = input("What's your name? ")
    print("Where would you like your adventure to take place? [forest/mountain/sea]")
    setting = input().lower()

    story = generate_story(name, setting)
    print("\nYour Adventure Story:")
    print(story)

if __name__ == "__main__":
    main()
