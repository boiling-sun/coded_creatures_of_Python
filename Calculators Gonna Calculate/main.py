import windows_and_buttons as gui


def main():
    root, top_frame, bottom_frame = gui.create_window()
    display = gui.create_display_label(top_frame)
    root.mainloop()

if __name__ == '__main__':
    main()
