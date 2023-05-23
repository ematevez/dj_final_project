from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import Solicitud_form, Items_form
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView,)
from .pdfcreator import *
import smtplib
import ssl
from email.message import EmailMessage

def solicitud(request):
    return render(request, 'unhido/pagina.html')

def general(request):
        return render(request, 'unhido/general.html')

def crear(request):
#Crea una solicitud
    if request.method == 'POST':
        form = Solicitud_form(request.POST, request.FILES)
        if form.is_valid():
                form.save()  
                solo = form.save()                
                pdf(request)
                return redirect('general') 
    else:
        form = Solicitud_form()

    return render(request, 'unhido/crear-solicitud.html', {'form': form})
#==============================================
#=============CREAR PDF========================
#==============================================
def pdf(request):
    lista_datos = (
    (1, 'Carlos', 'carlos@gmail.com', '2020-02-25'),
    (2, 'Jose', 'jose@gmail.com', '2019-03-12'),
    (3, 'Marcos', 'marcos@gmail.com', '2018-01-31'),
    (4, 'Luz', 'luz@gmail.com', '2017-02-15'),
    (5, 'Elmer', 'elmer@gmail.com', '2016-11-23'),)#*8
    
    print ("===================")
    print ("===================")
    print(request)
    print ("===================")
    print ("===================")
    print ("===================")
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



    pdf.output('media/informe/Reporte.pdf')
    mail()
    return render(request, 'unhido/pagina.html')

def mail():
    # Define email sender and receiver
    email_sender = 'bhpdjemaq2021@gmail.com'
    email_password = 'upgodrzziajcqbjv'
    email_receiver = 'ematevez@gmail.com'

    # Set the subject and body of the email
    subject = 'Check out your account!'
    body = """
    Se le ha enviado una solicitud: http://192.168.1.44:8000/dashboard/
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    with open("media/informe/Reporte.pdf", "rb") as f:
        em.add_attachment(
            f.read(),
            filename="Reporte.pdf",
            maintype="application",
            subtype="pdf"
        )
    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())