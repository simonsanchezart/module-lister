# Module Lister
<p align="center">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="Made with Love" />
    <img src="https://img.shields.io/badge/Made%20with-love-red" alt="MIT License"/>
</p>

Lists all the modules from python files in root and subfolders

```
usage: module-lister.py [-h] [--dump DUMP] [--ignore-zero IGNORE_ZERO]

options:
    -h, --help show this help message and exit
    --dump DUMP, -d DUMP Create a .txt in the root folder with the output
    --ignore-zero IGNORE_ZERO, -i IGNORE_ZERO Ommit python files with 0 modules
```

---

## Examples

`module-lister.py`

```
.\adjectives.py - (0) modules

.\countries.py - (0) modules

.\names.py - (0) modules

.\nouns.py - (0) modules

.\the-poet.py - (11) modules
        |__ adjectives
                |__ adjectives
        |__ countries
                |__ countries
        |__ names
                |__ names
        |__ neuralintents
                |__ GenericAssistant
        |__ nouns
                |__ nouns
        |__ random
                |__ choice, random
        |__ verbs
                |__ verbs
        |__ verses
                |__ verses
        |__ pyttsx3
        |__ speech_recognition
        |__ sys

.\verbs.py - (0) modules

.\verses.py - (0) modules

All base modules - (11)
        |__ adjectives
        |__ countries
        |__ names
        |__ neuralintents
        |__ nouns
        |__ pyttsx3
        |__ random
        |__ speech_recognition
        |__ sys
        |__ verbs
        |__ verses
```

---

`module-lister.py -i true`

