from math import pi, sin, cos, sqrt, radians


class TrochoidalRackPinion:

    def __init__(self,
                 module=11,
                 roller_pin_number=10,
                 roller_pin_diameter_coefficient=1.45455,
                 rack_tooth_profile_offset_coefficient=0.45455,
                 rack_addendum_coefficient=1.45455):

        self.module = module  # [mm]
        self.roller_pin_number = roller_pin_number
        self.roller_pin_diameter_coefficient = roller_pin_diameter_coefficient
        self.rack_tooth_profile_offset_coefficient = rack_tooth_profile_offset_coefficient
        self.rack_addendum_coefficient = rack_addendum_coefficient

        self.pinion_reference_radius = (module * roller_pin_number) / 2  # [mm]
        self.pinion_pitch_radius = (module * roller_pin_number) / \
            2 + module * rack_tooth_profile_offset_coefficient  # [mm]
        self.roller_pin_diameter = module * \
            roller_pin_diameter_coefficient  # [mm]
        self.rack_pitch = pi * module * \
            (1 + 2 * rack_tooth_profile_offset_coefficient /
             roller_pin_number)  # [mm]
        self.rack_tooth_profile_offset_distance = module * \
            rack_tooth_profile_offset_coefficient  # [mm]
        self.rack_addendum = module * rack_addendum_coefficient  # [mm]

    def profile_equation(self, phi):
        x = ((self.module * self.roller_pin_number) / 2 + self.module * self.rack_tooth_profile_offset_coefficient) * phi - \
            (self.module * self.roller_pin_number) / 2 * sin(phi) + \
            ((self.module * self.roller_pin_number * self.roller_pin_diameter_coefficient * sin(phi)) / 4) / \
            sqrt((self.roller_pin_number / 2 + self.rack_tooth_profile_offset_coefficient) ** 2 -
                 (self.roller_pin_number / 2 + self.rack_tooth_profile_offset_coefficient) * self.roller_pin_number *
                 cos(phi) + (self.roller_pin_number / 2) ** 2)

        y = (self.module * self.roller_pin_number) / 2 + self.module * self.rack_tooth_profile_offset_coefficient - \
            (self.module * self.roller_pin_number) / 2 * cos(phi) - ((self.module * self.roller_pin_diameter_coefficient) / 2 * (self.roller_pin_number / 2 + self.rack_tooth_profile_offset_coefficient - self.roller_pin_number / 2 * cos(phi))) / \
            sqrt((self.roller_pin_number / 2 + self.rack_tooth_profile_offset_coefficient) ** 2 - (self.roller_pin_number / 2 +
                 self.rack_tooth_profile_offset_coefficient) * self.roller_pin_number * cos(phi) + (self.roller_pin_number / 2) ** 2)

        return x, y

    def profile_generation(self, resolution):
        csv = []
        for i in range(resolution + 1):
            degree = i * (360 / resolution)
            csv.append([self.profile_equation(radians(degree))[0] /
                       10, self.profile_equation(radians(degree))[1] / 10])

        return csv

    def export_profile_to_csv(self):
        f = open("profiles/trochoidal_rack.csv", "w")
        for i in self.profile_generation(720):
            f.write(str(i[0]) + ", " + str(i[1]) + ", 0" + "\n")
        f.close()

    def print_design_parameters(self):
        print("\n\n\n")
        print("TROCHOIDAL PINION-RACK PAIR DESIGN PARAMETERS\n")
        print("Module:", self.module, "[mm]")
        print("\n\n\n")
