import bpy 
def delete_all(object):
    '''
    Main functionality
    '''
    mode = bpy.context.mode
    if mode == 'EDIT_MESH':
        mode = 'EDIT'
    bpy.ops.object.mode_set(mode='OBJECT')
    if hasattr(object, 'delete'):
        print('Coś tam działa')
        #object.delete()
    print(mode)
    bpy.ops.object.mode_set(mode=mode)




class BevelME(bpy.types.Operator):
    '''
    DESC
    '''
    bl_idname = "mesh.bevel_test"
    bl_label = "Bevel testo"
    bl_description = "B description"
    
    
    @classmethod
    def pool(self, context):
        '''
        Check if option visible
        '''
        if context.mode in ['EDIT_MESH', 'OBJECT']:
            return True
    
        return False
    
    def invoke(self, context, event):
        if context.object.select:
            return self.execute(context)
        else:
            self.report(type={"ERROR",}, message="Select object")
            return {'CANCELLED'}
    
    def execute(self, context):
        delete_all(bpy.ops.object)
        return {'FINISHED'}



    
