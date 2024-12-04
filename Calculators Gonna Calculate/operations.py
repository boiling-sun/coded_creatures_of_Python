# Global variables to track display value and calculator state
on_display_value = '0'  # Current value displayed on the calculator
values = []  # List to store values for calculations
operator = ''  # Current operator for calculations
appending = True  # Flag to indicate if we are appending to the current display value
MAX_LEN = 75  # Maximum length for the display value

def reset_all_global_vals():
    """Reset all global values to their initial state."""
    global on_display_value, values, operator
    set_on_display_value('0')
    values.clear()
    operator = ''
    print(f'Reset all global values: values: {values}, operator: {operator}, on_display_value: {on_display_value}')
    return

def process_operation(operation):
    """Process the given operation and set the operator."""
    global operator, appending
    print(f'Start of process_operation: values: {values}, operator: {operator}, on_display_value: {on_display_value}')
    equality_sign()  # Evaluate any previous operation
    operator = operation
    print(f'Operator set to: {operator}')
    appending = False
    print(f'Appending set to: {appending}')
    print(f'End of process_operation: values: {values}, operator: {operator}, on_display_value: {on_display_value}')
    return

def add_value_to_values(value):
    """Add a value to the list of values if conditions are met."""
    global values, on_display_value
    if on_display_value != 'Error' and len(values) < 2:
        values.append(value)
    else:
        print(f'Error adding value to values: {value}')
    print(f'Values: {values}')
    return

def equality_sign():
    """Evaluate the current operation and calculate the result."""
    global values, operator
    print(f'start of equality_sign operation: values: {values}, operator: {operator}, on_display_value: {on_display_value}')
    add_value_to_values(on_display_value)
    if operator and (result := calculate_result()):
        reset_all_global_vals()
        set_on_display_value(result)
        add_value_to_values(result)
    return

def calculate_result():
    """Calculate the result based on the current operator and values."""
    if len(values) != 2:
        print(f'Not enough values to perform calculation: {values}')
        return None
    else: 
        a, b = values  # Unpack values for calculation
        print(f'Calculating: values: {values}, operator: {operator}')
        try:
            result = eval(f'{a} {operator} {b}')
        except ZeroDivisionError:
            print("Error: Division by zero")
            return 'Error'
        else:
            print(f'Calculation result: {result}')
            return format_result(result)


def decimal_sign():
    """Add a decimal point to the display value if not already present."""
    global on_display_value
    if '.' in on_display_value:
        pass
    else:
        on_display_value += '.'
    print(f'on_display_value: {on_display_value}')
    return
            
def negative_sign():
    """Toggle the sign of the current display value."""
    global on_display_value
    if on_display_value.startswith('-'):
        on_display_value = on_display_value[1:]
    elif on_display_value == '0':
        pass
    else:
        on_display_value =  '-' + on_display_value
    print(f'on_display_value: {on_display_value}')
    return

def percent_sign():
    """Calculate the percentage of the current display value or the first value."""
    global on_display_value, values
    if len(values) == 0:
        result = float(on_display_value) / 100  # Calculate percentage of display value
    elif len(values) == 1:
        result = float(values[0]) * float(on_display_value) / 100  # Calculate percentage of first value
    result = format_result(result)
    set_on_display_value(result)
    print(f'on_display_value: {on_display_value}, values: {values}')
    return

def format_result(result):
    """Format the result for display."""
    if int(result) == float(result):
        result = int(result)
    return str(result)

def append_to_display_value(value):
    """Append a value to the current display value."""
    global on_display_value
    if on_display_value == '0':
        on_display_value = str(value)
    else:
        if len(on_display_value) < MAX_LEN:
            on_display_value += str(value)
    print(f'on_display_value: {on_display_value}')
    return
        
def set_on_display_value(value):
    """Set the display value based on provided input, ensuring it doesn't exceed max length."""
    global on_display_value
    value = str(value)
    if len(value) < MAX_LEN:
        on_display_value = value
    else:
        on_display_value = value[:MAX_LEN]
    print(f'on_display_value set: {on_display_value}')
    return

def enter_number(number):
    """Process the given number and update the display accordingly."""
    global appending
    if appending:
        append_to_display_value(number)
    else:
        set_on_display_value(number)
        appending = True
    return

def main():
    pass

if __name__ == '__main__':
    main()  

