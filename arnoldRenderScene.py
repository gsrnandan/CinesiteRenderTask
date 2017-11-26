import os

import PyQt4
import arnold

import arnoldRenderUtils as _arnoldRenderUtils

class ArnoldRenderScene(object):
	""" Arnold Render class to create a scene with lights, camera
		and geometry and render it
	"""
	def __init__(self, sceneName, color, imageType=None, path=None):
		""" Init method to initialize the object

			Args:
				sceneName(string): The name of the scene
				color(tuple): The color of the goemetry in the scene
				imageType(string): The extension/type of the image rendered
				path(string): The path for the image/log file
		"""
		self._sceneName = sceneName
		self._imageType = imageType or "jpg"
		self._path = path or os.getcwd()
		self._color = color

		# Properties for the image and log
	@property
	def image(self):
		imageName = "%s.%s" % (self._sceneName, self._imageType)
		return os.path.join(self._path, imageName)

	@property
	def log(self):
		logName = "%s.log" % self._sceneName
		return os.path.join(self._path, logName)

	def renderGeo(self):
		""" This method calls the arnold functions to setup and scene and render the image
		
		"""

		# Beging the arnold session
		arnold.AiBegin()

		# Set the log for debugging
		arnold.AiMsgSetLogFileName(self.log)
		arnold.AiMsgSetConsoleFlags(arnold.AI_LOG_ALL)

		# Set the attributes for shader
		attributes = {
			"Kd_color": ("rgb", (self._color[0], self._color[1], self._color[2])),
			"Ks": ("float", 0.05),
			"Ko": ("float", .5),
		}
		# Create a simple shader 
		shader = _arnoldRenderUtils.createSimpleShader("standard", "myshader1", attributes)

		# Set the attributes for a geo
		attributes = {
			"center": ("vector", (0.0, 4.0, 0.0)),
			"radius": ("float", 5.0),
			"shader": ("pointer", shader)
		}
		# Create a simple sphere and set the shader created above
		sph = _arnoldRenderUtils.createGeometry("sphere", "mysphere", attributes)
  
  		# Set camera attributes
		attributes = {
			"position": ("vector", (0.0,10.0,35.0)),
			"look_at": ("vector", (0.0,3.0,0.0)),
			"fov": ("float", 45.0),
		}  		
		# create a perspective camera
		camera = _arnoldRenderUtils.createCamera("persp_camera", "scene_Camera", attributes)
  
  		# Set light attributes
		attributes = {
			"position": ("vector", (0.0,30.0,0.0)),
			"intensity": ("float", 10.0),
			"radius": ("float", 4.0),
		}
		# Create point lights with different attributes
		point_lightA = _arnoldRenderUtils.createLight("point_light","pointLight_A",attributes)

		# Point Light B
		attributes["position"] = ("vector", (0.0, -30.0, 0.0))
		point_lightB = _arnoldRenderUtils.createLight("point_light","pointLight_B",attributes)

		# Point light C
		attributes = {
			"position": ("vector", (0.0,4.0,20.0)),
			"intensity": ("float", 5.0),
			"radius": ("float", 15.0),
		}
		point_lightC = _arnoldRenderUtils.createLight("point_light","pointLight_C",attributes)

		# Set attributes for render Parameters
		attributes = {
			"AA_samples": ("integer", 8),
			"xres": ("integer", 480),
			"yres": ("integer", 360),
			"GI_diffuse_depth": ("integer", 4),
			"camera": ("pointer", camera),
		}
		# Set the render options
		options = _arnoldRenderUtils.createUniverseOptions(attributes)
  
  		# Set the driver attributes
		attributes = {
			"filename": ("string", os.path.basename(self.image)),
			"gamma": ("float", 2.2),
		}
		driver = _arnoldRenderUtils.createOutputDriver("driver_jpeg","scene_driver",attributes)
  
  		# Create a filter
		filter = _arnoldRenderUtils.createFilter("gaussian_filter", "scene_filter", {})
  		
  		# Create an output array with the filter and driver
		outputArrayElements = ["RGBA RGBA scene_filter scene_driver"]
		outputs_array = _arnoldRenderUtils.createOutputArray(arnold.AI_TYPE_STRING, outputArrayElements, {})
		attributes = {
			"outputs": ("array", outputs_array),
		}
		_arnoldRenderUtils.assignAttributes(options,attributes)
  
		# render the image
		arnold.AiRender(arnold.AI_RENDER_MODE_CAMERA)
	
		# Arnold session shutdown
		arnold.AiEnd()

	def setColor(self,color):
		""" Sets the color for the object that is being rendered.

			Args:
				color(tuple): The r,g,b values of the color that is to be set
		
		"""
		self._color = color