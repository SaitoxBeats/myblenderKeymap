keyconfig_version = (4, 4, 30)
keyconfig_data = \
[("3D View",
  {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
  {"items":
   [("object.drop_it", {"type": 'V', "value": 'PRESS'}, None),
    ("object.keyframe_object_data", {"type": 'PAGE_DOWN', "value": 'PRESS', "ctrl": True}, None),
    ("object.keyframe_object_data", {"type": 'PAGE_UP', "value": 'PRESS', "ctrl": True}, None),
    ("object.cloudrig_metarig_toggle", {"type": 'T', "value": 'PRESS', "shift": True}, None),
    ("pose.cloudrig_generate", {"type": 'R', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.cursor3d", {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True}, None),
    ("transform.translate",
     {"type": 'RIGHTMOUSE', "value": 'CLICK_DRAG', "shift": True},
     {"properties":
      [("cursor_transform", True),
       ("release_confirm", True),
       ],
      },
     ),
    ("view3d.localview", {"type": 'NUMPAD_SLASH', "value": 'PRESS'}, None),
    ("view3d.localview", {"type": 'SLASH', "value": 'PRESS'}, None),
    ("view3d.localview", {"type": 'MOUSESMARTZOOM', "value": 'ANY'}, None),
    ("view3d.localview_remove_from", {"type": 'NUMPAD_SLASH', "value": 'PRESS', "alt": True}, None),
    ("view3d.localview_remove_from", {"type": 'SLASH', "value": 'PRESS', "alt": True}, None),
    ("view3d.rotate", {"type": 'MOUSEROTATE', "value": 'ANY'}, None),
    ("view3d.rotate", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
    ("view3d.move", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None),
    ("view3d.rotate", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
    ("view3d.move", {"type": 'TRACKPADPAN', "value": 'ANY', "shift": True}, None),
    ("view3d.zoom", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.dolly", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("view3d.view_selected",
     {"type": 'NUMPAD_PERIOD', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_all_regions", True),
       ],
      },
     ),
    ("view3d.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
    ("view3d.smoothview", {"type": 'TIMER1', "value": 'ANY', "any": True}, None),
    ("view3d.zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
    ("view3d.zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
    ("view3d.zoom",
     {"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'EQUAL', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'MINUS', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'WHEELINMOUSE', "value": 'PRESS'},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'WHEELOUTMOUSE', "value": 'PRESS'},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'EQUAL', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'MINUS', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.view_center_camera", {"type": 'HOME', "value": 'PRESS'}, None),
    ("view3d.view_center_lock", {"type": 'HOME', "value": 'PRESS'}, None),
    ("view3d.view_all",
     {"type": 'HOME', "value": 'PRESS'},
     {"properties":
      [("center", False),
       ],
      },
     ),
    ("view3d.view_all",
     {"type": 'HOME', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_all_regions", True),
       ("center", False),
       ],
      },
     ),
    ("view3d.view_all",
     {"type": 'C', "value": 'PRESS', "shift": True},
     {"properties":
      [("center", True),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'BACK_SLASH', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_view_pie'),
       ],
      },
     ),
    ("view3d.navigate", {"type": 'BACK_SLASH', "value": 'PRESS', "shift": True}, None),
    ("view3d.view_camera", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS'},
     {"properties":
      [("type", 'FRONT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_2', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITDOWN'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_4', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITLEFT'),
       ],
      },
     ),
    ("view3d.view_persportho", {"type": 'NUMPAD_5', "value": 'PRESS'}, None),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_6', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITRIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS'},
     {"properties":
      [("type", 'TOP'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_8', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITUP'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'BACK'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'BOTTOM'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_2', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANDOWN'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_4', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANLEFT'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_6', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANRIGHT'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_8', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANUP'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NUMPAD_4', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NUMPAD_6', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_9', "value": 'PRESS'},
     {"properties":
      [("angle", 3.1415927),
       ("type", 'ORBITRIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'FRONT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'TOP'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'BACK'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'LEFT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'BOTTOM'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'MIDDLEMOUSE', "value": 'CLICK_DRAG', "alt": True, "direction": 'NORTH'},
     {"properties":
      [("type", 'TOP'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'MIDDLEMOUSE', "value": 'CLICK_DRAG', "alt": True, "direction": 'SOUTH'},
     {"properties":
      [("type", 'BOTTOM'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'MIDDLEMOUSE', "value": 'CLICK_DRAG', "alt": True, "direction": 'EAST'},
     {"properties":
      [("type", 'RIGHT'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'MIDDLEMOUSE', "value": 'CLICK_DRAG', "alt": True, "direction": 'WEST'},
     {"properties":
      [("type", 'LEFT'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_center_pick", {"type": 'MIDDLEMOUSE', "value": 'CLICK', "alt": True}, None),
    ("view3d.ndof_orbit_zoom", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
    ("view3d.ndof_orbit", {"type": 'NDOF_MOTION', "value": 'ANY', "ctrl": True}, None),
    ("view3d.ndof_pan", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True}, None),
    ("view3d.ndof_all", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True, "ctrl": True}, None),
    ("view3d.view_selected", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
    ("view3d.view_roll",
     {"type": 'NDOF_BUTTON_ROLL_CW', "value": 'PRESS'},
     {"properties":
      [("angle", 1.5707964),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NDOF_BUTTON_ROLL_CCW', "value": 'PRESS'},
     {"properties":
      [("angle", -1.5707964),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS'},
     {"properties":
      [("type", 'FRONT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_BACK', "value": 'PRESS'},
     {"properties":
      [("type", 'BACK'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_LEFT', "value": 'PRESS'},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS'},
     {"properties":
      [("type", 'TOP'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_BOTTOM', "value": 'PRESS'},
     {"properties":
      [("type", 'BOTTOM'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'FRONT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'TOP'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK'},
     {"properties":
      [("deselect_all", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True},
     {"properties":
      [("toggle", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True},
     {"properties":
      [("center", True),
       ("object", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "alt": True},
     {"properties":
      [("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
     {"properties":
      [("toggle", True),
       ("center", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True, "alt": True},
     {"properties":
      [("center", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "alt": True},
     {"properties":
      [("toggle", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True, "alt": True},
     {"properties":
      [("toggle", True),
       ("center", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select_box", {"type": 'B', "value": 'PRESS'}, None),
    ("view3d.select_lasso",
     {"type": 'RIGHTMOUSE', "value": 'CLICK_DRAG', "ctrl": True},
     {"properties":
      [("mode", 'ADD'),
       ],
      },
     ),
    ("view3d.select_lasso",
     {"type": 'RIGHTMOUSE', "value": 'CLICK_DRAG', "shift": True, "ctrl": True},
     {"properties":
      [("mode", 'SUB'),
       ],
      },
     ),
    ("view3d.select_circle", {"type": 'C', "value": 'PRESS'}, None),
    ("view3d.clip_border", {"type": 'B', "value": 'PRESS', "alt": True}, None),
    ("view3d.zoom_border", {"type": 'B', "value": 'PRESS', "shift": True}, None),
    ("view3d.render_border", {"type": 'B', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.clear_render_border", {"type": 'B', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.camera_to_view", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.object_as_camera", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.copybuffer", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.pastebuffer", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
    ("wm.context_toggle",
     {"type": 'TAB', "value": 'PRESS', "shift": True},
     {"properties":
      [("data_path", 'tool_settings.use_snap'),
       ],
      },
     ),
    ("wm.call_panel",
     {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_PT_snapping'),
       ("keep_open", True),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_snap_pie'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'ACCENT_GRAVE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path", 'space_data.show_gizmo'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'PERIOD', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_pivot_pie'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'COMMA', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_orientations_pie'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'Z', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_shading_pie'),
       ],
      },
     ),
    ("view3d.toggle_shading",
     {"type": 'Z', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'WIREFRAME'),
       ],
      },
     ),
    ("view3d.toggle_xray", {"type": 'Z', "value": 'PRESS', "alt": True}, None),
    ("wm.context_toggle",
     {"type": 'Z', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("data_path", 'space_data.overlay.show_overlays'),
       ],
      },
     ),
    ("wm.tool_set_by_id",
     {"type": 'W', "value": 'PRESS'},
     {"properties":
      [("name", 'builtin.select_box'),
       ("cycle", True),
       ],
      },
     ),
    ],
   },
  ),
 ]


if __name__ == "__main__":
    # Only add keywords that are supported.
    from bpy.app import version as blender_version
    keywords = {}
    if blender_version >= (2, 92, 0):
        keywords["keyconfig_version"] = keyconfig_version
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data
    keyconfig_import_from_data(
        os.path.splitext(os.path.basename(__file__))[0],
        keyconfig_data,
        **keywords,
    )
