import os
import re
from thonny import get_workbench
from thonny.ui_utils import scale

CONFIGURATION_PATH = os.path.join (os.path.expanduser ("~"), ".config/lxsession", os.environ['DESKTOP_SESSION'], "desktop.conf")
GLOBAL_CONFIGURATION_PATH = os.path.join ("/etc/xdg/lxsession", os.environ['DESKTOP_SESSION'], "desktop.conf")

def pix():
    MAIN_BACKGROUND="#ededed"

    
    res_dir = os.path.join(os.path.dirname(__file__), "res")
    scrollbar_button_settings = {}
    for direction, element_name in [
        ("up", 'Vertical.Scrollbar.uparrow'), 
        ("down", 'Vertical.Scrollbar.downarrow'), 
        ("left", 'Horizontal.Scrollbar.leftarrow'),
        ("right", 'Horizontal.Scrollbar.rightarrow')]:
        # load the image
        img_name = "scrollbar-button-" + direction
        for suffix in ["", "-insens"]:
            get_workbench().get_image(os.path.join(res_dir, img_name + suffix + ".png"),
                                      img_name + suffix)
        
        scrollbar_button_settings[element_name] = {
            "element create" : (
                "image", img_name,
                ("!disabled", img_name),
                ("disabled", img_name + "-insens"),
            )
        }
    
    settings = {
        "." : {
            "configure" : {
                "background" : MAIN_BACKGROUND 
            }
        },
        "Toolbutton" : {
            "configure" : {
                "borderwidth" : 1
            },
            "map" : {
                "relief" : [("disabled", "flat"),
                            ("hover", "groove"),
                            ("!hover", "flat")],
                
                "background" : [("disabled",MAIN_BACKGROUND),
                                ("!hover", MAIN_BACKGROUND),
                                ("hover", "#ffffff")]
            }
        },
        "Treeview.Heading" : {
            "configure" : {
                "background" : "#f0f0f0",
                "foreground" : "#808080",
                "relief" : "flat",
                "borderwidth" : 1,
            },
            "map" : {
                "foreground" : [("active", "black")]
            }
        },
        "TNotebook.Tab" : {
            "map" : {
                "background" : [("!selected", "#d0d0d0"), 
                                ("selected", MAIN_BACKGROUND)],
            }
        },
        "ButtonNotebook.TNotebook.Tab" : {
            "map" : {
                "background" : [("!selected", "#d0d0d0"), 
                                ("selected", MAIN_BACKGROUND)],
                "padding" : [("selected", [scale(4),scale(2),scale(4),scale(3)]),
                             ("!selected", [scale(4),scale(2),scale(4),scale(3)])]
            }
        },
        "TScrollbar" : {
            "configure" : {
                "gripcount" : 0,
                "borderwidth" : 0,
                "padding" : scale(1),
                "relief" : "solid",
                "background" : "#9e9e9e",
                "darkcolor" : "#d6d6d6",
                "lightcolor" : "#d6d6d6",
                "bordercolor" : "#d6d6d6",
                "troughcolor" : "#d6d6d6",
                "arrowsize" : scale(1),
                "arrowcolor" : "gray",
            },
            "map" : {
                "background" : [],
                "darkcolor" : [],
                "lightcolor" : [],
            }
        },
        
        # Padding allows twaking thumb width
        "Vertical.TScrollbar" : {
            "layout" : [
                ('Vertical.Scrollbar.trough', {'sticky': 'ns', 'children': [
                    ('Vertical.Scrollbar.uparrow', {'side': 'top', 'sticky': ''}), 
                    ('Vertical.Scrollbar.downarrow', {'side': 'bottom', 'sticky': ''}), 
                    ("Vertical.Scrollbar.padding", {'sticky' : 'nswe', 'children' : [
                        ('Vertical.Scrollbar.thumb', {'expand' : 1, 'sticky': 'nswe'}),
                    ]}),
                ]})
            ]
        },
        
        "Horizontal.TScrollbar" : {
            "layout" : [
                ('Horizontal.Scrollbar.trough', {'sticky': 'we', 'children': [
                    ('Horizontal.Scrollbar.leftarrow', {'side': 'left', 'sticky': ''}), 
                    ('Horizontal.Scrollbar.rightarrow', {'side': 'right', 'sticky': ''}), 
                    ("Horizontal.Scrollbar.padding", {'sticky' : 'nswe', 'children' : [
                        ('Horizontal.Scrollbar.thumb', {'expand': 1, 'sticky': 'nswe'})
                    ]}),
                ]})
            ],
            "map" : {
                # Make disabled Hor Scrollbar invisible
                "background" : [("disabled", "#d6d6d6")],
                "troughcolor" : [("disabled", "#d6d6d6")],
                "bordercolor" : [("disabled", "#d6d6d6")],
                "darkcolor" : [("disabled", "#d6d6d6")],
                "lightcolor" : [("disabled", "#d6d6d6")],
            }
        },
        
        "TCombobox" : {
            "configure" : {
                "arrowsize" : scale(10),
            }
        },

        "Menubar" : {
            "configure" : {
                "background" : MAIN_BACKGROUND,
                "relief" : "flat",
                "activebackground" : "#ffffff",
                "activeborderwidth" : 0,
            }
        },
        "Menu" : {
            "configure" : {
                "background" : "#ffffff",
                "relief" : "flat",
                "borderwidth" : 1,
                "activeborderwidth" : 0,
                #"activebackground" : bg, # updated below
                #"activeforeground" : fg, 
            }
        },
        "Tooltip" : {
            "configure" : {
                "background" : "#808080",
                "foreground" : "#ffffff",
                "borderwidth" : 0,
                "padx" : 10,
                "pady" : 10
            }
        },
        "OPTIONS" : {
            "configure" : {
                "icons_in_menus" : False,
                "shortcuts_in_tooltips" : False
            }
        },
    }
    
    settings.update(scrollbar_button_settings)
    
    # try to refine settings according to system configuration
    if os.path.exists(GLOBAL_CONFIGURATION_PATH):
        with open(GLOBAL_CONFIGURATION_PATH) as fp:
            for line in fp:
                if "sGtk/ColorScheme" in line:
                    bgr = re.search (r"selected_bg_color:#([0-9a-fA-F]*)", line, re.M).group(1)  # @UndefinedVariable
                    fgr = re.search (r"selected_fg_color:#([0-9a-fA-F]*)", line, re.M).group(1)  # @UndefinedVariable
                    settings["Menu"]["configure"]["activeforeground"] = "#" + fgr[0:2] + fgr[4:6] + fgr[8:10] 
                    settings["Menu"]["configure"]["activebackground"] = "#" + bgr[0:2] + bgr[4:6] + bgr[8:10]
    if os.path.exists(CONFIGURATION_PATH):
        with open(CONFIGURATION_PATH) as fp:
            for line in fp:
                if "sGtk/ColorScheme" in line:
                    bgr = re.search (r"selected_bg_color:#([0-9a-fA-F]*)", line, re.M).group(1)  # @UndefinedVariable
                    fgr = re.search (r"selected_fg_color:#([0-9a-fA-F]*)", line, re.M).group(1)  # @UndefinedVariable
                    settings["Menu"]["configure"]["activeforeground"] = "#" + fgr[0:2] + fgr[4:6] + fgr[8:10] 
                    settings["Menu"]["configure"]["activebackground"] = "#" + bgr[0:2] + bgr[4:6] + bgr[8:10]
    
    return settings 

