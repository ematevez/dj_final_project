#https://pyfpdf.readthedocs.io/en/latest/reference/ln/index.html
# https://pyfpdf.readthedocs.io/en/latest/ReferenceManual/index.html
# https://pyfpdf.readthedocs.io/en/latest/reference/cell/index.html

from fpdf import FPDF



class PDF(FPDF):

    def header(self):
        #self.image('djangochat/Auxiliar/PDF-Creator/logo.png', x = 10, y = 10, w = 30, h = 30)

        self.set_font('Arial', '', 15)

        tcol_set(self, 'blue')
        tfont_size(self,45)
        tfont(self,'B')
        self.cell(w = 1, h = 20, txt = '      ', border = 0, ln=1,
                align = 'C', fill = 0)

        tfont_size(self,10)
        tcol_set(self, 'black')
        tfont(self,'I')
        self.cell(w = 0, h = 10, txt = 'Unidad de Apoyo a Investigaciones Hidrográficas y Oceanográficas', border = 0, ln=2,
                align = 'R', fill = 0)

        self.ln(5)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-20)

        # Arial italic 8
        self.set_font('Arial', 'I', 12)

        # Page number
        self.cell(w = 0, h = 10, txt =  'Pagina ' + str(self.page_no()) + '/{nb}',
                border = 0,
                align = 'C', fill = 0)   

def diccionario_colores(color): 
        colores = {
                'black' : (0,0,0), 
                'white' : (255,255,255),
                'green' : (96,218,117),
                'blue' : (96,181,218),
                'red': (239,71,71),
                'rose':(214,74,236),
                'gray':(103,103,103),
                'gray2':(233,233,233),
        }

        return colores[color]

def dcol_set(hoja, color):
        cr, cg, cb = diccionario_colores(color)
        hoja.set_draw_color(r= cr, g = cg, b= cb)

def bcol_set(hoja,color):
        cr, cg, cb = diccionario_colores(color)
        hoja.set_fill_color(r= cr, g = cg, b= cb)

def tcol_set(hoja, color):
        cr, cg, cb = diccionario_colores(color)
        hoja.set_text_color(r= cr, g = cg, b= cb)

def tfont_size(hoja, size):
        hoja.set_font_size(size)

def tfont(hoja, estilo, fuente='Arial'):
        hoja.set_font(fuente, style=estilo)

