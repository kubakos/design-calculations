from speed_reducers import Cycloidal


def main():
    ratio = 25
    module = 2.0
    mod_coeff = 0.4
    housing_pin_radius_coeff = 1.0
    output_pin_number = 4
    output_pin_diameter = 3

    x = Cycloidal(ratio, module, mod_coeff, housing_pin_radius_coeff,
                  output_pin_number, output_pin_diameter)
    x.print_design_parameters()
    x.save_profile_csv()


if __name__ == '__main__':
    main()
