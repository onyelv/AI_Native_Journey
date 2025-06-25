# Enhanced Hello World with Data Structures
# This script demonstrates proper use of dictionaries and lists for data management

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserProfile:
    """Data class to store user information."""
    name: str
    favorite_number: int
    lucky_number: int
    created_at: str = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()

class UserManager:
    """Manages user data using appropriate data structures."""
    
    def __init__(self):
        # Dictionary to store current user data
        self.current_user: Optional[UserProfile] = None
        
        # List to store multiple user profiles (for history)
        self.user_history: List[UserProfile] = []
        
        # Dictionary to store lucky number calculations
        self.lucky_calculations: Dict[str, int] = {
            'multiply_by_2': 2,
            'add_10': 10,
            'square_root_approx': 1.414,  # sqrt(2)
            'golden_ratio': 1.618
        }
        
        # List of greeting messages
        self.greeting_messages: List[str] = [
            "Hello there!",
            "Hi! Nice to meet you!",
            "Welcome!",
            "Greetings!",
            "Hey there!"
        ]
    
    def create_user_profile(self, name: str, favorite_number: int) -> UserProfile:
        """Creates a new user profile with calculated lucky number."""
        lucky_number = self.calculate_lucky_number(favorite_number)
        user = UserProfile(name=name, favorite_number=favorite_number, lucky_number=lucky_number)
        self.current_user = user
        self.user_history.append(user)
        return user
    
    def calculate_lucky_number(self, favorite_number: int) -> int:
        """Calculates lucky number using multiple methods."""
        # Use dictionary to store different calculation methods
        calculations = {
            'method1': favorite_number * self.lucky_calculations['multiply_by_2'],
            'method2': favorite_number + self.lucky_calculations['add_10'],
            'method3': int(favorite_number * self.lucky_calculations['golden_ratio'])
        }
        
        # Return the most interesting result (method1 for now)
        return calculations['method1']
    
    def get_random_greeting(self) -> str:
        """Gets a random greeting from the list."""
        import random
        return random.choice(self.greeting_messages)
    
    def get_user_stats(self) -> Dict[str, any]:
        """Returns statistics about user data."""
        if not self.user_history:
            return {}
        
        return {
            'total_users': len(self.user_history),
            'average_favorite_number': sum(u.favorite_number for u in self.user_history) / len(self.user_history),
            'average_lucky_number': sum(u.lucky_number for u in self.user_history) / len(self.user_history),
            'most_common_favorite': max(set(u.favorite_number for u in self.user_history), 
                                      key=lambda x: sum(1 for u in self.user_history if u.favorite_number == x))
        }

def main():
    """Main function demonstrating data structure usage."""
    # Initialize user manager
    user_manager = UserManager()
    
    print("🎉 Welcome to the Enhanced Hello World Program!")
    print("=" * 50)
    
    # Get user input
    user_name = input("Hello! What's your name? ").strip()
    
    # Validate input
    if not user_name:
        print("❌ Name cannot be empty!")
        return
    
    # Get favorite number with validation
    while True:
        try:
            favorite_number = int(input("What's your favorite number? "))
            break
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Create user profile using data structures
    user = user_manager.create_user_profile(user_name, favorite_number)
    
    # Display results using data from structures
    greeting = user_manager.get_random_greeting()
    print(f"\n{greeting}")
    print(f"Nice to meet you, {user.name}!")
    print(f"Your favorite number is: {user.favorite_number}")
    print(f"Your lucky number is: {user.lucky_number}")
    
    # Show some data structure benefits
    print("\n📊 Data Structure Benefits:")
    print(f"   • Your data is stored in a structured format")
    print(f"   • Your profile has been saved to history")
    print(f"   • Lucky number was calculated using multiple methods")
    
    # Display user statistics if we have multiple users
    stats = user_manager.get_user_stats()
    if stats:
        print(f"\n📈 User Statistics:")
        print(f"   • Total users: {stats['total_users']}")
        print(f"   • Average favorite number: {stats['average_favorite_number']:.1f}")
        print(f"   • Average lucky number: {stats['average_lucky_number']:.1f}")
        print(f"   • Most common favorite number: {stats['most_common_favorite']}")
    
    print("\nHave a great day! 🌟")

if __name__ == "__main__":
    main() 