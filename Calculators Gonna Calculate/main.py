import windows_and_buttons as gui

def main():
    root, top_frame, mid_frame, bottom_frame = gui.create_window()
    gui.create_display_label(top_frame)
    gui.create_buttons(bottom_frame)
    root.mainloop()

if __name__ == '__main__':
    main()
