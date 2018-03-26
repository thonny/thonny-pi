import os.path
import re
from thonny.globals import get_workbench

def pi():
    MAIN_BACKGROUND="#ededed"

    images = {
        "run.run_current_script.gif"    : "media-playback-start.png",
        "run.stop.gif"                  : "process-stop.png",
        "file.new_file.gif"             : "document-new.png",
        "file.open_file.gif"            : "document-open.png",
        "file.save_file.gif"            : "document-save.png",
        "tab_close.gif"                 : 'window-close.png',
        "tab_close_active.gif"          : "window-close-act.png",
        "run.debug_current_script.gif"  : "debug-run.png",
        "run.step_over.gif"             : "debug-step-over.png",
        "run.step_into.gif"             : "debug-step-into.png",
        "run.step_out.gif"              : "debug-step-out.png",
        "run.run_to_cursor.gif"         : "debug-run-cursor.png",
    }

    res_dir = os.path.join(os.path.dirname(__file__), "res")
    abs_images = {original : os.path.join(res_dir, images[original]) for original in images}
    
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
                "foreground" : "#808080"
            }
        },
        "TNotebook.Tab" : {
            "map" : {
                "background" : [("!selected", "#d0d0d0"), 
                                ("selected", MAIN_BACKGROUND)],
            }
        },
        "ButtonNotebook.Tab" : {
            "map" : {
                "background" : [("!selected", "#d0d0d0"), 
                                ("selected", MAIN_BACKGROUND)],
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
                #"activebackground" : bg, 
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
        "IMAGES" : {
            "configure" : abs_images
        },
    }
    
    # try to refine settings according to system configuration
    configuration_path = os.path.expanduser ("~/.config/lxsession/LXDE-pi/desktop.conf")
    if os.path.exists(configuration_path):
        with open(configuration_path) as fp:
            for line in fp:
                if "sGtk/FontName" in line:
                    fontname = re.search (r"=([^0-9]*) ([0-9]*)", line, re.M).group(1)  # @UndefinedVariable
                    fontsize = re.search (r"=([^0-9]*) ([0-9]*)", line, re.M).group(2)  # @UndefinedVariable
                    if re.search (r'\bBold\b', fontname):
                        fontweight = "bold"
                        fontname = fontname.replace (" Bold", "")
                    else:
                        fontweight = "normal"
                    if re.search (r'\bItalic\b', fontname):
                        fontslant = "italic"
                        fontname = fontname.replace (" Italic", "")
                    else:
                        fontslant = "roman"
                
                    fontspec = {"family" : fontname, "size" : fontsize,
                                "weight" : fontweight, "slant" : fontslant}
                    settings["TkDefaultFont"] = {"config" : fontspec}
                    settings["TkMenuFont"] =    {"config" : fontspec}
                    settings["TkHeadingFont"] = {"config" : fontspec}
                
                elif "sGtk/ColorScheme" in line:
                    bgr = re.search (r"selected_bg_color:#([0-9a-fA-F]*)", line, re.M).group(1)  # @UndefinedVariable
                    fgr = re.search (r"selected_fg_color:#([0-9a-fA-F]*)", line, re.M).group(1)  # @UndefinedVariable
                    settings["Menu"]["configure"]["activeforeground"] = "#" + fgr[0:2] + fgr[4:6] + fgr[8:10] 
                    settings["Menu"]["configure"]["activebackground"] = "#" + bgr[0:2] + bgr[4:6] + bgr[8:10] 
    
    
    return settings
    


def load_early_plugin():
    get_workbench().add_ui_theme("Raspberry Pi", "Enhanced Clam", pi)

