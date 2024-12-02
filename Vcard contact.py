import pandas as pd

def cleared_canal(canal):

    match canal:
        case "ALMACENES":
            return "ALM"
        
        case "AUTOSERVICIOS":
            return "AUT"
        
        case "CORPORATIVOS":
            return "COR"
        
        case "DIETETICAS":
            return "DIE"
        
        case "ESTABL. EDUCATIVOS":
            return "EDU"
        
        case "ESTACIONES DE SERVIC":
            return "SER"
        
        case "KIOSCOS":
            return "KIO"
        
        case "NO TRADICIONALES":
            return "NOT"

def cleared_category(category):

    match category:
        case "CLIENTE A":
            return "A"
        
        case "CLIENTE B1":
            return "B1"
        
        case "CLIENTE B2":
            return "B2"
        
        case "CLIENTE C":
            return "C"
        
        case "CLIENTE D":
            return "D"

def cleared_code(code):
    normal_code = str(int(code))
    return normal_code


def cleared_phone(phone):

    if phone is None or not isinstance(phone, str):
        return "No tiene numero"
    
    new_phone = phone.replace(" ", "")
    guiones = [pos for pos, char in enumerate(new_phone) if char == '-']

    if len(guiones) < 3:
        raise ValueError("El número de guiones es insuficiente para procesar el teléfono: {}".format(phone))

    sector1 = new_phone[guiones[0] + 1:guiones[1]]
    sector2 = new_phone[guiones[1] + 1:guiones[2]]
    sector3 = new_phone[guiones[2] + 1:]


    #Problemas codigo de pais
    if(len(sector1) < 3):
        sector1 = "+54"

    #Problemas codigo de area
    if(sector2 == "" or sector2 == "0341"):
        sector2 = "341"
    
    if(sector2 == "011"):
        sector2 = "11"

    #Problemas numero telefonico
    if(sector3.startswith("15")):
        sector3 = sector3[2:]

    if(len(sector3) < 7):
        return "Numero muy corto"
    
    else:
        return sector1 + sector2 + sector3

codigo = 123456
nuevo_codigo = cleared_code(codigo)

excel_shuffled = pd.read_excel(r'Archivos_necesarios\Maestro.xlsx')
excel_shuffled['Telefono'] = excel_shuffled['Telefono'].apply(cleared_phone)
excel_shuffled['Canal'] = excel_shuffled['Canal'].apply(cleared_canal)
excel_shuffled['Categoria'] = excel_shuffled['Categoria'].apply(cleared_category)
excel_shuffled['Codigo'] = excel_shuffled['Codigo'].apply(cleared_code)

excel_shuffled.to_excel(r'Archivos_necesarios\Maestro_limpio.xlsx', index=False)

excel_contacts = pd.read_excel(r'Archivos_necesarios\Maestro_limpio.xlsx')
excel_contacts = excel_contacts.astype(str)

with open(r'Archivos_necesarios\contactos.vcf', "w") as vcf_file:
    for index, row in excel_contacts.iterrows():
        
        if row['Telefono'] != "No tiene numero" and row['Telefono'] != "Numero muy corto":
            contact_name = row['Canal'] + "-" + row['Categoria'] + "-" + row['Codigo']
            contact_phone = row['Telefono']

            canal = row['Canal']
            category = row['Categoria']
            code = row["Codigo"]
            
            contact_N = f"{code};{canal};{category};"

            vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{contact_name}
N:{contact_N}
TEL:{contact_phone}
END:VCARD"""
            
            # Escribir en el archivo vCard
            vcf_file.write(vcard + "\n\n")




