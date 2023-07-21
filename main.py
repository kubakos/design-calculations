#!/usr/bin/env python3
from generators.gear_pairs import TrochoidalRackPinion


def main():
    # ratio = 25
    # module = 2.0
    # mod_coeff = 0.4
    # housing_pin_radius_coeff = 1.0
    # output_pin_number = 4
    # output_pin_diameter = 3

    # x = Cycloidal(ratio, module, mod_coeff, housing_pin_radius_coeff,
    #               output_pin_number, output_pin_diameter)
    # x.print_design_parameters()
    # x.export_profile_to_csv()

    y = TrochoidalRackPinion()
    y.print_design_parameters()
    y.export_profile_to_csv()


if __name__ == '__main__':
    main()
