import pytest
import tkinter as tk
from unittest.mock import patch, MagicMock
from functools import partial
from windows_and_buttons import create_window, create_display_label, create_expression_label, create_buttons

@pytest.fixture
def window_title():
    """Fixture for the title of the calculator window."""
    return "Calculator"

@pytest.fixture
def window_width():
    """Fixture for the width of the calculator window."""
    return 300

@pytest.fixture
def window_height():
    """Fixture for the height of the calculator window."""
    return 500

@pytest.fixture
def mock_calculator():
    """Fixture to create a mock calculator object with necessary methods."""
    calculator = MagicMock()
    calculator.display_value = '0'
    calculator.current_expression = ''
    calculator.reset_all = MagicMock()
    calculator.toggle_negative = MagicMock()
    calculator.process_operator = MagicMock()
    calculator.add_decimal = MagicMock()
    calculator.perform_operation = MagicMock()
    calculator.calculate_percent = MagicMock()
    calculator.enter_number = MagicMock()
    return calculator

def test_create_window(window_title, window_width, window_height):
    """Test the creation of the calculator window and its frames."""
    pack_kwargs = {'side': 'top', 'fill': 'both', 'expand': True}
    
    with patch('tkinter.Tk') as mock_tk, \
         patch('tkinter.Frame') as mock_frame:
        
        # Mock the Tk instance and Frame instances
        mock_root = MagicMock()
        mock_tk.return_value = mock_root
        
        # Create mock frames for the window
        mock_top_frame = MagicMock()
        mock_mid_frame = MagicMock()
        mock_bottom_frame = MagicMock()
        
        mock_frame.side_effect = [mock_top_frame, mock_mid_frame, mock_bottom_frame]
        
        # Call the function to create the window
        root, top_frame, mid_frame, bottom_frame = create_window(window_title, window_width, window_height, pack_kwargs)
        
        # Assertions to verify the behavior
        mock_tk.assert_called_once()  # Ensure Tk() was called once
        mock_root.title.assert_called_once_with(window_title)  # Check title set
        mock_root.geometry.assert_called_once_with(f'{window_width}x{window_height}')  # Check geometry
        
        # Check if frames were created and packed correctly
        assert top_frame is mock_top_frame  # Check top_frame is created correctly
        assert mid_frame is mock_mid_frame  # Check mid_frame is created correctly
        assert bottom_frame is mock_bottom_frame  # Check bottom_frame is created correctly
        
        # Ensure pack was called with expected arguments for each frame
        for frame in mock_frame.side_effect:
            frame.pack.assert_called_once_with(**pack_kwargs)
        
        # Check if the frames have the correct dimensions
        mock_frame.assert_any_call(mock_root, width=window_width, height=window_height * 0.05)
        mock_frame.assert_any_call(mock_root, width=window_width, height=window_height * 0.72)

def test_create_display_label(mock_calculator):
    """Test the creation of the display label in the calculator."""
    frame = MagicMock()
    display_label_kwargs = {'text': '', 'font': ('Arial', 12)}
    pack_kwargs = {'padx': 5, 'pady': 5}
    
    # Call the function to create the display label
    with patch('tkinter.Label') as mock_label:
        create_display_label(frame, mock_calculator, display_label_kwargs, pack_kwargs)
        
        # Check if the label was created and packed correctly
        mock_label.assert_called_once_with(frame, **display_label_kwargs)
        label_instance = mock_label.return_value
        label_instance.pack.assert_called_once_with(**pack_kwargs)
        
        # Check if the calculator's display_value is set correctly
        label_instance.config.assert_called_once_with(text=mock_calculator.display_value)

def test_create_expression_label(mock_calculator):
    """Test the creation of the expression label in the calculator."""
    frame = MagicMock()
    expression_label_kwargs = {'text': '', 'font': ('Arial', 12)}
    pack_kwargs = {'padx': 5, 'pady': 5}
    
    # Call the function to create the expression label
    with patch('tkinter.Label') as mock_label:
        create_expression_label(frame, mock_calculator, expression_label_kwargs, pack_kwargs)
        
        # Check if the label was created and packed correctly
        mock_label.assert_called_once_with(frame, **expression_label_kwargs)
        label_instance = mock_label.return_value
        label_instance.pack.assert_called_once_with(**pack_kwargs)
        
        # Check if the calculator's current_expression is set correctly
        label_instance.config.assert_called_once_with(text=mock_calculator.current_expression)

@pytest.fixture
def expected_commands(mock_calculator):
    """Fixture to define expected commands for calculator buttons."""
    return {
        'C': mock_calculator.reset_all,
        '±': mock_calculator.toggle_negative,
        '+': partial(mock_calculator.process_operator, '+'),
        '-': partial(mock_calculator.process_operator, '-'),
        '*': partial(mock_calculator.process_operator, '*'),
        '/': partial(mock_calculator.process_operator, '/'),
        '.': mock_calculator.add_decimal,
        '=': mock_calculator.perform_operation,
        '0': partial(mock_calculator.enter_number, '0'),  # Special case for '0'
        '1': partial(mock_calculator.enter_number, '1'),
        '2': partial(mock_calculator.enter_number, '2'),
        '3': partial(mock_calculator.enter_number, '3')
    }

@pytest.fixture
def buttons_creation_args(mock_calculator):
    """Fixture to provide arguments for button creation."""
    button_names = ['C', '±', '+', '1', '2', '3', '=', '0']
    frame = MagicMock(spec=tk.Frame)
    grid_rows = 4
    grid_columns = 4
    buttons_grid_kwargs = {'padx': 5, 'pady': 5}
    return [button_names, frame, mock_calculator, grid_rows, grid_columns, buttons_grid_kwargs]

def test_create_buttons_button_configuration(expected_commands, buttons_creation_args):
    """Test the configuration of buttons created in the calculator."""
    button_names = buttons_creation_args.pop(0)  # Extract button names
    
    for button_name in button_names:
        with patch('tkinter.Button') as mock_button:
            # Call the function to create buttons
            button = create_buttons(button_name, *buttons_creation_args)
            
            # Check if buttons were created and packed correctly
            assert mock_button.call_count == 1  # Check number of buttons created
            assert button[button_name].grid.call_count == 1  # Each button should have grid called once
            assert button[button_name].config.call_args[1]['text'] == button_name  # Compare the name
            
            # Check the command assigned to each button
            actual_command = button[button_name].config.call_args[1]['command']
            expected_command = expected_commands[button_name]
            assert actual_command.func == expected_command.func  # Compare the function
            assert actual_command.args == expected_command.args  # Compare the arguments
            
            if button_name == '0':
                assert button[button_name].config.call_count == 2  # '0' button should have a config call
                assert button[button_name].config.call_args[1]['width'] == 2  # Check width for '0'

def test_create_buttons(buttons_creation_args):
    """Test the creation of buttons in the calculator."""
    button_names = buttons_creation_args[0]
    
    with patch('tkinter.Button') as mock_button_class:
        # Call the function to create buttons
        buttons_dict = create_buttons(*buttons_creation_args)
        
        # Check if buttons were created
        assert mock_button_class.call_count == len(button_names)  # Check number of buttons created
        assert len(buttons_dict) == len(button_names)
        for button_name in button_names:
            button_instance = mock_button_class.return_value  # Get the specific mock for this button
            assert button_name in buttons_dict
            assert buttons_dict[button_name] == button_instance            

if __name__ == '__main__':
    pytest.main()
