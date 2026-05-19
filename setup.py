from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="phenofect",
    version="1.0.5", 
    license='MIT',
    author="Songwon Kim",
    author_email="kimsongwon10@korea.ac.kr",
    description="Python Package for Phenology Forecasting and Exploring under ClimaTe change (PhenoFECT) which is Korea and Japan data embedded integrated workflow.",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/SongWon03/PhenoFECT",
    packages=find_packages(),
    include_package_data=True, 
    package_data={
        "phenofect": ["Data/**/*.csv"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.10',
    install_requires=requirements
)

