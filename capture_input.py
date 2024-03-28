import csv
import keyboard


def on_press(key):
    # write the data in a csv file named 'record.csv'
    with open('record.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if key.name == 'up':
            writer.writerow(['up'])
        elif key.name == 'down':
            writer.writerow(['down'])
        elif key.name == 'right':
            writer.writerow(['right'])
        elif key.name == 'left':
            writer.writerow(['left'])
        elif key.name == 'enter':
            writer.writerow(['start'])
        elif key.name == 'backspace':
            writer.writerow(['select'])
        elif key.name == 'a':
            writer.writerow(['Y'])
        elif key.name == 'z':
            writer.writerow(['B'])
        elif key.name == 's':
            writer.writerow(['X'])
        elif key.name == 'x':
            writer.writerow(['A'])
        elif key.name == 'w':
            writer.writerow(['L'])
        elif key.name == 'e':
            writer.writerow(['R'])


# listen to all keyboard events
keyboard.on_press(on_press)

# keep the script running
keyboard.wait()
