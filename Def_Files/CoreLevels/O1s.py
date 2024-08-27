# S2P DEFINITION FILE--------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# FILENAMES------------------------------------------------------------
FileName_Array = [                             # List of Files
    'DATA/C P-OH-NR2 WithB_processed.xlsx',
    'DATA/E P-OH-COOH WithB_processed.xlsx']
      # 'DATA/D P-COOH WithB_processed.xlsx',
      # 'DATA/D P-COOH NoB_processed.xlsx']
    #    'DATA/D P-COOH NoB_processed.xlsx',
    #   'DATA/D P-COOH NoB_processed.xlsx',
    # 'DATA/D P-COOH NoB_processed.xlsx']
    #    'DATA/D P-COOH NoB_processed.xlsx',
    #   'DATA/D P-COOH NoB_processed.xlsx']
# ---------------------------------------------------------------------

SheetName = 'O1s Scan'                         # Name of the Excel spreadsheet
CoreName  = r'O 1s'                             # Title of the plot (Usually name of the Core level)

ImageFig  = 'O1s.png'

X_MIN , X_MAX, STEP = 528, 537, 3              # Binding energy Min and Max for S2p
Y_MIN, Y_MAX, Y_Offset = -0.02, 2.05, +0.1       # Min and Max in function of the highest peak

BE_correction = False                          # Correction of the binding energy DONE ALREADY IN THE FILE

ColorPerFile = [                               # Needs to have the same number as the number of file
    'cornflowerblue',
    'indianred',
    'gray',
    'tab:gray',
    'tab:gray',
    'tab:gray',
    'tab:gray',
    'tab:gray'
]

#LEGEND CONF----------------------------------------------------------
LegendCustom = [                                # Needs to have the same number as the number of file
    ['cornflowerblue', 'indianred'],            # Color Legend
    ['P-OH-NR$_2$', 'P-OH-COOH'],               # Label Legend
    [True]                                     # Show Legend
]
# ---------------------------------------------------------------------

# PEAK ARRAY-----------------------------------------------------------
Peaks_Array = ([
    ['O1s C=O (Normalised)',
    #['O1s C=O (Normalised)',                    # Name of the column
     12,                                         # Color used
     False,                                     # Show the label
     False,                                      # Show the line
     'C=O',                                 # Name of the label
     0.8,                                       # alpha value
     0,                                         # order
     True],                                     # plot the column or ignore

   ['O1s H-O-C, SO4, NOx (Normalised)',  # Name of the column
    13,  # Color used
    False,  # Show the label
    False,  # Show the line
    'H-O-C',  # Name of the label
    0.8,  # alpha value
    1,  # order
    True],  # plot the column or ignore

   ['O1s O-C=O, O-H (Normalised)',  # Name of the column
    14,  # Color used
    False,  # Show the label
    False,  # Show the line
    'O-C=O, O-H',  # Name of the label
    0.8,  # alpha value
    2,  # order
    True]],  # plot the column or ignore

   [['O1s C=O (Normalised)',  # Name of the column
    12,  # Color used
    True,  # Show the label
    False,  # Show the line
    'C=O',  # Name of the label
    0.8,  # alpha value
    0,  # order
    True],  # plot the column or ignore

   ['O1s H-O-C, SO4, NOx (Normalised)',  # Name of the column
    13,  # Color used
    True,  # Show the label
    False,  # Show the line
    'H-O-C',  # Name of the label
    0.8,  # alpha value
    1,  # order
    True],  # plot the column or ignore

   ['O1s O-C=O, O-H (Normalised)',  # Name of the column
    14,  # Color used
    True,  # Show the label
    False,  # Show the line
    'O-C=O, O-H',  # Name of the label
    0.8,  # alpha value
    2,  # order
    True]],  # plot the column or ignore

    [],
    [],
    [],
    [],
    [],
    []

)
# ----------------------------------------------------------------------

# EXTRA PEAK LABEL------------------------------------------------------
ExtraLabels_Array = [
    ['P-COOH No B',                     # name of the label
     166,                               # X position
     0.2,                               # Y position (1 is the intensity of the MAX peak of the first plot)
     'tab:gray',                        # Color used
     'No',                              # used of Line (if Yes write 'Line')
     0,                                 # rotation
    False],                             # show or ignore the label

    ['P-COOH with B',                   # name of the label
     166,                               # X position
     1.4,                               # Y position (1 is the intensity of the MAX peak of the first plot)
     'tab:gray',                        # Color used
     'No',                              # used of Line (if Yes write 'Line')
     0,                                 # rotation
    False],                             # show or ignore the label

    ['S2$p_{3/2}$ Au-S-R',              # name of the label
     161.4,                             # X position
     1.1,                               # Y position (1 is the intensity of the MAX peak of the first plot)
     'tab:gray',                        # Color used
     'Line',                            # used of Line (if Yes write 'Line')
     90,                                # rotation
     False]                              # show or ignore the label
]
# ----------------------------------------------------------------------

# OTHER LABEL ----------------------------------------------------------
OtherLabel_Array = [
    ['Other Label',                     # name of the label
     0.2,                               # X position
     0.,
     'k',                              # Color used
     0,                                 # rotation
     False]                             # show or ignore the label
]
# ----------------------------------------------------------------------

#  INSET----------------------------------------------------------------
Inset = [469.25,                        # High BE range
         467.25,                        # Low BE range
         4,                             # Intensity increase times X
         0.2,                           # Intensity offset  X x Y_MAX
         'k',                           # Color
         False]                         # Show or ignore the inset

data_INSET_X, data_INSET = [],[]
# ----------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------