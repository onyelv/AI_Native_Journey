import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime, timedelta
import json
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum

class Priority(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

class Status(Enum):
    SCHEDULED = "Scheduled"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    PENDING = "Pending"

class FocusLevel(Enum):
    DEEP = "Deep Focus"
    MEDIUM = "Medium Focus"
    LIGHT = "Light Focus"

@dataclass
class Appointment:
    """Data class for appointment management."""
    time: str
    title: str
    appointment_type: str
    duration: str
    status: str
    created_at: str = None
    appointment_id: int = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
        if self.appointment_id is None:
            self.appointment_id = hash(f"{self.time}{self.title}{self.created_at}")

@dataclass
class Task:
    """Data class for task management."""
    priority: str
    title: str
    due_date: str
    category: str
    status: str
    created_at: str = None
    task_id: int = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
        if self.task_id is None:
            self.task_id = hash(f"{self.title}{self.due_date}{self.created_at}")

@dataclass
class TimeBlock:
    """Data class for time block management."""
    time: str
    activity: str
    duration: str
    focus_level: str
    created_at: str = None
    block_id: int = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
        if self.block_id is None:
            self.block_id = hash(f"{self.time}{self.activity}{self.created_at}")

class DataManager:
    """Manages all data operations with proper data structures."""
    
    def __init__(self):
        # Lists to store structured data objects
        self.appointments: List[Appointment] = []
        self.tasks: List[Task] = []
        self.time_blocks: List[TimeBlock] = []
        
        # Dictionary for quick lookups and analytics
        self.appointment_types: Dict[str, int] = {}
        self.task_categories: Dict[str, int] = {}
        self.status_counts: Dict[str, int] = {}
        
        # Load existing data
        self.load_data()
        self.update_analytics()
    
    def add_appointment(self, appointment_data: Dict[str, Any]) -> Appointment:
        """Adds a new appointment with validation."""
        appointment = Appointment(**appointment_data)
        self.appointments.append(appointment)
        self.update_analytics()
        return appointment
    
    def add_task(self, task_data: Dict[str, Any]) -> Task:
        """Adds a new task with validation."""
        task = Task(**task_data)
        self.tasks.append(task)
        self.update_analytics()
        return task
    
    def add_time_block(self, block_data: Dict[str, Any]) -> TimeBlock:
        """Adds a new time block with validation."""
        time_block = TimeBlock(**block_data)
        self.time_blocks.append(time_block)
        self.update_analytics()
        return time_block
    
    def get_appointment_by_id(self, appointment_id: int) -> Optional[Appointment]:
        """Gets appointment by ID."""
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                return appointment
        return None
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Gets task by ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def get_time_block_by_id(self, block_id: int) -> Optional[TimeBlock]:
        """Gets time block by ID."""
        for time_block in self.time_blocks:
            if time_block.block_id == block_id:
                return time_block
        return None
    
    def delete_appointment(self, appointment_id: int) -> bool:
        """Deletes appointment by ID."""
        for i, appointment in enumerate(self.appointments):
            if appointment.appointment_id == appointment_id:
                del self.appointments[i]
                self.update_analytics()
                return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """Deletes task by ID."""
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                del self.tasks[i]
                self.update_analytics()
                return True
        return False
    
    def delete_time_block(self, block_id: int) -> bool:
        """Deletes time block by ID."""
        for i, time_block in enumerate(self.time_blocks):
            if time_block.block_id == block_id:
                del self.time_blocks[i]
                self.update_analytics()
                return True
        return False
    
    def update_appointment(self, appointment_id: int, new_data: Dict[str, Any]) -> bool:
        """Updates appointment data."""
        appointment = self.get_appointment_by_id(appointment_id)
        if appointment:
            for key, value in new_data.items():
                if hasattr(appointment, key):
                    setattr(appointment, key, value)
            self.update_analytics()
            return True
        return False
    
    def update_task(self, task_id: int, new_data: Dict[str, Any]) -> bool:
        """Updates task data."""
        task = self.get_task_by_id(task_id)
        if task:
            for key, value in new_data.items():
                if hasattr(task, key):
                    setattr(task, key, value)
            self.update_analytics()
            return True
        return False
    
    def update_time_block(self, block_id: int, new_data: Dict[str, Any]) -> bool:
        """Updates time block data."""
        time_block = self.get_time_block_by_id(block_id)
        if time_block:
            for key, value in new_data.items():
                if hasattr(time_block, key):
                    setattr(time_block, key, value)
            self.update_analytics()
            return True
        return False
    
    def get_appointments_by_status(self, status: str) -> List[Appointment]:
        """Gets appointments filtered by status."""
        return [app for app in self.appointments if app.status == status]
    
    def get_tasks_by_priority(self, priority: str) -> List[Task]:
        """Gets tasks filtered by priority."""
        return [task for task in self.tasks if task.priority == priority]
    
    def get_tasks_by_category(self, category: str) -> List[Task]:
        """Gets tasks filtered by category."""
        return [task for task in self.tasks if task.category == category]
    
    def get_overdue_tasks(self) -> List[Task]:
        """Gets tasks that are overdue."""
        today = datetime.now().date()
        overdue_tasks = []
        for task in self.tasks:
            try:
                due_date = datetime.strptime(task.due_date, "%Y-%m-%d").date()
                if due_date < today and task.status != Status.COMPLETED.value:
                    overdue_tasks.append(task)
            except ValueError:
                continue
        return overdue_tasks
    
    def update_analytics(self) -> None:
        """Updates analytics dictionaries."""
        # Reset analytics
        self.appointment_types.clear()
        self.task_categories.clear()
        self.status_counts.clear()
        
        # Count appointment types
        for appointment in self.appointments:
            self.appointment_types[appointment.appointment_type] = self.appointment_types.get(appointment.appointment_type, 0) + 1
        
        # Count task categories
        for task in self.tasks:
            self.task_categories[task.category] = self.task_categories.get(task.category, 0) + 1
        
        # Count statuses across all items
        for appointment in self.appointments:
            self.status_counts[appointment.status] = self.status_counts.get(appointment.status, 0) + 1
        for task in self.tasks:
            self.status_counts[task.status] = self.status_counts.get(task.status, 0) + 1
    
    def get_analytics(self) -> Dict[str, Any]:
        """Returns comprehensive analytics."""
        return {
            'total_appointments': len(self.appointments),
            'total_tasks': len(self.tasks),
            'total_time_blocks': len(self.time_blocks),
            'appointment_types': dict(self.appointment_types),
            'task_categories': dict(self.task_categories),
            'status_counts': dict(self.status_counts),
            'overdue_tasks': len(self.get_overdue_tasks()),
            'completed_tasks': len([t for t in self.tasks if t.status == Status.COMPLETED.value]),
            'pending_tasks': len([t for t in self.tasks if t.status == Status.PENDING.value])
        }
    
    def save_data(self) -> None:
        """Saves data to JSON file with proper serialization."""
        data = {
            'appointments': [asdict(app) for app in self.appointments],
            'tasks': [asdict(task) for task in self.tasks],
            'time_blocks': [asdict(block) for block in self.time_blocks]
        }
        try:
            with open('scheduler_data.json', 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save data: {e}")
    
    def load_data(self) -> None:
        """Loads data from JSON file with proper deserialization."""
        try:
            if os.path.exists('scheduler_data.json'):
                with open('scheduler_data.json', 'r') as f:
                    data = json.load(f)
                    
                    # Load appointments
                    self.appointments = [Appointment(**app_data) for app_data in data.get('appointments', [])]
                    
                    # Load tasks
                    self.tasks = [Task(**task_data) for task_data in data.get('tasks', [])]
                    
                    # Load time blocks
                    self.time_blocks = [TimeBlock(**block_data) for block_data in data.get('time_blocks', [])]
                    
        except Exception as e:
            print(f"Warning: Could not load data: {e}")
            self.appointments = []
            self.tasks = []
            self.time_blocks = []

class EntrepreneurScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Entrepreneur Scheduler Pro")
        self.root.geometry("1200x800")
        
        # Initialize data manager
        self.data_manager = DataManager()
        
        # Color scheme
        self.colors = {
            'primary': '#2c3e50',      # Dark blue
            'secondary': '#3498db',    # Light blue
            'accent': '#e74c3c',       # Red
            'success': '#27ae60',      # Green
            'warning': '#f39c12',      # Orange
            'background': '#ecf0f1',   # Light gray
            'surface': '#ffffff',      # White
            'text': '#2c3e50',         # Dark text
            'text_light': '#7f8c8d',   # Light text
            'gradient_start': '#667eea', # Purple gradient start
            'gradient_end': '#764ba2'   # Purple gradient end
        }
        
        self.root.configure(bg=self.colors['background'])
        
        # Configure ttk styles
        self.setup_styles()
        
        # Create main interface
        self.create_widgets()
        self.update_display()
        
    def setup_styles(self):
        """Configure custom ttk styles for modern appearance"""
        style = ttk.Style()
        
        # Configure notebook style
        style.configure('Custom.TNotebook', background=self.colors['background'])
        style.configure('Custom.TNotebook.Tab', 
                       background=self.colors['primary'],
                       foreground='white',
                       padding=[20, 10],
                       font=('Arial', 10, 'bold'))
        style.map('Custom.TNotebook.Tab',
                 background=[('selected', self.colors['secondary']),
                           ('active', self.colors['secondary'])],
                 foreground=[('selected', 'white'),
                           ('active', 'white')])
        
        # Configure button styles
        style.configure('Primary.TButton',
                       background=self.colors['secondary'],
                       foreground='white',
                       font=('Arial', 10, 'bold'),
                       padding=[15, 8])
        style.map('Primary.TButton',
                 background=[('active', self.colors['primary']),
                           ('pressed', self.colors['primary'])],
                 foreground=[('active', 'white'),
                           ('pressed', 'white')])
        
        style.configure('Success.TButton',
                       background=self.colors['success'],
                       foreground='white',
                       font=('Arial', 10, 'bold'),
                       padding=[15, 8])
        style.map('Success.TButton',
                 background=[('active', '#229954'),
                           ('pressed', '#229954')],
                 foreground=[('active', 'white'),
                           ('pressed', 'white')])
        
        style.configure('Warning.TButton',
                       background=self.colors['warning'],
                       foreground='white',
                       font=('Arial', 10, 'bold'),
                       padding=[15, 8])
        style.map('Warning.TButton',
                 background=[('active', '#e67e22'),
                           ('pressed', '#e67e22')],
                 foreground=[('active', 'white'),
                           ('pressed', 'white')])
        
        # Configure treeview style
        style.configure('Custom.Treeview',
                       background=self.colors['surface'],
                       foreground=self.colors['text'],
                       fieldbackground=self.colors['surface'],
                       font=('Arial', 9))
        style.configure('Custom.Treeview.Heading',
                       background=self.colors['primary'],
                       foreground='white',
                       font=('Arial', 10, 'bold'))
        
        # Configure frame style
        style.configure('Card.TFrame',
                       background=self.colors['surface'],
                       relief='raised',
                       borderwidth=1)
        
    def create_widgets(self):
        # Main container with gradient background
        main_frame = tk.Frame(self.root, bg=self.colors['background'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header with gradient effect
        header_frame = tk.Frame(main_frame, bg=self.colors['gradient_start'], height=100)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Title with modern styling
        title_label = tk.Label(header_frame, 
                              text="🚀 Entrepreneur Scheduler Pro", 
                              font=("Arial", 28, "bold"), 
                              bg=self.colors['gradient_start'], 
                              fg='black')
        title_label.pack(expand=True)
        
        # Subtitle
        subtitle_label = tk.Label(header_frame, 
                                 text="Master Your Time, Scale Your Business", 
                                 font=("Arial", 12), 
                                 bg=self.colors['gradient_start'], 
                                 fg='black')
        subtitle_label.pack(pady=(0, 20))
        
        # Notebook with custom style
        self.notebook = ttk.Notebook(main_frame, style='Custom.TNotebook')
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_calendar_tab()
        self.create_tasks_tab()
        self.create_time_blocks_tab()
        self.create_analytics_tab()
        
    def create_calendar_tab(self):
        calendar_frame = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(calendar_frame, text="📅 Calendar")
        
        # Header for calendar tab
        calendar_header = tk.Frame(calendar_frame, bg=self.colors['secondary'], height=60)
        calendar_header.pack(fill=tk.X, padx=10, pady=10)
        calendar_header.pack_propagate(False)
        
        header_label = tk.Label(calendar_header, 
                               text="Appointment Management", 
                               font=("Arial", 16, "bold"), 
                               bg=self.colors['secondary'], 
                               fg='black')
        header_label.pack(expand=True)
        
        # Controls with colored buttons
        controls_frame = ttk.Frame(calendar_frame)
        controls_frame.pack(fill=tk.X, padx=15, pady=15)
        
        ttk.Button(controls_frame, text="➕ Add Appointment", 
                  style='Primary.TButton',
                  command=self.add_appointment).pack(side=tk.LEFT, padx=5)
        ttk.Button(controls_frame, text="✏️ Edit Appointment", 
                  style='Warning.TButton',
                  command=self.edit_appointment).pack(side=tk.LEFT, padx=5)
        ttk.Button(controls_frame, text="🗑️ Delete Appointment", 
                  style='Warning.TButton',
                  command=self.delete_appointment).pack(side=tk.LEFT, padx=5)
        
        # Calendar display with custom styling
        self.calendar_tree = ttk.Treeview(calendar_frame, 
                                         columns=("ID", "Time", "Title", "Type", "Duration", "Status"), 
                                         show="headings", 
                                         height=15,
                                         style='Custom.Treeview')
        self.calendar_tree.heading("ID", text="🆔 ID")
        self.calendar_tree.heading("Time", text="⏰ Time")
        self.calendar_tree.heading("Title", text="📝 Title")
        self.calendar_tree.heading("Type", text="🏷️ Type")
        self.calendar_tree.heading("Duration", text="⏱️ Duration")
        self.calendar_tree.heading("Status", text="📊 Status")
        
        self.calendar_tree.column("ID", width=80)
        self.calendar_tree.column("Time", width=150)
        self.calendar_tree.column("Title", width=250)
        self.calendar_tree.column("Type", width=120)
        self.calendar_tree.column("Duration", width=120)
        self.calendar_tree.column("Status", width=120)
        
        self.calendar_tree.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
    def create_tasks_tab(self):
        tasks_frame = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(tasks_frame, text="📋 Tasks")
        
        # Header for tasks tab
        tasks_header = tk.Frame(tasks_frame, bg=self.colors['success'], height=60)
        tasks_header.pack(fill=tk.X, padx=10, pady=10)
        tasks_header.pack_propagate(False)
        
        header_label = tk.Label(tasks_header, 
                               text="Task Management", 
                               font=("Arial", 16, "bold"), 
                               bg=self.colors['success'], 
                               fg='black')
        header_label.pack(expand=True)
        
        # Controls
        controls_frame = ttk.Frame(tasks_frame)
        controls_frame.pack(fill=tk.X, padx=15, pady=15)
        
        ttk.Button(controls_frame, text="➕ Add Task", 
                  style='Primary.TButton',
                  command=self.add_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(controls_frame, text="✅ Complete Task", 
                  style='Success.TButton',
                  command=self.complete_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(controls_frame, text="🗑️ Delete Task", 
                  style='Warning.TButton',
                  command=self.delete_task).pack(side=tk.LEFT, padx=5)
        
        # Tasks display
        self.tasks_tree = ttk.Treeview(tasks_frame, 
                                      columns=("ID", "Priority", "Title", "Due Date", "Category", "Status"), 
                                      show="headings", 
                                      height=15,
                                      style='Custom.Treeview')
        self.tasks_tree.heading("ID", text="🆔 ID")
        self.tasks_tree.heading("Priority", text="⚡ Priority")
        self.tasks_tree.heading("Title", text="📝 Title")
        self.tasks_tree.heading("Due Date", text="📅 Due Date")
        self.tasks_tree.heading("Category", text="🏷️ Category")
        self.tasks_tree.heading("Status", text="📊 Status")
        
        self.tasks_tree.column("ID", width=80)
        self.tasks_tree.column("Priority", width=100)
        self.tasks_tree.column("Title", width=250)
        self.tasks_tree.column("Due Date", width=120)
        self.tasks_tree.column("Category", width=120)
        self.tasks_tree.column("Status", width=120)
        
        self.tasks_tree.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
    def create_time_blocks_tab(self):
        time_blocks_frame = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(time_blocks_frame, text="⏰ Time Blocks")
        
        # Header for time blocks tab
        blocks_header = tk.Frame(time_blocks_frame, bg=self.colors['warning'], height=60)
        blocks_header.pack(fill=tk.X, padx=10, pady=10)
        blocks_header.pack_propagate(False)
        
        header_label = tk.Label(blocks_header, 
                               text="Time Block Management", 
                               font=("Arial", 16, "bold"), 
                               bg=self.colors['warning'], 
                               fg='black')
        header_label.pack(expand=True)
        
        # Controls
        controls_frame = ttk.Frame(time_blocks_frame)
        controls_frame.pack(fill=tk.X, padx=15, pady=15)
        
        ttk.Button(controls_frame, text="➕ Add Time Block", 
                  style='Warning.TButton',
                  command=self.add_time_block).pack(side=tk.LEFT, padx=5)
        ttk.Button(controls_frame, text="✏️ Edit Time Block", 
                  style='Warning.TButton',
                  command=self.edit_time_block).pack(side=tk.LEFT, padx=5)
        ttk.Button(controls_frame, text="🗑️ Delete Time Block", 
                  style='Warning.TButton',
                  command=self.delete_time_block).pack(side=tk.LEFT, padx=5)
        
        # Time blocks display
        self.time_blocks_tree = ttk.Treeview(time_blocks_frame, 
                                            columns=("ID", "Time", "Activity", "Duration", "Focus Level"), 
                                            show="headings", 
                                            height=15,
                                            style='Custom.Treeview')
        self.time_blocks_tree.heading("ID", text="🆔 ID")
        self.time_blocks_tree.heading("Time", text="⏰ Time")
        self.time_blocks_tree.heading("Activity", text="📝 Activity")
        self.time_blocks_tree.heading("Duration", text="⏱️ Duration")
        self.time_blocks_tree.heading("Focus Level", text="🎯 Focus Level")
        
        self.time_blocks_tree.column("ID", width=80)
        self.time_blocks_tree.column("Time", width=150)
        self.time_blocks_tree.column("Activity", width=250)
        self.time_blocks_tree.column("Duration", width=120)
        self.time_blocks_tree.column("Focus Level", width=120)
        
        self.time_blocks_tree.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
    def create_analytics_tab(self):
        analytics_frame = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(analytics_frame, text="📊 Analytics")
        
        # Header for analytics tab
        analytics_header = tk.Frame(analytics_frame, bg=self.colors['accent'], height=60)
        analytics_header.pack(fill=tk.X, padx=10, pady=10)
        analytics_header.pack_propagate(False)
        
        header_label = tk.Label(analytics_header, 
                               text="Business Analytics", 
                               font=("Arial", 16, "bold"), 
                               bg=self.colors['accent'], 
                               fg='white')
        header_label.pack(expand=True)
        
        # Analytics display
        self.analytics_text = tk.Text(analytics_frame, 
                                     height=20, 
                                     font=("Courier", 10),
                                     bg=self.colors['surface'],
                                     fg=self.colors['text'])
        self.analytics_text.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
    def add_appointment(self):
        dialog = AppointmentDialog(self.root, "Add Appointment")
        if dialog.result:
            appointment = self.data_manager.add_appointment(dialog.result)
            self.update_display()
            self.data_manager.save_data()
            messagebox.showinfo("Success", f"Appointment '{appointment.title}' added successfully!")
            
    def edit_appointment(self):
        selection = self.calendar_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an appointment to edit.")
            return
            
        item = self.calendar_tree.item(selection[0])
        appointment_id = int(item['values'][0])
        appointment = self.data_manager.get_appointment_by_id(appointment_id)
        
        if appointment:
            dialog = AppointmentDialog(self.root, "Edit Appointment", asdict(appointment))
            if dialog.result:
                self.data_manager.update_appointment(appointment_id, dialog.result)
                self.update_display()
                self.data_manager.save_data()
                messagebox.showinfo("Success", "Appointment updated successfully!")
        else:
            messagebox.showerror("Error", "Appointment not found.")
            
    def delete_appointment(self):
        selection = self.calendar_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an appointment to delete.")
            return
            
        item = self.calendar_tree.item(selection[0])
        appointment_id = int(item['values'][0])
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this appointment?"):
            if self.data_manager.delete_appointment(appointment_id):
                self.update_display()
                self.data_manager.save_data()
                messagebox.showinfo("Success", "Appointment deleted successfully!")
            else:
                messagebox.showerror("Error", "Failed to delete appointment.")
                
    def add_task(self):
        dialog = TaskDialog(self.root, "Add Task")
        if dialog.result:
            task = self.data_manager.add_task(dialog.result)
            self.update_display()
            self.data_manager.save_data()
            messagebox.showinfo("Success", f"Task '{task.title}' added successfully!")
            
    def complete_task(self):
        selection = self.tasks_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a task to complete.")
            return
            
        item = self.tasks_tree.item(selection[0])
        task_id = int(item['values'][0])
        
        if self.data_manager.update_task(task_id, {'status': Status.COMPLETED.value}):
            self.update_display()
            self.data_manager.save_data()
            messagebox.showinfo("Success", "Task marked as completed!")
        else:
            messagebox.showerror("Error", "Failed to update task.")
            
    def delete_task(self):
        selection = self.tasks_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            return
            
        item = self.tasks_tree.item(selection[0])
        task_id = int(item['values'][0])
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this task?"):
            if self.data_manager.delete_task(task_id):
                self.update_display()
                self.data_manager.save_data()
                messagebox.showinfo("Success", "Task deleted successfully!")
            else:
                messagebox.showerror("Error", "Failed to delete task.")
                
    def add_time_block(self):
        dialog = TimeBlockDialog(self.root, "Add Time Block")
        if dialog.result:
            time_block = self.data_manager.add_time_block(dialog.result)
            self.update_display()
            self.data_manager.save_data()
            messagebox.showinfo("Success", f"Time block '{time_block.activity}' added successfully!")
            
    def edit_time_block(self):
        selection = self.time_blocks_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a time block to edit.")
            return
            
        item = self.time_blocks_tree.item(selection[0])
        block_id = int(item['values'][0])
        time_block = self.data_manager.get_time_block_by_id(block_id)
        
        if time_block:
            dialog = TimeBlockDialog(self.root, "Edit Time Block", asdict(time_block))
            if dialog.result:
                self.data_manager.update_time_block(block_id, dialog.result)
                self.update_display()
                self.data_manager.save_data()
                messagebox.showinfo("Success", "Time block updated successfully!")
        else:
            messagebox.showerror("Error", "Time block not found.")
            
    def delete_time_block(self):
        selection = self.time_blocks_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a time block to delete.")
            return
            
        item = self.time_blocks_tree.item(selection[0])
        block_id = int(item['values'][0])
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this time block?"):
            if self.data_manager.delete_time_block(block_id):
                self.update_display()
                self.data_manager.save_data()
                messagebox.showinfo("Success", "Time block deleted successfully!")
            else:
                messagebox.showerror("Error", "Failed to delete time block.")
                
    def update_display(self):
        # Clear existing items
        for tree in [self.calendar_tree, self.tasks_tree, self.time_blocks_tree]:
            for item in tree.get_children():
                tree.delete(item)
        
        # Update appointments
        for appointment in self.data_manager.appointments:
            self.calendar_tree.insert('', 'end', values=(
                appointment.appointment_id,
                appointment.time,
                appointment.title,
                appointment.appointment_type,
                appointment.duration,
                appointment.status
            ))
        
        # Update tasks
        for task in self.data_manager.tasks:
            self.tasks_tree.insert('', 'end', values=(
                task.task_id,
                task.priority,
                task.title,
                task.due_date,
                task.category,
                task.status
            ))
        
        # Update time blocks
        for time_block in self.data_manager.time_blocks:
            self.time_blocks_tree.insert('', 'end', values=(
                time_block.block_id,
                time_block.time,
                time_block.activity,
                time_block.duration,
                time_block.focus_level
            ))
        
        # Update analytics
        self.update_analytics_display()
        
    def update_analytics_display(self):
        analytics = self.data_manager.get_analytics()
        
        self.analytics_text.delete(1.0, tk.END)
        
        analytics_text = f"""
📊 ENTREPRENEUR SCHEDULER ANALYTICS
{'='*50}

📅 APPOINTMENTS
Total Appointments: {analytics['total_appointments']}
Appointment Types: {analytics['appointment_types']}

📋 TASKS
Total Tasks: {analytics['total_tasks']}
Completed Tasks: {analytics['completed_tasks']}
Pending Tasks: {analytics['pending_tasks']}
Overdue Tasks: {analytics['overdue_tasks']}
Task Categories: {analytics['task_categories']}

⏰ TIME BLOCKS
Total Time Blocks: {analytics['total_time_blocks']}

📈 STATUS OVERVIEW
Status Counts: {analytics['status_counts']}

🎯 RECOMMENDATIONS
"""
        
        # Add recommendations based on analytics
        if analytics['overdue_tasks'] > 0:
            analytics_text += f"⚠️  You have {analytics['overdue_tasks']} overdue tasks. Consider prioritizing them.\n"
        
        if analytics['pending_tasks'] > analytics['completed_tasks']:
            analytics_text += "📈 You have more pending than completed tasks. Focus on task completion.\n"
        
        if analytics['total_appointments'] == 0:
            analytics_text += "📅 No appointments scheduled. Consider adding some to stay organized.\n"
        
        completion_rate = (analytics['completed_tasks'] / max(analytics['total_tasks'], 1)) * 100
        analytics_text += f"📊 Task Completion Rate: {completion_rate:.1f}%\n"
        
        self.analytics_text.insert(1.0, analytics_text)

class AppointmentDialog:
    def __init__(self, parent, title, appointment_data=None):
        self.result = None
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("400x300")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Create form
        ttk.Label(self.dialog, text="Time (HH:MM):").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.time_entry = ttk.Entry(self.dialog)
        self.time_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        ttk.Label(self.dialog, text="Title:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.title_entry = ttk.Entry(self.dialog)
        self.title_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        ttk.Label(self.dialog, text="Type:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.type_combo = ttk.Combobox(self.dialog, values=["Meeting", "Call", "Presentation", "Review", "Other"])
        self.type_combo.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        ttk.Label(self.dialog, text="Duration:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.duration_entry = ttk.Entry(self.dialog)
        self.duration_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        ttk.Label(self.dialog, text="Status:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.status_combo = ttk.Combobox(self.dialog, values=["Scheduled", "In Progress", "Completed", "Cancelled"])
        self.status_combo.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        # Buttons
        button_frame = ttk.Frame(self.dialog)
        button_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        ttk.Button(button_frame, text="Save", command=self.save).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cancel", command=self.cancel).pack(side=tk.LEFT, padx=5)
        
        # Populate if editing
        if appointment_data:
            self.time_entry.insert(0, appointment_data['time'])
            self.title_entry.insert(0, appointment_data['title'])
            self.type_combo.set(appointment_data['appointment_type'])
            self.duration_entry.insert(0, appointment_data['duration'])
            self.status_combo.set(appointment_data['status'])
        else:
            self.status_combo.set("Scheduled")
            
        self.dialog.wait_window()
        
    def save(self):
        self.result = {
            'time': self.time_entry.get(),
            'title': self.title_entry.get(),
            'appointment_type': self.type_combo.get(),
            'duration': self.duration_entry.get(),
            'status': self.status_combo.get()
        }
        self.dialog.destroy()
        
    def cancel(self):
        self.dialog.destroy()

class TaskDialog:
    def __init__(self, parent, title, task_data=None):
        self.result = None
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("400x300")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Create form
        ttk.Label(self.dialog, text="Priority:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.priority_combo = ttk.Combobox(self.dialog, values=["High", "Medium", "Low"])
        self.priority_combo.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        ttk.Label(self.dialog, text="Title:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.title_entry = ttk.Entry(self.dialog)
        self.title_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        ttk.Label(self.dialog, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.due_date_entry = ttk.Entry(self.dialog)
        self.due_date_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        ttk.Label(self.dialog, text="Category:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.category_combo = ttk.Combobox(self.dialog, values=["Business", "Personal", "Financial", "Marketing", "Development", "Other"])
        self.category_combo.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        ttk.Label(self.dialog, text="Status:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.status_combo = ttk.Combobox(self.dialog, values=["Pending", "In Progress", "Completed"])
        self.status_combo.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        # Buttons
        button_frame = ttk.Frame(self.dialog)
        button_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        ttk.Button(button_frame, text="Save", command=self.save).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cancel", command=self.cancel).pack(side=tk.LEFT, padx=5)
        
        # Populate if editing
        if task_data:
            self.priority_combo.set(task_data['priority'])
            self.title_entry.insert(0, task_data['title'])
            self.due_date_entry.insert(0, task_data['due_date'])
            self.category_combo.set(task_data['category'])
            self.status_combo.set(task_data['status'])
        else:
            self.status_combo.set("Pending")
            
        self.dialog.wait_window()
        
    def save(self):
        self.result = {
            'priority': self.priority_combo.get(),
            'title': self.title_entry.get(),
            'due_date': self.due_date_entry.get(),
            'category': self.category_combo.get(),
            'status': self.status_combo.get()
        }
        self.dialog.destroy()
        
    def cancel(self):
        self.dialog.destroy()

class TimeBlockDialog:
    def __init__(self, parent, title, block_data=None):
        self.result = None
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("400x250")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Create form
        ttk.Label(self.dialog, text="Time (HH:MM):").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.time_entry = ttk.Entry(self.dialog)
        self.time_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        ttk.Label(self.dialog, text="Activity:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.activity_entry = ttk.Entry(self.dialog)
        self.activity_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        ttk.Label(self.dialog, text="Duration (hours):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.duration_entry = ttk.Entry(self.dialog)
        self.duration_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        ttk.Label(self.dialog, text="Focus Level:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.focus_combo = ttk.Combobox(self.dialog, values=["Deep Focus", "Medium Focus", "Light Focus"])
        self.focus_combo.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W+tk.E)
        
        # Buttons
        button_frame = ttk.Frame(self.dialog)
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)
        
        ttk.Button(button_frame, text="Save", command=self.save).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cancel", command=self.cancel).pack(side=tk.LEFT, padx=5)
        
        # Populate if editing
        if block_data:
            self.time_entry.insert(0, block_data['time'])
            self.activity_entry.insert(0, block_data['activity'])
            self.duration_entry.insert(0, block_data['duration'].split()[0])
            self.focus_combo.set(block_data['focus_level'])
            
        self.dialog.wait_window()
        
    def save(self):
        self.result = {
            'time': self.time_entry.get(),
            'activity': self.activity_entry.get(),
            'duration': f"{self.duration_entry.get()} hours",
            'focus_level': self.focus_combo.get()
        }
        self.dialog.destroy()
        
    def cancel(self):
        self.dialog.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = EntrepreneurScheduler(root)
    root.mainloop() 