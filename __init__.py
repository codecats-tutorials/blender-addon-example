import bpy 
from bpy.utils import register_module, unregister_module

from .bevel import *
    
bl_info = {
    "name": "BevelME",
    "author": "ssstrz",
    "version": (1, 0, 0),
    "blender": (2, 7, 1),
    "api": 36147,
    "location": "",
    "category": "Mesh",
    "description": "Delete selected object - test plugin",
    "warning": "",
    "wiki_url": "",
    "tracker_url": ""
}
def menu_draw(self, context):
    self.layout.operator_context = 'INVOKE_REGION_WIN'
    self.layout.operator(BevelME.bl_idname, 'BevelME')
    
def register():
    register_module(__name__)
    bpy.types.VIEW3D_MT_edit_mesh_specials.prepend(menu_draw)
    
def unregister():
    bpy.types.VIEW3D_MT_edit_mesh_specials.remove(menu_draw)
    unregister_module(__name__)
