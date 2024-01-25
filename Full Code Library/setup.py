

from setuptools import setup

APP_NAME = 'DaYa Car Analytics'
APP = ['main.py']
# DATA_FILES = []
DATA_FILES = [('Testicle', ['Testicle/'])]
OPTIONS = {
    'iconfile': 'icon.icns',
    # 'argv_emulation': True,
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': 'Desktop Founds Control',
        'CFBundleVersion': '0.1.0 stable',
        'CFBundleShortVersionString': '0.1.0',
        'NSHumanReadableCopyright': 'Copyright (c) 2023, DaYa Company, All Rights Reserved'
    }
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
