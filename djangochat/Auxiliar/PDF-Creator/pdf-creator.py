#https://pyfpdf.readthedocs.io/en/latest/reference/ln/index.html
# https://pyfpdf.readthedocs.io/en/latest/ReferenceManual/index.html
# https://pyfpdf.readthedocs.io/en/latest/reference/cell/index.html

from fpdf import FPDF

from referencias import *

class PDF(FPDF):

    def header(self):
        self.image('djangochat/Auxiliar/PDF-Creator/logo.png', x = 10, y = 10, w = 30, h = 30)

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



lista_datos = (
    (1, 'Carlos', 'carlos@gmail.com', '2020-02-25'),
    (2, 'Jose', 'jose@gmail.com', '2019-03-12'),
    (3, 'Marcos', 'marcos@gmail.com', '2018-01-31'),
    (4, 'Luz', 'luz@gmail.com', '2017-02-15'),
    (5, 'Elmer', 'elmer@gmail.com', '2016-11-23'),
)#*8


pdf = PDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.alias_nb_pages()

pdf.add_page()

# TEXTO
pdf.set_font('Arial', '', 15) 


# 1er encabezado ----
# tfont_size(pdf,15)
# tcol_set(pdf, 'black')
# tfont(pdf,'B')
# pdf.cell(w = 0, h = 10, txt = 'BUQUE OCEANOGRAFICO A.R.A. “PUERTO DESEADO”', border = 0, ln=2, align = 'R', fill = 0)
        
bcol_set(pdf, 'white')
tfont_size(pdf,10)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 8, txt = 'BUQUE OCEANOGRÁFICO A.R.A. "PUERTO DESEADO"', border = 0,
        align = 'C', fill = 0)
pdf.multi_cell(w = 0, h = 8, txt = 'FORMULARIO PEDIDO DE APROVISIONAMIENTOS/SERVICIOS', border = 0,
        align = 'C', fill = 0)
tfont(pdf,'')

h_sep = 8
pdf.ln(3)
tfont_size(pdf,12)

# fila 1 --
tcol_set(pdf, 'gray')
pdf.set_font('', 'U')
pdf.cell(w = 15, h = h_sep, txt = 'FECHA:', border = 0, 
        align = 'R', fill = 0)

tcol_set(pdf, 'black')    
pdf.set_font('', '')     
pdf.cell(w = 15, h = h_sep, txt = '25 DE MAYO 2023', border = 0,
        align = 'L', fill = 0)

# fila 2 --
pdf.ln(h = '')

tcol_set(pdf, 'gray')
pdf.set_font('', 'U')
pdf.cell(w = 21, h = h_sep, txt = 'CAMPAÑA:', border = 0, 
        align = 'R', fill = 0)

tcol_set(pdf, 'black') 
pdf.multi_cell(w = 0, h = h_sep, txt = '', border = 0,
        align = 'L', fill = 0)

# fila 3 --
tcol_set(pdf, 'gray')
pdf.set_font('', 'U')
pdf.cell(w = 40, h = h_sep, txt = 'FECHA REQUERIDA', border = 0, 
        align = 'R', fill = 0)

tcol_set(pdf, 'black')
pdf.set_font('', '')
pdf.cell(w = 21, h = h_sep, txt = '', border = 0,
        align = 'L', fill = 0)

# fila 4 --
pdf.ln(h = '')
tcol_set(pdf, 'gray')
pdf.set_font('', 'U')
pdf.cell(w = 16, h = h_sep, txt = 'RUBRO:', border = 0, 
        align = 'R', fill = 0)

tcol_set(pdf, 'black')
pdf.set_font('', '')
pdf.multi_cell(w = 0, h = h_sep, txt = '', border = 0,
        align = 'L', fill = 0)

# fila 5 --
tcol_set(pdf, 'gray')
pdf.set_font('', 'U')
pdf.cell(w = 23, h = h_sep, txt = 'PEDIDO N°:', border = 0, 
        align = 'R', fill = 0)

tcol_set(pdf, 'black')
pdf.set_font('', '')
pdf.cell(w = 45, h = h_sep, txt = '', border = 0,
        align = 'L', fill = 0)

# fila 6 --
pdf.ln(h = '')
tcol_set(pdf, 'gray')
pdf.set_font('', 'U')
pdf.cell(w = 45, h = h_sep, txt = 'NIVEL DE PRIORIDAD:', border = 0, 
        align = 'R', fill = 0)

tcol_set(pdf, 'black')
pdf.set_font('', '')
pdf.cell(w = 10, h = h_sep, txt = 'A(*)', border = 1,
        align = 'R', fill = 1)
pdf.cell(w = 10, h = h_sep, txt = 'A(*)', border = 1,
        align = '', fill = 1)

#--------------------------------------------------



pdf.ln(15)
# tabla ----

bcol_set(pdf, 'green')
tfont_size(pdf,15)
tfont(pdf,'B')
pdf.cell(w = 0, h = 15, txt = 'Delegados', border = 0,ln = 2, align = 'C', fill = 1)
tfont(pdf,'')

tfont_size(pdf,13)
bcol_set(pdf, 'blue')

pdf.cell(w = 20, h = 10, txt = 'ID', border = 0, align = 'C', fill = 1)
pdf.cell(w = 40, h = 10, txt = 'Nombre', border = 0, align = 'C', fill = 1)
pdf.cell(w = 70, h = 10, txt = 'Correo', border = 0, align = 'C', fill = 1)
pdf.multi_cell(w = 0, h = 10, txt = 'Fecha contrato', border = 0, align = 'C',
             fill = 1)


tfont_size(pdf,12)
dcol_set(pdf, 'blue')
tcol_set(pdf, 'gray')
# pdf.rect(x= 10, y= 60, w= 190, h= 53)
c = 0
for datos in lista_datos:

    c+=1
    if(c%2==0):bcol_set(pdf, 'gray2')
    else:bcol_set(pdf, 'white')

    pdf.cell(w = 20, h = 10, txt = str(datos[0]), border = 'TBL', align = 'C', fill = 1)
    pdf.cell(w = 40, h = 10, txt = datos[1], border = 'TB', align = 'C', fill = 1)
    pdf.cell(w = 70, h = 10, txt = datos[2], border = 'TB', align = 'C', fill = 1)
    pdf.multi_cell(w = 0, h = 10, txt = datos[3], border = 'TBR', align = 'C', fill = 1)



pdf.output('djangochat/Auxiliar/PDF-Creator/Reporte.pdf')