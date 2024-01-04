from flet import *

class App(UserControl):
    def __init__(self,pg:Page):
        super().__init__()

        self.pg = pg
        self.init_helper()
    
    def init_helper(self):
        self.pg.add(
            Container(
                expand=True,
                bgcolor='blue',
                content=Row(
                    spacing=0, # define o espaço entre os dois containers
                    controls=[
                    Container(
                        bgcolor='brown',
                        width=80,
                    ), # sidebar
                    Container(
                        bgcolor='red',
                        expand=True
                    ), # main screen
                ]

                )
                
            )
        )

app(target=App)