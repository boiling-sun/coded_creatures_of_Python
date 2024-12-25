import tkinter as tk
from itertools import cycle
from functools import partial


def create_window(title, width, height, pack_kwargs):
    """Create the main application window and its frames."""
    root = tk.Tk()  
    root.title(title)  
    root.geometry(f'{width}x{height}')  
    
    # Create top and bottom frames for layout
    top_frame = tk.Frame(root, width=width, height=height * 0.23)
    top_frame.pack(**pack_kwargs)

    mid_frame = tk.Frame(root, width=width, height=height * 0.05)
    mid_frame.pack(**pack_kwargs)
    
    bottom_frame = tk.Frame(root, width=width, height=height * 0.72)
    bottom_frame.pack(**pack_kwargs)

    return root, top_frame, mid_frame, bottom_frame
    
def create_display_label(frame, calculator, display_label_kwargs, pack_kwargs):
    """Create a label to display the calculator's output."""
    main_display = tk.Label(frame, **display_label_kwargs)
    main_display.pack(**pack_kwargs)

    # Update display with Calculator's display_value
    def update_main_display():
        main_display.config(text=calculator.display_value)

    # Add update method to calculator object
    calculator.update_main_display = update_main_display
    # Initialize display
    calculator.update_main_display()

def create_expression_label(frame, calculator, expression_label_kwargs, pack_kwargs):
    """Create a label to display the calculator's expression."""
    expression_label = tk.Label(frame, **expression_label_kwargs)
    expression_label.pack(**pack_kwargs)

    def update_expression_display():
        expression_label.config(text=calculator.current_expression)

    # Add update method to calculator object
    calculator.update_expression_display = update_expression_display
    # Initialize display
    calculator.update_expression_display()

def create_buttons(button_names, frame, calculator, grid_rows, grid_columns, buttons_grid_kwargs):
    """Create calculator buttons and arrange them in a grid."""
    def get_command(name):
        """Return the command function for a given button name."""
        match name:
            case 'C':
                return calculator.reset_all
            case '±':
                return calculator.toggle_negative
            case '+' | '-' | '*' | '/':
                return partial(calculator.process_operator, name)
            case '.':
                return calculator.add_decimal
            case '=':
                return calculator.perform_operation
            case '%':
                return calculator.calculate_percent
            case _:
                return partial(calculator.enter_number, name)

    buttons_dict = {}
    rows = cycle(range(grid_rows))  # Cycle through rows
    columns = cycle(range(grid_columns))  # Cycle through columns
    row = next(rows)

    for b in button_names:
        column = next(columns)
        button = tk.Button(frame)
        button.config(text=b, command=get_command(b))
        buttons_dict[b] = button
        if b == '0':
            button.grid(row=row, column=column, columnspan=2, **buttons_grid_kwargs)
            button.config(width=2, text=b, command=get_command(b))  # Make '0' button wider
            column = next(columns)  
            continue
        button.grid(row=row, column=column, **buttons_grid_kwargs)
        if row == 0:
            frame.grid_columnconfigure(column, weight=1)
        if column == 3:
            frame.grid_rowconfigure(row, weight=1)
            row = next(rows)
        
    return buttons_dict
        

def main():
    pass

if __name__ == '__main__':
    main()
