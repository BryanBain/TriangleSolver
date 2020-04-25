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
    :param angle1: The smaller of the two angles given
    :param side: The length of the side given
    :param angle2: The larger of the two angles given
    :return Tuple of the missing angle and sides opposite angles 1 and 2.
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
    :param angle1: The smaller of the two angles given
    :param angle2: The larger of the two angles given
    :param side: The length of the side given
    :param aas_choice: 1 if the known side is opposite the smaller angle; 
           2 otherwise
    :return Tuple of the missing angle ad sides opposite angles 1 and 2.
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

def ass(angle, side1, side2):
    """
    Solves an angle-side-side triangle.
    :param angle: The measure of the angle given, in degrees.
    :param side1: The side not opposite the known angle.
    :param side2: The side opposite the known angle.
    :return Tuple of missing side length and angle measures.
    """

    ass_no_triangle = side1 * sin(radians(angle)) / side2
    # TODO fix the 'Not a triangle' case
    if ass_no_triangle > 1:
        msg = "No triangle formed."
        return print(msg)

    angle1_opp_other_side = degrees(asin(ass_no_triangle))
    angle2_opp_other_side = 180 - angle1_opp_other_side

    if angle + angle2_opp_other_side >= 180:
        third_angle = 180 - angle - angle1_opp_other_side
        missing_side = (side2 * sin(radians(third_angle))) / (sin(radians(angle)))
        area = getArea(side1, side2, missing_side)

        return missing_side, angle1_opp_other_side, third_angle, area

    elif angle + angle2_opp_other_side < 180:
        third_angle1 = 180 - angle - angle1_opp_other_side
        missing_side1 = (side2 * sin(radians(third_angle1))) / (sin(radians(angle)))

        third_angle2 = 180 - angle - angle2_opp_other_side
        missing_side2 = (side2 * sin(radians(third_angle2))) / (sin(radians(angle)))

        area1 = getArea(side1, side2, missing_side1)
        area2 = getArea(side1, side2, missing_side2)

        return missing_side1, angle1_opp_other_side, third_angle1, 
        missing_side2, angle2_opp_other_side, third_angle2, area1, area2

    else:
        return "No triangle formed."


def sas(side1, angle, side2):
    """
    Solves a side-angle-side triangle.
    :param side1: The shorter of the two sides given
    :param angle: The angle given, in degrees.
    :param side2: The longer of the two sides given.
    :return Tuple of missing side length and angle measures.
    """

    unknown_side = sqrt(
        side1 ** 2 + side2 ** 2 - 2 * side1 * side2 * cos(radians(angle)))
    smaller_angle = degrees(
        acos((unknown_side ** 2 + side2 ** 2 - side1 ** 2) / (2 * unknown_side * side2)))
    third_angle = 180 - angle - smaller_angle
    area = getArea(side1, side2, unknown_side)

    return unknown_side, smaller_angle, third_angle, area


