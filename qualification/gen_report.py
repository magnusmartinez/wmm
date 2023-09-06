from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3 as A4
from datetime import datetime


def get_cented_text(page, text, font_size=10, font_family="Helvetica", max_width=A4[0]):
    text_width = page.stringWidth(text, font_family, font_size)
    x = (max_width - text_width) / 2 
    return x

def document_header(page, head):  
    w, h = A4
    page.setFont("Helvetica", 8)
    page.drawString(w - 100, h - 10, head['security_code'])

    page.setFont("Helvetica", 15)
    x = get_cented_text(page=page, text=head['title'].upper(), font_size=15, font_family="Helvetica", max_width=w)
    page.drawString(x, h - 40, head['title'].upper())
    page.setFont("Helvetica", 12)

    # x = get_cented_text(page=page, text=head['teacher'], font_size=12, font_family="Helvetica", max_width=w)
    # page.drawString(x, h - 65, head['teacher'])

def document_body(page, body, head):
    w, h = page._pagesize
    font_type = "Helvetica"


    # Variables
    counter = 0
    page.setFont(font_type, 7)
    y = 0
    line = 0
    _page = 1
    page_current = 0
    for qualification in body:


        # Header
        if page_current != _page:

            document_header(page, head)
            page.setStrokeColorRGB(0,0,0,1)
            page.setFont(font_type, 9)
            page.line(0, h - 100, w - 0, h - 100)
            page.drawString(5, h - 110, "NO.")
            page.drawString(30, h - 110, "ESTUDIANTE")
            page.drawString(210, h - 110, "PARTICIPACIÓN")
            page.drawString(290, h - 110, "CUADERNO")
            page.drawString(350, h - 110, "PRÁCTICA")
            page.drawString(410, h - 110, "EJERCICIO")
            page.drawString(470, h - 110, "EXPOSICIONES")
            page.drawString(550, h - 110, "TRABAJO FINAL")
            page.drawString(630, h - 110, "PENALIZACIÓN")
            page.drawString(710, h - 110, "CALIFICACIÓN MENSUAL A.")
            page.line(0, h - 120, w - 0, h - 120)
            page_current = _page

        counter += 1
        page.setStrokeColorRGB(0,0,0, 0.3)
        page.setFont(font_type, 9)
        p = 1055
        page.drawString(5, p-y, str(counter))
        page.drawString(30, p-y, str(qualification["student"]))
        page.drawString(210, p-y, str(qualification["participation_note"]))
        page.drawString(290, p-y, str(qualification["notebook_note"]))
        page.drawString(350, p-y, str(qualification["practice"]))
        page.drawString(410, p-y, str(qualification["exercise"]))
        page.drawString(470, p-y, str(qualification["presentation"]))
        page.drawString(550, p-y, str(qualification["final_work"]))
        page.drawString(630, p-y, str(qualification["penalty"]))
        page.drawString(710, p-y, str(qualification["value"]))
        page.line(0, 1045-y, w - 0, 1045-y)

        # Increment line
        y += 25
        line += 1


        # New page
        if line >= 40:
            y = 0
            line = 0
            _page = _page + 1
            page.showPage()

def to_pdf(filename: str, head: dict, body: dict):
    w, h = A4
    report = canvas.Canvas(filename, pagesize=A4)

    # Header
    document_header(report, head)

    # Body
    document_body(report, body, head)

    report.save()


def get_cented_text(page, text, font_size=10, font_family="Helvetica", max_width=A4[0]):
    text_width = page.stringWidth(text, font_family, font_size)
    x = (max_width - text_width) / 2 
    return x

def document_header_p(page, head):  
    w, h = A4
    page.setFont("Helvetica", 8)
    page.drawString(w - 100, h - 15, head['security_code'])

    page.setFont("Helvetica", 15)
    x = get_cented_text(page=page, text=head['title'].upper(), font_size=15, font_family="Helvetica", max_width=w)
    page.drawString(x, h - 40, head['title'].upper())
    page.setFont("Helvetica", 12)

    # x = get_cented_text(page=page, text=head['teacher'], font_size=12, font_family="Helvetica", max_width=w)
    # page.drawString(x, h - 65, head['teacher'])

