"""Модуль для формирования отчета в виде PDF-файла.

Для генерации используются библиотеки:
  - html2text: преобразование HTML в Markdown-формат;
  - reportlab: создание документов в формате PDF.

Доп. ссылки:
  - https://www.reportlab.com/docs/reportlab-userguide.pdf
  - http://stackoverflow.com/questions/35497616/
    python-reportlab-writing-special-chararacters-in-pdf-file
  - http://matthiaseisen.com/pp/patterns/p0150/
  - http://eric.sau.pe/tag/reportlab-getsamplestylesheet/
"""

import utils

import html2text

import datetime
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, cm
from reportlab.platypus import Paragraph, PageBreak, SimpleDocTemplate, \
                               Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
FONTNAME = "DejaVuSans"


class Reporter:
    """Класс Reporter выполняет формирование PDF-файла с отчетом."""

    @staticmethod
    def make(request_info, vacancies):
        """Сгенерировать отчет о найденных вакансиях 'vacancies' на
        основании запроса клиента 'request_info'.

        Параметры:
          - request_info (mailer.Mailer._get_request_info()): запрос клиента;
          - vacancies (hh.Hh.search()): список вакансий.

        Результат:
            - имя созданного файла.
        """

        def add_page_number(canvas, doc):
            """Добавить номер страницы."""
            page_num = canvas.getPageNumber()
            text = "%s" % page_num
            canvas.drawRightString(11 * cm, 1 * cm, text)

        def add_spaces(num=1):
            for i in range(num):
                story.append(Paragraph("", style_h3))

        def key_or_none(dic, key, mes):
            return mes if key not in dic or dic[key] is None else str(dic[key])

        def currency_to_str(vacancy):
            if "salary" not in vacancy or vacancy["salary"] is None:
                return "Не указано"
            else:
                if len(vacancy["salary"]) > 2:
                    return "{} - {}".format(
                        key_or_none(vacancy["salary"], "from", "Не указано"),
                        key_or_none(vacancy["salary"], "to", "Не указано"))
                else:
                    return "Не известно"

        def pretty_text(text):
            text = html2text.html2text(text)

            replaces = (("\n", "<br />\n"),
                        ("**", ""),
                        ("*", "-"),
                        ("\-", "-"))
            for source, target in replaces:
                text = text.replace(source, target)

            return text

        # Достаточность данных
        assert isinstance(request_info, dict)
        assert isinstance(vacancies, list)

        # Стили
        style_sheet = getSampleStyleSheet()

        style_h1 = style_sheet["Heading1"]
        style_h1.alignment = TA_CENTER
        style_h1.fontName = FONTNAME

        style_h2 = style_sheet["Heading2"]
        style_h2.alignment = TA_CENTER
        style_h2.fontName = FONTNAME

        style_h3 = style_sheet["Heading3"]
        style_h3.alignment = TA_CENTER
        style_h3.fontName = FONTNAME

        style_h4 = style_sheet["Heading4"]
        style_h4.alignment = TA_LEFT
        style_h4.fontName = FONTNAME

        style_table = style_sheet["Normal"]
        style_table.alignment = 1
        style_table.fontName = FONTNAME
        style_table.fontSize = 8

        style_body = style_sheet["BodyText"]
        style_body.fontName = FONTNAME
        style_body.alignment = TA_LEFT
        style_body.fontSize = 8
        style_body.spaceBefore = 10
        style_body.spaceAfter = 10

        # Формирование документа
        filename = "Вакансии для {}.pdf".\
            format(request_info["email"].replace("<", "").replace(">", ""))

        doc = SimpleDocTemplate(filename, pagesize=A4,
                                rightMargin=50, leftMargin=50,
                                topMargin=50, bottomMargin=50,
                                showBoundary=False, allowSplitting=True)

        story = list()

        story.append(Paragraph("Кадровое агентство \"{}\"".
                               format(utils.agency_name), style_h1))
        add_spaces(2)
        story.append(Paragraph("Дата отчета: {}".
                               format(datetime.datetime.now().
                                      strftime("%d.%m.%Y %H:%M:%S")),
                               style_h3))
        add_spaces(2)
        story.append(Paragraph("Найдено вакансий: {}".format(
                               len(vacancies) if vacancies else 0), style_h3))
        add_spaces(2)

        story.append(Paragraph("Запрос:", style_h3))
        table = Table(
                [[Paragraph("Клиент", style_table),
                  Paragraph(request_info["email"], style_table)],
                 [Paragraph("Вакансии", style_table),
                  Paragraph(request_info["title"], style_table)],
                 [Paragraph("Регион", style_table),
                  Paragraph(request_info["area"], style_table)],
                 [Paragraph("Уровень зарплаты", style_table),
                  Paragraph(key_or_none(request_info,
                                        "salary", "Не задано"),
                            style_table)],
                 [Paragraph("Опыт", style_table),
                  Paragraph(key_or_none(request_info,
                                        "experience", "Не задано"),
                            style_table)]],
                colWidths=[4 * cm, 6 * cm])
        table.setStyle(TableStyle([
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]))
        story.append(table)

        # Каждая вакансия на новой странице
        for i, vacancy in enumerate(vacancies, start=1):
            story.append(PageBreak())
            story.append(Paragraph("Вакансия №{} из {}".
                                   format(i, len(vacancies)), style_h3))

            story.append(Paragraph("Ключевая информация:", style_h4))

            table = Table([
                [Paragraph("Наименование вакансии", style_table),
                 Paragraph(vacancy["name"], style_table)],
                [Paragraph("Компания", style_table),
                 Paragraph(vacancy["employer"]["name"], style_table)],
                [Paragraph("Город", style_table),
                 Paragraph(vacancy["area"]["name"], style_table)],
                [Paragraph("Уровень зарплаты", style_table),
                 Paragraph(currency_to_str(vacancy), style_table)],
                [Paragraph("Требуемый опыт работы", style_table),
                 Paragraph(vacancy["experience"]["name"]
                           if "experience" in vacancy
                           else str(request_info["experience"]),
                           style_table)]
                ],
                colWidths=[5 * cm, 10 * cm])

            table.setStyle(TableStyle([
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ]))

            story.append(table)

            # Описание
            story.append(Paragraph("Описание:", style_h4))
            story.append(Paragraph(
                pretty_text(vacancy.get("description",
                                        "Описание отсутствует")),
                style_body))

        doc.build(story, onLaterPages=add_page_number)

        return filename
