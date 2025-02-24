import json
from pathlib import Path
from PIL import Image
import numpy as np

def calculate_metrics(image_path):
    """
    Calculates image metrics given a JSON file path.

    Args:
        json_file_path: Path to the JSON file containing image comparison data.

    Returns:
        A dictionary containing the calculated metrics.  Returns None if file
        does not exist or has errors
    """

    try:
        # Load the image
        img = Image.open(image_path)
        img_array = np.array(img)

        # Assuming white pixels represent background and black pixels represent mismatches
        total_pixels = img_array.size
        mismatched_pixels = np.sum(img_array == 0)  # Count black pixels

        # Calculate mismatch percentage
        mismatch_percentage = (mismatched_pixels / total_pixels) * 100 if total_pixels > 0 else 0

        # Extract height and width
        height, width = img_array.shape

        results = {
            "image_path": str(image_path),
            "total_pixels": total_pixels,
            "mismatched_pixels": mismatched_pixels,
            "mismatch_percentage": mismatch_percentage,
            "height": height,
            "width": width,
            }
        return results
    except FileNotFoundError:
        print(f"Error: File not found at {image_path}")
        return None
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

# image comparison paths
image_paths = [
    "010-py_05-train-example_1.png",
    "010-py_05-train-example_2.png",
    "010-py_05-train-example_3.png",
]

# gather metrics for each image and add to list
image_metrics = []
for path in image_paths:
    image_metrics.append(calculate_metrics(path))
print(json.dumps(image_metrics, indent=2))