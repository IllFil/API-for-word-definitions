import justpy as jp

class Doc:

    path = "/about"

    def serve(self):
        wp = jp.WebPage()

        div = jp.Div(a=wp, classes = "bg-gray-200 m-2")

        jp.Div(a = div, text = "Dictionary API", classes = "text-4xl m-2")
        jp.Div(a = div, text = "Get definitions of words:", classes = "text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text = """
        {"word": "bank", 
        "definition": 
        [")The sloping side of any hollow in the ground, especially when bordering a river.",
        "A financial institution where one can borrow money (upon which interest is due) or deposit money (in order to collect interest).",
        "Accumulation of a same substance, normally in big quantities, or arrangement of similar objects that is considered as a unit, for example: sand bank, fog bank, bank of ice.",
        "A place where supplies or stock of bodies or substances of the human body are preserved, usually of the same type, for future medical use, for example: blood bank, eye bank, sperm bank.",
        "A place where elements, usually of the same type are kept, for consultation or later use, for example: data bank, image bank.", "To tip laterally.", "To do business with a financial institution or keep an account at a financial institution.",
        "To act as the banker in a game or in gambling.", "To have confidence or faith in.", "A flight maneuver; the aircraft tips laterally about its longitudinal axis (especially in turning).", "A long ridge or pile."]}
        """)
        return wp