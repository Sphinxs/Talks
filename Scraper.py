# -*- coding: utf-8 -*-


from Tkinter import *

import requests as rq


def data ( site, param, houses ) :

    if ( not site.startswith ( 'http://' ) ):
        
	site = 'http://' + site

    html = rq.get ( site )

    html = html.text

    posi = html.index ( param ) + len ( param )

    return html [ posi : posi + houses ]


bitcoin = data ( 'dolarhoje.com/bitcoin/', 'id="nacional" value="', 6 )

blockch = data ( 'blockchain.info/address/1QAc9S5EmycqjzzWDc1yiWzr9jJLC8sLiY', '<span data-c="', 9 )


class aplication ( object ) :

    def __init__ ( self, root, btc, blk ) :

        self.fr = Frame ( root ).pack ()

        self.wd = Label ( self.fr, text = btc + ' Bitcoin', width = 25, height = 10, bg = 'grey16', fg = 'white' ).pack ( side = LEFT )

        self.dw = Label ( self.fr, text = blk + ' Block', width = 25, height = 10, bg = 'grey16', fg = 'white' ).pack ( side = RIGHT )


root = Tk ()


root.wm_title ( 'Bitcoin' )

aplication ( root, bitcoin, blockch )


root.mainloop ()
