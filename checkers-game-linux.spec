# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['checkersMain.py'],
    pathex=[],
    binaries=[],
    datas=[('checkers', 'checkers')],
    hiddenimports=[
        'checkers',
        'checkers.board',
        'checkers.game', 
        'checkers.piece',
        'checkers.constants',
        'minimax',
        'minimax.algorithm',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Checkers-Game',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Allow console on Linux (for error messages)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)