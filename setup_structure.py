import os

# Define folder structure
folders = [
    "notebooks",
    "models",
    "docs",
    "outputs/cluster_plots"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Optionally create empty README and requirements file
with open("README.md", "w") as f:
    f.write("# Unsupervised Customer Segmentation\n\nProject summary goes here.")

with open("requirements.txt", "w") as f:
    f.write("# Required libraries\npandas\nscikit-learn\nmatplotlib\nseaborn\nplotly\nmlxtend")

print("✅ Folder structure created.")
