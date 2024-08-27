
# LIBRARIES----------------------------------------------------------------------
import Def_Files.Plotting_Definition as PLT_Def
import matplotlib.pyplot as plt
# -------------------------------------------------------------------------------


# VARIABLES----------------------------------------------------------------------
#--------------------------------------------------------------------------------


SheetName = 'S2p Scan'                         # Name of the Excel spreadsheet
#SheetName = 'Ti2p Scan'                        # Name of the Excel spreadsheet
CoreName = r'S 2p'                             # Title of the plot (Usually name of the Core level)
#CoreName = r'Ti 2p'                             # Title of the plot (Usually name of the Core level)
OffsetRow =9                                    # Rows to miss in the Excel spreadsheet

SaveFig = False                                 # Save Figure as PNG
DPI = 300                                       # DPI level of the figure

font_type = 'Calibri'                           # Plot font used
font_size = 12                                  # Plot font size used
Fig_w, Fig_h = 12, 16                           # Size in cm

BE_correction = False                           # Correction of the binding energy

Y_MIN, Y_MAX, Y_Offset = -0.02, 1.6, 0.1

X_MIN , X_MAX, STEP = 158, 167, 2               # For S2p
#X_MIN , X_MAX, STEP = 453, 473, 4               # For Ti2p

# FILENAMES------------------------------------------------------------
FileName_Array = [
#     'DATA/SK_Example_processed.xlsx',
#     'Data/SK_Example_processed 2.xlsx']
      'DATA/D P-COOH NoB_processed.xlsx',
      'DATA/D P-COOH WithB_processed.xlsx']

ColorPerFile = [
    'k',
    'k'
]

# PEAK ARRAY-----------------------------------------------------------
Peaks_Array = [
    [['S2p3 Au-S (Normalised)',         # Name of the column
     'tab:blue',                            # Color used
     False,                             # Show the label
     True,                             # Show the line
     'S2$p_{3/2}$ Au-S',              # Name of the label
     0.6,                               # alpha value
     1,                                 # order
     True],                             # plot the column or ignore

    ['S2p1 Au-S (Normalised)',  # Name of the column
      'tab:blue',  # Color used
      False,  # Show the label
      False,  # Show the line
      'S2$p_{3/2}$ Au-S',  # Name of the label
      0.6,  # alpha value
      1,  # order
      True],  # plot the column or ignore

    ['S2p3 Au-S-R (Normalised)',  # Name of the column
      'tab:orange',  # Color used
      False,  # Show the label
      True,  # Show the line
      'S2$p_{3/2}$ Au-S-R',  # Name of the label
      0.6,  # alpha value
      1,  # order
      True],  # plot the column or ignore

     ['S2p1 Au-S-R (Normalised)',  # Name of the column
      'tab:orange',  # Color used
      False,  # Show the label
      False,  # Show the line
      'S2$p_{1/2}$ Au-S-R',  # Name of the label
      0.6,  # alpha value
      1,  # order
      True],

    ['S2p3 S-S (Normalised)',  # Name of the column
     'tab:green',  # Color used
     False,  # Show the label
     True,  # Show the line
     'S2$p_{3/2}$ S-S',  # Name of the label
     0.6,  # alpha value
     1,  # order
     True],  # plot the column or ignore

    ['S2p1 S-S (Normalised)',  # Name of the column
     'tab:green',  # Color used
     False,  # Show the label
     False,  # Show the line
     'S2$p_{1/2}$ S-S',  # Name of the label
     0.6,  # alpha value
     1,  # order
     True]],

    [['S2p3 Au-S (Normalised)',         # Name of the column
     'tab:blue',                            # Color used
     True,                              # Show the label
     True,                              # Show the line
     'Au-S',                            # Name of the label
     0.6,                               # alpha value
     1,                                 # order
     True],                             # plot the column or ignore

    ['S2p1 Au-S (Normalised)',  # Name of the column
      'tab:blue',  # Color used
      False,  # Show the label
      False,  # Show the line
      'S2$p_{3/2}$ Au-S',  # Name of the label
      0.6,  # alpha value
      1,  # order
      True],  # plot the column or ignore

    ['S2p3 Au-S-R (Normalised)',  # Name of the column
      'tab:orange',  # Color used
      True,  # Show the label
      True,  # Show the line
      'Au-S-R',  # Name of the label
      0.6,  # alpha value
      1,  # order
      True],  # plot the column or ignore

     ['S2p1 Au-S-R (Normalised)',  # Name of the column
      'tab:orange',  # Color used
      False,  # Show the label
      False,  # Show the line
      'S2$p_{1/2}$ Au-S-R',  # Name of the label
      0.6,  # alpha value
      1,  # order
      True],

    ['S2p3 S-S (Normalised)',  # Name of the column
     'tab:green',  # Color used
     True,  # Show the label
     True,  # Show the line
     'S-S',  # Name of the label
     0.6,  # alpha value
     1,  # order
     True],  # plot the column or ignore

    ['S2p1 S-S (Normalised)',  # Name of the column
     'tab:green',  # Color used
     False,  # Show the label
     False,  # Show the line
     'S2$p_{1/2}$ S-S',  # Name of the label
     0.6,  # alpha value
     1,  # order
     True]]
    # [['Ti2p3 4+ (Normalised)',          # Name of the column
    #  'blue',                            # Color used
    #  False,                             # Show the label
    #  False,                              # Show the line
    #  'Ti2$p_{3/2} ^{4+}$',              # Name of the label
    #  0.6,                               # alpha value
    #  1,                                 # order
    #  True],                             # plot the column or ignore
    #
    # ['Ti2p3 3+ (Normalised)',           # Name of the column
    #  'red',                             # Color used
    #  False,                              # Show the label
    #  True,                              # Show the line
    #  'Ti2$p_{3/2} ^{3+}$',              # Name of the label
    #  0.6,                               # alpha value
    #  2,                                 # order
    #  True],                             # plot the column or ignore
    #
    # ['Ti2p3 2+ (Normalised)',           # Name of the column
    #  'green',                           # Color used
    #  False,                              # Show the label
    #  True,                              # Show the line
    #  'Ti2$p_{3/2} ^{2+}$',              # Name of the label
    #  0.6,                               # alpha value
    #  3,                                 # order
    #  True]],                            # plot the column or ignore
    #
    # [['Ti2p3 4+ (Normalised)',          # Name of the column
    # 'blue',                             # Color used
    # True,                              # Show the label
    # True,                               # Show the line
    # 'Ti2$p_{3/2} ^{4+}$',               # Name of the label
    # 0.6,                                # alpha value
    # 1,                                  # order
    # True],                              # plot the column or ignore
    #
    # ['Ti2p3 3+ (Normalised)',           # Name of the column
    #  'red',                             # Color used
    #  True,                              # Show the label
    #  True,                              # Show the line
    #  'Ti2$p_{3/2} ^{3+}$',              # Name of the label
    #  0.6,                               # alpha value
    #  2,                                 # order
    #  True],                             # plot the column or ignore
    #
    # ['Ti2p3 2+ (Normalised)',           # Name of the column
    #  'green',                           # Color used
    #  True,                              # Show the label
    #  True,                              # Show the line
    #  'Ti2$p_{3/2} ^{2+}$',              # Name of the label
    #  0.6,                               # alpha value
    #  3,                                 # order
    #  True]]                             # plot the column or ignore
]
##----------------------------------------------------------------------

