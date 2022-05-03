import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['src/main.py','-F']
    run(opts)