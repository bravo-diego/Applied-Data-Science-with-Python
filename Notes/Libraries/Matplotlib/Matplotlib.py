# Matplotlib Architecture

# Matplotlib's pyplot is an example of a procedural method for building visualizations while SVG, HTML are declarative methods of creating visualizations.

    # Backend Layer -- Deals with the rendering of plots to screen or files. 
        # * FigureCanvas encapsulates the concept of a surface to draw into (paper)
        # ** Renderer does the drawing (paintbrush)
        # *** Event handles user inputs (keyboard and mouse events)

    # Artist Layer -- Contains containers such as Figure, Subplot, and Axes. Contains primitives, such as Line2D and Rectangle, and collections, such as PathCollection.
        # * Artist is the object that knows how to take the Renderer (paintbrush) and put ink on the canvas

    # Scripting Layer -- Simplifies access to the Artist and Backend layers.
    
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg # backend
from matplotlib.figure import Figure # figure object
plt.plot.__doc__

plt.figure() # create a figure
plt.plot(1, 1, 'o') # plot the point -- using a circle marker
plt.plot(3, 3, 'x')
plt.plot(5, 5, '*')
ax = plt.gca() # get a reference to the current axes
ax.axis([0,6,0,10]) # axis properties -- minimum value for x = 0; maximum value for x = 6; minimum value for y = 0; maximum value for y = 10

print(ax.get_children()) # children axes

plt.show() # print plot