## EXTRA PEAK LABEL-----------------------------------------------------
ExtraLabels_Array = [
    ['Ti 2$p_{1/2}$',                   # name of the label
     464,                            # X position
     1.55,                              # Y position (1 is the intensity of the MAX peak of the first plot)
     'grey',                            # Color used
     'Line',                            # used of Line (if Yes write 'Line')
     90,                                # rotation
     True]                              # show or ignore the label
]
##----------------------------------------------------------------------


## INSET----------------------------------------------------------------
Inset = [469.25,                        # High BE range
         467.25,                        # Low BE range
         4,                             # Intensity increase times X
         0.2,                           # Intensity offset  X x Y_MAX
         'k',                           # Color
         False]                         # Show or ignore the inset

data_INSET_X, data_INSET = [],[]
## ---------------------------------------------------------------------

##--------------------------------------------------------------------------------
##--------------------------------------------------------------------------------


## MAIN PROGRAM-------------------------------------------------------------------
# Initialise Main Plot
Fig, ax = plt.subplots()

File_Number, y_min, y_min2, y_max = 0, 0, 0, 1.6             # INITIALISE variables

for FileName in FileName_Array:

    data_filtered, data =  PLT_Def.LOAD_DATA(FileName,
                                             SheetName,
                                             OffsetRow)

    if Inset[5] :
        data_INSET_X, data_INSET = PLT_Def.INSET(Inset,
                                                 data,
                                                 data_filtered)

    if BE_correction:
        data_filtered , data = PLT_Def.BE_CORRECTION(data_filtered, data)

    y_min, y_max = PLT_Def.PLOT(Fig,
                                 ax,
                                 File_Number,               # File Number
                                 ColorPerFile,              # Color of the data
                                 data_filtered,             # Data without the 0 values
                                 data,                      # All data
                                 Peaks_Array[File_Number],               # Peaks definition
                                 ExtraLabels_Array,         # Peaks Labels definition
                                 Inset,                     # Inset definition
                                 data_INSET_X,              # Data_inset X value
                                 data_INSET,                # Data_inset Y value
                                 Y_MAX,                     # Y MAX calculated from the highest peak
                                 Y_MIN,                     # Y MIN calculated from the lowest peak
                                 Y_Offset,                  # Offset between each plot
                                 font_size)
    if File_Number == 0: y_min2 = y_min


    File_Number = File_Number +1

PLT_Def.PLOT_SETTING(Fig,
                     ax,
                     font_type,
                     font_size,
                     Fig_w,
                     Fig_h,
                     X_MIN,
                     X_MAX,
                     y_min2,
                     y_max,
                     STEP,
                     CoreName)                              # Name of the core level

if SaveFig: PLT_Def.SAVE_DATA(FileName_Array[0], SheetName, DPI)

plt.show()
## END MAIN PROGRAM---------------------------------------------------------------
