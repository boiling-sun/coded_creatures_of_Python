import pytest
from operations import Calculator

@pytest.fixture(scope='function')
def calculator():
    """Создаёт новый экземпляр калькулятора для тестов."""
    return Calculator()

def test_initial_state(calculator):
    """Тестирует начальное состояние калькулятора."""
    assert calculator.display_value == '0'
    assert calculator.values == []
    assert calculator.operator == ''
    assert calculator.appending is True
    assert calculator.current_expression == ''

def test_reset_all(calculator):
    """Тестирует сброс всех значений."""
    calculator.display_value = '42'
    calculator.add_to_values('42')
    calculator.operator = '+'
    calculator.current_expression = '42 + '
    calculator.reset_all()
    assert calculator.display_value == '0'
    assert calculator.values == []
    assert calculator.operator == ''
    assert calculator.appending is True
    assert calculator.current_expression == ''

def test_append_to_display(calculator):
    """Тестирует добавление числа к текущему значению."""
    calculator.append_to_display(5)
    assert calculator.display_value == '5'
    calculator.append_to_display(0)
    assert calculator.display_value == '50'

def test_enter_number(calculator):
    """Тестирует обработку чисел."""
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
    """Тестирует переключение знака числа."""
    calculator.set_display_value(15)
    calculator.toggle_negative()
    assert calculator.display_value == '-15'
    calculator.toggle_negative()
    assert calculator.display_value == '15'

def test_toggle_negative_zero(calculator):
    """Тестирует ввод отрицательного нуля."""
    calculator.set_display_value(0)
    calculator.toggle_negative()
    assert calculator.display_value == '0'  # Ноль остается нулем, знак не отображается

def test_add_decimal(calculator):
    """Тестирует добавление десятичной точки."""
    calculator.set_display_value(42)
    calculator.add_decimal()
    assert calculator.display_value == '42.'
    calculator.add_decimal()
    assert calculator.display_value == '42.'  # Точка не должна добавляться повторно

def test_add_to_values(calculator):
    """Тестирует добавление числа в список значений."""
    calculator.add_to_values('42')
    assert calculator.values == [42]
    calculator.add_to_values('420')
    assert calculator.values == [42, 420]
    calculator.add_to_values('4200')
    assert calculator.values == [42, 420]

def test_process_operator(calculator):
    """Тестирует обработку операторов."""
    calculator.set_display_value(10)
    calculator.process_operator('+')
    assert calculator.operator == '+'
    assert calculator.appending is False
    assert calculator.current_expression == '10.0 + '

def test_perform_operation(calculator):
    """Тестирует вычисление выражений."""
    calculator.set_display_value(7)
    calculator.process_operator('+')
    calculator.enter_number(3)
    calculator.perform_operation()
    assert calculator.display_value == '10'
    assert calculator.current_expression == '7.0 + 3.0'

def test_division_by_zero(calculator):
    """Тестирует деление на ноль."""
    calculator.set_display_value(7)
    calculator.process_operator('/')
    calculator.enter_number(0)
    calculator.perform_operation()
    assert calculator.display_value == 'Error'

def test_large_number_handling(calculator):
    """Тестирует обработку длинных чисел."""
    large_number = int('9' * 100)
    calculator.set_display_value(large_number)
    assert len(calculator.display_value) == calculator.MAX_LEN  # Ограничение длины MAX_LEN

def test_calculate_percent_no_values(calculator):
    """Тестирует знак процента без введенных значений."""
    calculator.set_display_value(50)
    calculator.calculate_percent()
    assert calculator.display_value == '0.5'

def test_calculate_percent_with_one_value(calculator):
    """Тестирует знак процента с одним введенным значением."""
    calculator.set_display_value(200)
    calculator.process_operator('*')
    calculator.enter_number(10)
    calculator.calculate_percent()  # 200 * 10% = 20
    calculator.perform_operation()
    assert calculator.display_value == '4000'  # 200 * 10%

def test_error_handling_after_operation(calculator):
    """Тестирует поведение калькулятора после ошибки."""
    calculator.set_display_value(10)
    calculator.process_operator('/')
    calculator.enter_number(0)
    calculator.perform_operation()
    assert calculator.display_value == 'Error'
    calculator.enter_number(5)  # Попытка продолжить ввод
    assert calculator.display_value == '5'  # Калькулятор должен начать заново

def test_expression_display_update(calculator):
    """Тестирует обновление выражения на дисплее."""
    calculator.set_display_value(8)
    calculator.process_operator('*')
    assert calculator.current_expression == '8.0 * '
    calculator.enter_number(5)
    calculator.perform_operation()
    assert calculator.current_expression == '8.0 * 5.0'

def test_repeated_equals(calculator):
    """Тестирует поведение калькулятора при повторном нажатии "="."""
    calculator.set_display_value(5)
    calculator.process_operator('+')
    calculator.enter_number(3)
    calculator.perform_operation()
    assert calculator.display_value == '8'
    calculator.perform_operation()  # Повторное "="
    assert calculator.display_value == '11'  # Добавляется предыдущее значение (8 + 3)


def test_chained_operations(calculator):
    """Тестирует последовательные операции."""
    calculator.set_display_value(5)
    calculator.process_operator('+')
    calculator.enter_number(3)
    calculator.perform_operation()
    assert calculator.display_value == '8'
    calculator.process_operator('*')
    calculator.enter_number(2)
    calculator.perform_operation()
    assert calculator.display_value == '16'
