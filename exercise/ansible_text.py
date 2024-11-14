from monai.transforms import LoadImage

# Charger une image DICOM et la convertir en format compatible pour deep learning
dicom_img = LoadImage(image_only=True)("path/to/image.dcm")
