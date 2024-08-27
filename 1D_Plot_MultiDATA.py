# LIBRARIES----------------------------------------------------------------------
import matplotlib.pyplot as plt
import Def_Files.Plotting_Definition as PLT_Def
import Def_Files.CoreLevels.S2p as CORE_LEVELS  # USE THE CORRECT CORE LEVEL
# -------------------------------------------------------------------------------

# VARIABLES----------------------------------------------------------------------
OffsetRow = 9                                   # Rows to miss in the Excel spreadsheet
SaveFig   = False                               # Save Figure as PNG
DPI       = 300                                 # DPI level of the figure

font_type = 'Verdana'                           # Plot font used
font_size = 12                                  # Plot font size used
Fig_w     = 12                                 # Size in cm
Fig_h     = 18                                  # Size in cm

IsFitPlot = True                               # Show a line plot with or without Fit
IsOffset  = False                                # Show an offset
# -------------------------------------------------------------------------------

# OTHER VARIABLES----------------------------------------------------------------
SheetName = CORE_LEVELS.SheetName               # Name of the Excel spreadsheet
CoreName = CORE_LEVELS.CoreName                 # Title of the plot (Usually name of the Core level)
ImageFig = CORE_LEVELS.ImageFig


# -------------------------------------------------------------------------------

# Initialise Main Plot-----------------------------------------------------------
Fig, ax = plt.subplots()

        # INITIALISE variables
# --------------------------------------------------------------------------------