```
.\addon\menu\main_menu.py - (3) modules
        |__ ...
                |__ bl_info
        |__ ..operator
                |__ mesh_operators, extra_operators
        |__ bpy

.\addon\menu\uv_menu.py - (3) modules
        |__ ...
                |__ bl_info
        |__ ..operator
                |__ extra_operators, uv_operators
        |__ bpy

.\addon\menu\__init__.py - (2) modules
        |__ .main_menu
                |__ MAG_MT_MAIN_MENU
        |__ .uv_menu
                |__ MAG_MT_UV_MENU

.\addon\operator\add_snapper.py - (6) modules
        |__ ..utility
                |__ addon as AD_U
                |__ events as EVNT_U
                |__ imports as IMP_U
                |__ materials as MAT_U
                |__ modifiers as MOD_U
        |__ bpy

.\addon\operator\beveler.py - (16) modules
        |__ ..utility
                |__ addon as AD_U
                |__ color as COL_U
                |__ draw as DRW_U
                |__ events as EVNT_U
                |__ imports as IMP_U
                |__ materials as MAT_U
                |__ mesh as MSH_U
                |__ modifiers as MOD_U
                |__ mouse as MOUS_U
                |__ rendering as RNDER_U
                |__ selections as SEL_U
        |__ collections
                |__ deque
        |__ bl_math
        |__ bmesh
        |__ bpy
        |__ bpy.types

.\addon\operator\bug_reporter.py - (4) modules
        |__ ..utility
                |__ addon as AD_U
                |__ events as EVNT_U
        |__ bpy
        |__ platform

.\addon\operator\display_non_planar.py - (6) modules
        |__ ..utility
                |__ addon as AD_U
                |__ events as EVNT_U
                |__ imports as IMP_U
                |__ materials as MAT_U
                |__ modifiers as MOD_U
        |__ bpy

.\addon\operator\edge_aligner.py - (13) modules
        |__ ..utility
                |__ addon as AD_U
                |__ color as COL_U
                |__ draw as DRW_U
                |__ events as EVNT_U
                |__ mesh as MSH_U
                |__ mouse as MOUS_U
                |__ selections as SEL_U
        |__ collections
                |__ deque, namedtuple
        |__ bmesh
        |__ bpy
        |__ bpy.types
        |__ math
        |__ mathutils

.\addon\operator\export_at_origin.py - (3) modules
        |__ ..utility
                |__ addon as AD_U
                |__ events as EVNT_U
        |__ bpy

.\addon\operator\mesh_inspector.py - (11) modules
        |__ ..utility
                |__ addon as AD_U
                |__ color as COL_U
                |__ draw as DRW_U
                |__ events as EVNT_U
                |__ mouse as MOUS_U
                |__ selections as SEL_U
        |__ collections
                |__ deque
        |__ bmesh
        |__ bpy
        |__ bpy.types
        |__ mathutils

.\addon\operator\mesh_name_to_object_name.py - (3) modules
        |__ ..utility
                |__ addon as AD_U
                |__ events as EVNT_U
        |__ bpy

.\addon\operator\non_uniform_to_collection.py - (3) modules
        |__ ..utility
                |__ addon as AD_U
                |__ events as EVNT_U
        |__ bpy

.\addon\operator\uv_stack.py - (4) modules
        |__ ..utility
                |__ addon as AD_U
        |__ bmesh
        |__ bpy
        |__ mathutils

.\addon\operator\__init__.py - (10) modules
        |__ .add_snapper
                |__ MAG_OT_ADD_SNAPPER
        |__ .beveler
                |__ MAG_OT_BEVELER
        |__ .bug_reporter
                |__ MAG_OT_BUG_REPORT
        |__ .display_non_planar
                |__ MAG_OT_DISPLAY_NON_PLANAR
        |__ .edge_aligner
                |__ MAG_OT_EDGE_ALIGNER
        |__ .export_at_origin
                |__ MAG_OT_EXPORT_AT_ORIGIN
        |__ .mesh_inspector
                |__ MAG_OT_MESH_INSPECTOR
        |__ .mesh_name_to_object_name
                |__ MAG_OT_MESH_NAME_TO_OBJECT_NAME
        |__ .non_uniform_to_collection
                |__ MAG_OT_NON_UNIFORM_TO_COLLECTION
        |__ .uv_stack
                |__ MAG_OT_STACK_UV

.\addon\property\preferences.py - (4) modules
        |__ ..operator
                |__ mesh_operators, uv_operators, extra_operators, operators
        |__ ..utility.addon
                |__ addon_name
        |__ bpy.props
                |__ BoolProperty
        |__ bpy

.\addon\property\__init__.py - (1) modules
        |__ .preferences
                |__ MAGNOLIA_PREFERENCES

.\addon\register\keymap.py - (1) modules
        |__ bpy

.\addon\utility\addon.py - (5) modules
        |__ ...import
                |__
        |__ pathlib
                |__ Path
        |__ bpy
        |__ bpy.types
        |__ os

.\addon\utility\color.py - (1) modules
        |__ enum
                |__ Enum

.\addon\utility\draw.py - (5) modules
        |__ .mouse
                |__ PADDING
        |__ gpu_extras.batch
                |__ batch_for_shader
        |__ blf
        |__ bpy
        |__ gpu

.\addon\utility\events.py - (3) modules
        |__ enum
                |__ Enum
        |__ bpy
        |__ bpy.types

.\addon\utility\imports.py - (4) modules
        |__ .
                |__ addon
        |__ bpy
        |__ bpy.types
        |__ os

.\addon\utility\materials.py - (3) modules
        |__ enum
                |__ Enum
        |__ bpy
        |__ bpy.types

.\addon\utility\mesh.py - (4) modules
        |__ .
                |__ events as eUtils
        |__ bmesh
        |__ bpy
        |__ bpy.types

.\addon\utility\modifiers.py - (2) modules
        |__ bpy
                |__ types as bt
        |__ enum
                |__ Enum

.\addon\utility\mouse.py - (1) modules
        |__ bpy.types

.\addon\utility\rendering.py - (3) modules
        |__ enum
                |__ Enum
        |__ numpy
                |__ true_divide
        |__ bpy

.\addon\utility\selections.py - (3) modules
        |__ enum
                |__ Enum
        |__ bpy
        |__ bpy.types

All base modules - (34)
        |__ add_snapper
        |__ beveler
        |__ bl_math
        |__ blf
        |__ bmesh
        |__ bpy
        |__ bpyprops
        |__ bpytypes
        |__ bug_reporter
        |__ collections
        |__ display_non_planar
        |__ edge_aligner
        |__ enum
        |__ export_at_origin
        |__ gpu
        |__ gpu_extrasbatch
        |__ import
        |__ main_menu
        |__ math
        |__ mathutils
        |__ mesh_inspector
        |__ mesh_name_to_object_name
        |__ mouse
        |__ non_uniform_to_collection
        |__ numpy
        |__ operator
        |__ os
        |__ pathlib
        |__ platform
        |__ preferences
        |__ utility
        |__ utilityaddon
        |__ uv_menu
        |__ uv_stack
```
