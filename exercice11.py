from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "B", 12)
        self.cell(0, 10, "Plan de Estudio Salesforce Developer (Junior)", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(0)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("DejaVu", "", 10)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()

# Agregar fuente ANTES de usarla
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.add_font("DejaVu", "B", "DejaVuSans.ttf", uni=True)

pdf.add_page()

# Documentación oficial
official_docs = """📘 Documentación Oficial:
- Apex: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/
- LWC: https://developer.salesforce.com/docs/component-library/documentation/en/lwc
- Visualforce: https://developer.salesforce.com/docs/atlas.en-us.pages.meta/pages/
- SOQL: https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/

"""
pdf.chapter_body(official_docs)

# Contenidos por semana
pdf.chapter_title("Semana 1-2: Fundamentos de Salesforce & Apex")
semana1 = """- Arquitectura de Salesforce (multi-tenant, MVC)
- Introducción a Apex:
  - Sintaxis básica (variables, tipos, operadores)
  - Clases y métodos
  - Control de flujo (if, switch, bucles)
  - Colecciones (List, Set, Map)
  - Tipos de datos especiales (Date, Datetime, Id)
- Práctica: Escribir clases y métodos simples, usar colecciones.

📘 Recurso: https://trailhead.salesforce.com/content/learn/modules/apex_database"""
pdf.chapter_body(semana1)

pdf.chapter_title("Semana 3-4: Apex Orientado a Objetos y Triggers")
semana2 = """- Programación orientada a objetos (clases, herencia, interfaces)
- DML – insert, update, delete, upsert
- SOQL (Salesforce Object Query Language)
- Triggers (before y after)
- Contexto de ejecución de triggers (Trigger.isInsert, etc.)

📘 Recurso: https://trailhead.salesforce.com/content/learn/modules/apex_triggers"""
pdf.chapter_body(semana2)

pdf.chapter_title("Semana 5-6: Lightning Web Components (LWC)")
semana3 = """- LWC vs Aura vs Visualforce
- Estructura de un componente (.html, .js, .meta.xml)
- Decoradores: @api, @track, @wire
- Comunicación entre componentes (props y eventos)
- Conexión con Apex usando @wire o imperative Apex

📘 Recurso: https://trailhead.salesforce.com/content/learn/modules/lwc-basics"""
pdf.chapter_body(semana3)

pdf.chapter_title("Semana 7-8: Formularios, Eventos y Navegación en LWC")
semana4 = """- Formularios con lightning-input, lightning-record-edit-form
- Validaciones en LWC
- Manejo de eventos personalizados
- Navegación entre páginas usando NavigationMixin

📘 Recurso: https://trailhead.salesforce.com/content/learn/projects/quick-start-lightning-web-components"""
pdf.chapter_body(semana4)

pdf.chapter_title("Semana 9: Visualforce")
semana5 = """- Qué es Visualforce y cuándo se usa
- Sintaxis de páginas VF (<apex:page>, <apex:form>, <apex:repeat>)
- Conexión con controladores Apex
- Buenas prácticas de compatibilidad

📘 Recurso: https://trailhead.salesforce.com/content/learn/modules/visualforce_fundamentals"""
pdf.chapter_body(semana5)

pdf.chapter_title("Semana 10-11: Tests y Buenas Prácticas")
semana6 = """- Unit Tests en Apex (@isTest)
- Bulkification y límites de gobierno
- Seguridad: CRUD/FLS, with sharing
- Organización de código: controladores, servicios, DTOs

📘 Recurso: https://trailhead.salesforce.com/content/learn/modules/apex_testing"""
pdf.chapter_body(semana6)

pdf.chapter_title("Semana 12: Proyecto Integrador")
semana7 = """- Crear una aplicación con:
  - Backend en Apex
  - Frontend en LWC
  - Página adicional en Visualforce
  - Al menos un test unitario"""
pdf.chapter_body(semana7)

# Guardar PDF
output_path = "plan_estudio_salesforce_junior.pdf"
pdf.output(output_path)

print(f"PDF guardado en: {output_path}")

