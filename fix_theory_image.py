import os
import re

filepath = "/home/ubuntu/Shine_Academy_Naroda/lib/features/learning/learning_engine/widgets/theory_widget.dart"

with open(filepath, "r") as f:
    content = f.read()

# Replace the placeholder with an actual Image widget
# We will use Image.asset since the images will be stored locally in assets/images/
new_image_code = """
            ClipRRect(
              borderRadius: BorderRadius.circular(12),
              child: Image.asset(
                visualUrl,
                width: double.infinity,
                height: 250,
                fit: BoxFit.cover,
                errorBuilder: (context, error, stackTrace) {
                  return Container(
                    color: Colors.grey[200],
                    height: 150,
                    child: Center(
                      child: Text("Image missing: $visualUrl", style: const TextStyle(color: Colors.grey)),
                    ),
                  );
                },
              ),
            ),
"""

old_placeholder_code = """
            ClipRRect(
              borderRadius: BorderRadius.circular(12),
              child: Container(
                color: Colors.grey[200],
                width: double.infinity,
                height: 150,
                child: const Center(
                  child: Text(
                    "Image Placeholder",
                    style: TextStyle(color: Colors.grey),
                  ),
                ),
              ),
            ),
"""

if old_placeholder_code.strip() in content:
    content = content.replace(old_placeholder_code.strip(), new_image_code.strip())
else:
    # Just a basic regex if exact match fails
    content = re.sub(r"ClipRRect\([\s\S]*?Image Placeholder[\s\S]*?\),", new_image_code.strip() + ",", content)

with open(filepath, "w") as f:
    f.write(content)

print("Updated TheoryWidget to support real images.")
