#!/usr/bin/env python3
from math import *


class StrainWaveGear():

    def __init__(self) -> None:
        pass


class Cycloidal():

    def __init__(self, ratio=25, module=2.0, mod_coeff=0.4, housing_pin_radius_coeff=1.0, output_pin_number=4, output_pin_diameter=3):
        self.ratio = ratio  # i
        self.module = module  # m
        self.mod_coeff = mod_coeff  # x
        self.housing_pin_radius_coeff = housing_pin_radius_coeff  # rc_star
        self.output_pin_number = output_pin_number
        self.output_pin_diameter = output_pin_diameter  # dp

        # Cycloidal Disc
        self.teeth_number = self.ratio  # z1
        self.eccentricity = (self.module / 2) * (1 - self.mod_coeff)  # e0
        self.disc_pitch_diameter = self.module * self.teeth_number  # d1
        self.disc_dedendum_diameter = self.module * \
            (self.teeth_number + self.mod_coeff -
             2 * self.housing_pin_radius_coeff)  # df1
        self.disc_addendum_diameter = self.module * \
            (self.teeth_number + 2 - self.mod_coeff -
             2 * self.housing_pin_radius_coeff)  # da1

        # Housing
        self.housing_pin_number = self.teeth_number + 1  # z2
        self.housing_pin_diameter = 2 * self.housing_pin_radius_coeff * self.module  # dc
        self.housing_pitch_diameter = self.module * self.housing_pin_number  # d2
        self.housing_dedendum_diameter_min = (
            self.disc_addendum_diameter / 2 + self.eccentricity) * 2  # df2min
        self.housing_dedendum_diameter_max = self.housing_pitch_diameter - \
            0.15 * (self.housing_pin_diameter / 2)  # df2max
        self.housing_addendum_diameter = self.module * \
            (self.housing_pin_number - 2 * self.housing_pin_radius_coeff)  # da2

        # Output
        self.output_hole_diameter = self.output_pin_diameter + 2 * self.eccentricity  # dw

    def profile_equation(self, phi):
        x = self.module / 2 * ((self.teeth_number + 1) * sin(phi) -
                               (1 - self.mod_coeff) * sin((self.teeth_number + 1) * phi) +
                               (2 * self.housing_pin_radius_coeff * ((1 - self.mod_coeff) * sin((self.teeth_number + 1) * phi) - sin(phi))) /
                               (sqrt(1 - 2 * (1 - self.mod_coeff) * cos(phi * self.teeth_number) + (1 - self.mod_coeff) ** 2)))

        y = self.module / 2 * ((self.teeth_number + 1) * cos(phi) -
                               (1 - self.mod_coeff) * cos((self.teeth_number + 1) * phi) +
                               (2 * self.housing_pin_radius_coeff * ((1 - self.mod_coeff) * cos((self.teeth_number + 1) * phi) - cos(phi))) /
                               (sqrt(1 - 2 * (1 - self.mod_coeff) * cos(phi * self.teeth_number) + (1 - self.mod_coeff) ** 2)))

        return x, y

    def profile_generation(self, resolution):
        csv = []
        for i in range(resolution + 1):
            degree = i * (360 / resolution)
            csv.append([self.profile_equation(radians(degree))[0] /
                       10, self.profile_equation(radians(degree))[1] / 10])

        return csv

    def print_design_parameters(self):
        print("CYCLOIDAL SPEED REDUCER PARAMETERS\n")
        print("Ratio(i):", self.ratio)
        print("\n")
        print("CYCLOIDAL DISC")
        print("Module(m):", self.module)
        print("Modification Coefficient(x):", self.mod_coeff)
        print("Teeth Number(z1):", self.teeth_number)
        print("Eccentricity(e0):", self.eccentricity)
        print("Disc Pitch Diameter(d1):", self.disc_pitch_diameter)
        print("Output Hole Diameter(dw):", self.output_hole_diameter)
        print("\n")
        print("HOUSING")
        print("Housing Pin Radius Coefficient(rc*):",
              self.housing_pin_radius_coeff)
        print("Housing Pin Number(z2):", self.housing_pin_number)
        print("Housing Pin Diameter(dc):", self.housing_pin_diameter)
        print("Housing Pitch Diameter(d2):", self.housing_pitch_diameter)
        print("Min Housing Dedendum Diameter(df2min):",
              self.housing_dedendum_diameter_min)
        print("Max Housing Dedendum Diameter(df2max):",
              self.housing_dedendum_diameter_max)
        print("\n")
        print("OUTPUT")
        print("Output Pin Number:", self.output_pin_number)
        print("Output Pin Diameter(dp):", self.output_pin_diameter)
        print("\n")

    def save_profile_csv(self):
        f = open("profiles/cycloid_profile.csv", "w")
        for i in self.profile_generation(720):
            f.write(str(i[0]) + ", " + str(i[1]) + ", 0" + "\n")
        f.close()
