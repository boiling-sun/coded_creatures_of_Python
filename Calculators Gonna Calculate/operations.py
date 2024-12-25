class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    
    Instance Attributes:
        display_value (str): Current value displayed on the calculator.
        values (list): List to store values for calculations.
        operator (str): Current operator for calculations.
        appending (bool): Flag to indicate if we are appending to the current display value.
        current_expression (str): Expression to calculate.
        
    Class Attribute:
        MAX_LEN (int): Maximum length for the display value.
    """
    MAX_LEN = 75

    def __init__(self):
        self.display_value = '0'  
        self.values = []
        self.operator = ''
        self.appending = True
        self.current_expression = ''
        # Placeholders for GUI updating displays
        self.update_main_display = lambda: None
        self.update_expression_display = lambda: None

    def reset_all(self):
        """Reset all attributes to their initial state."""
        self.display_value = '0'
        self.values.clear()
        self.operator = ''
        self.appending = True
        self.current_expression = ''
        self.update_displays()
        print(f'Reset all global values: values: {self.values}, operator: {self.operator}, display_value: {self.display_value}')

    def update_displays(self):
        """Update the main and expression displays."""
        self.update_main_display()
        self.update_expression_display()

    def append_to_display(self, value):
        """Append a value to the current display value."""
        if self.display_value == '0':
            self.set_display_value(value)
        else:
            if len(self.display_value) < self.MAX_LEN:
                self.display_value += str(value)
        self.update_main_display()
        print(f'display_value: {self.display_value}')

    def set_display_value(self, value):
        """Set the display value based on provided input, ensuring it doesn't exceed max length."""
        value = str(value)
        self.display_value = value[:self.MAX_LEN] if len(value) > self.MAX_LEN else value
        self.update_main_display()
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
        if self.display_value == 'Error':
            self.reset_all()
            
        if not self.operator or not self.values:
            self.add_to_values(self.display_value)
            self.operator = operation
            self.appending = False
            print(f'Appending set to: {self.appending}')
            print(f'Operator set to: {self.operator}')
            self.current_expression = f'{self.values[0]} {self.operator} '
            self.update_expression_display()
        else:
            self.handle_existing_operator(operation)
                        
        print(f'End of process_operation: values: {self.values}, operator: {self.operator}, display_value: {self.display_value}')

    def handle_existing_operator(self, operation):
        """Handle the case when an operator is already set."""
        if self.appending:
            self.add_to_values(self.display_value)
        if len(self.values) == 2:
            expression = f'{self.values[0]} {self.operator} {self.values[1]}'
            print(f'Calculating: {self.values[0]} {self.operator} {self.values[1]}')
            result = self.calculate_result()
            #self.update_expression_display()
            self.reset_all()
            self.set_display_value(result)
            self.add_to_values(result)
            self.appending = False
            self.update_main_display()
            self.current_expression = expression
            self.update_expression_display()
            self.operator = operation
        elif len(self.values) == 1:
            self.operator = operation
            self.current_expression = f'{self.values[0]} {self.operator} '
            self.update_expression_display()
            
    # def perform_operation(self):
    #     """Evaluate the current operation and calculate the result."""
    #     self.add_to_values(self.display_value)
    #     if self.operator and (result := self.calculate_result()):
    #         self.reset_all()
    #         self.set_display_value(result)
    #         self.add_to_values(result)
        
    def perform_operation(self):
        # if self.display_value != 'Error':
        #     self.current_expression += self.display_value
        #     #self.update_expression_display()  # Обновляем выражение
        #result = self.calculate_result()
        #self.update_expression_display()
        #self.reset_all()
        #self.set_display_value(result)
        #self.add_to_values(result)
        #self.operator = ''
        #self.update_main_display()  # Обновляем результат
        if self.appending:
            self.add_to_values(self.display_value)
        if len(self.values) == 2:
            expression = f'{self.values[0]} {self.operator} {self.values[1]}'
            print(f'Calculating: {self.values[0]} {self.operator} {self.values[1]}')

            result = self.calculate_result()
            #self.update_expression_display()
            #self.reset_all()
            self.set_display_value(result)
            #self.add_to_values(result)
            self.values[0] = result
            self.appending = False
            self.update_main_display()
            self.current_expression = expression
            self.update_expression_display()
        
            
    def calculate_result(self):
        """Calculate the result based on the current operator and values."""

        if len(self.values) != 2:
            print(f'Not enough values to perform calculation: {self.values}')
            return None
        
        a, b = map(float, self.values)
       
        # self.current_expression = f'{a} {self.operator} {b}'
        # self.update_expression_display()
        # print(f'Calculating: {a} {self.operator} {b}')

        try:
            if self.operator == '+':
                result = a + b
            elif self.operator == '-':
                result = a - b
            elif self.operator == '*':
                result = a * b
            elif self.operator == '/':
                result = a / b
        except ZeroDivisionError as e:
            print(f'Error: {e}')
            return 'Error'
        else:
            return self.format_result(result)
    
    def format_result(self, result):
        """Format the result for display."""
        return str(int(result) if int(result) == result else result)

    def toggle_negative(self):
        """Toggle the sign of the current display value."""
        if self.display_value.startswith('-'):
            self.display_value = self.display_value[1:]
        elif self.display_value != '0':
            self.display_value = '-' + self.display_value
        self.update_main_display()

    def calculate_percent(self):
        """Calculate the percentage of the current display value or the first value."""
        if len(self.values) == 0:
            result = float(self.display_value) / 100
        elif len(self.values) == 1:
            result = float(self.values[0]) * float(self.display_value) / 100
        self.set_display_value(self.format_result(result))
        self.update_main_display()
        print(f'display_value: {self.display_value}, values: {self.values}')

    def add_decimal(self):
        """Add a decimal point to the display value if not already present."""
        if '.' in self.display_value:
            pass
        else:
            self.display_value += '.'
        self.update_main_display()
        print(f'on_display_value: {self.display_value}')


def main():
    pass

if __name__ == '__main__':
    main()  

