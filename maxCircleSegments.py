
import math


def largestSegment(radius, segments):
    flag = False

    circle_areas = []
    for r in radius:
        circle_areas.append(math.pi * r * r)

    i = 0
    j = max(circle_areas)
    while i + 1e-5 <= j:
        x = (i + j) / 2
        pieces = 0
        for area in circle_areas:
            pieces += area // x
            if pieces >= segments:
                i = x
                flag = True
                break

        if not flag:
            j = x
        flag = False
    return round(x, 4)


# Example 1.
radii = [1, 1, 1, 2, 2, 3]
numberOfGuests = 6
print(largestSegment(radii, numberOfGuests))
# Output: 7.0686

# Example 2.
radii = [4, 3, 3]
numberOfGuests = 3
print(largestSegment(radii, numberOfGuests))
# Output: 28.2743

# Example 3.
radii = [6, 7]
numberOfGuests = 12
print(largestSegment(radii, numberOfGuests))
# Output: 21.9911