def sss(side1, side2, side3):
    """
    Solves a side-side-side triangle.
    :param side1: The shortest of the three given sides
    :param side2: The next shortest of the three given sides
    :param side3: The longest of the three given sides
    :return Tuple of the three missing angle measures, in degrees.
    """

    if side1 + side2 <= side3:
        return print("No triangle is formed.")
    smallest_angle = degrees(
        acos((side3 ** 2 + side2 ** 2 - side1 ** 2) / (2 * side3 * side2)))
    largest_angle = degrees(
        acos((side2 ** 2 + side1 ** 2 - side3 ** 2) / (2 * side2 * side1)))
    middle_angle = 180 - smallest_angle - largest_angle
    area = getArea(side1, side2, side3)

    return smallest_angle, middle_angle, largest_angle, area



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
            known_angle = float(input("Please enter the angle measure. "))
            assert known_angle > 0 and known_angle < 180, "Angle must be between 0 and 180 degrees."
            known_side_opp_angle = float(input("Please enter the side opposite the known angle. "))
            assert known_side_opp_angle > 0, "Side length must be positive."
            other_known_side = float(input("Please enter the other of the two known sides. "))
            assert other_known_side > 0, "Side length must be positive."

            ass_no_triangle = other_known_side * sin(radians(known_angle)) / known_side_opp_angle
            angle1_opp_other_side = degrees(asin(ass_no_triangle))
            angle2_opp_other_side = 180 - angle1_opp_other_side


            if known_angle + angle2_opp_other_side >= 180:
                side1 = ass(known_angle, other_known_side, known_side_opp_angle)[0]
                angle_opp_given_side = ass(known_angle, other_known_side, known_side_opp_angle)[1]
                angle3 = ass(known_angle, other_known_side, known_side_opp_angle)[2]
                area_ass1 = ass(known_angle, other_known_side, known_side_opp_angle)[3]
                print()
                print("One triangle formed.")
                print("The length of the missing side is {:.2f}".format(side1))
                print("The measure of the angle across from the side length of {0:.2f} is {1:.2f} degrees".format(other_known_side, angle_opp_given_side))
                print("The measure of the angle across from the side length of {0:.2f} is {1:.2f} degrees.".format(side1, angle3))
                print("The area of the triangle is about {0:.2f} square units.".format(area_ass1))
                print()

            else:
                side1a = ass(known_angle, other_known_side, known_side_opp_angle)[0]
                angle_opp_given_side1 = ass(known_angle, other_known_side, known_side_opp_angle)[1]
                angle3a = ass(known_angle, other_known_side, known_side_opp_angle)[2]
                side1b = ass(known_angle, other_known_side, known_side_opp_angle)[3]
                angle_opp_given_side2 = ass(known_angle, other_known_side, known_side_opp_angle)[4]
                angle3b = ass(known_angle, other_known_side, known_side_opp_angle)[5]

                area_ass1a = ass(known_angle, other_known_side, known_side_opp_angle)[6]
                area_ass1b = ass(known_angle, other_known_side, known_side_opp_angle)[7]
                print()
                print("Two triangles formed.")
                print("Case 1:")
                print("The length of the missing side is {:.2f}".format(side1a))
                print("The measure of the angle across from the side length of {0:.2f} is {1:.2f} degrees".format(other_known_side, angle_opp_given_side1))
                print("The measure of the angle across from the side length of {0:.2f} is {1:.2f} degrees.".format(side1a, angle3a))
                print("The area of the first triangle is about {0:.2f} square units.".format(area_ass1a))
                print("Case 2:")
                print("The length of the missing side is {:.2f}".format(side1b))
                print("The measure of the angle across from the side length of {0:.2f} is {1:.2f} degrees".format(other_known_side, angle_opp_given_side2))
                print("The measure of the angle across from the side length of {0:.2f} is {1:.2f} degrees.".format(side1b, angle3b))
                print("The area of the second triangle is about {0:.2f} square units".format(area_ass1b))
                print()

        # SAS Case
        elif choice == "4":
            known_angle = float(input("Please enter the angle measure. "))
            assert known_angle > 0 and known_angle < 180, "Angle must be between 0 and 180 degrees."
            shorter_side = float(input("Please enter the shorter side length. "))
            assert shorter_side > 0, "Side length must be positive."
            longer_side = float(input("Please enter the longer side length. "))
            assert longer_side > 0, "Side length must be positive."

            side3 = sas(shorter_side, known_angle, longer_side)[0]
            smaller_angle = sas(shorter_side, known_angle, longer_side)[1]
            larger_angle = sas(shorter_side, known_angle, longer_side)[2]
            area_sas = sas(shorter_side, known_angle, longer_side)[3]
            print()
            print("The side opposite the {0:.2f} degree angle measures {1:.2f}".format(known_angle, side3))
            print("The angle opposite the side length of {0:.2f} is {1:.2f}".format(shorter_side, smaller_angle))
            print("The angle opposite the side length of {0:.2f} is {1:.2f}".format(longer_side, larger_angle))
            print("The area of the triangle is about {0:.2f} square units.".format(area_sas))
            print()

        # SSS Case
        elif choice == "5":
            shortest_side = float(input("Please enter the length of the shortest side. "))
            assert shortest_side > 0, "Side length must be positive."
            middle_side = float(input("Please enter the length of the next shortest side. "))
            assert middle_side > 0, "Side length must be positive."
            longest_side = float(input("Please enter the length of the longest side. "))
            assert longest_side > 0, "Side length must be positive."

            # if shortest_side + middle_side <= longest_side:
            #     print("No triangle formed.")

            small_angle = sss(shortest_side, middle_side, longest_side)[0]
            med_angle = sss(shortest_side, middle_side, longest_side)[1]
            large_angle = sss(shortest_side, middle_side, longest_side)[2]
            area_sss = sss(shortest_side, middle_side, longest_side)[3]
            print()
            print("The measure of the angle opposite the side length of {0:.2f} is {1:.2f}".format(shortest_side, small_angle))
            print("The measure of the angle opposite the side length of {0:.2f} is {1:.2f}".format(middle_side, med_angle))
            print("The measure of the angle opposite the side length of {0:.2f} is {1:.2f}".format(longest_side, large_angle))
            print("The area of the triangle is about {0:.2f} square units.".format(area_sss))
            print()

        elif choice == 'q':
            quit = True

if __name__ == "__main__":
    main()