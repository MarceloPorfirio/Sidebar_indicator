import flet
from flet import *
def main (page:Page):
    page.theme_mode = 'light'


    txtsearch = TextField(
        label='Buscar Musica'
    )
    appBar = AppBar(
        title=Column([
            Text('A Musica',size=30),
            txtsearch,
        ])
    )
    page.add(
       appBar
        
    )
flet.app(target=main, assets_dir='mymusic',view=WEB_BROWSER)