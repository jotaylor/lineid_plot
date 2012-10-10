#!  /usr/bin/env python

###################################################################################
'''
DATE: 09/20/12

AUTHOR: Jo Taylor, RIA

PURPOSE: This is a program that will plot the spectrum from 3 STIS gratings
and label lines that I measured using "splot". It requires user installation of 
the lineid_plot module.
'''
###################################################################################

# Load packages.
import numpy as np
import pyfits as pf
import pylab as pl
import lineid_plot

# Read in 230L grating wavelength and flux.
infile230 = "g230l_fine.fits"
data230 = pf.getdata(infile230,1)
wave230 = data230.field('wavelength')
flux230 = data230.field('flux')
wave0 = wave230[0]
flux0 = flux230[0]

# Read in 430L grating wavelength and flux.
infile430 = "g430l.fits"
data430 = pf.getdata(infile430,1)
wave430 = data430.field('wavelength')
flux430 = data430.field('flux')
wave1 = wave430[0]
flux1 = flux430[0]

# Read in 750L grating wavelength and flux.
infile750 = "g750l.fits"
data750 = pf.getdata(infile750,1)
wave750 = data750.field('wavelength')
flux750 = data750.field('flux')
wave2 = wave750[0]
flux2 = flux750[0]

# Combine all wavelength and flux arrays.
# Parts of the 230L grating are not included to cut off noise.
# Parts of the 430L grating are not included to cut off noise.
wave_all = np.append(wave0[60:1014],wave1[87:1022])
flux_all = np.append(flux0[60:1014],flux1[87:1022])

# Define the line wavelengths and labels for lines.
line_wavel = [1851.5, 2036.6, 2329.1, 2757.7, 3573.4, 3626., 3942.9, 3963.5, 4267.5, 4348.4, 3088.3, 3139.1]
line_label = ["Lya", "Si IV", "Si II", "Si II", "Fe II", "Fe II", "Fe II", "Fe II", "Mg II", "Mg I", "Zn II", "Zn II"]

# Plot the actual data and axes using the lineid_plot module.
# Plot the labels using pylab. 
fsize = 18
lineid_plot.plot_line_ids(wave_all,flux_all,line_wavel,line_label)
pl.ylabel("Flux [ergs/s/cm$^2$/$\AA$]",fontsize=fsize)
pl.xlabel("Wavelength [$\AA$]",fontsize=fsize)

