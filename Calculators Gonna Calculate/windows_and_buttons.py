import tkinter as tk
import configs
from itertools import cycle
from functools import partial


# Constants for window title and size
WINDOW_TITLE = 'calculators gonna calculate!'
WINDOW_HEIGHT, WINDOW_WIDTH = 400, 400

# Global variables to track display value and calculator state
DISPLAY = None
on_display_value = '0'
values = []
operator = ''

def create_window():
    """Create the main application window and its frames."""
    root = tk.Tk()  
    root.title(WINDOW_TITLE)  
    root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')  
    
    # Create top and bottom frames for layout
    top_frame = tk.Frame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT * 0.25)
    top_frame.pack(**configs.PACK_KWARGS)
    
    bottom_frame = tk.Frame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT * 0.75)
    bottom_frame.pack(**configs.PACK_KWARGS)
    
    return root, top_frame, bottom_frame

def create_display_label(frame):
    """Create a label to display the calculator's output."""
    label = tk.Label(frame, text='0', **configs.DISPLAY_LABEL_KWARGS)  
    label.pack(**configs.PACK_KWARGS)
    return label

def update_label(value=None, *, param=None):
    """Update the label's text dynamically based on the provided value."""
    global on_display_value
    
    if param == 'append':
        # Append value to the existing value on display
        if value == '.' and '.' in on_display_value:
            pass
        else:
            on_display_value += str(value)
            if '.' not in on_display_value:
                on_display_value = on_display_value.lstrip('0')  # Remove leading zeros
    elif value == '-':
        if on_display_value.startswith('-'):
            on_display_value = on_display_value[1:]
        elif on_display_value == '0':
            pass
        else:
            on_display_value =  '-' + on_display_value
    else:
        # Set the display value based on the provided value or reset to '0'
        on_display_value = str(value) if value else '0'
    
    # Update the display with the new value
    DISPLAY.config(text=on_display_value) 
    return

def create_buttons(frame):
    """Create calculator buttons and arrange them in a grid."""

    def get_command(name):
        match name:
            case 'C':
                return clear_all
            case '±':
                return partial(update_label, '-')
            case '+' | '-' | '*' | '/':
                return partial(process_operation, name)
            case '=':
                return equal
            case _:
                return partial(update_label, name, param='append')

    rows = cycle(range(configs.GRID_ROWS))  # Cycle through rows
    columns = cycle(range(configs.GRID_COLUMNS))  # Cycle through columns
    buttons = []
    row = next(rows)

    for butt in 'C±%/789*456-123+0.=':
        column = next(columns)
        button = tk.Button(frame, text=butt)
        button.config(command=get_command(butt))
        buttons.append(butt)
        if butt == '0':
            button.grid(row=row, column=column, columnspan=2, **configs.BUTTONS_GRID_KWARGS)
            button.config(width=2)  # Make '0' button wider
            column = next(columns)  
            continue
        button.grid(row=row, column=column, **configs.BUTTONS_GRID_KWARGS)
        if row == 0:
            frame.grid_columnconfigure(column, weight=1)
        if column == 3:
            frame.grid_rowconfigure(row, weight=1)
            row = next(rows)
    return buttons

# some helper functions
def clear_all():
    update_label()
    clear_global_vals()
    
def clear_global_vals():
    global values, operator
    values.clear()
    operator = ''

def update_on_display(value):
    global on_display_value
    on_display_value = value
    update_label(on_display_value)

def process_operation(operation):
    """Process the given operation and update values and display accordingly."""
    global values, on_display_value, operator
    
    # Append the current display value to the list of values
    if on_display_value:
        values.append(on_display_value)

    if not operator or len(values) == 1:
        # If no operator is set, just set the current operation
        operator = operation
        print(f'values: {values}, operator: {operator}')
    else:
        # Calculate the result using the current operator and values
        print(f'in "process_operation" : before calculation: values: {values}, operator: {operator}')
        result = calculate(*values)
        print(f'in "process_operation" : after calculation: values: {values}, operator: {operator}, result {result}')
        update_on_display(result)  # Update the display with the result
        
        # Clear previous values and set the new operator
        values.clear()
        print(values)
        operator = operation
        #clear_global_vals()
        
        # Store the result for further calculations
        values.append(result)

    # Reset the display value for the next input
    on_display_value = ''    
    print(f'end of the "process_operation" function: values: {values}, operator: {operator}')

def calculate(a, b=None):
    if b:
        print(f'{a}{operator}{b}={str(eval(f'{a}{operator}{b}'))}')
    else: 
        print(f'{a}{operator}{b}={a}')
    return str(eval(f'{a}{operator}{b}')) if b else str(a)
        
def equal():
    global values, on_display_value
    if on_display_value:
        values.append(on_display_value)
    print(f'in "equal" : before calculation: values: {values}, operator: {operator}')
    result = calculate(*values)
    print(f'in "equal" : after calculation: values: {values}, operator: {operator}, result {result}')
    update_on_display(result)  # Update the display with the resul
    clear_global_vals()
    # Store the result for further calculations
    values.append(result)
    # Reset the display value for the next input
    on_display_value = ''    
    print(f'end of the "equal" function: values: {values}, operator: {operator}')

def main():
    global DISPLAY
    root, top_frame, bottom_frame = create_window()
    DISPLAY = create_display_label(top_frame)
    buttons = create_buttons(bottom_frame)
    #update_label(DISPLAY, '01234', param='')
    root.mainloop()

if __name__ == '__main__':
    main()

