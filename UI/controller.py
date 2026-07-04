import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        anno = self._view._txtAnno.value

        if anno == "":
            self._view.create_alert("Inserire un anno")
            return

        try:
            anno = int(anno)
        except ValueError:
            self._view.create_alert("L'anno deve essere un numero")
            return

        if anno < 1816 or anno > 2016:
            self._view.create_alert("Inserire un anno tra 1816 e 2016")
            return

        self._model.buildGraph(anno)
        self._view._txt_result.controls.clear()

        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view._txt_result.controls.append(ft.Text(""))
        self._view._txt_result.controls.append(
            ft.Text(f"Il grafo ha {self._model.getNumComponentiConnesse()} componenti connesse.")
        )
        self._view._txt_result.controls.append(ft.Text(""))
        self._view._txt_result.controls.append(ft.Text("Di seguito il dettaglio sui nodi:"))

        gradi = self._model.getGradi()

        for stato, grado in gradi:
            self._view._txt_result.controls.append(ft.Text(f"{stato.StateNme} -- {grado} vicini."))

        self.popolaDropdown()

        self._view.update_page()

    def popolaDropdown(self):
        self._view._dd_stato.options.clear()

        stati = self._model.getAllNodes()

        for stato in stati:
            self._view._dd_stato.options.append(
                ft.dropdown.Option(
                    key=str(stato.CCode),
                    text=stato.StateNme,
                    data=stato
                )
            )



    def handleRaggiungibili(self, e):
        pass
