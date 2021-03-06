Your Spectral Savior: lineid_plot
===============

Info about the lineid_plot module
-------------------------

Recently I was trying to label some lines in spectra- I asked around to a few 
python users and got a few methods. All of them were pretty cumbersome though, and 
required a lot of effort to tailor to my needs. 

I searched around on the internet and found this link:
http://packages.python.org/lineid_plot/
The source code can be found on github as well:
https://github.com/phn/lineid_plot

There are instructions on the page on how to use this handy module that labels
lines on a spectrum. The nice part is you just have to make two lists, one with
your line locations and the label you want for each respective element in the
list. Then you just plot it using the linid_plot.plot_line_ids command that 
has 4 arguments: xdata list/array, ydata list/array, line wavelengths list, line 
labels list. You can also still use pylab or matplotlib on the same plot- for
instance, I created x and y labels using pylab. The example on the websites above
use matplotlib, while I use pylab. You can also still interact with the plot as 
usual but zooming in, panning, etc. The lines will move with the plot but the 
labels may go off the screen if you move too far.

I have also included the script (lines.py) I used to generate my spectrum 
with labeled lines as well as the 3 FITS files of the spectra used in the script.
You can see the resultant plot in plot_screenshot.png. 

You have to install the lineid_plot module before you can run my script. Matt 
Davis provided me with this really handy link for installing modules, if you need:
http://stsdas.stsci.edu/configuration.html#python 

Let the labeling begin.

Also, I should note that I am not the creator of this module, only a happy user.
See the github page for author information.

-Jo Taylor
