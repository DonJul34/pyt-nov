from monai.transforms import LoadImage

# Charger une image DICOM et la convertir en format compatible pour deep learning
dicom_img = LoadImage(image_only=True)("path/to/image.dcm")
{
  "nom": "Alice",
  "age": 25,
  "actif": true,
  "compétences": ["Python", "Django", "SQL"]
}
import json
data = '{"nom": "Alice", "age": 25}'
dict_data = json.loads(data)  # Convertit en dictionnaire Python
print(dict_data["nom"])  # Alice
with open('data.json', 'r') as f:
    dict_data = json.load(f)
print(dict_data["age"])  # 25
data = {"nom": "Bob", "actif": False}
json_str = json.dumps(data, indent=4)  # Beautification avec indent
print(json_str)
