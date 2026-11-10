from pyscript import document


non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222),
}



def periodic(e):
   
    document.getElementById("div_name").innerHTML = ""

    
    element_Name = document.getElementById("input1").value

   
    var2 = non_metals.get(element_Name, ("Element not found", "-", "-"))

    
    document.getElementById("div_name").innerHTML = f"""
Symbol: {element_Name}
Element: {var2[0]}
Atomic Number: {var2[1]}
Atomic Mass: {var2[2]}
"""