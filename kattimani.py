import face_recognition
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Load sample images and learn to recognize faces
durga_image = face_recognition.load_image_file("durga.jpg.jpeg")
durga_face_encoding = face_recognition.face_encodings(durga_image)[0]
sangi_image = face_recognition.load_image_file("sangi.jpg")
sangi_face_encoding = face_recognition.face_encodings(sangi_image)[0]

# Known face encodings and names
known_face_encodings = [durga_face_encoding, sangi_face_encoding]
known_face_names = ["durga", "sangi"]

# Load and process unknown image

unknown_image = face_recognition.load_image_file("unknown1.jpg.jpeg")
# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
pil_image = Image.fromarray(unknown_image)
draw = ImageDraw.Draw(pil_image)
font = ImageFont.truetype("arial.ttf", 16)

# unknown_image = face_recognition.load_image_file("unknown2.jpg.jpg")
# face_locations = face_recognition.face_locations(unknown_image)
# face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
# pil_image = Image.fromarray(unknown_image)
# draw = ImageDraw.Draw(pil_image)
# font = ImageFont.truetype("arial.ttf", 16)

# Loop through detected faces
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # Check for matches
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "unknown"

    if True in matches:
        # Find first match index
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Get text bounding box
    text_bbox = draw.textbbox((0, 0), name, font=font)
    # Calculate text width and height
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Draw face bounding box and label
    draw.rectangle(((left, top), (right, bottom)), outline=(48, 63, 159))
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(48, 63, 159), outline=(48, 63, 159))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 0), font=font)

# Release drawing resources and show the image
del draw
pil_image.show()

# old code
# import face_recognition
# from PIL import Image, ImageDraw
# import numpy as np

# # Load a sample picture and learn how to recognize it.
# durga_image = face_recognition.load_image_file("durga.jpg.jpeg")
# durga_face_encoding = face_recognition.face_encodings(durga_image)[0]

# # Load a second sample picture and learn how to recognize it.
# sangi_image = face_recognition.load_image_file("sangi.jpg")
# sangi_face_encoding = face_recognition.face_encodings(sangi_image)[0]

# # Create arrays of known face encodings and their names
# known_face_encodings = [
#     durga_face_encoding,
#     sangi_face_encoding,
# ]
# known_face_names = [
#     "durga",
#     "sangi"
# ]


# unknown1_image = face_recognition.load_image_file("unknown1.jpg.jpeg")
# # Find all the faces and face encodings in the unknown image
# face_locations = face_recognition.face_locations(unknown1_image)
# face_encodings = face_recognition.face_encodings(unknown1_image, face_locations)
# pil_image = Image.fromarray(unknown1_image)
# draw = ImageDraw.Draw(pil_image)

# unknown2_image = face_recognition.load_image_file("unknown2.jpg.jpg")
# face_locations = face_recognition.face_locations(unknown2_image)
# face_encodings = face_recognition.face_encodings(unknown2_image, face_locations)
# pil_image = Image.fromarray(unknown2_image)
# draw = ImageDraw.Draw(pil_image) 


# # Loop through each face found in the unknown image
# for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#     # See if the face is a match for the known face(s)
#     matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#     name = "unknown"

#     if True in matches:
#         first_match_index = matches.index(True)
#         name = known_face_names[first_match_index]

#     # Draw a box around the face using the Pillow module
#     draw.rectangle(((left, top), (right, bottom)), outline=(48, 63, 159))
#     # Draw a label with a name below the face
#     text_width, text_height = draw.textsize(name)
#     draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(48, 63, 159), outline=(48, 63, 159))
#     draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 0))


# # Remove the drawing library from memory as per the Pillow docs
# del draw

# pil_image.show()

# # You can also save a copy of the new image to disk if you want by uncommenting this line
# # pil_image.save("image_with_boxes.jpg")

