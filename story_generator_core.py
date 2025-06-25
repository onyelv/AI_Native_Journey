#!/usr/bin/env python3
"""
Core AI-Generated Functions for Interactive Story Generator
Implements the three essential features: Interactive Gapped Sentences, 
AI-Guided Tense Prompts, and Narrative Flow Integration
"""

import re
import random
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class StoryElement:
    """Data class for story elements with validation."""
    word_type: str
    value: str
    tense: Optional[str] = None
    validation_rules: Optional[List[str]] = None

class StoryValidator:
    """AI-generated validation logic for story inputs."""
    
    @staticmethod
    def validate_adjective(adjective: str) -> Tuple[bool, str]:
        """Validates adjective input with AI guidance."""
        if not adjective or not adjective.strip():
            return False, "Please enter an adjective - it cannot be empty!"
        
        cleaned = adjective.strip().lower()
        
        # Check for single word
        if ' ' in cleaned:
            return False, "Please enter a single adjective (one word)."
        
        # Check for letters only
        if not re.match(r'^[a-zA-Z]+$', cleaned):
            return False, "Please enter an adjective using only letters."
        
        # Check for reasonable length
        if len(cleaned) < 2:
            return False, "Please enter a longer adjective (at least 2 letters)."
        
        return True, ""

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        """Validates character name input."""
        if not name or not name.strip():
            return False, "Please enter a character name - it cannot be empty!"
        
        cleaned = name.strip()
        
        # Allow letters, spaces, and hyphens for names
        if not re.match(r'^[a-zA-Z\s\-]+$', cleaned):
            return False, "Please enter a name using only letters, spaces, and hyphens."
        
        # Check for reasonable length
        if len(cleaned) < 2:
            return False, "Please enter a longer name (at least 2 characters)."
        
        return True, ""

    @staticmethod
    def validate_place(place: str) -> Tuple[bool, str]:
        """Validates place input."""
        if not place or not place.strip():
            return False, "Please enter a place - it cannot be empty!"
        
        cleaned = place.strip()
        
        # Allow letters, spaces, and common place characters
        if not re.match(r'^[a-zA-Z\s\-\']+$', cleaned):
            return False, "Please enter a place using only letters, spaces, hyphens, and apostrophes."
        
        # Check for reasonable length
        if len(cleaned) < 3:
            return False, "Please enter a longer place name (at least 3 characters)."
        
        return True, ""

    @staticmethod
    def validate_past_tense(verb: str) -> Tuple[bool, str]:
        """AI-powered past tense validation with comprehensive verb checking."""
        if not verb or not verb.strip():
            return False, "Please enter a past tense verb!"
        
        cleaned = verb.strip().lower()
        
        # Common -ed endings
        if cleaned.endswith('ed'):
            return True, ""
        
        # Comprehensive irregular past tense verbs
        irregular_past = {
            'went', 'saw', 'came', 'found', 'made', 'took', 'gave', 'wrote', 'drove',
            'flew', 'ate', 'drank', 'ran', 'swam', 'built', 'bought', 'brought',
            'caught', 'chose', 'drew', 'fell', 'felt', 'fought', 'forgot', 'got',
            'grew', 'heard', 'held', 'kept', 'knew', 'left', 'lost', 'met', 'paid',
            'put', 'read', 'rode', 'said', 'sat', 'slept', 'spoke', 'stood', 'thought',
            'threw', 'understood', 'woke', 'wore', 'won', 'wrote', 'broke', 'chose',
            'drove', 'froze', 'hid', 'rode', 'rose', 'shook', 'shrank', 'sprang',
            'stole', 'struck', 'swore', 'tore', 'wore', 'wrote'
        }
        
        if cleaned in irregular_past:
            return True, ""
        
        return False, "Please enter a valid past tense verb (ends with -ed or is irregular like 'went', 'found')"

    @staticmethod
    def validate_future_tense(phrase: str) -> Tuple[bool, str]:
        """AI-powered future tense validation."""
        if not phrase or not phrase.strip():
            return False, "Please enter a future tense action!"
        
        cleaned = phrase.strip().lower()
        
        # Check for "will" + base verb pattern
        if cleaned.startswith('will '):
            base_verb = cleaned[5:].strip()
            if base_verb and len(base_verb) > 0:
                # Additional validation for base verb
                if re.match(r'^[a-zA-Z]+$', base_verb):
                    return True, ""
        
        return False, "Please enter a future tense phrase starting with 'will' (e.g., 'will discover', 'will explore')"

