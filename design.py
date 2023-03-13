from math import *


PIN_RADIUS_COEFF = 0


RATIO = 29              # i
MODULE = 3.5            # m
MODIFICATION_COEFF = 0  # x


teeth_number = RATIO


def profile_equation(phi):
    x = MODULE / 2 * ((teeth_number + 1) * sin(phi) -
                      (1 - MODIFICATION_COEFF) * sin((teeth_number + 1) * phi) +
                      (2 * PIN_RADIUS_COEFF * ((1 - MODIFICATION_COEFF) * sin((teeth_number + 1) * phi) - sin(phi))) /
                      (sqrt(1 - 2 * (1 - MODIFICATION_COEFF) * cos(phi * teeth_number) + (1 - MODIFICATION_COEFF) ** 2)))

    y = MODULE / 2 * ((teeth_number + 1) * cos(phi) -
                      (1 - MODIFICATION_COEFF) * cos((teeth_number + 1) * phi) +
                      (2 * PIN_RADIUS_COEFF * ((1 - MODIFICATION_COEFF) * cos((teeth_number + 1) * phi) - cos(phi))) /
                      (sqrt(1 - 2 * (1 - MODIFICATION_COEFF) * cos(phi * teeth_number) + (1 - MODIFICATION_COEFF) ** 2)))

    return x, y


def profile_generation(resolution):
    increment = 360 / resolution
    x = []
    y = []
    csv = []

    for i in range(resolution):
        degree = i * increment
        t = radians(degree)

        x.append(profile_equation(t)[0])
        y.append(profile_equation(t)[1])
        csv.append([round(x[i], 3), round(y[i], 3)])

    return x, y, csv


def print_design_parameters():
    print("CYCLOIDAL SPEED REDUCER PARAMETERS:")
    print()


if __name__ == "__main__":
    print_design_parameters()

    f = open("cycloid_profile.csv", "a")
    for i in profile_generation(300)[2]:
        f.write(str(i[0]) + ", " + str(i[1]) + ", 0" + "\n")
    f.close()
