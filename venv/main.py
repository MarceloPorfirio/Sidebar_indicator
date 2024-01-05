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
                        padding=padding.only(top=50,),
                        bgcolor='white',
                        width=80,
                        content=Row(
                            # spacing=0,
                            controls=[
                                Column(
                                    expand=True,
                                    controls=[
                                        Row(
                                            controls=[
                                                Container(
                                                    expand=True,
                                                    height=40,
                                                    content=Icon(
                                                        icons.CHAT_BUBBLE,
                                                        color='blue'
                                                    )
                                                )
                                            ]
                                        )
                                    ]
                                    
                                        
                                      
                                ),
                                Column(
                                    
                                    controls=[
                                        Container(bgcolor='red',width=3,height=40)
                                    ]
                                )
                            ]
                        )
                    ), # sidebar
                    Container(
                        bgcolor='green',
                        expand=True
                    ), # main screen
                ]

                )
                
            )
        )

app(target=App)