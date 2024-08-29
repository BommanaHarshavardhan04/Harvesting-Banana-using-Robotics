from PIL import Image, ImageDraw, ImageFont

def draw_dashed_line(draw, start, end, color, width, dash_length):
    """Draw a dashed line using the specified dash length."""
    x1, y1 = start
    x2, y2 = end
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    num_dashes = int(length / dash_length)
    
    for i in range(num_dashes):
        start_x = x1 + (x2 - x1) * (i / num_dashes)
        start_y = y1 + (y2 - y1) * (i / num_dashes)
        end_x = x1 + (x2 - x1) * ((i + 0.5) / num_dashes)
        end_y = y1 + (y2 - y1) * ((i + 0.5) / num_dashes)
        draw.line([(start_x, start_y), (end_x, end_y)], fill=color, width=width)

# Create a new image with white background
img = Image.new('RGB', (800, 600), (255, 255, 255))

# Draw the banana tree
draw = ImageDraw.Draw(img)
draw.rectangle([(100, 50), (150, 200)], fill=(128, 64, 0))  # Tree trunk
draw.ellipse([(50, 200), (200, 350)], fill=(0, 128, 0))  # Tree leaves

# Draw bananas on the tree
# Raw (green) bananas
draw.ellipse([(120, 220), (140, 240)], fill=(0, 255, 0))  # Banana 1
draw.ellipse([(160, 200), (180, 220)], fill=(0, 255, 0))  # Banana 2

# Ripe (yellow) bananas
draw.ellipse([(200, 220), (220, 240)], fill=(255, 255, 0))  # Banana 3
draw.ellipse([(240, 200), (260, 220)], fill=(255, 255, 0))  # Banana 4

# Draw the robot
draw.rectangle([(300, 50), (400, 150)], fill=(128, 128, 128))  # Robot body
draw.rectangle([(350, 150), (370, 200)], fill=(255, 0, 0))  # Robot arm

# Draw the basket close to the robot's hand
draw.rectangle([(400, 270), (500, 370)], fill=(255, 255, 255))  # Basket
draw.line([(400, 320), (500, 320)], fill=(0, 0, 0))  # Basket handle

# Draw the cutting action with a dashed line
draw_dashed_line(draw, (200, 230), (350, 150), (255, 0, 0), 2, 10)  # Dashed line for cutting Banana 3
draw_dashed_line(draw, (240, 210), (370, 150), (255, 0, 0), 2, 10)  # Dashed line for cutting Banana 4

# Draw bananas falling into the basket (after cutting)
# Falling Bananas (Banana 3)
draw.ellipse([(410, 260), (430, 280)], fill=(255, 255, 0))  # Cut Banana 3 falling
draw.ellipse([(430, 280), (450, 300)], fill=(255, 255, 0))  # Cut Banana 3 piece falling
# Falling Bananas (Banana 4)
draw.ellipse([(430, 220), (450, 240)], fill=(255, 255, 0))  # Cut Banana 4 falling
draw.ellipse([(450, 240), (470, 260)], fill=(255, 255, 0))  # Cut Banana 4 piece falling

# Draw arrows indicating the falling direction
draw.line([(200, 240), (410, 260)], fill=(0, 0, 0), width=3)  # Arrow for Banana 3
draw.polygon([(410, 260), (405, 250), (415, 250)], fill=(0, 0, 0))  # Arrowhead for Banana 3

draw.line([(240, 220), (430, 220)], fill=(0, 0, 0), width=3)  # Arrow for Banana 4
draw.polygon([(430, 220), (425, 210), (435, 210)], fill=(0, 0, 0))  # Arrowhead for Banana 4

# Add explanatory text
font = ImageFont.truetype('arial.ttf', 20)
draw.text((100, 400), '1. Raw (green) bananas on the tree (not cut)', font=font, fill=(0, 0, 0))
draw.text((100, 430), '2. Ripe (yellow) bananas on the tree (being cut)', font=font, fill=(0, 0, 0))
draw.text((100, 460), '3. Cut ripe bananas falling into the basket near the robot', font=font, fill=(0, 0, 0))

# Add labels for key elements
draw.text((120, 210), 'Banana 1', font=font, fill=(0, 0, 0))
draw.text((160, 190), 'Banana 2', font=font, fill=(0, 0, 0))
draw.text((200, 210), 'Banana 3', font=font, fill=(0, 0, 0))
draw.text((240, 190), 'Banana 4', font=font, fill=(0, 0, 0))
draw.text((320, 100), 'Robot', font=font, fill=(0, 0, 0))
draw.text((410, 260), 'Basket', font=font, fill=(0, 0, 0))

# Display the image
img.show()
