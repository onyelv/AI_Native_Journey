#!/usr/bin/env python3
"""
Interactive Story Generator
AI-powered storytelling application with tense guidance for teenagers
"""

import re
from typing import Dict, Optional

def validate_word_input(input_text: str, word_type: str) -> tuple[bool, str]:
    """
    Validates user input for different word types.
    
    Args:
        input_text: The user's input string
        word_type: Type of word being validated ('adjective', 'name', 'place')
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not input_text or not input_text.strip():
        return False, f"Please enter a {word_type} - it cannot be empty!"
    
    # Remove extra spaces and check if it's only letters and spaces
    cleaned_input = input_text.strip()
    if not re.match(r'^[a-zA-Z\s]+$', cleaned_input):
        return False, f"Please enter a {word_type} using only letters and spaces."
    
    # For names and places, allow multiple words. For adjectives, prefer single word
    if word_type == 'adjective' and ' ' in cleaned_input:
        return False, "Please enter a single adjective (one word)."
    
    return True, ""

def get_foundation_words() -> Dict[str, str]:
    """
    Gets the foundation words (adjective, name, place) from the user.
    
    Returns:
        Dictionary with keys: 'adjective', 'name', 'place'
    """
    foundation_words = {}
    
    print("\n" + "="*50)
    print("📚 Let's start building your story!")
    print("="*50)
    
    # Get adjective
    while True:
        adjective = input("\nEnter an adjective (e.g., brave, curious, mysterious): ").strip()
        is_valid, error_msg = validate_word_input(adjective, 'adjective')
        if is_valid:
            foundation_words['adjective'] = adjective
            break
        else:
            print(f"❌ {error_msg}")
    
    # Get name
    while True:
        name = input("Enter a character name: ").strip()
        is_valid, error_msg = validate_word_input(name, 'name')
        if is_valid:
            foundation_words['name'] = name
            break
        else:
            print(f"❌ {error_msg}")
    
    # Get place
    while True:
        place = input("Enter a place (e.g., small town, big city, magical forest): ").strip()
        is_valid, error_msg = validate_word_input(place, 'place')
        if is_valid:
            foundation_words['place'] = place
            break
        else:
            print(f"❌ {error_msg}")
    
    return foundation_words

def provide_tense_guidance(tense_type: str) -> str:
    """
    Provides helpful guidance for tense requirements.
    
    Args:
        tense_type: Either 'past' or 'future'
    
    Returns:
        Guidance message string
    """
    if tense_type == 'past':
        return ("💡 AI Guidance: Now we need a past tense verb to describe what happened next!\n"
                "   Try words like 'discovered', 'explored', 'created', 'found', 'learned', 'built'")
    elif tense_type == 'future':
        return ("💡 AI Guidance: Now let's look to the future! We need a future tense action!\n"
                "   Try phrases like 'will discover', 'will explore', 'will create', 'will build', 'will learn'")
    else:
        return "💡 AI Guidance: Please provide a word that fits the story!"

def validate_past_tense(verb: str) -> tuple[bool, str]:
    """
    Validates if input is a past tense verb.
    
    Args:
        verb: The verb to validate
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not verb or not verb.strip():
        return False, "Please enter a past tense verb!"
    
    cleaned_verb = verb.strip().lower()
    
    # Check for common -ed endings
    if cleaned_verb.endswith('ed'):
        return True, ""
    
    # Common irregular past tense verbs
    irregular_past = {
        'went', 'saw', 'came', 'found', 'made', 'took', 'gave', 'wrote', 'drove',
        'flew', 'ate', 'drank', 'ran', 'swam', 'built', 'bought', 'brought',
        'caught', 'chose', 'drew', 'fell', 'felt', 'fought', 'forgot', 'got',
        'grew', 'heard', 'held', 'kept', 'knew', 'left', 'lost', 'met', 'paid',
        'put', 'read', 'rode', 'said', 'sat', 'slept', 'spoke', 'stood', 'thought',
        'threw', 'understood', 'woke', 'wore', 'won', 'wrote'
    }
    
    if cleaned_verb in irregular_past:
        return True, ""
    
    return False, "Please enter a valid past tense verb (ends with -ed or is irregular like 'went', 'found')"

