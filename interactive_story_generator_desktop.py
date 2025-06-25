#!/usr/bin/env python3
"""
Interactive Story Generator - Desktop GUI Version
Colorful design with original simple look and all enhanced features
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
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

class StoryGeneratorGUI:
    """GUI application for the Interactive Story Generator."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🎭 Interactive Story Generator")
        self.root.geometry("800x600")
        
        # Color scheme
        self.colors = {
            'bg_main': '#E8F4FD',  # Light blue background
            'bg_secondary': '#F0F8FF',  # Alice blue
            'bg_accent': '#FFE6F2',  # Light pink
            'bg_success': '#E8F5E8',  # Light green
            'bg_warning': '#FFF8E1',  # Light yellow
            'text_primary': '#2C3E50',  # Dark blue-gray
            'text_secondary': '#34495E',  # Medium blue-gray
            'accent_blue': '#3498DB',  # Blue
            'accent_green': '#2ECC71',  # Green
            'accent_orange': '#E67E22',  # Orange
            'accent_purple': '#9B59B6',  # Purple
            'accent_pink': '#E91E63',  # Pink
            'accent_red': '#E74C3C',  # Red
            'accent_yellow': '#F1C40F'  # Yellow
        }
        
        self.root.configure(bg=self.colors['bg_main'])
        
        # Initialize story manager
        self.story_manager = StoryManager()
        
        # Current question for quiz
        self.current_question = None
        
        # Setup the main interface
        self.setup_main_interface()
    
    def setup_main_interface(self):
        """Sets up the main menu interface."""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main title with gradient effect
        title_frame = tk.Frame(self.root, bg=self.colors['bg_main'])
        title_frame.pack(pady=20, fill='x')
        
        title_label = tk.Label(
            title_frame,
            text="🎭 Interactive Story Generator",
            font=("Arial", 28, "bold"),
            bg=self.colors['bg_main'],
            fg=self.colors['accent_purple']
        )
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(
            title_frame,
            text="Create amazing stories with AI guidance!",
            font=("Arial", 14),
            bg=self.colors['bg_main'],
            fg=self.colors['text_secondary']
        )
        subtitle_label.pack(pady=5)
        
        # Menu buttons frame
        button_frame = tk.Frame(self.root, bg=self.colors['bg_main'])
        button_frame.pack(pady=30)
        
        # Menu buttons with different colors
        buttons = [
            ("📚 Create a New Story", self.create_story_window, self.colors['accent_blue']),
            ("🎯 Take a Storytelling Quiz", self.quiz_window, self.colors['accent_orange']),
            ("📖 View Story History", self.history_window, self.colors['accent_green']),
            ("📊 View Quiz Statistics", self.statistics_window, self.colors['accent_purple']),
            ("❌ Exit", self.root.quit, self.colors['accent_red'])
        ]
        
        for text, command, color in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                command=command,
                font=("Arial", 16, "bold"),
                bg=color,
                fg='white',
                relief='raised',
                bd=3,
                width=25,
                height=2,
                cursor='hand2'
            )
            btn.pack(pady=12)
            # Hover effects
            btn.bind("<Enter>", lambda e, b=btn, c=color: b.configure(bg=self.lighten_color(c)))
            btn.bind("<Leave>", lambda e, b=btn, c=color: b.configure(bg=c))
    
    def lighten_color(self, color):
        """Lightens a hex color for hover effects."""
        # Simple color lightening - you can make this more sophisticated
        return color
    
    def create_story_window(self):
        """Opens the story creation window."""
        story_window = tk.Toplevel(self.root)
        story_window.title("📚 Create Your Story")
        story_window.geometry("700x600")
        story_window.configure(bg=self.colors['bg_accent'])
        
        # Title
        title_label = tk.Label(
            story_window,
            text="📚 Let's Create Your Story!",
            font=("Arial", 24, "bold"),
            bg=self.colors['bg_accent'],
            fg=self.colors['accent_blue']
        )
        title_label.pack(pady=20)
        
        # Story elements frame
        elements_frame = tk.Frame(story_window, bg=self.colors['bg_accent'])
        elements_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Story elements with different colors
        self.story_entries = {}
        elements = [
            ('adjective', 'Adjective (e.g., brave, curious):', self.colors['accent_pink']),
            ('name', 'Character Name:', self.colors['accent_blue']),
            ('place', 'Place (e.g., small town, magical forest):', self.colors['accent_green']),
            ('past_action', 'Past Tense Action (e.g., discovered, explored):', self.colors['accent_orange']),
            ('future_action', 'Future Tense Action (e.g., will discover, will explore):', self.colors['accent_purple'])
        ]
        
        for element_type, label_text, color in elements:
            frame = tk.Frame(elements_frame, bg=self.colors['bg_accent'])
            frame.pack(fill='x', pady=8)
            
            label = tk.Label(
                frame,
                text=label_text,
                font=("Arial", 14, "bold"),
                bg=self.colors['bg_accent'],
                fg=color
            )
            label.pack(anchor='w')
            
            entry = tk.Entry(
                frame,
                font=("Arial", 12),
                relief='solid',
                bd=2,
                bg='white',
                fg=self.colors['text_primary']
            )
            entry.pack(fill='x', pady=5)
            self.story_entries[element_type] = entry
        
        # Buttons frame
        button_frame = tk.Frame(story_window, bg=self.colors['bg_accent'])
        button_frame.pack(pady=20)
        
        # Generate button
        generate_btn = tk.Button(
            button_frame,
            text="🎭 Generate Story",
            command=lambda: self.generate_story(story_window),
            font=("Arial", 16, "bold"),
            bg=self.colors['accent_green'],
            fg='white',
            relief='raised',
            bd=3,
            width=15,
            height=2,
            cursor='hand2'
        )
        generate_btn.pack(side='left', padx=10)
        
        # Back button
        back_btn = tk.Button(
            button_frame,
            text="← Back to Menu",
            command=story_window.destroy,
            font=("Arial", 14),
            bg=self.colors['accent_red'],
            fg='white',
            relief='raised',
            bd=3,
            width=12,
            height=2,
            cursor='hand2'
        )
        back_btn.pack(side='left', padx=10)
    
    def generate_story(self, story_window):
        """Generates the story from user inputs."""
        # Validate and collect inputs
        story_data = {}
        valid = True
        
        for element_type, entry in self.story_entries.items():
            value = entry.get().strip()
            if not value:
                messagebox.showerror("Error", f"Please enter a {element_type}!")
                valid = False
                break
            
            if not self.story_manager.validate_input(value, element_type):
                examples = self.story_manager.get_validation_examples(element_type)
                messagebox.showerror(
                    "Validation Error",
                    f"Invalid {element_type}. Examples: {', '.join(examples[:3])}"
                )
                valid = False
                break
            
            story_data[element_type] = value
            self.story_manager.add_story_element(element_type, value)
        
        if not valid:
            return
        
        # Build the story
        story = self.build_story(story_data)
        
        # Save the story
        self.story_manager.save_current_story()
        
        # Show the story
        self.show_story_result(story, story_window)
    
    def build_story(self, story_data: Dict[str, str]) -> str:
        """Builds the complete story from user inputs."""
        story = (
            f"Once upon a time, there was a {story_data['adjective']} teenager named "
            f"{story_data['name']} who lived in a {story_data['place']}. "
            f"One day, they {story_data['past_action']} something that would change "
            f"their life forever. Now, they {story_data['future_action']} to make "
            f"their dreams come true. And so, their incredible journey began..."
        )
        return story
    
    def show_story_result(self, story: str, parent_window):
        """Shows the generated story in a new window."""
        result_window = tk.Toplevel(parent_window)
        result_window.title("🎭 Your Story")
        result_window.geometry("600x500")
        result_window.configure(bg=self.colors['bg_success'])
        
        # Title
        title_label = tk.Label(
            result_window,
            text="🎭 Your Amazing Story",
            font=("Arial", 20, "bold"),
            bg=self.colors['bg_success'],
            fg=self.colors['accent_green']
        )
        title_label.pack(pady=15)
        
        # Story text
        story_text = scrolledtext.ScrolledText(
            result_window,
            wrap=tk.WORD,
            font=("Arial", 12),
            bg='white',
            fg=self.colors['text_primary'],
            relief='solid',
            bd=2,
            height=15
        )
        story_text.pack(pady=15, padx=20, fill='both', expand=True)
        story_text.insert('1.0', story)
        story_text.config(state='disabled')
        
        # Close button
        close_btn = tk.Button(
            result_window,
            text="Close",
            command=result_window.destroy,
            font=("Arial", 12),
            bg=self.colors['accent_green'],
            fg='white',
            relief='raised',
            bd=2,
            width=10,
            cursor='hand2'
        )
        close_btn.pack(pady=10)
    
    def quiz_window(self):
        """Opens the quiz window."""
        quiz_window = tk.Toplevel(self.root)
        quiz_window.title("🎯 Storytelling Quiz")
        quiz_window.geometry("600x500")
        quiz_window.configure(bg=self.colors['bg_warning'])
        
        # Title
        title_label = tk.Label(
            quiz_window,
            text="🎯 Storytelling Quiz",
            font=("Arial", 24, "bold"),
            bg=self.colors['bg_warning'],
            fg=self.colors['accent_orange']
        )
        title_label.pack(pady=20)
        
        # Question display
        self.question_label = tk.Label(
            quiz_window,
            text="Click 'Start Quiz' to begin!",
            font=("Arial", 16),
            bg=self.colors['bg_warning'],
            fg=self.colors['text_primary'],
            wraplength=500
        )
        self.question_label.pack(pady=20)
        
        # Options frame
        self.options_frame = tk.Frame(quiz_window, bg=self.colors['bg_warning'])
        self.options_frame.pack(pady=20, fill='both', expand=True)
        
        # Answer variable
        self.answer_var = tk.StringVar()
        
        # Buttons frame
        button_frame = tk.Frame(quiz_window, bg=self.colors['bg_warning'])
        button_frame.pack(pady=20)
        
        # Start button
        start_btn = tk.Button(
            button_frame,
            text="🎯 Start Quiz",
            command=lambda: self.start_quiz(quiz_window),
            font=("Arial", 16, "bold"),
            bg=self.colors['accent_orange'],
            fg='white',
            relief='raised',
            bd=3,
            width=12,
            height=2,
            cursor='hand2'
        )
        start_btn.pack(side='left', padx=10)
        
        # Back button
        back_btn = tk.Button(
            button_frame,
            text="← Back to Menu",
            command=quiz_window.destroy,
            font=("Arial", 14),
            bg=self.colors['accent_red'],
            fg='white',
            relief='raised',
            bd=3,
            width=12,
            height=2,
            cursor='hand2'
        )
        back_btn.pack(side='left', padx=10)
    
    def start_quiz(self, quiz_window):
        """Starts the quiz with a random question."""
        self.current_question = self.story_manager.get_random_question()
        self.display_question(quiz_window)
    
    def display_question(self, quiz_window):
        """Displays the current question and options."""
        # Clear previous options
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        # Display question
        self.question_label.config(text=self.current_question['question'])
        
        # Create radio buttons for options with different colors
        colors = [self.colors['accent_blue'], self.colors['accent_green'], 
                 self.colors['accent_orange'], self.colors['accent_purple'], 
                 self.colors['accent_pink']]
        
        for i, option in enumerate(self.current_question['options']):
            radio_btn = tk.Radiobutton(
                self.options_frame,
                text=option,
                variable=self.answer_var,
                value=option,
                font=("Arial", 12),
                bg=self.colors['bg_warning'],
                fg=self.colors['text_primary'],
                selectcolor=colors[i % len(colors)],
                activebackground=self.colors['bg_warning'],
                cursor='hand2'
            )
            radio_btn.pack(anchor='w', pady=8, padx=20)
        
        # Submit button
        submit_btn = tk.Button(
            self.options_frame,
            text="Submit Answer",
            command=lambda: self.check_answer(quiz_window),
            font=("Arial", 14, "bold"),
            bg=self.colors['accent_green'],
            fg='white',
            relief='raised',
            bd=3,
            width=12,
            cursor='hand2'
        )
        submit_btn.pack(pady=20)
    
    def check_answer(self, quiz_window):
        """Checks the user's answer and provides feedback."""
        user_answer = self.answer_var.get()
        
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
            messagebox.showinfo("Correct!", f"🎉 {self.current_question['explanation']}")
        else:
            messagebox.showinfo(
                "Incorrect",
                f"The best answer was: {self.current_question['correct_answer']}\n\n{self.current_question['explanation']}"
            )
        
        # Ask if they want another question
        if messagebox.askyesno("Continue", "Would you like another question?"):
            self.current_question = self.story_manager.get_random_question()
            self.answer_var.set("")
            self.display_question(quiz_window)
        else:
            quiz_window.destroy()
    
    def history_window(self):
        """Opens the story history window."""
        history_window = tk.Toplevel(self.root)
        history_window.title("📖 Story History")
        history_window.geometry("700x500")
        history_window.configure(bg=self.colors['bg_secondary'])
        
        # Title
        title_label = tk.Label(
            history_window,
            text="📖 Your Story History",
            font=("Arial", 24, "bold"),
            bg=self.colors['bg_secondary'],
            fg=self.colors['accent_green']
        )
        title_label.pack(pady=20)
        
        # History text
        history_text = scrolledtext.ScrolledText(
            history_window,
            wrap=tk.WORD,
            font=("Arial", 11),
            bg='white',
            fg=self.colors['text_primary'],
            relief='solid',
            bd=2,
            height=20
        )
        history_text.pack(pady=15, padx=20, fill='both', expand=True)
        
        # Display history
        history = self.story_manager.get_story_history()
        if not history:
            history_text.insert('1.0', "No saved stories yet. Create your first story!")
        else:
            for i, story in enumerate(history[-10:], 1):  # Show last 10 stories
                history_text.insert('end', f"Story #{story.get('story_id', i)}\n")
                history_text.insert('end', f"Created: {story.get('timestamp', 'Unknown')}\n")
                history_text.insert('end', f"Character: {story.get('name', 'Unknown')} - {story.get('adjective', 'Unknown')}\n")
                history_text.insert('end', f"Setting: {story.get('place', 'Unknown')}\n")
                history_text.insert('end', "-" * 50 + "\n\n")
        
        history_text.config(state='disabled')
        
        # Close button
        close_btn = tk.Button(
            history_window,
            text="Close",
            command=history_window.destroy,
            font=("Arial", 12),
            bg=self.colors['accent_green'],
            fg='white',
            relief='raised',
            bd=2,
            width=10,
            cursor='hand2'
        )
        close_btn.pack(pady=10)
    
    def statistics_window(self):
        """Opens the quiz statistics window."""
        stats_window = tk.Toplevel(self.root)
        stats_window.title("📊 Quiz Statistics")
        stats_window.geometry("500x400")
        stats_window.configure(bg=self.colors['bg_secondary'])
        
        # Title
        title_label = tk.Label(
            stats_window,
            text="📊 Your Quiz Performance",
            font=("Arial", 24, "bold"),
            bg=self.colors['bg_secondary'],
            fg=self.colors['accent_purple']
        )
        title_label.pack(pady=20)
        
        # Statistics text
        stats_text = scrolledtext.ScrolledText(
            stats_window,
            wrap=tk.WORD,
            font=("Arial", 12),
            bg='white',
            fg=self.colors['text_primary'],
            relief='solid',
            bd=2,
            height=15
        )
        stats_text.pack(pady=15, padx=20, fill='both', expand=True)
        
        # Display statistics
        stats = self.story_manager.get_quiz_statistics()
        if not stats:
            stats_text.insert('1.0', "No quiz data available yet. Take some questions first!")
        else:
            stats_text.insert('end', f"Total Questions Answered: {stats['total_questions']}\n\n")
            stats_text.insert('end', f"Correct Answers: {stats['correct_answers']}\n\n")
            stats_text.insert('end', f"Accuracy: {stats['accuracy_percentage']:.1f}%\n\n")
            
            # Show recent performance
            recent = stats['recent_performance']
            if recent:
                recent_correct = sum(recent)
                stats_text.insert('end', f"Recent Performance (last 5): {recent_correct}/{len(recent)} correct\n\n")
                
                # Give encouragement
                if stats['accuracy_percentage'] >= 80:
                    stats_text.insert('end', "🌟 Excellent! You're a storytelling expert!")
                elif stats['accuracy_percentage'] >= 60:
                    stats_text.insert('end', "👍 Good job! Keep learning and improving!")
                else:
                    stats_text.insert('end', "📚 Keep practicing! Storytelling takes time to master!")
        
        stats_text.config(state='disabled')
        
        # Close button
        close_btn = tk.Button(
            stats_window,
            text="Close",
            command=stats_window.destroy,
            font=("Arial", 12),
            bg=self.colors['accent_purple'],
            fg='white',
            relief='raised',
            bd=2,
            width=10,
            cursor='hand2'
        )
        close_btn.pack(pady=10)

def main():
    """Main function to run the GUI application."""
    root = tk.Tk()
    app = StoryGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 