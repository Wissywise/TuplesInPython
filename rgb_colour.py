
colors = (
    ("Red", (255, 0, 0)),
    ("Green", (0, 255, 0)),
    ("Blue", (0, 0, 255)),
    ("Yellow", (255, 255, 0)),
    ("Cyan", (0, 255, 255)),
    ("Magenta", (255, 0, 255)),
    ("White", (255, 255, 255)),
    ("Black", (0, 0, 0))
)

print("Available Colors:")
for color in colors:
    print(color[0])

choice = input("\nEnter a color name to get its RGB value: ").strip().title()

for name, rgb in colors:
    if name == choice:
        print(f"RGB value of {name} is {rgb}")
        break
else:
    print("Color not found! Please choose from the list.")