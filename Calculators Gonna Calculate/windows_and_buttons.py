import tkinter as tk

# Constants for window title and size
WINDOW_TITLE = 'calculators gonna calculate!'
WINDOW_SIZE = '400x400'

# Configuration for the display label
DISPLAY_LABEL_KWARGS = {
    'bg': 'green',           # Background color
    'compound': 'right',     # Text alignment
    'padx': 10,              # Padding on the x-axis
    'pady': 10,              # Padding on the y-axis
    'font': ('Courier New', 30),  # Font style and size
    'fg': 'white',           # Text color
    'anchor': 'e'            # Text anchor position
}

def create_window():
    """Create the main application window and its frames."""
    root = tk.Tk()  
    root.title(WINDOW_TITLE)  
    root.geometry(WINDOW_SIZE)  
    
    # Create top and bottom frames for layout
    top_frame = tk.Frame(root, width=400, height=100)
    top_frame.pack(expand=True, fill='both', padx=10, pady=10)
    bottom_frame = tk.Frame(root, width=400, height=300)
    bottom_frame.pack(expand=True, fill='both', padx=10, pady=10)
    return root, top_frame, bottom_frame

def create_display_label(frame):
    """Create a label to display the calculator's output."""
    label = tk.Label(frame, text='0', **DISPLAY_LABEL_KWARGS)  
    label.pack(expand=True, fill='both', padx=10, pady=10)
    return label

def update_label(label, value, param=None):
    """Update the label's text dynamically based on the provided value."""
    if param == 'append':
        # Append value to the existing label text
        current_text = label.cget('text')
        label.config(text=f'{current_text}{str(value)}')  # Update label text
    else:
        # Set label text to the new value
        label.config(text=str(value)) 
    return

def main():
    root, top_frame, bottom_frame = create_window()
    display = create_display_label(top_frame)
    update_label(display, '1234', param='')
    root.mainloop()

if __name__ == '__main__':
    main()

