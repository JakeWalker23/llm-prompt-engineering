from helpers.generate_image_json import generate_image_json

print(generate_image_json('./Image/flip.png').content[0].text)
print(generate_image_json('./Image/shot.png').content[0].text)