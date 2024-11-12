def create_keyboard_map():
    keyboard_map = {}
    
    keyboard = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', '*', 'H', 'J', 'K', 'L'],
        [' ', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ' ', ' ']
    ]

    for i in range(len(keyboard)):
        for j in range(len(keyboard[i])):
            keyboard_map[keyboard[i][j]] = (i, j)
    return keyboard_map

# Calculate the total distance using a dictionary
def get_distance(word):
    keyboard_map = create_keyboard_map()
    current_position = keyboard_map['*']  # Start at '*' position
    total_distance = 0

    for ch in word:
        if ch in keyboard_map:  # Check if the character exists on the keyboard
            target_position = keyboard_map[ch]
            # Calculate Manhattan distance
            total_distance += abs(current_position[0] - target_position[0]) + abs(current_position[1] - target_position[1])
            # Move to the new position
            current_position = target_position
        else:
            print(f"Character '{ch}' not on keyboard.")
    
    return total_distance

# Main function
if __name__ == "__main__":
    word = input("Enter the word to type: ")
    print("Total distance:", get_distance(word))