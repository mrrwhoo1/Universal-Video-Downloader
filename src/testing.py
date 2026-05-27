import flet as ft

def main(page: ft.Page):
    # 1. Define the Dropdown control
    dd = ft.Dropdown(
        width=200,
        label="Select a Color",
        hint_text="Choose your favorite color",
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )

    # 2. Add it to the page
    page.add(dd)

ft.app(target=main)