def get_past_tense_action() -> str:
    """
    Gets a past tense verb from the user.
    
    Returns:
        Past tense verb as string
    """
    print("\n" + "="*50)
    print(provide_tense_guidance('past'))
    print("="*50)
    
    while True:
        past_verb = input("\nEnter a past tense verb: ").strip()
        is_valid, error_msg = validate_past_tense(past_verb)
        if is_valid:
            return past_verb
        else:
            print(f"❌ {error_msg}")

def validate_future_tense(phrase: str) -> tuple[bool, str]:
    """
    Validates if input is a future tense phrase.
    
    Args:
        phrase: The phrase to validate
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not phrase or not phrase.strip():
        return False, "Please enter a future tense action!"
    
    cleaned_phrase = phrase.strip().lower()
    
    # Check if it starts with "will" followed by a base verb
    if cleaned_phrase.startswith('will '):
        base_verb = cleaned_phrase[5:].strip()
        if base_verb and len(base_verb) > 0:
            return True, ""
    
    return False, "Please enter a future tense phrase starting with 'will' (e.g., 'will discover', 'will explore')"

def get_future_tense_action() -> str:
    """
    Gets a future tense action from the user.
    
    Returns:
        Future tense phrase as string
    """
    print("\n" + "="*50)
    print(provide_tense_guidance('future'))
    print("="*50)
    
    while True:
        future_phrase = input("\nEnter a future tense action: ").strip()
        is_valid, error_msg = validate_future_tense(future_phrase)
        if is_valid:
            return future_phrase
        else:
            print(f"❌ {error_msg}")

def build_story(story_data: Dict[str, str]) -> str:
    """
    Builds the complete story from user inputs.
    
    Args:
        story_data: Dictionary with story elements
    
    Returns:
        Complete story string
    """
    # Ensure all required keys exist
    required_keys = ['adjective', 'name', 'place', 'past_action', 'future_action']
    for key in required_keys:
        if key not in story_data:
            story_data[key] = f"[missing {key}]"
    
    story = (
        f"Once upon a time, there was a {story_data['adjective']} teenager named "
        f"{story_data['name']} who lived in a {story_data['place']}. "
        f"One day, they {story_data['past_action']} something that would change "
        f"their life forever. Now, they {story_data['future_action']} to make "
        f"their dreams come true. And so, their incredible journey began..."
    )
    
    return story

def format_story_display(story: str) -> str:
    """
    Formats the story for display with visual enhancements.
    
    Args:
        story: The story string to format
    
    Returns:
        Formatted story string
    """
    formatted_story = "\n" + "🎭" + "="*48 + "🎭\n"
    formatted_story += "                    YOUR STORY\n"
    formatted_story += "🎭" + "="*48 + "🎭\n\n"
    formatted_story += story + "\n\n"
    formatted_story += "🎭" + "="*48 + "🎭\n"
    formatted_story += "           Thanks for creating with us!\n"
    formatted_story += "🎭" + "="*48 + "🎭\n"
    
    return formatted_story

def generate_interactive_story() -> str:
    """
    Main function that orchestrates the entire story generation process.
    
    Returns:
        Complete formatted story
    """
    try:
        print("🚀 Welcome to the Interactive Story Generator!")
        print("Let's create an amazing story together!")
        
        # Step 1: Get foundation words
        foundation = get_foundation_words()
        
        # Step 2: Get past tense action
        past_action = get_past_tense_action()
        
        # Step 3: Get future tense action
        future_action = get_future_tense_action()
        
        # Step 4: Build the complete story
        story_data = {
            **foundation,
            'past_action': past_action,
            'future_action': future_action
        }
        
        complete_story = build_story(story_data)
        
        # Step 5: Format for display
        formatted_story = format_story_display(complete_story)
        
        return formatted_story
        
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for trying the Interactive Story Generator!")
        return ""
    except Exception as e:
        print(f"\n❌ Oops! Something went wrong: {e}")
        return ""

def main():
    """Main execution function."""
    while True:
        story = generate_interactive_story()
        if story:
            print(story)
        
        play_again = input("\nWould you like to create another story? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y', 'yeah', 'sure']:
            print("\n👋 Thanks for using the Interactive Story Generator! See you next time!")
            break

if __name__ == "__main__":
    main() 