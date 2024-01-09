import time
import random
from paragraph import generate_paragraph

def calculate_accuracy(prompt_text, user_input):
    prompt_words = prompt_text.split()
    user_words = user_input.split()
    
    correct_words = sum(pw == uw for pw, uw in zip(prompt_words, user_words))
    accuracy = (correct_words / len(prompt_words)) * 100
    return accuracy

def typing_speed_test():
    while True:
        prompt_text = generate_paragraph()
        
        print("Type the following text as fast as you can:")
        print(prompt_text)
        
        input("Press Enter when you are ready to start.")
        
        start_time = time.time()
        user_input = input("Type here: ")
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        words_per_minute = (len(prompt_text.split()) / elapsed_time) * 60
        
        accuracy = calculate_accuracy(prompt_text, user_input)
        
        print("\nYour typing speed: {:.2f} words per minute.".format(words_per_minute))
        print("Your accuracy: {:.2f}%".format(accuracy))
        
        play_again = input("Do you want to try another paragraph? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    typing_speed_test()