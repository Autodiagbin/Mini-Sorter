import dearpygui.dearpygui as dpg
import sorter
from pathlib import Path

min_h = 500
min_w = 500


dpg.create_context()

def proceed():
    dpg.hide_item("feedback")
    dpg.configure_item("modal_id", show=False)
    if dpg.get_value("path").strip():
        sorting = sorter.Sorter(dir=dpg.get_value("path"))
        if sorting.check_dir():
            sorting.sort()
            print("Sorted")
        else:
            dpg.set_value(item="feedback",value="Le chemin est invalide")
            dpg.show_item("feedback")
    else:
        dpg.set_value(item="feedback",value="Le chemin n'a pas été communiqué")
        dpg.show_item("feedback")

def set_directory(sender,app_data,user_data):
    dpg.set_value("path",value=app_data["file_path_name"])

def load_shortcuts():
    dpg.add_group(tag="shortcuts",horizontal=True)
    for shortcut in sorter.shortcuts:
        dpg.add_button(label=shortcut.name,callback=set_path,parent="shortcuts",tag=f"shortcut{shortcut.name}",user_data=shortcut)
    
def set_path(sender,user_data,app_data):
    dpg.set_value("path",value=app_data)

with dpg.window(label="Tutorial", width=min_h, height=min_w,min_size=(min_w,min_h),no_move=True):
    dpg.add_file_dialog(directory_selector=True, show=False, callback=set_directory, tag="file_dialog_id",height=min_h-35,width=min_w-15,modal=True)
    
    dpg.add_button(label="Choisir un dossier",callback=lambda: dpg.show_item("file_dialog_id"))
    dpg.add_input_text(label="Dossier", tag="path",enabled=False)
    dpg.add_button(label="Trier le dossier", callback=proceed,tag="run")
    dpg.add_text("The action has failed",color=(255,0,0),tag="feedback",show=False)

    with dpg.popup("run", mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modal_id"):
        dpg.add_text("Êtes-vous sûr de vouloir trier ce dossier par catégories ?")
        dpg.add_button(label="Oui", callback=proceed)
        dpg.add_button(label="Non, retourner au menu", callback=lambda: dpg.configure_item("modal_id", show=False))
    dpg.add_text("---------")
    load_shortcuts()

dpg.create_viewport(title='Custom Title', width=min_w, height=min_h,resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()