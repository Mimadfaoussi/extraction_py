import os
import glob
import re
import json


extracted_data = []


# Expanded list of common car models for regex pattern
model_pattern = (
    r"(Aveo|Spark|Optra|Nubira|Cruz|Captiva|Chevrolet|Daewoo|"
    r"Toyota|Corolla|Camry|Yaris|Prius|Highlander|Rav4|Hilux|Land Cruiser|"
    r"Honda|Civic|Accord|CR-V|Pilot|Jazz|City|Fit|Odyssey|"
    r"Ford|Focus|Fiesta|Mustang|Escape|Explorer|Ranger|"
    r"Volkswagen|Golf|Polo|Passat|Tiguan|Jetta|Atlas|"
    r"Hyundai|Elantra|Tucson|Sonata|Santa Fe|Kona|"
    r"Nissan|Altima|Maxima|Rogue|Sentra|Versa|Pathfinder|"
    r"BMW|X1|X3|X5|X6|3 Series|5 Series|7 Series|"
    r"Mercedes-Benz|C-Class|E-Class|S-Class|GLA|GLC|GLE|GLS|"
    r"Audi|A3|A4|A6|Q3|Q5|Q7|Q8|"
    r"Kia|Sorento|Sportage|Soul|Seltos|Optima|"
    r"Mazda|CX-3|CX-5|CX-9|Mazda3|Mazda6|"
    r"Jeep|Wrangler|Cherokee|Grand Cherokee|Compass|Renegade|"
    r"Subaru|Impreza|Forester|Outback|Ascent|"
    r"Chevrolet|Cruze|Malibu|Impala|Silverado|Blazer|Equinox|"
    r"Dodge|Charger|Challenger|Durango|"
    r"Fiat|500|Panda|"
    r"Peugeot|308|3008|5008|"
    r"Renault|Clio|Megane|Kadjar|Koleos|"
    r"Volvo|XC40|XC60|XC90|"
    r"Land Rover|Range Rover|Discovery|Defender|"
    r"Mitsubishi|Outlander|Pajero|"
    r"Jaguar|F-Pace|E-Pace|"
    r"Suzuki|Swift|Vitara|Baleno|"
    r"Skoda|Octavia|Superb|Kodiaq|"
    r"Tata|Nano|Harrier|Nexon|"
    r"Mahindra|XUV500|Scorpio|Thar|Bolero"
    r")"
)



def print_ten(names):
    for i in range (10):
        print(names[i])



directory_path = "./CHEVROLET"

word_files = glob.glob(os.path.join(directory_path, "*.docx"))

file_names = [os.path.basename(file) for file in word_files]

#print_ten(file_names)

for file_name in file_names:
    name_without_ext = file_name.replace(".docx", "")

    product_match = re.search(r"^[^\d]+", name_without_ext)    
    product_name = product_match.group(0).strip() if product_match else "Unknown"

    # Extract Models/Variants: words that are capitalized or known model terms
    model_match = re.findall(model_pattern, name_without_ext, re.IGNORECASE)
    models = list(set(model_match)) if model_match else ["Unknown"]
    # Extract Reference Numbers: digits with potential '=' separators
    # Reference pattern includes digits, letters, and symbols like `=`, `-`, `(`, `)`
    references_match = re.findall(r"\b(?:\d{4,}(?:=\d{4,})?)\b", name_without_ext)
    references = references_match if references_match else ["Unknown"]

    # Append extracted information as a dictionary
    extracted_data.append({
        "file_name": file_name,
        "product_name": product_name,
        "models": models,
        "references": references
    })

# Save to JSON file
with open("extracted_data.json", "w") as json_file:
    json.dump(extracted_data, json_file, indent=4)

print("Extraction complete. Data saved to 'extracted_data.json'")



