import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Приветствие"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    greeting_text = ft.Text("", size=20)
    name_field = ft.TextField(label="Введите ваше имя")
    
    def update_greeting(e):
        name = name_field.value
        if name:
            hour = datetime.now().hour
            if 6 <= hour < 12:
                greeting = "Доброе утро"
            elif 12 <= hour < 18:
                greeting = "Добрый день"
            elif 18 <= hour < 24:
                greeting = "Добрый вечер"
            else:
                greeting = "Доброй ночи"
            
            greeting_text.spans = [
                ft.TextSpan(text=f"{greeting}, "),
                ft.TextSpan(
                    text=name,
                    style=ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
                ),
                ft.TextSpan(text="!")
            ]
        page.update()
    
    name_field.on_change = update_greeting

    def clear_all(e):
        name_field.value = ""
        greeting_text.spans = []
        page.update()

    clear_button = ft.ElevatedButton(
        "Очистить всё",
        on_click=clear_all,
        bgcolor=ft.Colors.RED_400,
        color=ft.Colors.WHITE
    )
    
    page.add(
        ft.Column([
            name_field,
            greeting_text,
            ft.Divider(),
            clear_button
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)