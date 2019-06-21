_mssql.__version__
pymssql.__version__
socket.__name__
a = sys.stdout
reload(sys)
sys.setdefaultencoding("utf-8")
# -*- mode: python -*-

block_cipher = None


a = Analysis(['yinpin_inhi_act.py'],
             pathex=['C:\\Users\\Administrator\\PycharmProjects\\inhi'],
             binaries=[],
             datas=[],
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
          name='yinpin_inhi_act',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
