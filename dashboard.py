import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Text("✅ Color test", color=ft.colors.RED),
        ft.Container(bgcolor=ft.colors.GREEN, width=100, height=100)
    )

ft.app(target=main)

