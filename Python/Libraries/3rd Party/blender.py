import bpy # import Blender Python API



# Accessing data in Blender

# Accessing objects
objects = bpy.data.objects # get a collection of all objects in the current Blender file
object = objects["Cube"] # get a reference to a specific object in the scene by name
name = object.name # get the name property of the object
# Accessing object location
location = object.location # get the location property of the object as a Vector class
rotation_euler = object.rotation_euler # get the rotation angles in radians of the object as an Euler class
rotation_quaternion = object.rotation_quaternion # get the rotation of the object as a quaternion
scale = object.scale # get the scale property of the object as a Vector class 
matrix_world = object.matrix_world # get the world transformation matrix of the object as a 4x4 Matrix class containing location, rotation and scale
translation = matrix_world.to_translation() # get the translation component of the matrix as a Vector class, equivalent to matrix_world.translation
rotation_euler = matrix_world.to_euler() # get the rotation component of the matrix as an Euler class
scale = matrix_world.to_scale() # get the scale component of the matrix as a Vector class
rotation_scale_matrix = object.matrix_world.to_3x3() # convert the 4x4 matrix to a 3x3 matrix containing only rotation and scale
rotation = rotation_scale_matrix.normalized() # normalize the 3x3 matrix to remove scale, leaving only rotation
dimensions = object.dimensions # get the dimensions of the object as a Vector class representing width, height and depth

# Accessing object modifiers
modifiers = object.modifiers # get a collection of all modifiers applied to the object
modifier = modifiers["Subdivision"] == modifiers[0] # get a reference to a specific modifier by name or index

# Accessing collections
collections = bpy.data.collections # get a collection of all collections in the current Blender file
collection = collections["Collection"] # get a reference to a specific collection by name


# Accessing context in Blender
context = bpy.context # get the current context in Blender
active_object = context.active_object # get the currently active object in the scene
active_object = context.object # same as above, shorthand for context.active_object
selected_objects = context.selected_objects # get a list of currently selected objects in the scene


# Creating a property group 
class PropertyGroup(bpy.types.PropertyGroup): # define a new property group class to hold custom properties
    float_prop = bpy.props.FloatProperty( # define a new float property
        name="open", # name of the property to be displayed as default label in the UI
        description="A float property", # description of the property to be displayed as tooltip in the UI
        default=10, # default value of the property
        min=0.0, # minimum value of the property
        max=100.0, # maximum value of the property
        step=0.1, # step size for incrementing/decrementing the property in the UI
        subtype='NONE', # subtype of the property, can be used to define special behavior or UI representation
        soft_min=0.0, # soft minimum value for UI sliders, will make the slider slow down when approaching this value
        soft_max=100.0, # soft maximum value for UI sliders, will make the slider slow down when approaching this value
        precision=3 # number of decimal places to display in the UI
    )
    int_prop = bpy.props.IntProperty( # define a new integer property
        name="count", # name of the property to be displayed as default label in the UI
        description="An integer property example", # description of the property to be displayed as tooltip in the UI
        default=5, # default value of the property
        min=0, # minimum value of the property
        max=100, # maximum value of the property
        step=1, # step size for incrementing/decrementing the property in the UI
        subtype='NONE', # subtype of the property, can be used to define special behavior or UI representation
        soft_min=0, # soft minimum value for UI sliders, will make the slider slow down when approaching this value
        soft_max=100, # soft maximum value for UI sliders, will make the slider slow down when approaching this value
    )
    enum_prop = bpy.props.EnumProperty( # define a new enum property
        name="options", # name of the property to be displayed as default label in the UI
        description="An enum property example", # description of the property to be displayed as tooltip in the UI
        items=[ # list of enum items as tuples of (identifier, name, description)
            ('OPT_A', "Option A", "Description for option A"),
            ('OPT_B', "Option B", "Description for option B"),
            ('OPT_C', "Option C", "Description for option C")
        ],
        default='OPT_A' # default selected item by identifier
    )

    


class MyPanel(bpy.types.Panel): # define a new panel to be added to the UI
    bl_label = "My Panel" # label of the panel to be displayed
    bl_idname = "MY_PANEL" # unique identifier for the panel to be referenced
    bl_space_type = "VIEW_3D" # space where the panel will be displayed
    bl_region_type = "UI" # region within the space where the panel will be displayed
    bl_category = "Item" # category tab in the UI where the panel will be located
    
    def draw(self, context): # method to called to define the layout of the panel
        object = context.object # get the active object, same as context.active_object
        layout = self.layout # get the layout object for the panel
        row = layout.row() # create a new row in the layout
        col = layout.column() # create a new column in the layout
        row.label(text="this is a panel") # add a label to the row
        row.prop(object.properties, "open") # diplays the specific property by attribute name from the property group, the UI will match the property attributes used in its definition 
        row.operator("wm.save_mainfile") # add a button with a predefined operator in Blender
        

def register(): # function called by Blender when loading or enabling the add-on
    bpy.utils.register_class(PropertyGroup) # register the property group class with Blender
    bpy.utils.register_class(MyPanel) # register the panel class with Blender to make it available in the UI
    bpy.types.Object.properties = bpy.props.PointerProperty(type=PropertyGroup) # add a pointer property to the Object type to hold an instance of the custom property group for each object

def unregister(): # function called by Blender when unloading the script
    bpy.utils.unregister_class(bpy.types.MY_PANEL) # unregister the panel class when no longer needed using its unique bl_idname