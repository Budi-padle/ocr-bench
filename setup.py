from setuptools import setup, find_packages

setup(
    name='ocr-bench',
    version='0.1.0',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=['pillow', 'numpy'],
)
