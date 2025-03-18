import pandas as pd
import os
import openpyxl

print(openpyxl.__version__)

def the_coordinates(name, output_file):
    size_of_wafer = 3
    diameter_of_wafer = size_of_wafer * 2.54 * 10000
    radius_of_wafer = diameter_of_wafer / 2

    # Tile properties
    tile_full_length_x_dir = 2756.294
    tile_full_length_y_dir = 4900
    pos1x_Q1 = tile_full_length_x_dir / 2 + 1250 + 30
    pos1y_Q1 = tile_full_length_y_dir / 2 + 50 + 1250 + 30 + 50
    step_y = tile_full_length_y_dir

    names_and_coordinates_list = []

    for j in range(10):
        previous_position_for_Q_1_4 = pos1x_Q1
        previous_position_for_Q_2_3 = pos1x_Q1
        x_direction_length = 3350

        for i in range(17):
            extra_length = 0
            x_direction_length += tile_full_length_x_dir
            y_direction_length = (j + 1) * tile_full_length_y_dir

            if x_direction_length**2 + y_direction_length**2 < radius_of_wafer**2:
                for Q in [1, 2, 3, 4]:
                    names_and_coordinates_list.append([
                        f"R{j+1}C{i+1}Q{Q}",
                        previous_position_for_Q_1_4 + extra_length / 2 - 15 - 328.147 + 242.3 + 50,
                        pos1y_Q1 + j * step_y - 1830 + 1780 + 50,
                        j + 1,
                        i + 1,
                        Q
                    ])

                previous_position_for_Q_1_4 += tile_full_length_x_dir
                previous_position_for_Q_2_3 += tile_full_length_x_dir

    # Save to Excel
    df = pd.DataFrame(names_and_coordinates_list, columns=["Names", "X Coordinate", "Y Coordinate", "Row", "Column", "Quadrant"])
    df.to_excel(output_file, index=False, engine="openpyxl")
    
    return df

if __name__ == "__main__":
    output_file = os.path.join(os.getcwd(), "Coordinates.xlsx")
    the_coordinates("wafer_data", output_file)
    print(f"Excel file saved to {output_file}")
