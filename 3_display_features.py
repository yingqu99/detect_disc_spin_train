import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Paths
data_folder = "/home/subblue-3/nextGen/data/attitude_estimation_in_lab_20250820/"
output_figure_folder = "/home/subblue-3/nextGen/data/attitude_estimation_in_lab_20250820/3_geo_feature/"
output_data_folder = "/home/subblue-3/nextGen/data/attitude_estimation_in_lab_20250820/"


# Read excel file
df_raw_data = pd.read_excel(os.path.join(data_folder, "2_processed_raw__geo_feature__touch_line.xlsx"))
# print(df_raw_data)


# Sort by roll_true
df_sort_roll = df_raw_data.sort_values('roll_true').reset_index(drop=True)
df_sort_roll.to_excel(os.path.join(data_folder, "3_sort_roll_true.xlsx"), index=False)


# Sort by roll_true
df_sort_pitch = df_raw_data.sort_values('pitch_true').reset_index(drop=True)
df_sort_pitch.to_excel(os.path.join(output_data_folder, "3_sort_pitch_true.xlsx"), index=False)

#====================== display roll & pitch =====================#


# display roll + pitch
plt.figure(figsize=(15, 8))
plt.plot(df_sort_roll.index, df_sort_roll['roll_true'], 'o-', color = 'red', label='roll true', linewidth=2, markersize=6)
plt.plot(df_sort_roll.index, df_sort_roll['pitch_true'], 's-', color = 'blue', label='pitch true', linewidth=2, markersize=6)
plt.legend(loc='upper left')
plt.grid(True, alpha = 0.5)
plt.xlabel("index", fontsize = 14)
plt.ylabel("roll+pitch", fontsize = 14)
plt.savefig(os.path.join(output_figure_folder, "3_sort_roll_true__roll+pitch.png"), dpi=300, bbox_inches='tight')
# plt.show()
plt.close()


# display roll + pitch
plt.figure(figsize=(15, 8))
plt.plot(df_sort_pitch.index, df_sort_pitch['roll_true'], 'o-', color = 'red', label='roll true', linewidth=2, markersize=6)
plt.plot(df_sort_pitch.index, df_sort_pitch['pitch_true'], 's-', color = 'blue', label='pitch true', linewidth=2, markersize=6)
plt.legend(loc='upper left')
plt.grid(True, alpha = 0.5)
plt.xlabel("index", fontsize = 14)
plt.ylabel("roll+pitch", fontsize = 14)
plt.savefig(os.path.join(output_figure_folder, "3_sort_pitch_true__roll+pitch.png"), dpi=300, bbox_inches='tight')
# plt.show()
plt.close()

#====================== display roll - related =====================#


# display roll - diameter & area
plt.figure(figsize=(15, 8))
plt.plot(df_sort_roll['roll_true'], df_sort_roll['diameter_pnt1_x'], 'o-', color = 'red', alpha=0.5, label='diameter_pnt1_x', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['diameter_pnt1_y'], 'o-', color = 'blue', alpha=0.5, label='diameter_pnt1_y', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['diameter_pnt2_x'], 'o-', color = 'green', alpha=0.5, label='diameter_pnt2_x', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['diameter_pnt2_y'], 'o-', color = 'cyan', alpha=0.5, label='diameter_pnt2_y', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['diameter_orientation'], 'o-', color = 'violet', alpha=0.5, label='diameter_orientation', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['diameter_distance'], 'o-', color = 'brown', alpha=0.5, label='diameter_distance', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['max_contour_area']/100, 'o-', color = 'black', alpha=0.5, label='max_contour_area / 100', linewidth=2, markersize=4)
plt.legend(loc='upper left')
plt.grid(True, alpha = 0.5)
plt.title("roll - diameter & area", fontsize=20)
plt.xlabel("roll [degree]", fontsize=14)
plt.ylabel("diameter & area", fontsize=14)
plt.savefig(os.path.join(output_figure_folder, "3_sort_roll_true__roll__diameter.png"), dpi=300, bbox_inches='tight')
# plt.show()
plt.close()



# display roll - pole
plt.figure(figsize=(15, 8))
plt.plot(df_sort_roll['roll_true'], df_sort_roll['pole_left_x'], 'o-', color = 'red', alpha=0.5, label='pole_left_x', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['pole_left_y'], 'o-', color = 'blue', alpha=0.5, label='pole_left_y', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['pole_right_x'], 'o-', color = 'green', alpha=0.5, label='pole_right_x', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['pole_right_y'], 'o-', color = 'cyan', alpha=0.5, label='pole_right_y', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['pole_top_x'], 'o-', color = 'yellow', alpha=0.5, label='pole_top_x', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['pole_top_y'], 'o-', color = 'black', alpha=0.5, label='pole_top_y', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['pole_bottom_x'], 'o-', color = 'magenta', alpha=0.5, label='pole_bottom_x', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['pole_bottom_y'], 'o-', color = 'purple', alpha=0.5, label='pole_bottom_y', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['pole_orientation_lr'], 'o-', color = 'brown', alpha=0.5, label='pole_orientation_lr', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['pole_orientation_tb'], 'o-', color = 'orange', alpha=0.5, label='pole_orientation_tb', linewidth=2, markersize=4)
plt.legend(loc='upper left')
plt.grid(True, alpha = 0.5)
plt.title("roll - pole", fontsize=20)
plt.xlabel("roll [degree]", fontsize=14)
plt.ylabel("pole", fontsize=14)
plt.savefig(os.path.join(output_figure_folder, "3_sort_roll_true__roll__poles.png"), dpi=300, bbox_inches='tight')
# plt.show()
plt.close()


