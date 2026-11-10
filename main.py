from pyscript import document, display


elements = {
    "F": ("FLUORINE", 9, 18.9984),
    "H": ("HYDROGEN", 1, 1.0079),
    "N": ("NITROGEN", 7, 14.0067),
    "Xe": ("XENON", 54, 131.293),
    "He": ("HELIUM", 2, 4.0026),
    "Ne": ("NEON", 10, 20.1797),
    "Ar": ("ARGON", 18, 39.948),
    "Kr": ("KRYPTON", 36, 83.8),
    "Rn": ("RADON", 86, 222),
    "C": ("CARBON", 6, 12.0107),
    "O": ("OXYGEN", 8, 15.9994),
    "P": ("PHOSPHORUS", 15, 30.9738),
    "S": ("SULFUR", 16, 32.065),
    "Cl": ("CHLORINE", 17, 35.453),
    "Se": ("SELENIUM", 34, 78.96),
    "Br": ("BROMINE", 35, 79.904),
    "I": ("IODINE", 53, 126.9045),
}


not_found_message = (
    "Sorry! This element does not exist in the non-metals list. "
    + "Please note that the input is case sensitive."
)


def search_element(e):
  
    elementA = document.getElementById("elementA").value

   
    result = elements.get(elementA, (not_found_message, "-", "-"))

   
    document.getElementById("symbol").innerText = elementA  # element symbol
    document.getElementById("name").innerText = result[0]  # element name
    document.getElementById("number").innerText = result[1]  # atomic number
    document.getElementById("mass").innerText = result[2]  # atomic mass