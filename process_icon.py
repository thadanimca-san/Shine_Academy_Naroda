import cv2
import numpy as np

# Load image
img = cv2.imread('assets/app_icon.png', cv2.IMREAD_UNCHANGED)
print(f"Original shape: {img.shape}")

# Convert to RGB (ignore alpha for processing if exists)
if img.shape[2] == 4:
    rgb = img[:,:,:3]
else:
    rgb = img

# The background is a solid blueish color. 
# Let's find the white circle. 
# Convert to grayscale
gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

# Threshold to find bright areas (the white circle)
# White circle has high pixel values
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    # Find the largest contour which should be the circle
    largest_contour = max(contours, key=cv2.contourArea)
    
    # Get bounding box and minimum enclosing circle to be safe
    (x,y), radius = cv2.minEnclosingCircle(largest_contour)
    center = (int(x), int(y))
    radius = int(radius)
    print(f"Detected circle at {center} with radius {radius}")
    
    # Create an empty mask (same size as image)
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    
    # Draw a filled circle on the mask (slightly reduce radius to remove anti-aliasing artifacts from blue)
    cv2.circle(mask, center, radius - 2, 255, -1)
    
    # Create output image with alpha channel
    out = np.zeros((img.shape[0], img.shape[1], 4), dtype=np.uint8)
    out[:,:,:3] = rgb
    out[:,:,3] = mask
    
    # Crop to the bounding box of the circle to remove excess empty space
    # (Optional, but usually good for icons)
    # x1 = max(0, center[0] - radius)
    # y1 = max(0, center[1] - radius)
    # x2 = min(img.shape[1], center[0] + radius)
    # y2 = min(img.shape[0], center[1] + radius)
    # cropped = out[y1:y2, x1:x2]
    
    # Save the processed image
    cv2.imwrite('assets/app_icon_round.png', out)
    print("Saved to assets/app_icon_round.png")
else:
    print("No contours found.")
