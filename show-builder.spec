# PyInstaller spec for Show Builder — builds a single-file desktop app that
# bundles the templates + brand presets so it runs with no install.
#   pyinstaller show-builder.spec
# Produces dist/"Show Builder"(.exe on Windows). On macOS also emits a .app.
block_cipher = None

a = Analysis(
    ['show_builder.py'],
    pathex=[],
    binaries=[],
    datas=[('templates', 'templates'), ('brands', 'brands')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz, a.scripts, a.binaries, a.zipfiles, a.datas, [],
    name='Show Builder',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    runtime_tmpdir=None,
    console=False,          # windowed app — no terminal window
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# macOS: wrap the binary in a .app bundle
app = BUNDLE(
    exe,
    name='Show Builder.app',
    icon=None,
    bundle_identifier='com.harriseventgroup.showbuilder',
)