def document_body_p(page, body, head):
    w, h = page._pagesize
    font_type = "Helvetica"


    # Variables
    counter = 0
    page.setFont(font_type, 7)
    y = 0
    line = 0
    _page = 1
    page_current = 0
    for qualification in body:


        # Header
        if page_current != _page:

            document_header_p(page, head)
            page.setStrokeColorRGB(0,0,0,1)
            page.setFont(font_type, 9)
            page.line(0, h - 100, w - 0, h - 100)
            page.drawString(5, h - 110, "NO.")
            page.drawString(30, h - 110, "ESTUDIANTE")
            page.drawString(210, h - 110, "PARTICIPACIÓN")
            page.drawString(290, h - 110, "CUADERNO")
            page.drawString(350, h - 110, "PRÁCTICA")
            page.drawString(410, h - 110, "EJERCICIO")
            page.drawString(470, h - 110, "EXPOSICIONES")
            page.drawString(550, h - 110, "TRABAJO FINAL")
            page.drawString(630, h - 110, "PENALIZACIÓN")
            page.drawString(710, h - 110, "CALIFICACIÓN PERIODICA A.")
            page.line(0, h - 120, w - 0, h - 120)
            page_current = _page

        counter += 1
        page.setStrokeColorRGB(0,0,0, 1)
        page.setFont(font_type, 9)
        p = 1055
        page.drawString(5, p-y, str(counter))
        page.drawString(30, p-y, str(qualification["student"]))
        page.drawString(210, p-y, str(qualification["participation_note"]))
        page.drawString(290, p-y, str(qualification["notebook_note"]))
        page.drawString(350, p-y, str(qualification["practice"]))
        page.drawString(410, p-y, str(qualification["exercise"]))
        page.drawString(470, p-y, str(qualification["presentation"]))
        page.drawString(550, p-y, str(qualification["final_work"]))
        page.drawString(630, p-y, str(qualification["penalty"]))
        page.drawString(710, p-y, str(qualification["value"]))

        page.line(0, 1045-y, w - 0, 1045-y)

        for index, period in enumerate(qualification["_children"]):
            
            # Increment line
            y += 25
            line += 1
            page.drawString(30, p-y, str(period["student"]))
            page.drawString(210, p-y, str(period["participation_note"]))
            page.drawString(290, p-y, str(period["notebook_note"]))
            page.drawString(350, p-y, str(period["practice"]))
            page.drawString(410, p-y, str(period["exercise"]))
            page.drawString(470, p-y, str(period["presentation"]))
            page.drawString(550, p-y, str(period["final_work"]))
            page.drawString(630, p-y, str(period["penalty"]))
            page.drawString(710, p-y, str(period["value"]))

            page.setStrokeColorRGB(0,0,0, 0.3)
            
            if index + 1 == len(qualification["_children"]):
                page.setStrokeColorRGB(0,0,0, 1)
            page.line(0, 1045-y, w - 0, 1045-y)


        # Increment line
        y += 25
        line += 1


        # New page
        if line >= 40:
            y = 0
            line = 0
            _page = _page + 1
            page.showPage()

def document_footer_p(page, body, head):
    w, h = A4
    page.setFont("Helvetica", 8)
    page.drawString(w - 100, h - (h - 10), head['security_code'])
    page.drawString(w - (w - 25), h - (h - 10), f"GENERADO EN: {datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')}")

    # page.setFont("Helvetica", 15)
    # x = get_cented_text(page=page, text=head['title'].upper(), font_size=15, font_family="Helvetica", max_width=w)
    # page.drawString(x, h - 40, head['title'].upper())
    # page.setFont("Helvetica", 12)

def to_pdf_p(filename: str, head: dict, body: dict):
    w, h = A4
    report = canvas.Canvas(filename, pagesize=A4)

    # Header
    document_header_p(report, head)

    # Body
    document_body_p(report, body, head)

    # # Footer
    # document_footer_p(report, body, head)

    report.save()
