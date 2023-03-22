from speed_reducers import Cycloidal, StrainWaveGear


if __name__ == '__main__':
    x = Cycloidal()
    x.print_design_parameters()
    x.save_profile_csv()
