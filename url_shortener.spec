# url_shortener.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['url_shortener.py'],
    pathex=[],
    binaries=[],
    datas=[('E:\\testcopy\\copy.ico', '.')],
    hiddenimports=['pystray._util.win32', 'pystray._win32'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='url_shortener',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to False to hide the console
    icon='E:\\testcopy\\copy.ico'  # Specify the path to your icon file
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='url_shortener'
)

app = BUNDLE(
    coll,
    name='url_shortener',
    icon='E:\\testcopy\\copy.ico',
    onefile=True  # This is the key option for creating a single executable
)
