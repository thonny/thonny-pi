from setuptools import setup
import os.path
import sys

setupdir = os.path.dirname(__file__)

requirements = []
for line in open(os.path.join(setupdir, 'requirements.txt'), encoding="UTF-8"):
    if line.strip() and not line.startswith('#'):
        requirements.append(line)

setup(
      name="thonny-pi-theme",
      version="0.1b1",
      description="Raspberry Pi for Thonny IDE",
      long_description="""UI theme for Thonny IDE, which makes it look more like GTK apps in Raspberry Pi Pixel desktop. 
More info about Thonny: http://thonny.org.""",
      url="https://bitbucket.org/plas/thonny-pi-theme/",
      author="Aivar Annamaa",
	  author_email="aivar.annamaa@gmail.com",
      license="MIT",
      classifiers=[
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: Freeware",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Education",
        "Topic :: Software Development",
        "Topic :: Software Development :: Embedded Systems",
      ],
      keywords="IDE education programming  Thonny Raspberry Pi",
      platforms=["Windows", "macOS", "Linux"],
      python_requires=">=3.4",
	  package_data={'thonnycontrib.pi_theme': ['res/*']},
      install_requires=requirements,
      packages=["thonnycontrib.pi_theme"],
)