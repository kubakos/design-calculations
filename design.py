#!/usr/bin/env python3
from math import *


RATIO = 40  # i
MODULE = 1  # m
MODIFICATION_COEFF = 0.4  # x
HOUSING_PIN_RADIUS_COEFF = 1  # rc_star
OUTPUT_PIN_NUMBER = 3
OUTPUT_PIN_DIAMETER = 2  # dp


# CYCLOIDAL DISC
teeth_number = RATIO  # z1
eccentricity = (MODULE / 2) * (1 - MODIFICATION_COEFF)  # e0
disc_pitch_diameter = MODULE * teeth_number  # d1
disc_dedendum_diameter = MODULE * \
    (teeth_number + MODIFICATION_COEFF - 2 * HOUSING_PIN_RADIUS_COEFF)  # df1
disc_addendum_diameter = MODULE * \
    (teeth_number + 2 - MODIFICATION_COEFF - 2 * HOUSING_PIN_RADIUS_COEFF)  # da1

# HOUSING
housing_pin_number = teeth_number + 1  # z2
housing_pin_diameter = 2 * HOUSING_PIN_RADIUS_COEFF * MODULE  # dc
housing_pitch_diameter = MODULE * housing_pin_number  # d2
housing_dedendum_diameter_min = (
    disc_addendum_diameter / 2 + eccentricity) * 2  # df2min
housing_dedendum_diameter_max = housing_pitch_diameter - \
    0.15 * (housing_pin_diameter / 2)  # df2max
housing_addendum_diameter = MODULE * \
    (housing_pin_number - 2 * HOUSING_PIN_RADIUS_COEFF)  # da2

# OUTPUT
output_hole_diameter = OUTPUT_PIN_DIAMETER + 2 * eccentricity  # dw


def profile_equation(phi):
    x = MODULE / 2 * ((teeth_number + 1) * sin(phi) -
                      (1 - MODIFICATION_COEFF) * sin((teeth_number + 1) * phi) +
                      (2 * HOUSING_PIN_RADIUS_COEFF * ((1 - MODIFICATION_COEFF) * sin((teeth_number + 1) * phi) - sin(phi))) /
                      (sqrt(1 - 2 * (1 - MODIFICATION_COEFF) * cos(phi * teeth_number) + (1 - MODIFICATION_COEFF) ** 2)))

    y = MODULE / 2 * ((teeth_number + 1) * cos(phi) -
                      (1 - MODIFICATION_COEFF) * cos((teeth_number + 1) * phi) +
                      (2 * HOUSING_PIN_RADIUS_COEFF * ((1 - MODIFICATION_COEFF) * cos((teeth_number + 1) * phi) - cos(phi))) /
                      (sqrt(1 - 2 * (1 - MODIFICATION_COEFF) * cos(phi * teeth_number) + (1 - MODIFICATION_COEFF) ** 2)))

    return x, y


def profile_generation(resolution):
    csv = []
    for i in range(resolution + 1):
        degree = i * (360 / resolution)
        csv.append([round(profile_equation(radians(degree))[0] / 10, 3), round(
            profile_equation(radians(degree))[1] / 10, 3)])

    return csv


def print_design_parameters():
    print("CYCLOIDAL SPEED REDUCER PARAMETERS\n")
    print("Ratio(i):", RATIO)
    print("\n")
    print("CYCLOIDAL DISC")
    print("Module(m):", MODULE)
    print("Modification Coefficient(x):", MODIFICATION_COEFF)
    print("Teeth Number(z1):", teeth_number)
    print("Eccentricity(e0):", eccentricity)
    print("Disc Pitch Diameter(d1):", disc_pitch_diameter)
    print("Output Hole Diameter(dw):", output_hole_diameter)
    print("\n")
    print("HOUSING")
    print("Housing Pin Radius Coefficient(rc*):", HOUSING_PIN_RADIUS_COEFF)
    print("Housing Pin Number(z2):", housing_pin_number)
    print("Housing Pin Diameter(dc):", housing_pin_diameter)
    print("Housing Pitch Diameter(d2):", housing_pitch_diameter)
    print("Min, Max Housing Dedendum Diameter(df2min, df2max):",
          housing_dedendum_diameter_min, housing_dedendum_diameter_max)
    print("\n")
    print("OUTPUT")
    print("Output Pin Number:", OUTPUT_PIN_NUMBER)
    print("Output Pin Diameter(dp):", OUTPUT_PIN_DIAMETER)
    print("\n")


if __name__ == "__main__":
    print_design_parameters()

    f = open("cycloid_profile.csv", "w")
    for i in profile_generation(720):
        f.write(str(i[0]) + ", " + str(i[1]) + ", 0" + "\n")
    f.close()
