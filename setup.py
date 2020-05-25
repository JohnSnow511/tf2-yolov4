from setuptools import find_packages, setup


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="tf2_yolov4",
    version="0.0.1",
    description="TensorFlow 2.x implementation of YOLOv4",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sicara/tf2-yolov4",
    license="MIT",
    install_requires=["tensorflow-addons>=0.10.0"],
    extras_require={"publish": ["bumpversion>=0.5.3", "twine>=1.13.0"],},
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
