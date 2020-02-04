# -*- mode: python -*-

block_cipher = None

added_files = [
    ('user_interface/home_screen_pic.png','user_interface'),
    ('user_interface/hash_app_icon.ico','user_interface')
]

a = Analysis(['hash_app.py'],
             pathex=[],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='hash_app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , 
          icon='user_interface/hash_app_icon.ico')
