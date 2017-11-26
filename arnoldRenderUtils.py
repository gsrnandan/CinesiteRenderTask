""" This is a render utils module which has functions to create
	the scene utilities

"""

import arnold


# A dictionary to store the the data type and its corresponding
# arnold setter function
attributesTypeFuncMap = {
	"string": arnold.AiNodeSetStr,
	"vector": arnold.AiNodeSetVec,
	"float": arnold.AiNodeSetFlt,
	"pointer": arnold.AiNodeSetPtr,
	"rgb": arnold.AiNodeSetRGB,
	"integer": arnold.AiNodeSetInt,
	"array": arnold.AiNodeSetArray,
}


def assignAttributes(arnoldNode, attributes):
	""" Method to assign attributes to the arnold node

		This method iterates through the attribute list, finds 
		the data types and its relevant funcitons and sets
		the AiNode attribute

		Args:
			arnoldNode(AiNode): This is the node that gets the attributes
								assigned
			attributes(dict): The dictionary with attribute name, (type,value)
	"""

	for attr, (attrtype, value) in attributes.iteritems():
		attributeFunc = attributesTypeFuncMap.get(attrtype)
		if isinstance(value, (tuple, list)):
			attributeFunc(arnoldNode, attr, *value)
		else:
			attributeFunc(arnoldNode, attr, value)


def createGeometry(geo, name, attributes):
	""" Method to create a geometry 

		This method takes the type,name,attributes 
		and creates a geometry

		Args:
			geo(string): The geometry type
			name(string): The name of the geometry
			attributes(dict): The dictionary with attribute name, (type,value)

		Returns:
			geometry(AiNode): Returns the geometry created with the attributes set
	"""
	geometry = arnold.AiNode(geo)
	arnold.AiNodeSetStr(geometry, "name", name)
	assignAttributes(geometry, attributes)
	return geometry


def createSimpleShader(shaderType, name, attributes):
	""" Method to create a shader 

		This method takes the type,name,attributes  
		and creates a shader

		Args:
			shaderType(string): The shader type
			name(string): The name of the geometry
			attributes(dict): The dictionary with attribute name, (type,value)

		Returns:
			shader(AiNode): Returns the shader created with the attributes set
	"""
	shader = arnold.AiNode(shaderType)
	arnold.AiNodeSetStr(shader, "name", name)
	assignAttributes(shader, attributes)
	return shader

		
def createLight(lightType, name, attributes):
	""" Method to create a light 

		This method takes the type,name,attributes 
		and creates a light

		Args:
			lightType(string): The light type
			name(string): The name of the light
			attributes(dict): The dictionary with attribute name, (type,value)
		Returns:
			light(AiNode): Returns the light created with the attributes set
	"""
	light = arnold.AiNode(lightType)
	arnold.AiNodeSetStr(light, "name", name)
	assignAttributes(light, attributes)
	return light

def createCamera(cameraType, name, attributes):
	""" Method to create a camera 

		This method takes the type,name,attributes 
		and creates a camera

		Args:
			cameraType(string): The camera type
			name(string): The name of the camera
			attributes(dict): The dictionary with attribute name, (type,value)

		Returns:
			camera(AiNode): Returns the camera created with the attributes set
	"""
	camera = arnold.AiNode(cameraType)
	arnold.AiNodeSetStr(camera, "name", name)
	assignAttributes(camera, attributes)
	return camera

def createUniverseOptions(attributes):
	""" Method to define the render options

		This method is called to set the rendering parameters

		Args:
			attributes(dict): The dictionary with attribute name, (type,value)

		Returns:
			options(AiUniverseGetOptions): The variable with the render parameters set

	"""
	options = arnold.AiUniverseGetOptions()
	assignAttributes(options, attributes)
	return options

def createOutputDriver(driverType, name, attributes):
	""" Method to create an output driver with the specified type

		This method takes the type,name,attributes 
		and creates an output driver

		Args:
			driverType(string): The driver type
			name(string): The name of the driver
			attributes(dict): The dictionary with attribute name, (type,value)

		Returns:
			driver(AiNode): Returns the driver created with the attributes set
	"""
	driver = arnold.AiNode(driverType)
	arnold.AiNodeSetStr(driver, "name", name)
	assignAttributes(driver, attributes)
	return driver

def createFilter(filterType, name, attributes):
	""" Method to create a filter with the specified type

		This method takes the type,name,attributes 
		and creates an image filter

		Args:
			filterType(string): The filter type
			name(string): The name of the filter
			attributes(dict): The dictionary with attribute name, (type,value)

		Returns:
			filter(AiNode): Returns the filter created with the attributes set
	"""
	filter = arnold.AiNode(filterType)
	arnold.AiNodeSetStr(filter, "name", name)
	assignAttributes(filter, attributes)
	return filter

def createOutputArray(arrayType, elements, attributes):
	""" Method to create an outputArray 

		This method takes the type,name,attributes 
		and creates an outputArray

		Args:
			arrayType(ARNOLD STRING): The array type
			elements(string): The elements of the array
			attributes(dict): The dictionary with attribute name, (type,value)

		Returns:
			outputArray(AiNode): Returns the array created with the attributes set
	"""
	outputsArray = arnold.AiArrayAllocate(1, 1, arrayType)
	for element in elements:
		arnold.AiArraySetStr(outputsArray, elements.index(element), element)
	assignAttributes(outputsArray, attributes)
	return outputsArray 