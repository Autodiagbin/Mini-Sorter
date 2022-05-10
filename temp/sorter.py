import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Tutorial"):
    dpg.add_text("Left Click Me")

    # check out simple module for details
    with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modal_id"):
        dpg.add_text("Êtes-vous sûr de vouloir trier ce dossier par catégories ?")
        dpg.add_button(label="Oui", callback=lambda: dpg.configure_item("modal_id", show=False))
        dpg.add_button(label="Non, retourner au menu", callback=lambda: dpg.configure_item("modal_id", show=False))

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()