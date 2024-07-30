import win32com.client
import os


def change_lnk_target(lnk_path, new_target, path_to_change):
    # Crea un objeto Shell
    shell = win32com.client.Dispatch("WScript.Shell")
    
    # Carga el archivo .lnk
    shortcut = shell.CreateShortCut(lnk_path)
    if path_to_change in shortcut.TargetPath:
        index_truncated = len(path_to_change)
        # Cambia la ruta de destino
        print(f"\n{new_target}{shortcut.TargetPath[index_truncated:]}")
        shortcut.TargetPath = new_target+shortcut.TargetPath[index_truncated:]
        
    
    # Guarda el archivo .lnk con la nueva ruta
    shortcut.Save()


def find_lnk_files(directory):
    """
    Devuelve una lista con todos los archivos .lnk en el directorio especificado.

    :param directory: Ruta del directorio donde buscar archivos .lnk
    :return: Lista de rutas completas de los archivos .lnk encontrados
    """
    lnk_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.lnk'):
                lnk_files.append(os.path.join(root, file))
    return lnk_files


