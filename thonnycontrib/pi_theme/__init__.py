import os.path
import tkinter
import re
from tkinter import ttk
from thonny.globals import get_workbench

MAIN_BACKGROUND="#ededed"

def theme_tweaker():
    style = ttk.Style()
    style.configure(".", background=MAIN_BACKGROUND)
    style.configure("Toolbutton", borderwidth=1)
    style.map("Toolbutton",
              relief=[("disabled", "flat"),("hover", "groove"),("!hover", "flat")],
              background=[("disabled",MAIN_BACKGROUND),("!hover", MAIN_BACKGROUND), ("hover", "#ffffff")])
    style.configure("Treeview.Heading", relief="flat", borderwidth=1,
                    background="#f0f0f0", foreground="#808080")
    style.map("TNotebook.Tab", background=[("!selected", "#d0d0d0"), ("selected", MAIN_BACKGROUND)])
    style.map("ButtonNotebook.Tab", background=[("!selected", "#d0d0d0"), ("selected", MAIN_BACKGROUND)])
    for line in open (os.path.join (os.path.expanduser ("~"), ".config/lxsession/LXDE-pi/desktop.conf"), "r"):
        if "sGtk/FontName" in line:
            fontname = re.search (r"=([^0-9]*) ([0-9]*)", line, re.M).group(1)
            fontsize = re.search (r"=([^0-9]*) ([0-9]*)", line, re.M).group(2)
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
    menfont=tkinter.font.nametofont("TkMenuFont")
    menfont.configure(family=fontname)
    menfont.configure(size=fontsize)
    menfont.configure(weight=fontweight)
    menfont.configure(slant=fontslant)
    deffont=tkinter.font.nametofont("TkDefaultFont")
    deffont.configure(family=fontname)
    deffont.configure(size=fontsize)
    deffont.configure(weight=fontweight)
    deffont.configure(slant=fontslant)
    headfont=tkinter.font.nametofont("TkHeadingFont")
    headfont.configure(family=fontname)
    headfont.configure(size=fontsize)
    headfont.configure(weight=fontweight)
    headfont.configure(slant=fontslant)


def _running_on_pixel():
    # TODO: find out
    return True


def load_early_plugin():
    if not _running_on_pixel():
        return
    for line in open (os.path.join (os.path.expanduser ("~"), ".config/lxsession/LXDE-pi/desktop.conf"), "r"):
        if "sGtk/ColorScheme" in line:
            bgr = re.search (r"selected_bg_color:#([0-9a-fA-F]*)", line, re.M).group(1)
            fgr = re.search (r"selected_fg_color:#([0-9a-fA-F]*)", line, re.M).group(1)
            bg = "#" + bgr[0:2] + bgr[4:6] + bgr[8:10]
            fg = "#" + fgr[0:2] + fgr[4:6] + fgr[8:10]

    sd = get_workbench().set_default
    # sto("window_icons", ["thonny.png"]) # not necessary, because it"s now included by default on Linux
    sd("theme.preferred_theme", "clam")
    sd("theme.main_background", MAIN_BACKGROUND)
    sd("theme.menubar_options", {
        "background" : MAIN_BACKGROUND,
        "relief" : "flat",
        "activebackground" : "#ffffff",
        "activeborderwidth" : 0,
        })
    sd("theme.menu_options", {
        "background" : "#ffffff",
        "relief" : "flat",
        "borderwidth" : 1,
        "activeborderwidth" : 0,
        "activebackground" : bg,
        "activeforeground" : fg,
        })
    sd("theme.icons_in_menus", False)
    sd("theme.shortcuts_in_tooltips", False)
    sd("theme.tooltip_options",  {
        "background" : "#808080",
        "foreground" : "#ffffff",
        "borderwidth" : 0,
        "padx" : 10,
        "pady" : 10
        })

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
    for original in images:
        get_workbench().map_image(original, os.path.join(res_dir, images[original]))

    get_workbench().set_theme_tweaker(theme_tweaker)