class TenseGuidanceAI:
    """AI-generated tense guidance system."""
    
    @staticmethod
    def get_past_tense_examples() -> List[str]:
        """Returns helpful past tense examples for teenagers."""
        return [
            "discovered", "explored", "created", "found", "learned", "built",
            "made", "took", "gave", "wrote", "drove", "flew", "ate", "drank",
            "ran", "swam", "went", "saw", "came", "felt", "thought", "knew"
        ]
    
    @staticmethod
    def get_future_tense_examples() -> List[str]:
        """Returns helpful future tense examples for teenagers."""
        return [
            "will discover", "will explore", "will create", "will build",
            "will learn", "will make", "will find", "will write", "will drive",
            "will fly", "will run", "will swim", "will go", "will see",
            "will feel", "will think", "will know"
        ]
    
    @staticmethod
    def generate_guidance_message(tense_type: str, context: str = "") -> str:
        """Generates contextual AI guidance messages."""
        if tense_type == 'past':
            examples = random.sample(TenseGuidanceAI.get_past_tense_examples(), 3)
            return (
                f"💡 AI Guidance: Now we need a past tense verb to describe what happened next!\n"
                f"   Try words like: {', '.join(examples)}\n"
                f"   {context}"
            )
        elif tense_type == 'future':
            examples = random.sample(TenseGuidanceAI.get_future_tense_examples(), 3)
            return (
                f"💡 AI Guidance: Now let's look to the future! We need a future tense action!\n"
                f"   Try phrases like: {', '.join(examples)}\n"
                f"   {context}"
            )
        else:
            return "💡 AI Guidance: Please provide a word that fits the story!"

class StoryBuilder:
    """AI-generated story construction logic."""
    
    @staticmethod
    def create_story_template() -> str:
        """Creates the base story template with gapped sentences."""
        return (
            "Once upon a time, there was a [ADJECTIVE] teenager named [NAME] "
            "who lived in a [PLACE]. One day, they [PAST_ACTION] something that "
            "would change their life forever. Now, they [FUTURE_ACTION] to make "
            "their dreams come true. And so, their incredible journey began..."
        )
    
    @staticmethod
    def build_story_from_elements(story_data: Dict[str, str]) -> str:
        """Builds complete story from user inputs with AI integration."""
        template = StoryBuilder.create_story_template()
        
        # Ensure all required elements exist
        required_elements = ['adjective', 'name', 'place', 'past_action', 'future_action']
        for element in required_elements:
            if element not in story_data:
                story_data[element] = f"[missing {element}]"
        
        # Replace placeholders with user inputs
        story = template.replace('[ADJECTIVE]', story_data['adjective'])
        story = story.replace('[NAME]', story_data['name'])
        story = story.replace('[PLACE]', story_data['place'])
        story = story.replace('[PAST_ACTION]', story_data['past_action'])
        story = story.replace('[FUTURE_ACTION]', story_data['future_action'])
        
        return story
    
    @staticmethod
    def format_story_for_display(story: str, user_inputs: Dict[str, str]) -> str:
        """Formats story with visual enhancements and highlights user inputs."""
        formatted_story = "\n" + "🎭" + "="*48 + "🎭\n"
        formatted_story += "                    YOUR STORY\n"
        formatted_story += "🎭" + "="*48 + "🎭\n\n"
        
        # Highlight user inputs in the story
        highlighted_story = story
        for key, value in user_inputs.items():
            highlighted_story = highlighted_story.replace(value, f"**{value}**")
        
        formatted_story += highlighted_story + "\n\n"
        formatted_story += "🎭" + "="*48 + "🎭\n"
        formatted_story += "           Thanks for creating with us!\n"
        formatted_story += "🎭" + "="*48 + "🎭\n"
        
        return formatted_story

