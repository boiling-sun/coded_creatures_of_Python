import windows_and_buttons as gui
import configs
from operations import Calculator



def main():
    calculator = Calculator()
    root, top_frame, mid_frame, bottom_frame = gui.create_window(configs.PACK_KWARGS)
    gui.create_display_label(top_frame, 
                             calculator, 
                             configs.DISPLAY_LABEL_KWARGS, 
                             configs.PACK_KWARGS)
    gui.create_buttons(bottom_frame, 
                       calculator,
                       configs.GRID_ROWS, 
                       configs.GRID_COLUMNS, 
                       configs.BUTTONS_GRID_KWARGS)
    root.mainloop()

if __name__ == '__main__':
    main()