def update_fonts():
    if os.path.exists(GLOBAL_CONFIGURATION_PATH):
        with open(GLOBAL_CONFIGURATION_PATH) as fp:
            for line in fp:
                if "sGtk/FontName" in line:
                    fontname = re.search(r"=([^0-9]*) ([0-9]*)", line, re.M).group(1)  # @UndefinedVariable
                    fontsize = re.search(r"=([^0-9]*) ([0-9]*)", line, re.M).group(2)  # @UndefinedVariable
                    if re.search(r'\bBold\b', fontname):
                        fontweight = "bold"
                        fontname = fontname.replace(" Bold", "")
                    else:
                        fontweight = "normal"
                    if re.search(r'\bItalic\b', fontname):
                        fontslant = "italic"
                        fontname = fontname.replace(" Italic", "")
                    else:
                        fontslant = "roman"
                    
                    from tkinter import font
                    for name in ["TkDefaultFont", "TkMenuFont", "TkHeadingFont"]:
                        font.nametofont(name).configure(family=fontname, size=fontsize,
                                                        weight=fontweight, slant=fontslant)
    
    if os.path.exists(CONFIGURATION_PATH):
        with open(CONFIGURATION_PATH) as fp:
            for line in fp:
                if "sGtk/FontName" in line:
                    fontname = re.search(r"=([^0-9]*) ([0-9]*)", line, re.M).group(1)  # @UndefinedVariable
                    fontsize = re.search(r"=([^0-9]*) ([0-9]*)", line, re.M).group(2)  # @UndefinedVariable
                    if re.search(r'\bBold\b', fontname):
                        fontweight = "bold"
                        fontname = fontname.replace(" Bold", "")
                    else:
                        fontweight = "normal"
                    if re.search(r'\bItalic\b', fontname):
                        fontslant = "italic"
                        fontname = fontname.replace(" Italic", "")
                    else:
                        fontslant = "roman"
                    
                    from tkinter import font
                    for name in ["TkDefaultFont", "TkMenuFont", "TkHeadingFont"]:
                        font.nametofont(name).configure(family=fontname, size=fontsize,
                                                        weight=fontweight, slant=fontslant)
                    
def load_plugin():
    """Note that fonts and some images are set globally, 
    ie. all themes will inherit these"""
    update_fonts()
    
    # set custom images
    images = {
        "run-current-script"   : "media-playback-start.png",
        "stop"                 : "process-stop.png",
        "new-file"             : "document-new.png",
        "open-file"            : "document-open.png",
        "save-file"            : "document-save.png",
        "debug-current-script" : "debug-run.png",
        "step-over"            : "debug-step-over.png",
        "step-into"            : "debug-step-into.png",
        "step-out"             : "debug-step-out.png",
        "run-to-cursor"        : "debug-run-cursor.png",
        "tab-close"            : 'window-close.png',
        "tab-close-active"     : "window-close-act.png",
        "resume"               : "resume.png",
    }

    res_dir = os.path.join(os.path.dirname(__file__), "res")
    global_image_map = {}
    theme_image_map = {}
    for image in images:
        if image in ["tab-close", "tab-close-active"]:
            target = theme_image_map
        else:
            target = global_image_map
        
        target[image] = os.path.join(res_dir, images[image])
    
    get_workbench().update_image_mapping(global_image_map)
    get_workbench().add_ui_theme("Raspberry Pi", "Enhanced Clam", pix, theme_image_map)
    get_workbench().set_default("view.ui_theme", "Raspberry Pi")

