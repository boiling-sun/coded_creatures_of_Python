import tkinter as tk
from itertools import cycle
from functools import partial

# Constants for window title and size
WINDOW_TITLE = 'calculators gonna calculate!'
WINDOW_HEIGHT, WINDOW_WIDTH = 400, 450

ALL_BUTTON_NAMES = 'C±%/789*456-123+0.='

def create_window(pack_kwargs):
    """Create the main application window and its frames."""
    root = tk.Tk()  
    root.title(WINDOW_TITLE)  
    root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')  
    
    # Create top and bottom frames for layout
    top_frame = tk.Frame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT * 0.23)
    top_frame.pack(**pack_kwargs)

    mid_frame = tk.Frame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT * 0.05)
    mid_frame.pack(**pack_kwargs)
    
    bottom_frame = tk.Frame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT * 0.72)
    bottom_frame.pack(**pack_kwargs)

    return root, top_frame, mid_frame, bottom_frame
    
def create_display_label(frame, calculator, display_label_kwargs, pack_kwargs):
    """Create a label to display the calculator's output."""
    label = tk.Label(frame, **display_label_kwargs)
    label.pack(**pack_kwargs)

    # Update display with Calculator's display_value
    def update_display():
        label.config(text=calculator.display_value)

    # Add update method to calculator object
    calculator.update_display = update_display
    calculator.update_display()

def create_buttons(frame, calculator, grid_rows, grid_columns, buttons_grid_kwargs):
    """Create calculator buttons and arrange them in a grid."""
    def get_command(name):
        match name:
            case 'C':
                return calculator.reset_all
            case '±':
                return calculator.toggle_negative
            case '+' | '-' | '*' | '/':
                return partial(calculator.process_operator, name)
            case '.':
                return calculator.decimal_sign
            case '=':
                return calculator.perform_operation
            case '%':
                return calculator.calculate_percent
            case _:
                return partial(calculator.enter_number, name)

    rows = cycle(range(grid_rows))  # Cycle through rows
    columns = cycle(range(grid_columns))  # Cycle through columns
    row = next(rows)

    for butt in ALL_BUTTON_NAMES:
        column = next(columns)
        button = tk.Button(frame, text=butt)
        button.config(command=lambda b=butt: (get_command(b)(), calculator.update_display()))

        if butt == '0':
            button.grid(row=row, column=column, columnspan=2, **buttons_grid_kwargs)
            button.config(width=2)  # Make '0' button wider
            column = next(columns)  
            continue
        button.grid(row=row, column=column, **buttons_grid_kwargs)
        if row == 0:
            frame.grid_columnconfigure(column, weight=1)
        if column == 3:
            frame.grid_rowconfigure(row, weight=1)
            row = next(rows)

def main():
    pass

if __name__ == '__main__':
    main()