# display roll - touch line
plt.figure(figsize=(15, 8))
plt.plot(df_sort_roll['roll_true'], df_sort_roll['touch_line_topmost_point_x'], 'o-', color = 'red', alpha=0.5, label='touch_line_topmost_point_x', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['touch_line_topmost_point_y'], 'o-', color = 'blue', alpha=0.5, label='touch_line_topmost_point_y', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['touch_line_bottommost_point_x'], 'o-', color = 'green', alpha=0.5, label='touch_line_bottommost_point_x', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['touch_line_bottommost_point_y'], 'o-', color = 'cyan', alpha=0.5, label='touch_line_bottommost_point_y', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['touch_line_total_length'], 'o-', color = 'yellow', alpha=0.5, label='touch_line_total_length', linewidth=2, markersize=4)
plt.plot(df_sort_roll['roll_true'], df_sort_roll['touch_line_num_points'], 'o-', color = 'black', alpha=0.5, label='touch_line_num_points', linewidth=2, markersize=4)
plt.legend(loc='upper left')
plt.grid(True, alpha = 0.5)
plt.title("roll - window touch", fontsize=20)
plt.xlabel("roll [degree]", fontsize=14)
plt.ylabel("window touch", fontsize=14)
plt.savefig(os.path.join(output_figure_folder, "3_sort_roll_true__roll__window_touch.png"), dpi=300, bbox_inches='tight')
# plt.show()
plt.close()




#====================== display pitch - related =====================#


# display pitch - diameter & area
plt.figure(figsize=(15, 8))
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['diameter_pnt1_x'], 'o-', color = 'red', alpha=0.5, label='diameter_pnt1_x', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['diameter_pnt1_y'], 'o-', color = 'blue', alpha=0.5, label='diameter_pnt1_y', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['diameter_pnt2_x'], 'o-', color = 'green', alpha=0.5, label='diameter_pnt2_x', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['diameter_pnt2_y'], 'o-', color = 'cyan', alpha=0.5, label='diameter_pnt2_y', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['diameter_orientation'], 'o-', color = 'violet', alpha=0.5, label='diameter_orientation', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['diameter_distance'], 'o-', color = 'brown', alpha=0.5, label='diameter_distance', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['max_contour_area']/100, 'o-', color = 'black', alpha=0.5, label='max_contour_area / 100', linewidth=2, markersize=4)
plt.legend(loc='upper left')
plt.grid(True, alpha = 0.5)
plt.title("pitch - diameter & area", fontsize=20)
plt.xlabel("pitch [degree]", fontsize=14)
plt.ylabel("diameter & area", fontsize=14)
plt.savefig(os.path.join(output_figure_folder, "3_sort_pitch_true__pitch__diameter.png"), dpi=300, bbox_inches='tight')
# plt.show()
plt.close()



# display pitch - pole
plt.figure(figsize=(15, 8))
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['pole_left_x'], 'o-', color = 'red', alpha=0.5, label='pole_left_x', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['pole_left_y'], 'o-', color = 'blue', alpha=0.5, label='pole_left_y', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['pole_right_x'], 'o-', color = 'green', alpha=0.5, label='pole_right_x', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['pole_right_y'], 'o-', color = 'cyan', alpha=0.5, label='pole_right_y', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['pole_top_x'], 'o-', color = 'yellow', alpha=0.5, label='pole_top_x', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['pole_top_y'], 'o-', color = 'black', alpha=0.5, label='pole_top_y', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['pole_bottom_x'], 'o-', color = 'magenta', alpha=0.5, label='pole_bottom_x', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['pole_bottom_y'], 'o-', color = 'purple', alpha=0.5, label='pole_bottom_y', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['pole_orientation_lr'], 'o-', color = 'brown', alpha=0.5, label='pole_orientation_lr', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['pole_orientation_tb'], 'o-', color = 'orange', alpha=0.5, label='pole_orientation_tb', linewidth=2, markersize=4)
plt.legend(loc='upper left')
plt.grid(True, alpha = 0.5)
plt.title("pitch - pole", fontsize=20)
plt.xlabel("pitch [degree]", fontsize=14)
plt.ylabel("pole", fontsize=14)
plt.savefig(os.path.join(output_figure_folder, "3_sort_pitch_true__pitch__poles.png"), dpi=300, bbox_inches='tight')
# plt.show()
plt.close()


# display pitch - touch line
plt.figure(figsize=(15, 8))
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['touch_line_topmost_point_x'], 'o-', color = 'red', alpha=0.5, label='touch_line_topmost_point_x', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['touch_line_topmost_point_y'], 'o-', color = 'blue', alpha=0.5, label='touch_line_topmost_point_y', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['touch_line_bottommost_point_x'], 'o-', color = 'green', alpha=0.5, label='touch_line_bottommost_point_x', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['touch_line_bottommost_point_y'], 'o-', color = 'cyan', alpha=0.5, label='touch_line_bottommost_point_y', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['touch_line_total_length'], 'o-', color = 'yellow', alpha=0.5, label='touch_line_total_length', linewidth=2, markersize=4)
plt.plot(df_sort_pitch['pitch_true'], df_sort_pitch['touch_line_num_points'], 'o-', color = 'black', alpha=0.5, label='touch_line_num_points', linewidth=2, markersize=4)
plt.legend(loc='upper left')
plt.grid(True, alpha = 0.5)
plt.title("pitch - window touch", fontsize=20)
plt.xlabel("pitch [degree]", fontsize=14)
plt.ylabel("window touch", fontsize=14)
plt.savefig(os.path.join(output_figure_folder, "3_sort_pitch_true__pitch__window_touch.png"), dpi=300, bbox_inches='tight')
# plt.show()
plt.close()



