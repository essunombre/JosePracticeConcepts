import math
import datetime

width = float(input('Enter the width of the tire in mm (ex 205): '))
ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))
volume = math.pi * (pow(width,2)) * ratio * ((width * ratio) + (2540 * diameter))/ 10000000000
# volume = pow(width, 2)
print(f'The approximate volume is {volume:.2f} liters')

today = datetime.datetime.now()

with open('w1/volumes.txt', 'at') as volume_file:
    print(f'----------------------', file=volume_file)
    print(f'Date: {today:%m-%d-%Y}', file=volume_file)
    print(f'Width: {width}', file=volume_file)
    print(f'Aspect Ratio: {ratio}', file=volume_file)
    print(f'Diameter: {diameter}', file=volume_file)
    print(f'----------------------', file=volume_file)