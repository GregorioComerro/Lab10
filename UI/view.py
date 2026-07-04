import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        # page stuff
        self._page = page
        self._page.title = "TdP 2024 - Lab 10"
        self._page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self._page.theme_mode = ft.ThemeMode.LIGHT

        # controller
        self._controller = None

        # graphical elements
        self._title = None

        self._txtAnno = None
        self._dd_stato = None

        self._btnCalcola = None
        self._btnRaggiungibili = None

        self._txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text(
            "Country Borders",
            color="blue",
            size=28,
            weight=ft.FontWeight.W_400
        )

        self._page.controls.append(self._title)

        # campo anno
        self._txtAnno = ft.TextField(
            label="Anno",
            width=360,
            height=70
        )

        # bottone calcola confini
        self._btnCalcola = ft.ElevatedButton(
            text="Calcola Confini",
            width=240,
            height=42,
            on_click=self._controller.handleCalcola
        )

        row1 = ft.Row(
            controls=[
                self._txtAnno,
                self._btnCalcola
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12
        )

        self._page.controls.append(row1)

        # dropdown stato
        self._dd_stato = ft.Dropdown(
            label="Stato",
            width=360,
            height=70,
            options=[]
        )

        # bottone stati raggiungibili
        self._btnRaggiungibili = ft.ElevatedButton(
            text="Stati Raggiungibili",
            width=240,
            height=42,
            on_click=self._controller.handleRaggiungibili
        )

        row2 = ft.Row(
            controls=[
                self._dd_stato,
                self._btnRaggiungibili
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12
        )

        self._page.controls.append(row2)

        # spazio per stampare i risultati
        self._txt_result = ft.ListView(
            expand=1,
            spacing=10,
            padding=20,
            auto_scroll=False
        )

        self._page.controls.append(self._txt_result)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()