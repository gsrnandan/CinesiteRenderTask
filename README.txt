This Folder contains the python files to open a widget, set a color for the object and render the geo.

It has the following files

1) arnoldRenderGUI.py - The main funciton, which creates a GUI with the render and set color button. 
2) arnoldRenderScene.py - This module contains the scene information. This sets up the scene and renders the geo in arnold
3) arnoldRenderUtils.py - This module has all the funcitons required for the arnoldRenderScene module. This has functions defined to create the geo, camera, shader, filter, driver and the output array.
4) colorBox.py - This module creates the color picker widget and reads the color.
5) constants - The constants for the default color and scene name.