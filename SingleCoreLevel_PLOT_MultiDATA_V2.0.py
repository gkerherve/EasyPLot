
# LIBRARIES----------------------------------------------------------------------
import matplotlib.pyplot as plt
import Def_Files.Plotting_Definition as PLT_Def
import Def_Files.CoreLevels.S2p as CORE_LEVELS  # USE THE CORRECT CORE LEVEL
# -------------------------------------------------------------------------------

# VARIABLES----------------------------------------------------------------------
OffsetRow = 9                                   # Rows to miss in the Excel spreadsheet
SaveFig   = True                                # Save Figure as PNG
DPI       = 300                                 # DPI level of the figure

font_type = 'Verdana'                           # Plot font used
font_size = 19                                  # Plot font size used
Fig_w     = 12                                  # Size in cm
Fig_h     = 18                                  # Size in cm

IsFitPlot = True                               # Show a line plot with or without Fit
IsOffset  = False                                # Show an offset
# -------------------------------------------------------------------------------

# OTHER VARIABLES----------------------------------------------------------------
SheetName = CORE_LEVELS.SheetName               # Name of the Excel spreadsheet
CoreName = CORE_LEVELS.CoreName                 # Title of the plot (Usually name of the Core level)
ImageFig = CORE_LEVELS.ImageFig
BE_correction = CORE_LEVELS.BE_correction

X_MIN , X_MAX, STEP = (CORE_LEVELS.X_MIN,
                       CORE_LEVELS.X_MAX,
                       CORE_LEVELS.STEP)

Y_MIN, Y_MAX, Y_Offset = (CORE_LEVELS.Y_MIN,
                          CORE_LEVELS.Y_MAX,
                          CORE_LEVELS.Y_Offset)

FileName_Array = CORE_LEVELS.FileName_Array
ColorPerFile = CORE_LEVELS.ColorPerFile
LegendCustom = CORE_LEVELS.LegendCustom
Peaks_Array = CORE_LEVELS.Peaks_Array
ExtraLabels_Array = CORE_LEVELS.ExtraLabels_Array
OtherLabel_Array = CORE_LEVELS.OtherLabel_Array
Inset = CORE_LEVELS.Inset
data_INSET_X, data_INSET = CORE_LEVELS.data_INSET_X, CORE_LEVELS.data_INSET
# -------------------------------------------------------------------------------


# Initialise Main Plot-----------------------------------------------------------
Fig, ax = plt.subplots()

File_Number, y_min, y_min2, y_max, y_max_old, Offset = 0, 0, 0, 0, 0, 0             # INITIALISE variables
# --------------------------------------------------------------------------------

#  MAIN PROGRAM ------------------------------------------------------------------


for FileName in FileName_Array:
    print(FileName)
    data_filtered, data =  PLT_Def.LOAD_DATA(FileName,
                                             SheetName,
                                             OffsetRow)

    if Inset[5] :
        data_INSET_X, data_INSET = PLT_Def.INSET(Inset,
                                                 data,
                                                 data_filtered)

    if BE_correction:
        data_filtered , data = PLT_Def.BE_CORRECTION(data_filtered, data)

    y_min, y_max, y_max_old, Offset = PLT_Def.PLOT(Fig,
                                                 ax,
                                                 IsFitPlot,                 # Fitting plot or line plot
                                                 IsOffset,                  # Offset or no Offset in Line plot
                                                 File_Number,               # File Number
                                                 ColorPerFile,              # Color of the data
                                                 data_filtered,             # Data without the 0 values
                                                 data,                      # All data
                                                 Peaks_Array[File_Number],  # Peaks definition
                                                 ExtraLabels_Array,         # Peaks Labels definition
                                                 Inset,                     # Inset definition
                                                 data_INSET_X,              # Data_inset X value
                                                 data_INSET,                # Data_inset Y value
                                                 y_max_old,                 # Get the previous y_max value
                                                 Y_MAX,                     # Y MAX calculated from the highest peak
                                                 Y_MIN,                     # Y MIN calculated from the lowest peak
                                                 Y_Offset,                  # Offset between each plot
                                                 Offset,
                                                 y_max,
                                                 font_size)
    if File_Number == 0: y_min2 = y_min


    File_Number = File_Number +1

PLT_Def.EXTRA_LABEL(Fig, ax, y_max, ExtraLabels_Array, font_size)

PLT_Def.OTHER_LABEL(Fig, ax, OtherLabel_Array, font_size)

PLT_Def.PLOT_SETTING(Fig,
                     ax,
                     font_type,
                     font_size,
                     LegendCustom,
                     Fig_w,
                     Fig_h,
                     X_MIN,
                     X_MAX,
                     y_min2,
                     y_max_old + y_max * (Y_MAX-1),
                     STEP,
                     CoreName)                              # Name of the core level

if SaveFig:
    for File_Core in FileName_Array:
        PLT_Def.SAVE_DATA2(CoreName, DPI)

plt.show()
#  END MAIN PROGRAM---------------------------------------------------------------
