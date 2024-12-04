"""
This code defines configuration options for a GUI application using the Tkinter library in Python.
It includes packing options for frames, grid configuration for buttons, and settings for a display label.
"""

# Packing options for frames
PACK_KWARGS = {
    'expand': True,          # Allow the widget to expand to fill any extra space
    'fill': 'both',          # Fill the widget both horizontally and vertically
    'padx': 10,              # Padding on the x-axis
    'pady': 10               # Padding on the y-axis
}

# Grid configuration for buttons
GRID_ROWS, GRID_COLUMNS = 5, 4
BUTTONS_GRID_KWARGS = {
    'padx': 5,               # Padding on the x-axis
    'pady': 5,               # Padding on the y-axis
    'sticky': 'nsew',        # Make buttons expand to fill grid space
}

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