class UserInputCollector:
    """AI-generated user input collection with validation."""
    
    def __init__(self):
        self.validator = StoryValidator()
        self.guidance_ai = TenseGuidanceAI()
    
    def get_foundation_words(self) -> Dict[str, str]:
        """Collects foundation words with AI validation."""
        foundation_words = {}
        
        print("\n" + "="*50)
        print("📚 Let's start building your story!")
        print("="*50)
        
        # Get adjective
        while True:
            adjective = input("\nEnter an adjective (e.g., brave, curious, mysterious): ").strip()
            is_valid, error_msg = self.validator.validate_adjective(adjective)
            if is_valid:
                foundation_words['adjective'] = adjective
                break
            else:
                print(f"❌ {error_msg}")
        
        # Get name
        while True:
            name = input("Enter a character name: ").strip()
            is_valid, error_msg = self.validator.validate_name(name)
            if is_valid:
                foundation_words['name'] = name
                break
            else:
                print(f"❌ {error_msg}")
        
        # Get place
        while True:
            place = input("Enter a place (e.g., small town, big city, magical forest): ").strip()
            is_valid, error_msg = self.validator.validate_place(place)
            if is_valid:
                foundation_words['place'] = place
                break
            else:
                print(f"❌ {error_msg}")
        
        return foundation_words
    
    def get_past_tense_action(self) -> str:
        """Collects past tense action with AI guidance."""
        print("\n" + "="*50)
        print(self.guidance_ai.generate_guidance_message('past'))
        print("="*50)
        
        while True:
            past_verb = input("\nEnter a past tense verb: ").strip()
            is_valid, error_msg = self.validator.validate_past_tense(past_verb)
            if is_valid:
                return past_verb
            else:
                print(f"❌ {error_msg}")
    
    def get_future_tense_action(self) -> str:
        """Collects future tense action with AI guidance."""
        print("\n" + "="*50)
        print(self.guidance_ai.generate_guidance_message('future'))
        print("="*50)
        
        while True:
            future_phrase = input("\nEnter a future tense action: ").strip()
            is_valid, error_msg = self.validator.validate_future_tense(future_phrase)
            if is_valid:
                return future_phrase
            else:
                print(f"❌ {error_msg}")

class StoryGeneratorCore:
    """Main AI-generated core logic orchestrator."""
    
    def __init__(self):
        self.input_collector = UserInputCollector()
        self.story_builder = StoryBuilder()
    
    def generate_story(self) -> str:
        """Main function that orchestrates the entire story generation process."""
        try:
            print("🚀 Welcome to the Interactive Story Generator!")
            print("Let's create an amazing story together!")
            
            # Step 1: Get foundation words
            foundation = self.input_collector.get_foundation_words()
            
            # Step 2: Get past tense action
            past_action = self.input_collector.get_past_tense_action()
            
            # Step 3: Get future tense action
            future_action = self.input_collector.get_future_tense_action()
            
            # Step 4: Build the complete story
            story_data = {
                **foundation,
                'past_action': past_action,
                'future_action': future_action
            }
            
            complete_story = self.story_builder.build_story_from_elements(story_data)
            
            # Step 5: Format for display
            formatted_story = self.story_builder.format_story_for_display(complete_story, story_data)
            
            return formatted_story
            
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for trying the Interactive Story Generator!")
            return ""
        except Exception as e:
            print(f"\n❌ Oops! Something went wrong: {e}")
            return ""

# Example usage and testing functions
def test_core_functions():
    """Test the core functions to ensure they work correctly."""
    print("🧪 Testing Core Functions...")
    
    # Test validation
    validator = StoryValidator()
    assert validator.validate_adjective("brave")[0] == True
    assert validator.validate_adjective("")[0] == False
    assert validator.validate_name("Alex Smith")[0] == True
    assert validator.validate_past_tense("discovered")[0] == True
    assert validator.validate_future_tense("will explore")[0] == True
    
    # Test story building
    story_data = {
        'adjective': 'brave',
        'name': 'Alex',
        'place': 'small town',
        'past_action': 'discovered',
        'future_action': 'will explore'
    }
    
    story = StoryBuilder.build_story_from_elements(story_data)
    assert "brave" in story
    assert "Alex" in story
    assert "discovered" in story
    assert "will explore" in story
    
    print("✅ All core functions tested successfully!")

if __name__ == "__main__":
    # Run tests
    test_core_functions()
    
    # Example usage
    generator = StoryGeneratorCore()
    story = generator.generate_story()
    if story:
        print(story) 