# -*- mode: python -*-
a = Analysis(['EPIC_grader.py'],
             pathex=['/Users/jamiecounsell/Dropbox (Personal)/Developer/EPIC_grader'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='EPIC_grader',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='EPIC_grader')
