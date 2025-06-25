#!/usr/bin/env python3
"""
Flask Web Application for Interactive Story Generator
Integrates Python backend with HTML frontend
"""

from flask import Flask, render_template, request, jsonify, session
import re
import json
import os
import random
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import uuid

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

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

@app.route('/')
def index():
    """Main page route."""
    return render_template('interactive_story_generator.html')

@app.route('/api/generate_story', methods=['POST'])
def generate_story():
    """API endpoint to generate a story."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['adjective', 'name', 'place', 'past_action', 'future_action']
        for field in required_fields:
            if field not in data or not data[field].strip():
                return jsonify({
                    'success': False,
                    'error': f'Missing or empty field: {field}'
                }), 400
        
        # Validate each field
        for field in required_fields:
            if not story_manager.validate_input(data[field], field):
                examples = story_manager.get_validation_examples(field)
                return jsonify({
                    'success': False,
                    'error': f'Invalid {field}. Examples: {", ".join(examples[:3])}'
                }), 400
        
        # Add story elements
        for field in required_fields:
            story_manager.add_story_element(field, data[field])
        
        # Build the story
        story = build_story(data)
        
        # Save the story
        story_manager.save_current_story()
        
        return jsonify({
            'success': True,
            'story': story,
            'message': 'Story generated successfully!'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500

def build_story(story_data: Dict[str, str]) -> str:
    """Builds the complete story from user inputs."""
    story = (
        f"Once upon a time, there was a {story_data['adjective']} teenager named "
        f"{story_data['name']} who lived in a {story_data['place']}. "
        f"One day, they {story_data['past_action']} something that would change "
        f"their life forever. Now, they {story_data['future_action']} to make "
        f"their dreams come true. And so, their incredible journey began..."
    )
    return story

@app.route('/api/get_question', methods=['GET'])
def get_question():
    """API endpoint to get a random quiz question."""
    try:
        question = story_manager.get_random_question()
        return jsonify({
            'success': True,
            'question': question
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500

@app.route('/api/submit_answer', methods=['POST'])
def submit_answer():
    """API endpoint to submit a quiz answer."""
    try:
        data = request.get_json()
        
        if 'question' not in data or 'user_answer' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing question or user_answer'
            }), 400
        
        question = data['question']
        user_answer = data['user_answer']
        correct_answer = question['correct_answer']
        is_correct = user_answer == correct_answer
        
        # Record the score
        story_manager.add_quiz_score(
            question['question'],
            user_answer,
            correct_answer,
            is_correct
        )
        
        return jsonify({
            'success': True,
            'is_correct': is_correct,
            'correct_answer': correct_answer,
            'explanation': question['explanation']
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500

@app.route('/api/get_history', methods=['GET'])
def get_history():
    """API endpoint to get story history."""
    try:
        history = story_manager.get_story_history()
        return jsonify({
            'success': True,
            'history': history
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500

@app.route('/api/get_statistics', methods=['GET'])
def get_statistics():
    """API endpoint to get quiz statistics."""
    try:
        stats = story_manager.get_quiz_statistics()
        return jsonify({
            'success': True,
            'statistics': stats
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500

@app.route('/api/validate_input', methods=['POST'])
def validate_input():
    """API endpoint to validate user input."""
    try:
        data = request.get_json()
        
        if 'input_text' not in data or 'element_type' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing input_text or element_type'
            }), 400
        
        input_text = data['input_text']
        element_type = data['element_type']
        
        is_valid = story_manager.validate_input(input_text, element_type)
        examples = story_manager.get_validation_examples(element_type)
        
        return jsonify({
            'success': True,
            'is_valid': is_valid,
            'examples': examples
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Move HTML file to templates directory
    if os.path.exists('interactive_story_generator.html'):
        import shutil
        shutil.move('interactive_story_generator.html', 'templates/interactive_story_generator.html')
    
    print("🎭 Interactive Story Generator - Flask Web Application")
    print("=" * 50)
    print("Starting server...")
    print("Open your browser and go to: http://localhost:5001")
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5001) 