"""
Name: Triangle_Solver.py
Author: Bryan Bain
Date: May 16, 2019
Purpose: Solves ASA, AAS, ASS, SAS, and SSS Triangles
"""

from math import sin, cos, radians, sqrt, degrees, acos, asin

def getArea(side1, side2, side3):
    """
    Uses Heron's formula to calculate the area of the triangle.
    :param side1: Any of the three sides of the triangle.
    :param side2: Any of the remaining two sides of the triangle.
    :param side3: The last side of the triangle.
    :return: The area of the triangle.
    """
    s = 0.5*(side1 + side2 + side3)     # Calculate the semi-perimeter, s
    area = sqrt(s*(s - side1)*(s - side2)*(s - side3))
    return area

def asa():
    """
    Solves an angle-side-angle triangle
    """
    
    small_angle = float(input("Please enter the smaller angle measure. "))
    assert small_angle > 0 and small_angle < 180, "Angle must be between 0 and 180 degrees."
    large_angle = float(input("Please enter the larger angle measure. "))
    assert large_angle > 0 and large_angle < 180, "Angle must be between 0 and 180 degrees."
    assert small_angle + large_angle < 180, "There are too many degrees for the given angle measures."
    known_side = float(input("Please enter the length of the side you are given. "))
    assert known_side > 0, "Side length must be positive."

    missing_angle = 180 - small_angle - large_angle
    side1 = (known_side * sin(radians(small_angle))) / sin(radians(missing_angle))
    side2 = (known_side * sin(radians(large_angle))) / sin(radians(missing_angle))
    area = getArea(known_side, side1, side2)

    print()
    print(f"The unknown angle is {missing_angle:.2f} degrees.")
    print(f"The side opposite the {large_angle:.2f} degree angle is {side2:.2f}.")
    print(f"The side opposite the {small_angle:.2f} degree angle is {side1:.2f}.")
    print(f"The area of the triangle is {area:.2f} square units.")
    print()  

def aas():
    """
    Solves an angle-angle-side triangle.
    """
    
    small_angle = float(input("Please enter the smaller angle measure. "))
    assert small_angle > 0 and small_angle < 180, "Angle must be between 0 and 180 degrees."
    large_angle = float(input("Please enter the larger angle measure. "))
    assert large_angle > 0 and large_angle < 180, "Angle must be between 0 and 180 degrees."
    assert small_angle + large_angle < 180, "There are too many degrees for the given angle measures."
    third_angle = 180 - small_angle - large_angle
    known_side = float(input("Please enter the length of the side you are given. "))
    assert known_side > 0, "Side length must be positive."
    print("1. The smaller angle.")
    print("2. The larger angle.\n")
    aas_choice = input("Which side is the known angle across from? Pick either if the angles are equal. ")
    
    if aas_choice == "1":
        side1 = (known_side * sin(radians(large_angle))) / sin(radians(small_angle))
        side2 = (known_side * sin(radians(third_angle))) / sin(radians(small_angle))
        area = getArea(known_side, side1, side2)
        print(f"The unknown angle is {third_angle:.2f} degrees.")
        print()
        print(f"The side opposite the {large_angle:.2f} degree angle measures {side1:.2f}")
        print(f"The side opposite the {third_angle:.2f} degree angles measures {side2:.2f}")
        print(f"The area of the triangle is {area:.2f}")
        print()
    
    else:
        side1 = (known_side * sin(radians(small_angle))) / sin(radians(large_angle))
        side2 = (known_side * sin(radians(third_angle))) / sin(radians(large_angle))
        area = getArea(known_side, side1, side2)
        print(f"The third angle is {third_angle:.2f} degrees.")
        print()
        print(f"The side opposite the {small_angle:.2f} degree angle is about {side1:.2f}")
        print(f"The side opposite the {third_angle:.2f} degree angle is about {side2:.2f}")
        print(f"The area of the triangle is {area:.2f}")
        print()

