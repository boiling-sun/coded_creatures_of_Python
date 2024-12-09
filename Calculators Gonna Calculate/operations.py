class Calculator:
    """
    Instance attributes track display value and calculator state.
    on_display_value (str): Current value displayed on the calculator
    values (list): List to store values for calculations
    operator (str): Current operator for calculations
    appending (bool): # Flag to indicate if we are appending to the current display value
    
    Class attribute:
    MAX_LEN (int): 75 is naximum length for the display value
    """
    MAX_LEN = 75

    def __init__(self):
        self.display_value = '0'  
        self.values = []
        self.operator = ''
        self.appending = True

    def reset_all(self):
        """Reset all attributes to their initial state."""
        self.display_value = '0'
        self.values.clear()
        self.operator = ''
        self.appending = True
        print(f'Reset all global values: values: {self.ues}, operator: {self.rator}, display_value: {self.display_value}')

    def append_to_display(self, value):
        """Append a value to the current display value."""
        if self.display_value == '0':
            self.display_value = str(value)
        else:
            if len(self.display_value) < self.MAX_LEN:
                self.display_value += str(value)
        print(f'display_value: {self.display_value}')

    def set_display_value(self, value):
        """Set the display value based on provided input, ensuring it doesn't exceed max length."""
        value = str(value)
        self.display_value = value[:self.MAX_LEN] if len(value) > self.MAX_LEN else value
        print(f'display_value set: {self.display_value}')

    def enter_number(self, number):
        """Process the given number and update the display accordingly."""
        if self.appending:
            self.append_to_display(number)
        else:
            self.set_display_value(number)
            self.appending = True

    def add_to_values(self, value):
        """Add a value to the list of values if conditions are met."""
        if self.display_value != 'Error' and len(self.values) < 2:
            self.values.append(float(value))
        else:
            print(f'Error adding value to values: {value}')
        print(f'Values: {self.values}')

    def process_operator(self, operation):
        """Process the given operation and set the operator."""
        print(f'Start of process_operation: values: {self.values}, operator: {self.operator}, display_value: {self.display_value}')
        self.perform_operation()  # Evaluate any previous operation
        self.operator = operation
        print(f'Operator set to: {self.operator}')
        self.appending = False
        print(f'Appending set to: {self.appending}')
        print(f'End of process_operation: values: {self.values}, operator: {self.operator}, display_value: {self.display_value}')

    def perform_operation(self):
        """Evaluate the current operation and calculate the result."""
        self.add_to_values(self.display_value)
        if self.operator and (result := self.calculate_result()):
            self.reset_all()
            self.set_display_value(result)
            self.add_to_values(result)

    def calculate_result(self):
        """Calculate the result based on the current operator and values."""
        if len(self.values) != 2:
            print(f'Not enough values to perform calculation: {self.values}')
            return None
        a, b = self.values
        try:
            if self.operator == '+':
                result = a + b
            elif self.operator == '-':
                result = a - b
            elif self.operator == '*':
                result = a * b
            elif self.operator == '/':
                result = a / b
        except Exception as e:
            print(f"Error: {e}")
            return 'Error'
        return self.format_result(result)
    
    def format_result(self, result):
        """Format the result for display."""
        if int(result) == float(result):
            result = int(result)
        return str(result)

    def toggle_negative(self):
        """Переключить знак текущего значения."""
        if self.display_value.startswith('-'):
            self.display_value = self.display_value[1:]
        elif self.display_value != '0':
            self.display_value = '-' + self.display_value

    def calculate_percent(self):
        """Calculate the percentage of the current display value or the first value."""
        if len(self.values) == 0:
            result = float(self.display_value) / 100
        elif len(self.values) == 1:
            result = float(self.values[0]) * float(self.on_display_value) / 100
        self.set_display_value(self.format_result(result))
        print(f'display_value: {self.display_value}, values: {self.values}')

    def decimal_sign(self):
        """Add a decimal point to the display value if not already present."""
        if '.' in self.display_value:
            pass
        else:
            self.display_value += '.'
        print(f'on_display_value: {self.display_value}')


def main():
    pass

if __name__ == '__main__':
    main()  

