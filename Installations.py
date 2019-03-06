
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        from pip._internal import main as pip2
        pip2(['install', package])


  install('pyodbc')
  install('pandas')
  install('numpy')
  install('sqlalchemy')
  install('sqlite3')
  
  
  
