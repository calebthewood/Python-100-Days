from math import ceil

coverage = 5
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

def paint_calc(height, width, cover):
    """Calculates num of paint cans needed for a job. Rounds up."""
    cans_needed = ceil((height * width) / cover)
    print (f"You\'ll need {cans_needed} cans of paint.")

paint_calc(height=test_h, width=test_w, cover=coverage)