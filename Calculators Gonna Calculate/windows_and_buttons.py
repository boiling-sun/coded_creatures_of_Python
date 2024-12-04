import tkinter as tk
import configs
import operations as ops
from itertools import cycle
from functools import partial


# Constants for window title and size
WINDOW_TITLE = 'calculators gonna calculate!'
WINDOW_HEIGHT, WINDOW_WIDTH = 400, 450

ALL_BUTTON_NAMES = 'C±%/789*456-123+0.='

MAIN_DISPLAY = None
CALCULATION_DISPLAY = None



def create_window():
    """Create the main application window and its frames."""
    root = tk.Tk()  
    root.title(WINDOW_TITLE)  
    root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')  
    
    # Create top and bottom frames for layout
    top_frame = tk.Frame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT * 0.23)
    top_frame.pack(**configs.PACK_KWARGS)

    mid_frame = tk.Frame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT * 0.05)
    mid_frame.pack(**configs.PACK_KWARGS)
    
    bottom_frame = tk.Frame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT * 0.72)
    bottom_frame.pack(**configs.PACK_KWARGS)
    
    return root, top_frame, mid_frame, bottom_frame

def create_display_label(frame):
    """Create a label to display the calculator's output."""
    global MAIN_DISPLAY
    label = tk.Label(frame, text='0', **configs.DISPLAY_LABEL_KWARGS)  
    label.pack(**configs.PACK_KWARGS)
    MAIN_DISPLAY = label
    #return label

def config_display_w_arg(func):
    def wrapper(arg):
        func(arg)
        MAIN_DISPLAY.config(text=ops.on_display_value)
    return wrapper

def config_display(func):
    def wrapper():
        func()
        MAIN_DISPLAY.config(text=ops.on_display_value)
    return wrapper


@config_display
def clear_command():
    ops.reset_all_global_vals()

@config_display
def negative_command():
    ops.negative_sign()

@config_display
def decimal_command():
    ops.decimal_sign()

@config_display
def equals_command():
    ops.equality_sign()

@config_display
def percent_command():
    ops.percent_sign()

@config_display_w_arg
def process_operator_command(current_operator):
     ops.process_operation(current_operator)

@config_display_w_arg
def enter_number_command(number):
    ops.enter_number(number)

def create_buttons(frame):
    """Create calculator buttons and arrange them in a grid."""
    def get_command(name):
        match name:
            case 'C':
                return clear_command
            case '±':
                return negative_command
            case '+' | '-' | '*' | '/':
                return partial(process_operator_command, name)
            case '.':
                return decimal_command
            case '=':
                return equals_command
            case '%':
                return percent_command
            case _:
                return partial(enter_number_command, name)

    rows = cycle(range(configs.GRID_ROWS))  # Cycle through rows
    columns = cycle(range(configs.GRID_COLUMNS))  # Cycle through columns
    #buttons = []
    row = next(rows)

    for butt in ALL_BUTTON_NAMES:
        column = next(columns)
        button = tk.Button(frame, text=butt)
        button.config(command=get_command(butt))
        #buttons.append(butt)
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
    #return buttons
    return

def main():
    global DISPLAY
    root, top_frame, mid_frame, bottom_frame = create_window()
    DISPLAY = create_display_label(top_frame)
    buttons = create_buttons(bottom_frame)
    root.mainloop()

if __name__ == '__main__':
    main()

