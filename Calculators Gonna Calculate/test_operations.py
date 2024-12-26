import pytest
from operations import Calculator

@pytest.fixture(scope='function')
def calculator():
    """Creates a new instance of the Calculator for testing."""
    return Calculator()

def test_initial_state(calculator):
    """Tests the initial state of the calculator."""
    assert calculator.display_value == '0'  
    assert calculator.values == []  
    assert calculator.operator == ''  
    assert calculator.appending is True  
    assert calculator.current_expression == ''  

def test_reset_all(calculator):
    """Tests resetting all values to their initial state."""
    # Set some values before resetting
    calculator.display_value = '42'
    calculator.add_to_values('42')
    calculator.operator = '+'
    calculator.current_expression = '42 + '
    
    # Reset all values
    calculator.reset_all()
    
    # Assert all values are reset
    assert calculator.display_value == '0'
    assert calculator.values == []
    assert calculator.operator == ''
    assert calculator.appending is True
    assert calculator.current_expression == ''

def test_append_to_display(calculator):
    """Tests appending a number to the current display value."""
    calculator.append_to_display(5)
    assert calculator.display_value == '5'
    calculator.append_to_display(0)
    assert calculator.display_value == '50'

def test_enter_number(calculator):
    """Tests the handling of entering numbers."""
    calculator.enter_number(7)
    assert calculator.display_value == '7'
    calculator.enter_number(3)
    assert calculator.display_value == '73'
    
    calculator.appending = False
    calculator.enter_number(8)
    assert calculator.display_value == '8'
    calculator.enter_number(8)
    assert calculator.display_value == '88'

def test_toggle_negative(calculator):
    """Tests toggling the sign of a number."""
    calculator.set_display_value(15)
    calculator.toggle_negative()
    assert calculator.display_value == '-15'
    calculator.toggle_negative()
    assert calculator.display_value == '15'

def test_toggle_negative_zero(calculator):
    """Tests entering a negative zero."""
    calculator.set_display_value(0)
    calculator.toggle_negative()
    assert calculator.display_value == '0'  # Ноль остается нулем, знак не отображается

def test_add_decimal(calculator):
    """Tests adding a decimal point."""
    calculator.set_display_value(42)
    calculator.add_decimal()
    assert calculator.display_value == '42.'
    calculator.add_decimal()
    assert calculator.display_value == '42.'  # Точка не должна добавляться повторно

def test_add_to_values(calculator):
    """Tests adding a number to the list of values."""
    calculator.add_to_values('42')
    assert calculator.values == [42]
    calculator.add_to_values('420')
    assert calculator.values == [42, 420]
    calculator.add_to_values('4200')
    assert calculator.values == [42, 420]

def test_process_operator(calculator):
    """Tests processing operators."""
    calculator.set_display_value(10)
    calculator.process_operator('+')
    assert calculator.operator == '+'
    assert calculator.appending is False
    assert calculator.current_expression == '10 + '

def test_perform_operation(calculator):
    """Tests performing calculations."""
    calculator.set_display_value(7)
    calculator.process_operator('+')
    calculator.enter_number(3)
    calculator.perform_operation()

    # Assert result of the operation
    assert calculator.display_value == '10'
    assert calculator.current_expression == '7 + 3'

def test_division_by_zero(calculator):
    """Tests division by zero handling."""
    calculator.set_display_value(7)
    calculator.process_operator('/')
    calculator.enter_number(0)
    calculator.perform_operation()
    
    # Assert error message for division by zero
    assert calculator.display_value == 'Error'

def test_large_number_handling(calculator):
    """Tests handling of large numbers."""
    large_number = int('9' * 100)
    calculator.set_display_value(large_number)

     # Assert the display value length does not exceed MAX_LEN
    assert len(calculator.display_value) == calculator.MAX_LEN

def test_calculate_percent_no_values(calculator):
    """Tests percentage calculation without any entered values."""
    calculator.set_display_value(50)
    calculator.calculate_percent()
    
    # Assert result of the percentage calculation
    assert calculator.display_value == '0.5'

def test_calculate_percent_with_one_value(calculator):
    """Tests percentage calculation with one entered value."""
    calculator.set_display_value(200)
    calculator.process_operator('*')
    calculator.enter_number(10)
    calculator.calculate_percent()  # 200 * 10% = 20
    calculator.perform_operation()

    # Assert the result of the percentage operation
    assert calculator.display_value == '4000'  # 200 * 20

def test_error_handling_after_operation(calculator):
    """Tests calculator behavior after an error occurs."""
    calculator.set_display_value(10)
    calculator.process_operator('/')
    calculator.enter_number(0)
    calculator.perform_operation()
    
    # Assert error message on division by zero
    assert calculator.display_value == 'Error'
    
    # Attempt to continue input after error
    calculator.enter_number(5)
    assert calculator.display_value == '5'  # Calculator should reset and show 5

def test_expression_display_update(calculator):
    """Tests updating the expression displayed on the calculator."""
    calculator.set_display_value(8)
    calculator.process_operator('*')
    assert calculator.current_expression == '8 * '
    calculator.enter_number(5)
    calculator.perform_operation()
    assert calculator.current_expression == '8 * 5'

def test_repeated_equals(calculator):
    """Tests the calculator's behavior when the equals button is pressed repeatedly."""
    calculator.set_display_value(5)
    calculator.process_operator('+')
    calculator.enter_number(3)
    calculator.perform_operation()
    
    # Assert result after first operation
    assert calculator.display_value == '8'
    
    # Press equals again
    calculator.perform_operation()  # Repeated "="
    
    # Assert result of repeated operation
    assert calculator.display_value == '11'  # Should add previous value (8 + 3)

def test_chained_operations(calculator):
    """Tests performing chained operations."""
    calculator.set_display_value(5)
    calculator.process_operator('+')
    calculator.enter_number(3)
    calculator.perform_operation()
    
    # Assert result of the first operation
    assert calculator.display_value == '8'
    
    calculator.process_operator('*')
    calculator.enter_number(2)
    calculator.perform_operation()
    
    # Assert result of the second operation
    assert calculator.display_value == '16'


if __name__ == '__main__':
    pytest.main()
