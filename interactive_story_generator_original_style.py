#!/usr/bin/env python3
"""
Interactive Story Generator - Original Style with Enhanced Features
Simple, clean interface with all the advanced functionality
"""

import re
import json
import os
import random
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime

@dataclass
class StoryElement:
    """Data class for story elements with validation."""
    word_type: str
    value: str
    validation_rules: List[str]
    examples: List[str]

class StoryManager:
    """Manages story data using dictionaries and lists for better organization."""
    
    def __init__(self):
        # Dictionary to store current story data
        self.current_story: Dict[str, str] = {}
        
        # List to store multiple stories (for history/backup)
        self.story_history: List[Dict[str, str]] = []
        
        # Dictionary to store validation rules and examples
        self.validation_data: Dict[str, Dict] = {
            'adjective': {
                'rules': ['single_word', 'letters_only', 'min_length_2'],
                'examples': ['brave', 'curious', 'mysterious', 'adventurous', 'creative']
            },
            'name': {
                'rules': ['letters_spaces_hyphens', 'min_length_2'],
                'examples': ['Alex', 'Maya', 'Jordan', 'Sam', 'Taylor']
            },
            'place': {
                'rules': ['letters_spaces_apostrophes', 'min_length_3'],
                'examples': ['small town', 'big city', 'magical forest', 'space station', 'underwater cave']
            },
            'past_action': {
                'rules': ['past_tense', 'verb_form'],
                'examples': ['discovered', 'explored', 'created', 'found', 'learned', 'built']
            },
            'future_action': {
                'rules': ['future_tense', 'will_format'],
                'examples': ['will discover', 'will explore', 'will create', 'will build', 'will learn']
            }
        }
        
        # List of irregular past tense verbs for validation
        self.irregular_past_verbs: List[str] = [
            'went', 'saw', 'came', 'found', 'made', 'took', 'gave', 'wrote', 'drove',
            'flew', 'ate', 'drank', 'ran', 'swam', 'built', 'bought', 'brought',
            'caught', 'chose', 'drew', 'fell', 'felt', 'fought', 'forgot', 'got',
            'grew', 'heard', 'held', 'kept', 'knew', 'left', 'lost', 'met', 'paid',
            'put', 'read', 'rode', 'said', 'sat', 'slept', 'spoke', 'stood', 'thought',
            'threw', 'understood', 'woke', 'wore', 'won', 'wrote', 'broke', 'chose',
            'drove', 'froze', 'hid', 'rode', 'rose', 'shook', 'shrank', 'sprang',
            'stole', 'struck', 'swore', 'tore', 'wore', 'wrote'
        ]
        
        # List of dictionaries for interactive questions with multiple-choice options
        self.interactive_questions: List[Dict[str, any]] = [
            {
                'question': 'What type of story are we creating?',
                'options': ['Adventure', 'Mystery', 'Fantasy', 'Science Fiction', 'Realistic'],
                'correct_answer': 'Adventure',
                'explanation': 'Adventure stories are exciting and full of action!',
                'category': 'story_type'
            },
            {
                'question': 'What should be the main character\'s personality trait?',
                'options': ['Brave and courageous', 'Smart and clever', 'Kind and caring', 'Funny and witty', 'Strong and determined'],
                'correct_answer': 'Brave and courageous',
                'explanation': 'Brave characters make for exciting adventures!',
                'category': 'character_trait'
            },
            {
                'question': 'Where should our story take place?',
                'options': ['A magical forest', 'A busy city', 'A mysterious island', 'A space station', 'A hidden cave'],
                'correct_answer': 'A magical forest',
                'explanation': 'Magical forests are perfect for adventure stories!',
                'category': 'setting'
            },
            {
                'question': 'What should happen to start the adventure?',
                'options': ['Find a mysterious map', 'Discover a hidden door', 'Meet a talking animal', 'Receive a magical letter', 'Fall through a portal'],
                'correct_answer': 'Find a mysterious map',
                'explanation': 'Maps lead to treasure and adventure!',
                'category': 'plot_start'
            },
            {
                'question': 'What should the character do next?',
                'options': ['Follow the map to find treasure', 'Ask for help from friends', 'Study the map carefully', 'Tell an adult about it', 'Ignore the map'],
                'correct_answer': 'Follow the map to find treasure',
                'explanation': 'Following the map will lead to an exciting journey!',
                'category': 'plot_action'
            },
            {
                'question': 'What obstacle should the character face?',
                'options': ['A dark cave to explore', 'A river to cross', 'A puzzle to solve', 'A storm to weather', 'A creature to befriend'],
                'correct_answer': 'A puzzle to solve',
                'explanation': 'Puzzles make the story more interactive and challenging!',
                'category': 'obstacle'
            },
            {
                'question': 'How should the story end?',
                'options': ['Find a great treasure', 'Make new friends', 'Learn an important lesson', 'Return home safely', 'Start a new adventure'],
                'correct_answer': 'Learn an important lesson',
                'explanation': 'Stories with lessons are meaningful and memorable!',
                'category': 'ending'
            },
            {
                'question': 'What tense should we use for the story?',
                'options': ['Past tense (walked, ran)', 'Present tense (walk, run)', 'Future tense (will walk, will run)', 'Mixed tenses', 'Past perfect (had walked)'],
                'correct_answer': 'Past tense (walked, ran)',
                'explanation': 'Past tense is most common for storytelling!',
                'category': 'grammar'
            },
            {
                'question': 'What should be the story\'s theme?',
                'options': ['Friendship and teamwork', 'Courage and bravery', 'Discovery and learning', 'Family and love', 'Growth and change'],
                'correct_answer': 'Courage and bravery',
                'explanation': 'Courage themes make stories inspiring!',
                'category': 'theme'
            },
            {
                'question': 'What should the character learn?',
                'options': ['To be brave in difficult situations', 'To work well with others', 'To think before acting', 'To appreciate what they have', 'To never give up'],
                'correct_answer': 'To be brave in difficult situations',
                'explanation': 'Learning bravery helps characters grow!',
                'category': 'lesson'
            }
        ]
        
        # Track user's quiz performance
        self.quiz_scores: List[Dict[str, any]] = []
        
        # Load existing stories if available
        self.load_stories()
    
    def get_random_question(self) -> Dict[str, any]:
        """Gets a random question from the interactive questions list."""
        return random.choice(self.interactive_questions)
    
    def get_questions_by_category(self, category: str) -> List[Dict[str, any]]:
        """Gets all questions from a specific category."""
        return [q for q in self.interactive_questions if q['category'] == category]
    
    def add_quiz_score(self, question: str, user_answer: str, correct_answer: str, is_correct: bool) -> None:
        """Records a quiz score for tracking performance."""
        score_entry = {
            'question': question,
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'is_correct': is_correct,
            'timestamp': datetime.now().isoformat()
        }
        self.quiz_scores.append(score_entry)
    
    def get_quiz_statistics(self) -> Dict[str, any]:
        """Returns statistics about quiz performance."""
        if not self.quiz_scores:
            return {}
        
        total_questions = len(self.quiz_scores)
        correct_answers = sum(1 for score in self.quiz_scores if score['is_correct'])
        accuracy = (correct_answers / total_questions) * 100
        
        return {
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'accuracy_percentage': accuracy,
            'recent_performance': [score['is_correct'] for score in self.quiz_scores[-5:]]
        }
    
    def add_story_element(self, element_type: str, value: str) -> bool:
        """Adds a story element to the current story."""
        if self.validate_input(value, element_type):
            self.current_story[element_type] = value
            return True
        return False
    
    def get_story_element(self, element_type: str) -> Optional[str]:
        """Gets a story element from the current story."""
        return self.current_story.get(element_type)
    
    def is_story_complete(self) -> bool:
        """Checks if all required story elements are present."""
        required_elements = ['adjective', 'name', 'place', 'past_action', 'future_action']
        return all(element in self.current_story for element in required_elements)
    
    def save_current_story(self) -> None:
        """Saves the current story to history."""
        if self.is_story_complete():
            story_with_timestamp = {
                **self.current_story,
                'timestamp': datetime.now().isoformat(),
                'story_id': len(self.story_history) + 1
            }
            self.story_history.append(story_with_timestamp)
            self.save_stories()
    
    def get_story_history(self) -> List[Dict[str, str]]:
        """Returns the list of saved stories."""
        return self.story_history
    
    def clear_current_story(self) -> None:
        """Clears the current story data."""
        self.current_story = {}
    
    def get_validation_examples(self, element_type: str) -> List[str]:
        """Gets examples for a specific element type."""
        return self.validation_data.get(element_type, {}).get('examples', [])
    
    def validate_input(self, input_text: str, element_type: str) -> bool:
        """Validates input based on element type rules."""
        if not input_text or not input_text.strip():
            return False
        
        cleaned_input = input_text.strip()
        rules = self.validation_data.get(element_type, {}).get('rules', [])
        
        for rule in rules:
            if not self._apply_validation_rule(cleaned_input, rule, element_type):
                return False
        
        return True
    
    def _apply_validation_rule(self, text: str, rule: str, element_type: str) -> bool:
        """Applies a specific validation rule."""
        if rule == 'single_word':
            return ' ' not in text
        elif rule == 'letters_only':
            return bool(re.match(r'^[a-zA-Z]+$', text))
        elif rule == 'letters_spaces_hyphens':
            return bool(re.match(r'^[a-zA-Z\s\-]+$', text))
        elif rule == 'letters_spaces_apostrophes':
            return bool(re.match(r'^[a-zA-Z\s\']+$', text))
        elif rule == 'min_length_2':
            return len(text) >= 2
        elif rule == 'min_length_3':
            return len(text) >= 3
        elif rule == 'past_tense':
            return text.lower().endswith('ed') or text.lower() in self.irregular_past_verbs
        elif rule == 'future_tense':
            return text.lower().startswith('will ')
        elif rule == 'will_format':
            return len(text.lower().split()) >= 2 and text.lower().startswith('will ')
        elif rule == 'verb_form':
            return len(text) >= 3  # Basic verb length check
        
        return True
    
    def save_stories(self) -> None:
        """Saves stories to a JSON file."""
        try:
            with open('story_history.json', 'w') as f:
                json.dump(self.story_history, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save stories: {e}")
    
    def load_stories(self) -> None:
        """Loads stories from a JSON file."""
        try:
            if os.path.exists('story_history.json'):
                with open('story_history.json', 'r') as f:
                    self.story_history = json.load(f)
        except Exception as e:
            print(f"Warning: Could not load stories: {e}")
            self.story_history = []

# Global story manager instance
story_manager = StoryManager()

def ask_interactive_question() -> str:
    """
    Asks a random interactive question from the list of dictionaries.
    
    Returns:
        The user's answer as a string
    """
    question_data = story_manager.get_random_question()
    
    print("\n" + "="*50)
    print("🎯 INTERACTIVE STORY QUESTION")
    print("="*50)
    print(f"Question: {question_data['question']}")
    print("\nOptions:")
    
    # Display options with letters
    for i, option in enumerate(question_data['options'], 1):
        print(f"   {chr(64 + i)}. {option}")
    
    print("="*50)
    
    # Get user answer
    while True:
        user_input = input("Enter your choice (A, B, C, D, or E): ").strip().upper()
        
        # Validate input
        if user_input in ['A', 'B', 'C', 'D', 'E']:
            # Convert letter to index
            choice_index = ord(user_input) - 65  # A=0, B=1, etc.
            
            if choice_index < len(question_data['options']):
                user_answer = question_data['options'][choice_index]
                
                # Check if answer is correct
                is_correct = user_answer == question_data['correct_answer']
                
                # Record the score
                story_manager.add_quiz_score(
                    question_data['question'],
                    user_answer,
                    question_data['correct_answer'],
                    is_correct
                )
                
                # Provide feedback
                print(f"\n✅ Your answer: {user_answer}")
                if is_correct:
                    print("🎉 Correct! " + question_data['explanation'])
                else:
                    print(f"💡 The best answer was: {question_data['correct_answer']}")
                    print(f"💭 {question_data['explanation']}")
                
                return user_answer
            else:
                print("❌ Invalid choice. Please enter A, B, C, D, or E.")
        else:
            print("❌ Invalid input. Please enter A, B, C, D, or E.")

def show_quiz_statistics() -> None:
    """Displays quiz performance statistics."""
    stats = story_manager.get_quiz_statistics()
    
    if not stats:
        print("\n📊 No quiz data available yet. Take some questions first!")
        return
    
    print("\n📊 QUIZ PERFORMANCE STATISTICS")
    print("="*50)
    print(f"Total Questions Answered: {stats['total_questions']}")
    print(f"Correct Answers: {stats['correct_answers']}")
    print(f"Accuracy: {stats['accuracy_percentage']:.1f}%")
    
    # Show recent performance
    recent = stats['recent_performance']
    if recent:
        recent_correct = sum(recent)
        print(f"Recent Performance (last 5): {recent_correct}/{len(recent)} correct")
        
        # Give encouragement based on performance
        if stats['accuracy_percentage'] >= 80:
            print("🌟 Excellent! You're a storytelling expert!")
        elif stats['accuracy_percentage'] >= 60:
            print("👍 Good job! Keep learning and improving!")
        else:
            print("📚 Keep practicing! Storytelling takes time to master!")

def validate_word_input(input_text: str, word_type: str) -> tuple[bool, str]:
    """
    Validates user input for different word types using the StoryManager.
    
    Args:
        input_text: The user's input string
        word_type: Type of word being validated ('adjective', 'name', 'place')
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if story_manager.validate_input(input_text, word_type):
        return True, ""
    
    examples = story_manager.get_validation_examples(word_type)
    example_text = f"Examples: {', '.join(examples[:3])}"
    
    if not input_text or not input_text.strip():
        return False, f"Please enter a {word_type} - it cannot be empty! {example_text}"
    
    return False, f"Please enter a valid {word_type}. {example_text}"

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
            story_manager.add_story_element('adjective', adjective)
            break
        else:
            print(f"❌ {error_msg}")
    
    # Get name
    while True:
        name = input("Enter a character name: ").strip()
        is_valid, error_msg = validate_word_input(name, 'name')
        if is_valid:
            foundation_words['name'] = name
            story_manager.add_story_element('name', name)
            break
        else:
            print(f"❌ {error_msg}")
    
    # Get place
    while True:
        place = input("Enter a place (e.g., small town, big city, magical forest): ").strip()
        is_valid, error_msg = validate_word_input(place, 'place')
        if is_valid:
            foundation_words['place'] = place
            story_manager.add_story_element('place', place)
            break
        else:
            print(f"❌ {error_msg}")
    
    return foundation_words

def provide_tense_guidance(tense_type: str) -> str:
    """
    Provides helpful guidance for tense requirements using data from StoryManager.
    
    Args:
        tense_type: Either 'past' or 'future'
    
    Returns:
        Guidance message string
    """
    examples = story_manager.get_validation_examples(f'{tense_type}_action')
    
    if tense_type == 'past':
        return (f"💡 AI Guidance: Now we need a past tense verb to describe what happened next!\n"
                f"   Try words like: {', '.join(examples[:5])}")
    elif tense_type == 'future':
        return (f"💡 AI Guidance: Now let's look to the future! We need a future tense action!\n"
                f"   Try phrases like: {', '.join(examples[:5])}")
    else:
        return "💡 AI Guidance: Please provide a word that fits the story!"

def validate_past_tense(verb: str) -> tuple[bool, str]:
    """
    Validates if input is a past tense verb using StoryManager data.
    
    Args:
        verb: The verb to validate
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if story_manager.validate_input(verb, 'past_action'):
        return True, ""
    
    examples = story_manager.get_validation_examples('past_action')
    return False, f"Please enter a valid past tense verb. Examples: {', '.join(examples[:3])}"

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
            story_manager.add_story_element('past_action', past_verb)
            return past_verb
        else:
            print(f"❌ {error_msg}")

def validate_future_tense(phrase: str) -> tuple[bool, str]:
    """
    Validates if input is a future tense phrase using StoryManager data.
    
    Args:
        phrase: The phrase to validate
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if story_manager.validate_input(phrase, 'future_action'):
        return True, ""
    
    examples = story_manager.get_validation_examples('future_action')
    return False, f"Please enter a valid future tense phrase. Examples: {', '.join(examples[:3])}"

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
            story_manager.add_story_element('future_action', future_phrase)
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

def show_story_history() -> None:
    """Displays the history of saved stories."""
    history = story_manager.get_story_history()
    
    if not history:
        print("\n📚 No saved stories yet. Create your first story!")
        return
    
    print(f"\n📚 Story History ({len(history)} stories):")
    print("="*60)
    
    for i, story in enumerate(history[-5:], 1):  # Show last 5 stories
        print(f"\n{i}. Story #{story.get('story_id', i)}")
        print(f"   Created: {story.get('timestamp', 'Unknown')}")
        print(f"   Character: {story.get('name', 'Unknown')} - {story.get('adjective', 'Unknown')}")
        print(f"   Setting: {story.get('place', 'Unknown')}")
        print("-" * 40)

def generate_interactive_story() -> str:
    """
    Main function that orchestrates the entire story generation process.
    
    Returns:
        Complete formatted story
    """
    try:
        print("🚀 Welcome to the Interactive Story Generator!")
        print("Let's create an amazing story together!")
        
        # Step 1: Ask an interactive question to engage the user
        print("\n🎯 Let's start with a fun question about storytelling!")
        interactive_answer = ask_interactive_question()
        
        # Step 2: Get foundation words
        foundation = get_foundation_words()
        
        # Step 3: Ask another interactive question
        print("\n🎯 Another storytelling question!")
        second_answer = ask_interactive_question()
        
        # Step 4: Get past tense action
        past_action = get_past_tense_action()
        
        # Step 5: Get future tense action
        future_action = get_future_tense_action()
        
        # Step 6: Build the complete story
        story_data = {
            **foundation,
            'past_action': past_action,
            'future_action': future_action
        }
        
        complete_story = build_story(story_data)
        
        # Step 7: Save the story to history
        story_manager.save_current_story()
        
        # Step 8: Format for display
        formatted_story = format_story_display(complete_story)
        
        return formatted_story
        
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for trying the Interactive Story Generator!")
        return ""
    except Exception as e:
        print(f"\n❌ Oops! Something went wrong: {e}")
        return ""

def main():
    """Main execution function with original simple style."""
    while True:
        print("\n" + "="*50)
        print("🎭 Interactive Story Generator")
        print("="*50)
        print("1. Create a new story")
        print("2. Take a storytelling quiz")
        print("3. View story history")
        print("4. View quiz statistics")
        print("5. Exit")
        print("="*50)
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            story_manager.clear_current_story()  # Clear for new story
            story = generate_interactive_story()
            if story:
                print(story)
        elif choice == '2':
            print("\n🎯 Let's test your storytelling knowledge!")
            for i in range(3):  # Ask 3 questions
                ask_interactive_question()
                if i < 2:  # Don't ask if they want to continue after the last question
                    continue_quiz = input("\nContinue with another question? (y/n): ").strip().lower()
                    if continue_quiz not in ['y', 'yes']:
                        break
        elif choice == '3':
            show_story_history()
        elif choice == '4':
            show_quiz_statistics()
        elif choice == '5':
            print("\n👋 Thanks for using the Interactive Story Generator! See you next time!")
            break
        else:
            print("❌ Please enter a valid option (1-5).")

if __name__ == "__main__":
    main() 