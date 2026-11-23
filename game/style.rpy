
#this part of the project was the only part of the project that used AI (:

init offset = -2

define clinic_white  = "#f4fbfa"
define clinic_mint   = "#cfeee9"
define clinic_teal   = "#3fb8af"
define clinic_navy   = "#1d3a44"
define clinic_grey   = "#8aa3a8"
define evil_red      = "#b3122e"
define evil_green    = "#7dff9a"
define evil_dark     = "#0d1a1c"

define gui.accent_color         = clinic_teal
define gui.idle_color           = clinic_grey
define gui.idle_small_color     = clinic_grey
define gui.hover_color          = evil_red
define gui.selected_color       = clinic_teal
define gui.insensitive_color    = "#8aa3a888"
define gui.muted_color          = "#9fd6d0"
define gui.hover_muted_color    = "#c9ece8"
define gui.text_color           = clinic_navy
define gui.interface_text_color = clinic_navy

define gui.text_font           = "DejaVuSans.ttf"
define gui.name_text_font      = "DejaVuSans-Bold.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"
define gui.text_size           = 26
define gui.name_text_size      = 50
define gui.interface_text_size = 26
define gui.label_text_size     = 28
define gui.title_text_size     = 64

define gui.textbox_height  = 220
define gui.textbox_yalign  = 1.0
define gui.name_xpos       = 260
define gui.name_ypos       = -20
define gui.dialogue_xpos   = 260
define gui.dialogue_ypos   = 60
define gui.dialogue_width  = 1400

init offset = 0

style window:
    background Frame(Composite((1920, 220),
        (0, 0), Solid("#f4fbfaee"),
        (0, 0), Solid(clinic_teal, xysize=(1920, 4))), 0, 0)

style namebox:
    background Solid(clinic_teal)
    xpadding 28
    ypadding 6

style say_label:
    color "#ffffff"
    bold True

style say_dialogue:
    color clinic_navy
    line_spacing 4

style choice_button:
    background Solid("#f4fbfacc")
    hover_background Solid(evil_dark)
    xminimum 900
    xpadding 40
    ypadding 14

style choice_button_text:
    color clinic_navy
    hover_color evil_green
    xalign 0.5

style main_menu_frame:
    background Solid(clinic_mint)

style game_menu_outer_frame:
    background Solid(clinic_white)

style navigation_button_text:
    color clinic_navy
    hover_color evil_red
    selected_color clinic_teal

style main_menu_title:
    color clinic_navy
    size 72

style main_menu_version:
    color clinic_grey

style bar:
    left_bar Solid(clinic_teal)
    right_bar Solid(clinic_mint)
    ysize 20

style slider:
    left_bar Solid(clinic_teal)
    right_bar Solid(clinic_mint)
    thumb Solid(clinic_navy, xysize=(20, 28))
    ysize 28

init python:
    def gui_corrupt():
        style.window.background = Frame(Composite((1920, 220),
            (0, 0), Solid("#0d1a1cf2"),
            (0, 0), Solid("#b3122e", xysize=(1920, 4))), 0, 0)
        style.say_dialogue.color = "#7dff9a"
        style.say_label.color = "#ffffff"
        style.namebox.background = Solid("#b3122e")
        style.choice_button_text.color = "#7dff9a"
        style.choice_button_text.hover_color = "#b3122e"
        style.choice_button.background = Solid("#0d1a1ccc")
        style.choice_button.hover_background = Solid("#f4fbfa")
        renpy.style.rebuild()

define intern = Character("Intern", who_color=clinic_teal)
define doctor = Character("Dr. Vale", who_color=evil_red)
define nurse  = Character("Nurse", who_color=clinic_grey)