def ass():
    """
    Solves an angle-side-side triangle.
    """
    
    known_angle = float(input("Please enter the angle measure in degrees. "))
    assert known_angle > 0 and known_angle < 180, "Angle must be between 0 and 180 degrees."
    known_side_opp_angle = float(input("Please enter the side opposite the known angle. "))
    assert known_side_opp_angle > 0, "Side length must be positive."
    other_known_side = float(input("Please enter the other of the two known sides. "))
    assert other_known_side > 0, "Side length must be positive."

    ass_no_triangle = other_known_side * sin(radians(known_angle)) / known_side_opp_angle
    
    if ass_no_triangle > 1:
        print("\nNo triangle formed.\n")
        return 
    
    angle1_opp_other_side = degrees(asin(ass_no_triangle))
    angle2_opp_other_side = 180 - angle1_opp_other_side

    if known_angle + angle2_opp_other_side >= 180:
        third_angle = 180 - known_angle - angle1_opp_other_side
        missing_side = (known_side_opp_angle * sin(radians(third_angle))) / (sin(radians(known_angle)))
        area = getArea(known_side_opp_angle, other_known_side, missing_side)
        print()
        print("One triangle formed.\n\n")
        print(f"The length of the missing side is {missing_side:.2f}")
        print(f"The measure of the angle across from the side length of {other_known_side:.2f} is {angle1_opp_other_side:.2f} degrees")
        print(f"The measure of the angle across from the side length of {missing_side:.2f} is {third_angle:.2f} degrees.")
        print(f"The area of the triangle is about {area:.2f} square units.")
        print()

    else:
        # using angle1_opp_other_side
        third_angle1 = 180 - known_angle - angle1_opp_other_side
        missing_side1 = (known_side_opp_angle * sin(radians(third_angle1))) / (sin(radians(known_angle)))
        
        # using angle2_opp_other_side
        third_angle2 = 180 - known_angle - angle2_opp_other_side
        missing_side2 = (known_side_opp_angle * sin(radians(third_angle2))) / (sin(radians(known_angle)))
        
        area1 = getArea(known_side_opp_angle, other_known_side, missing_side1)
        area2 = getArea(known_side_opp_angle, other_known_side, missing_side2)

        print("\nTwo triangles formed.")
        print("Case 1:")
        print(f"The length of the missing side is {missing_side1:.2f}")
        print(f"The measure of the angle across from the side length of {other_known_side:.2f} is {angle1_opp_other_side:.2f} degrees")
        print(f"The measure of the angle across from the side length of {missing_side1:.2f} is {third_angle1:.2f} degrees.")
        print(f"The area of the first triangle is about {area1:.2f} square units.\n")
        print("Case 2:")
        print(f"The length of the missing side is {missing_side2:.2f}")
        print(f"The measure of the angle across from the side length of {other_known_side:.2f} is {angle2_opp_other_side:.2f} degrees")
        print(f"The measure of the angle across from the side length of {missing_side2:.2f} is {third_angle2:.2f} degrees.")
        print(f"The area of the second triangle is about {area2:.2f} square units\n")

def sas():
    """
    Solves a side-angle-side triangle.
    """
    
    known_angle = float(input("Please enter the angle measure in degrees. "))
    assert known_angle > 0 and known_angle < 180, "Angle must be between 0 and 180 degrees."
    shorter_side = float(input("Please enter the shorter side length. "))
    assert shorter_side > 0, "Side length must be positive."
    longer_side = float(input("Please enter the longer side length. "))
    assert longer_side > 0, "Side length must be positive."
    
    unknown_side = sqrt(
        shorter_side ** 2 + longer_side ** 2 - 2 * shorter_side * longer_side * cos(radians(known_angle)))
    smaller_angle = degrees(
        acos((unknown_side ** 2 + longer_side ** 2 - shorter_side ** 2) / (2 * unknown_side * longer_side)))
    third_angle = 180 - known_angle - smaller_angle
    area = getArea(shorter_side, longer_side, unknown_side)

    print()
    print(f"The side opposite the {known_angle:.2f} degree angle measures {unknown_side:.2f}")
    print(f"The angle opposite the side length of {shorter_side:.2f} is {smaller_angle:.2f}")
    print(f"The angle opposite the side length of {longer_side:.2f} is {third_angle:.2f}")
    print(f"The area of the triangle is about {area:.2f} square units.")
    print()

def sss():
    """
    Solves a side-side-side triangle.
    """
    
    shortest_side = float(input("Please enter the length of the shortest side. "))
    assert shortest_side > 0, "Side length must be positive."
    middle_side = float(input("Please enter the length of the next shortest side. "))
    assert middle_side > 0, "Side length must be positive."
    longest_side = float(input("Please enter the length of the longest side. "))
    assert longest_side > 0, "Side length must be positive."

    if shortest_side + middle_side <= longest_side:
        print("\nNo triangle formed.\n")
        return
    
    smallest_angle = degrees(
        acos((longest_side ** 2 + middle_side ** 2 - shortest_side ** 2) / (2 * longest_side * middle_side)))
    largest_angle = degrees(
        acos((middle_side ** 2 + shortest_side ** 2 - longest_side ** 2) / (2 * middle_side * shortest_side)))
    middle_angle = 180 - smallest_angle - largest_angle
    area = getArea(shortest_side, middle_side, longest_side)
    
    print()
    print(f"The measure of the angle opposite the side length of {shortest_side:.2f} is {smallest_angle:.2f}")
    print(f"The measure of the angle opposite the side length of {middle_side:.2f} is {middle_angle:.2f}")
    print(f"The measure of the angle opposite the side length of {longest_side:.2f} is {largest_angle:.2f}")
    print(f"The area of the triangle is about {area:.2f} square units.")
    print()



def main():
    quit = False
    while not quit:
        print("1. ASA")
        print("2. AAS")
        print("3. ASS")
        print("4. SAS")
        print("5. SSS")
        choice = input("Please enter the type of triangle you want to solve. Press 'q' to quit. ")

        # ASA Case
        if choice == "1":
            asa()

        # AAS Case
        elif choice == "2":
            aas()

        # ASS Case
        elif choice == "3":
            ass()

        # SAS Case
        elif choice == "4":
            sas()
            
        # SSS Case
        elif choice == "5":
            sss()

        elif choice == 'q':
            quit = True

if __name__ == "__main__":
    main()