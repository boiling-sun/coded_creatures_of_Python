import windows_and_buttons as gui
import configs


def main():
    root, top_frame, mid_frame, bottom_frame = gui.create_window()
    gui.create_display_label(top_frame)
    gui.create_buttons(bottom_frame, 
                       configs.GRID_ROWS, 
                       configs.GRID_COLUMNS, 
                       configs.BUTTONS_GRID_KWARGS)
    root.mainloop()

if __name__ == '__main__':
    main()
