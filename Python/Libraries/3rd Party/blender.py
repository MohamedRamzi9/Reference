import bpy # import Blender Python API



# Accessing data in Blender

# Accessing objects
objects = bpy.data.objects # get a collection of all objects in the current Blender file
object = objects["Cube"] # get a reference to a specific object in the scene by name
name = object.name # get the name property of the object
# Accessing object location
location = object.location # get the location property of the object as a Vector class
location.x == location[0] # individual components of the Vector can be accessed by name or index (x, y, z) or (0, 1, 2)
rotation_euler = object.rotation_euler # get the rotation angles in radians of the object as an Euler class
rotation_quaternion = object.rotation_quaternion # get the rotation of the object as a quaternion
scale = object.scale # get the scale property of the object as a Vector class 
matrix_world = object.matrix_world # get the world transformation matrix of the object as a 4x4 Matrix class containing location, rotation and scale
translation = matrix_world.to_translation() # get the translation component of the matrix as a Vector class, equivalent to matrix_world.translation
rotation_euler = matrix_world.to_euler() # get the rotation component of the matrix as an Euler class
scale = matrix_world.to_scale() # get the scale component of the matrix as a Vector class
rotation_scale_matrix = object.matrix_world.to_3x3() # convert the 4x4 matrix to a 3x3 matrix containing only rotation and scale
rotation = rotation_scale_matrix.normalized() # normalize the 3x3 matrix to remove scale, leaving only rotation

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


# Accessing properties
float_prop = bpy.props.FloatProperty(name="open", default=10) # define a new float property with a name and default value and register it with Blender RNA system



class MyPanel(bpy.types.Panel): # define a new panel to be added to the UI
    bl_label = "My Panel" # label of the panel to be displayed
    bl_idname = "MY_PANEL" # unique identifier for the panel to be referenced
    bl_space_type = "VIEW_3D" # space where the panel will be displayed
    bl_region_type = "UI" # region within the space where the panel will be displayed
    bl_category = "Item" # category tab in the UI where the panel will be located
    
    def draw(self, context): # method to called to define the layout of the panel
        layout = self.layout # get the layout object for the panel
        row = layout.row() # create a new row in the layout
        col = layout.column() # create a new column in the layout
        row.label(text="this is a panel") # add a label to the row
        row.operator("wm.save_mainfile") # add a button with a predefined operator in Blender
        
        selected_object = context.object # get the currently selected object in the scene

def register(): # function called by Blender when loading the script as 
    bpy.utils.register_class(MyPanel) # register the panel class with Blender to make it available in the UI, when reregistering use the same bl_idname, it unregisters the previous class first
def unregister(): # function called by Blender when unloading the script
    bpy.utils.unregister_class(bpy.types.MY_PANEL) # unregister the panel class when no longer needed using its unique bl_idname