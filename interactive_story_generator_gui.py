#!/usr/bin/env python3
"""
Interactive Story Generator GUI
A graphical user interface for the AI-powered storytelling application
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import os
import random
import re
from typing import Dict, List, Optional
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

class InteractiveStoryGeneratorGUI:
    """Graphical User Interface for the Interactive Story Generator."""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎭 Interactive Story Generator")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2c3e50')
        
        # Initialize story manager
        self.story_manager = StoryManager()
        
        # Current question for quiz
        self.current_question = None
        self.selected_answer = tk.StringVar()
        
        # Create the main interface
        self.create_widgets()
        
    def create_widgets(self):
        """Creates the main GUI widgets."""
        # Main title
        title_frame = tk.Frame(self.root, bg='#3498db', height=80)
        title_frame.pack(fill=tk.X, padx=10, pady=10)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, 
                              text="🎭 Interactive Story Generator", 
                              font=("Arial", 24, "bold"), 
                              bg='#3498db', 
                              fg='white')
        title_label.pack(expand=True)
        
        subtitle_label = tk.Label(title_frame, 
                                 text="Create Amazing Stories with AI Guidance", 
                                 font=("Arial", 12), 
                                 bg='#3498db', 
                                 fg='white')
        subtitle_label.pack()
        
        # Main buttons frame
        buttons_frame = tk.Frame(self.root, bg='#2c3e50')
        buttons_frame.pack(fill=tk.X, padx=20, pady=20)
        
        # Create buttons with modern styling
        button_style = {
            'font': ('Arial', 12, 'bold'),
            'width': 20,
            'height': 2,
            'relief': 'raised',
            'borderwidth': 2
        }
        
        # Main action buttons
        tk.Button(buttons_frame, 
                 text="📝 Create New Story", 
                 bg='#27ae60', fg='white',
                 command=self.create_story_window,
                 **button_style).pack(pady=10)
        
        tk.Button(buttons_frame, 
                 text="🎯 Take Storytelling Quiz", 
                 bg='#e74c3c', fg='white',
                 command=self.start_quiz,
                 **button_style).pack(pady=10)
        
        tk.Button(buttons_frame, 
                 text="📚 View Story History", 
                 bg='#f39c12', fg='white',
                 command=self.show_story_history,
                 **button_style).pack(pady=10)
        
        tk.Button(buttons_frame, 
                 text="📊 View Quiz Statistics", 
                 bg='#9b59b6', fg='white',
                 command=self.show_quiz_statistics,
                 **button_style).pack(pady=10)
        
        # Status frame
        status_frame = tk.Frame(self.root, bg='#34495e', height=100)
        status_frame.pack(fill=tk.X, padx=10, pady=10)
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(status_frame, 
                                    text="Ready to create amazing stories! 🚀", 
                                    font=("Arial", 10), 
                                    bg='#34495e', 
                                    fg='white')
        self.status_label.pack(expand=True)
        
    def create_story_window(self):
        """Opens a new window for story creation."""
        story_window = tk.Toplevel(self.root)
        story_window.title("Create New Story")
        story_window.geometry("800x600")
        story_window.configure(bg='#ecf0f1')
        
        # Title
        title_label = tk.Label(story_window, 
                              text="📝 Create Your Story", 
                              font=("Arial", 18, "bold"), 
                              bg='#ecf0f1', 
                              fg='#2c3e50')
        title_label.pack(pady=20)
        
        # Story elements frame
        elements_frame = tk.Frame(story_window, bg='#ecf0f1')
        elements_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Input fields
        fields = [
            ("Adjective (e.g., brave, curious):", "adjective"),
            ("Character Name:", "name"),
            ("Place (e.g., magical forest):", "place"),
            ("Past Action (e.g., discovered):", "past_action"),
            ("Future Action (e.g., will explore):", "future_action")
        ]
        
        self.story_entries = {}
        
        for i, (label_text, field_name) in enumerate(fields):
            frame = tk.Frame(elements_frame, bg='#ecf0f1')
            frame.pack(fill=tk.X, pady=10)
            
            label = tk.Label(frame, text=label_text, font=("Arial", 10, "bold"), bg='#ecf0f1', fg='#2c3e50')
            label.pack(anchor=tk.W)
            
            entry = tk.Entry(frame, font=("Arial", 12), width=40)
            entry.pack(fill=tk.X, pady=5)
            self.story_entries[field_name] = entry
        
        # Buttons frame
        buttons_frame = tk.Frame(story_window, bg='#ecf0f1')
        buttons_frame.pack(pady=20)
        
        tk.Button(buttons_frame, 
                 text="🎭 Generate Story", 
                 bg='#27ae60', fg='white',
                 font=("Arial", 12, "bold"),
                 command=lambda: self.generate_story(story_window),
                 width=15).pack(side=tk.LEFT, padx=10)
        
        tk.Button(buttons_frame, 
                 text="❌ Cancel", 
                 bg='#e74c3c', fg='white',
                 font=("Arial", 12, "bold"),
                 command=story_window.destroy,
                 width=15).pack(side=tk.LEFT, padx=10)
    
    def generate_story(self, window):
        """Generates a story from the input fields."""
        # Get values from entries
        story_data = {}
        for field_name, entry in self.story_entries.items():
            value = entry.get().strip()
            if not value:
                messagebox.showerror("Error", f"Please fill in the {field_name} field!")
                return
            story_data[field_name] = value
        
        # Build the story
        story = (
            f"Once upon a time, there was a {story_data['adjective']} teenager named "
            f"{story_data['name']} who lived in a {story_data['place']}. "
            f"One day, they {story_data['past_action']} something that would change "
            f"their life forever. Now, they {story_data['future_action']} to make "
            f"their dreams come true. And so, their incredible journey began..."
        )
        
        # Save to story manager
        for field_name, value in story_data.items():
            self.story_manager.add_story_element(field_name, value)
        self.story_manager.save_current_story()
        
        # Show the story
        self.show_generated_story(story, window)
    
    def show_generated_story(self, story, parent_window):
        """Shows the generated story in a new window."""
        story_window = tk.Toplevel(parent_window)
        story_window.title("Your Generated Story")
        story_window.geometry("600x400")
        story_window.configure(bg='#2c3e50')
        
        # Title
        title_label = tk.Label(story_window, 
                              text="🎭 Your Story", 
                              font=("Arial", 18, "bold"), 
                              bg='#2c3e50', 
                              fg='white')
        title_label.pack(pady=20)
        
        # Story text
        story_text = scrolledtext.ScrolledText(story_window, 
                                              font=("Arial", 12), 
                                              bg='#ecf0f1',
                                              fg='#2c3e50',
                                              wrap=tk.WORD,
                                              height=15)
        story_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        story_text.insert(tk.END, story)
        story_text.config(state=tk.DISABLED)
        
        # Close button
        tk.Button(story_window, 
                 text="✅ Close", 
                 bg='#27ae60', fg='white',
                 font=("Arial", 12, "bold"),
                 command=story_window.destroy,
                 width=15).pack(pady=20)
        
        self.status_label.config(text="Story generated successfully! 🎉")
    
    def start_quiz(self):
        """Starts the interactive quiz."""
        self.current_question = self.story_manager.get_random_question()
        self.show_quiz_question()
    
    def show_quiz_question(self):
        """Shows a quiz question in a new window."""
        quiz_window = tk.Toplevel(self.root)
        quiz_window.title("Storytelling Quiz")
        quiz_window.geometry("700x500")
        quiz_window.configure(bg='#ecf0f1')
        
        # Title
        title_label = tk.Label(quiz_window, 
                              text="🎯 Storytelling Quiz", 
                              font=("Arial", 18, "bold"), 
                              bg='#ecf0f1', 
                              fg='#2c3e50')
        title_label.pack(pady=20)
        
        # Question
        question_label = tk.Label(quiz_window, 
                                 text=self.current_question['question'], 
                                 font=("Arial", 12, "bold"), 
                                 bg='#ecf0f1', 
                                 fg='#2c3e50',
                                 wraplength=600)
        question_label.pack(pady=20)
        
        # Options frame
        options_frame = tk.Frame(quiz_window, bg='#ecf0f1')
        options_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create radio buttons for options
        for i, option in enumerate(self.current_question['options']):
            radio = tk.Radiobutton(options_frame, 
                                  text=f"{chr(65 + i)}. {option}", 
                                  variable=self.selected_answer,
                                  value=option,
                                  font=("Arial", 11),
                                  bg='#ecf0f1',
                                  fg='#2c3e50',
                                  selectcolor='#3498db')
            radio.pack(anchor=tk.W, pady=5)
        
        # Submit button
        tk.Button(quiz_window, 
                 text="Submit Answer", 
                 bg='#27ae60', fg='white',
                 font=("Arial", 12, "bold"),
                 command=lambda: self.check_answer(quiz_window),
                 width=15).pack(pady=20)
    
    def check_answer(self, window):
        """Checks the quiz answer and shows feedback."""
        user_answer = self.selected_answer.get()
        
        if not user_answer:
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        
        is_correct = user_answer == self.current_question['correct_answer']
        
        # Record the score
        self.story_manager.add_quiz_score(
            self.current_question['question'],
            user_answer,
            self.current_question['correct_answer'],
            is_correct
        )
        
        # Show result
        if is_correct:
            messagebox.showinfo("Correct! 🎉", 
                              f"Your answer: {user_answer}\n\n{self.current_question['explanation']}")
        else:
            messagebox.showinfo("Good try! 💡", 
                              f"Your answer: {user_answer}\n\n"
                              f"The best answer was: {self.current_question['correct_answer']}\n\n"
                              f"{self.current_question['explanation']}")
        
        window.destroy()
        self.status_label.config(text="Quiz completed! Check your statistics! 📊")
    
    def show_story_history(self):
        """Shows the story history in a new window."""
        history_window = tk.Toplevel(self.root)
        history_window.title("Story History")
        history_window.geometry("800x600")
        history_window.configure(bg='#ecf0f1')
        
        # Title
        title_label = tk.Label(history_window, 
                              text="📚 Story History", 
                              font=("Arial", 18, "bold"), 
                              bg='#ecf0f1', 
                              fg='#2c3e50')
        title_label.pack(pady=20)
        
        # History text
        history_text = scrolledtext.ScrolledText(history_window, 
                                                font=("Arial", 11), 
                                                bg='#ecf0f1',
                                                fg='#2c3e50',
                                                wrap=tk.WORD)
        history_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        history = self.story_manager.get_story_history()
        if not history:
            history_text.insert(tk.END, "No stories created yet. Start creating your first story! 🚀")
        else:
            for i, story in enumerate(history[-10:], 1):  # Show last 10 stories
                history_text.insert(tk.END, f"Story #{story.get('story_id', i)}\n")
                history_text.insert(tk.END, f"Created: {story.get('timestamp', 'Unknown')}\n")
                history_text.insert(tk.END, f"Character: {story.get('name', 'Unknown')} - {story.get('adjective', 'Unknown')}\n")
                history_text.insert(tk.END, f"Setting: {story.get('place', 'Unknown')}\n")
                history_text.insert(tk.END, "-" * 50 + "\n\n")
        
        history_text.config(state=tk.DISABLED)
        
        # Close button
        tk.Button(history_window, 
                 text="✅ Close", 
                 bg='#27ae60', fg='white',
                 font=("Arial", 12, "bold"),
                 command=history_window.destroy,
                 width=15).pack(pady=20)
    
    def show_quiz_statistics(self):
        """Shows quiz statistics in a new window."""
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Quiz Statistics")
        stats_window.geometry("600x400")
        stats_window.configure(bg='#ecf0f1')
        
        # Title
        title_label = tk.Label(stats_window, 
                              text="📊 Quiz Statistics", 
                              font=("Arial", 18, "bold"), 
                              bg='#ecf0f1', 
                              fg='#2c3e50')
        title_label.pack(pady=20)
        
        # Statistics text
        stats_text = scrolledtext.ScrolledText(stats_window, 
                                              font=("Arial", 12), 
                                              bg='#ecf0f1',
                                              fg='#2c3e50',
                                              wrap=tk.WORD)
        stats_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        stats = self.story_manager.get_quiz_statistics()
        if not stats:
            stats_text.insert(tk.END, "No quiz data available yet. Take some questions first! 🎯")
        else:
            stats_text.insert(tk.END, f"Total Questions Answered: {stats['total_questions']}\n")
            stats_text.insert(tk.END, f"Correct Answers: {stats['correct_answers']}\n")
            stats_text.insert(tk.END, f"Accuracy: {stats['accuracy_percentage']:.1f}%\n\n")
            
            recent = stats['recent_performance']
            if recent:
                recent_correct = sum(recent)
                stats_text.insert(tk.END, f"Recent Performance (last 5): {recent_correct}/{len(recent)} correct\n\n")
                
                if stats['accuracy_percentage'] >= 80:
                    stats_text.insert(tk.END, "🌟 Excellent! You're a storytelling expert!\n")
                elif stats['accuracy_percentage'] >= 60:
                    stats_text.insert(tk.END, "👍 Good job! Keep learning and improving!\n")
                else:
                    stats_text.insert(tk.END, "📚 Keep practicing! Storytelling takes time to master!\n")
        
        stats_text.config(state=tk.DISABLED)
        
        # Close button
        tk.Button(stats_window, 
                 text="✅ Close", 
                 bg='#27ae60', fg='white',
                 font=("Arial", 12, "bold"),
                 command=stats_window.destroy,
                 width=15).pack(pady=20)
    
    def run(self):
        """Runs the GUI application."""
        self.root.mainloop()

def main():
    """Main function to run the GUI application."""
    app = InteractiveStoryGeneratorGUI()
    app.run()

if __name__ == "__main__":
    main() 