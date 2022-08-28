from cProfile import label
import easygui as gui


# gui.msgbox(msg="Hello!", title="My first message box", ok_button="Click me")
# color = gui.buttonbox(
#     msg="What's your favorite color?",
#     title="Choose wisely...",
#     choices=("Red", "Yellow", "Blue")
# )
# print(color)
# colors = ("Red", "Yellow", "Blue")
# index = gui.indexbox(
#     msg="What's your favorite color?",
#     title="Choose wisely...",
#     choices=colors,
# )
# print(index)
# fruite = gui.enterbox(
#     msg="What is your favorite fruite?",
#     title="Favorite fruite",
# )

# print(fruite)
file_path = gui.fileopenbox(title="Select a file")
print(file_path)
