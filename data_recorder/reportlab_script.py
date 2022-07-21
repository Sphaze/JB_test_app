import io, os
from tkinter import MITER
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm, cm
from reportlab.lib.testutils import testsFolder
from reportlab.lib.pagesizes import letter, A4, A3, A2
from reportlab import rl_config
from .models import Post
from urllib import response
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, tables, Image, Spacer, Frame
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from reportlab.graphics import renderPDF
from reportlab.lib.colors import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.pdfmetrics import Font



class Report:

    def __init__(self, filename):   

        self.filename = filename
        self.elements = []         
        self.pagesize = A4
        self.width, self.height = self.pagesize
        self.buffer = io.BytesIO()
        self.c = self.createCanvas(self.buffer)
        self.styles = getSampleStyleSheet()


    def createCanvas(self, buffer):           
        myCanvas = canvas.Canvas(buffer, self.pagesize, bottomup=0)
        return myCanvas


    def includeFooter(self, pageNumber):      
          
        footer_line_h = self.height-60   
        self.c.line(cm, footer_line_h, self.width - inch + 1.05*cm, footer_line_h) 
        self.c.setFont("Times-Roman", 8)    
        self.c.drawString(1.1*cm, footer_line_h+10, "Report:")
        self.c.drawString(inch, footer_line_h+10, "NCR Report")
        self.c.drawString(4.5*inch+cm, footer_line_h+10, "TUS University\u2122")
        self.c.drawString(7*inch+7*mm, footer_line_h+10, "Page %d" % pageNumber)



    def page_one(self, pagenumber):      
        logo = os.path.join(settings.STATIC_ROOT,"img/logo_1.PNG")
        logoX = (self.height/2) + 2.5*cm
        logoY = (self.width/2) - 4*inch + 1.5*cm

        self.c.drawImage(logo, width=56, x=logoX, y=logoY, preserveAspectRatio=True, mask='auto')
       
        lineStart = 1*cm
        lineEnd = self.width - inch + 1.05*cm
        line_Y = 2*inch - 20
   
        self.c.line(lineStart, line_Y, lineEnd, line_Y)

        '''set fonts for text blobs''' 

        heading_font = "Helvetica"
        heading_fontsize = 9
        answer_font = "Helvetica-Bold"
        answer_fontsize = 11

      
        ### left column ###
        ''' heading blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Report:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+0.5*cm+2*mm)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("NCR Report")
        self.c.drawText(textobject)
        ''' heading blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+1.5*cm)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Comment:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+2*cm+2*mm)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("placeholder")
        self.c.drawText(textobject)
        ''' heading blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+3*cm)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Created by:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+3.5*cm+2*mm)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("placeholder")
        self.c.drawText(textobject)

        
        ### center column ###
        ''' heading blob '''  
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch)
        textobject.moveCursor(3*inch,0)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Printed by:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+0.5*cm+2*mm)
        textobject.moveCursor(3*inch,0)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("placeholder")
        self.c.drawText(textobject)
        ''' heading blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+1.5*cm)
        textobject.moveCursor(3*inch,0)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Execution time:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+2*cm+2*mm)
        textobject.moveCursor(3*inch,0)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("placeholder")
        self.c.drawText(textobject)
        ''' heading blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+3*cm)
        textobject.moveCursor(3*inch,0)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Order Time:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+3.5*cm+2*mm)
        textobject.moveCursor(3*inch,0)   
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("placeholder")
        self.c.drawText(textobject)


        ### right column ###
        
        ''' heading blob '''  
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch)
        textobject.moveCursor(6*inch,0)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Current Date:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+0.5*cm+2*mm)
        textobject.moveCursor(6*inch,0)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("20/07/2022")
        self.c.drawText(textobject)
        ''' heading blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+1.5*cm)
        textobject.moveCursor(6*inch,0)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Job ID:")
        self.c.drawText(textobject)

        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+2*cm+2*mm)
        textobject.moveCursor(6*inch,0)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("placeholder")
        self.c.drawText(textobject)

        data = Post.objects.last() #most recent database object from my database model called "Post"
        
        '''headings'''

        a1 = "NCR ID:"
        a2 = "Date of NCR:"
        a3 = "Advice Number:"
        a4 = "Job Reference Number:"
        a5 = "Status:"
        a6 = "Audit ID:"
        a7 = "Non Conformance Code:"
        a8 = "Company:"
        a9 = "Site:"
        a10 = "Severity:"
        a11 = "Person responsible:"
        a12 = "NCR Status:"
        a13 = "Target completion date:"
        a14 = "Date of completion:"

        '''convert ISO timestring (2022-07-13 11:53:52+00:00) to date with desired format '''

        NCR_date = str(str(data.date_posted)[8:10]) +'/'+str(str(data.date_posted)[5:7])+'/'+str(str(data.date_posted)[0:4])
    
        '''answers'''

        b1 = str(data.ncr_number)
        b2 = NCR_date
        b3 = "This is test text"
        b4 = "This is test text"
        b5 = "This is test text"
        b6 = "This is test text"
        b7 = "This is test text"
        b8 = "This is test text"
        b9 = "This is test text"
        b10 = "This is test text"
        b11 = "This is test text"
        b12 = "This is test text"
        b13 = "This is test text"
        b14 = "This is test text"

        # tuples containing the data for the text objects
        headings = (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14)
        answers = (b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14)
        
        # summary title
        textobject = self.c.beginText() 
        textobject.setLeading(30)
        textobject.setFont("Helvetica-Bold", 14)
        textobject.setTextOrigin(inch, inch*5+0.5*cm)
        textobject.textLine("Report Conditions:")
        self.c.drawText(textobject)

        # heading fields output
        lineSpacing=18
        textobject = self.c.beginText()
        textobject.setTextOrigin(inch, inch*5+0.5*cm)
        textobject.moveCursor(0,1.2*cm)  
        textobject.setFont("Helvetica", 10)
        for line in headings:
            textobject.setLeading(lineSpacing)
            textobject.textLine(line) #add the data from the list to the buffer

        self.c.drawText(textobject)
        
        # answer fields output
        textobject = self.c.beginText()
        textobject.setTextOrigin(inch * 4, inch*5+0.5*cm)
        textobject.moveCursor(0,1.2*cm)
        for line in answers:
            textobject.setLeading(lineSpacing)
            textobject.textLine(line)

        self.c.drawText(textobject)
        self.includeFooter(pagenumber)
 

    def page_two(self, pagenumber):           
        self.c.showPage()
        self.c.saveState()
        self.c.scale(0.7,0.7)
        self.pencil(self.c, "Description")
        self.c.scale(1.43,1.43)
        self.c.rect(1.6*cm,inch,7*inch,9*inch, fill=0)
        self.c.restoreState()
        self.includeFooter(pagenumber)

    
    def page_three(self, pagenumber):       
        self.c.showPage()
        self.c.setFont('Helvetica-Bold',16)
        self.c.drawString(self.width/2 - 3.5*inch, self.height/2 - 5*inch, "Related media")
        self.c.rect(1.6*cm,inch,7*inch,9*inch, fill=0)
        self.includeFooter(pagenumber)


    def page_four(self, pagenumber):        
        self.c.showPage()
        self.c.saveState()
        self.c.scale(0.7,0.7)
        self.pencil(self.c, "Comments")
        self.c.scale(1.43,1.43)
        self.c.rect(1.6*cm,inch,7*inch,9*inch, fill=0)
        self.c.restoreState()
        self.includeFooter(pagenumber)



    def pencil(self,canvas, text):
        u = inch/10

        canvas._leading = 200
        canvas.setStrokeColor(black)
        canvas.setFillColor(red)
        canvas.circle(30*u, 5*u, 5*u, stroke=1, fill=1)
        canvas.setFillColor(beige)
        canvas.rect(10*u,0,20*u,10*u, stroke=1, fill=1)
        canvas.setFillColor(black)
        canvas.setFont("Helvetica-Bold", 20)
        canvas.drawCentredString(2*inch-1, inch-25, text) 
        self.penciltip(canvas,debug=0)
        canvas.setDash([10,5,16,10],0)


    def penciltip(self, canvas, debug=1):
        u = inch/10.0

        if debug:
            canvas.scale(2.8,2.8)
            canvas.setLineWidth(0.25) # small lines
        canvas.setStrokeColor(black)
        canvas.setFillColor(tan)
        p = canvas.beginPath()
        p.moveTo(10*u,0)
        p.lineTo(0,5*u)
        p.lineTo(10*u,10*u)
        p.curveTo(11.5*u,10*u, 11.5*u,7.5*u, 10*u,7.5*u)
        p.curveTo(12*u,7.5*u, 11*u,2.5*u, 9.7*u,2.5*u)
        p.curveTo(10.5*u,2.5*u, 11*u,0, 10*u,0)
        canvas.drawPath(p, stroke=1, fill=1)
        canvas.setFillColor(black)
        p = canvas.beginPath()
        p.moveTo(0,5*u)
        p.lineTo(4*u,3*u)
        p.lineTo(5*u,4.5*u)
        p.lineTo(3*u,6.5*u)
        canvas.drawPath(p, stroke=1, fill=1)
        if debug:
            canvas.setStrokeColor(green) # put in a frame of reference
            canvas.grid([0,5*u,10*u,15*u], [0,5*u,10*u])


    def coord(self, x, y, unit):
      
        x = x * unit
        y = self.height -  y * unit
        return x, y

       

    def getBuffer(self):  
        self.page_one(pagenumber=1) 
        self.page_two(pagenumber=2) 
        self.page_three(pagenumber=3) 
        self.page_four(pagenumber=4) 
        self.c.save() #save the canvas
        self.buffer.seek(0)
       
        return self.buffer

    

    def generate(request):

        doc = Report("report.pdf")
        response = HttpResponse()
        response.content = doc.getBuffer()
        response.headers['Content-Disposition'] = 'inline; filename=' + doc.filename
        response.headers['Content-Type'] = 'application/pdf'
        
        return response




#  debugging aid:
# 'function' object has no attribute 'get'....this error usually means a function is missing parenthesis when it's returned
#  build() takes 1 positional argument but 2 were given....this error usually means that there should be zero or one less arguments in the function call for "build" function
#  The view didn't return an HttpResponse object....this error means that the function isn't returning anything and nothing is being accessed because of this
# 'NoneType' object has no attribute....this error means that one function isn't returning anything, and another function isn't working because of that
#  build() takes 0 positional arguments but 1 was given.... this error usually means that you're missing a "self" parameter in one or more function calls (or in the function itself). Relate the data with self.build() instead of [Class Name].build()...this error can also mean that the function needs at least one parameter instead of none.
#  TypeError at /report_pdf, 'method' object is not iterable.... this error means that a function reference is returned, and not the actual function (self.function() should be used with the parenthesis instead of self.function)
#  UnboundLocalError at /report_pdf, local variable 'canvas' referenced before assignment.... this error could mean that you're defining a variable name with a variable name already used in a library, for example "canvas = canvas.Canvas", change it to "myCanvas = canvas.Canvas"
       
        