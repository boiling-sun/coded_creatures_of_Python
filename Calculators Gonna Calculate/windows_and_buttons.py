import tkinter as tk
from itertools import cycle
from functools import partial

# Constants for window title and size
WINDOW_TITLE = 'calculators gonna calculate!'
WINDOW_HEIGHT, WINDOW_WIDTH = 400, 400

# Packing options for frames
PACK_KWARGS = {
    'expand': True,
    'fill': 'both',
    'padx': 10,
    'pady': 10
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

# Global variables to track display value and calculator state
DISPLAY = None
on_display_value = '0'
value_1 = 0
value_2 = 0
operator = ''

def create_window():
    """Create the main application window and its frames."""
    root = tk.Tk()  
    root.title(WINDOW_TITLE)  
    root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')  
    
    # Create top and bottom frames for layout
    top_frame = tk.Frame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT * 0.25)
    top_frame.pack(**PACK_KWARGS)
    
    bottom_frame = tk.Frame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT * 0.75)
    bottom_frame.pack(**PACK_KWARGS)
    
    return root, top_frame, bottom_frame

def create_display_label(frame):
    """Create a label to display the calculator's output."""
    label = tk.Label(frame, text='0', **DISPLAY_LABEL_KWARGS)  
    label.pack(**PACK_KWARGS)
    return label

def update_label(label, value=None, *, param=None):
    """Update the label's text dynamically based on the provided value."""
    global on_display_value
    
    if param == 'append':
        # Append value to the existing value on display
        on_display_value += str(value)
        on_display_value = on_display_value.lstrip('0')  # Remove leading zeros
    else:
        # Set the display value based on the provided value or reset to '0'
        on_display_value = str(value) if value else '0'
    
    # Update the label with the new value
    label.config(text=on_display_value) 
    return


def create_buttons(frame):
    """Create calculator buttons and arrange them in a grid."""
    rows = cycle(range(GRID_ROWS))  # Cycle through rows
    columns = cycle(range(GRID_COLUMNS))  # Cycle through columns
    buttons = []
    row = next(rows)

    for butt in 'C±%/789x456-123+0,=':
        column = next(columns)
        button = tk.Button(frame, text=butt)
        button.config(command=partial(update_label, DISPLAY, butt, param='append')) # Rewrite with correct functionality: now appends symbol to the display 
        buttons.append(butt)
        if butt == '0':
            button.grid(row=row, column=column, columnspan=2, **BUTTONS_GRID_KWARGS)
            button.config(width=2)  # Make '0' button wider
            column = next(columns)  
            continue
        button.grid(row=row, column=column, **BUTTONS_GRID_KWARGS)
        if row == 0:
            frame.grid_columnconfigure(column, weight=1)
        if column == 3:
            frame.grid_rowconfigure(row, weight=1)
            row = next(rows)
    return buttons



def main():
    global DISPLAY
    root, top_frame, bottom_frame = create_window()
    DISPLAY = create_display_label(top_frame)
    buttons = create_buttons(bottom_frame)
    update_label(DISPLAY, '1234', param='')
    root.mainloop()

if __name__ == '__main__':
    main()

