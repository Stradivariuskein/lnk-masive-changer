import argparse
import sys
from utils import find_lnk_files, change_lnk_target

def main(target_folder, path_to_change, new_path):
    print(f"Directorio de destino: {target_folder}")
    print(f"Ruta a cambiar: {path_to_change}")
    print(f"Nueva ruta: {new_path}")

    files = find_lnk_files(target_folder)

    for file in files:
        change_lnk_target(file, new_path, path_to_change)

if __name__ == "__main__":
    # Configura el analizador de argumentos
    parser = argparse.ArgumentParser(description="Script para manejar rutas y archivos.")
    
    # Define los argumentos esperados
    parser.add_argument('--target_folder', type=str, help='Directorio de destino', required=True)
    parser.add_argument('--path_to_change', type=str, help='Ruta a cambiar', required=True)
    parser.add_argument('--new_path', type=str, help='Nueva ruta', required=True)
    
    # Analiza los argumentos
    args = parser.parse_args()
    
    # Llama a la función principal con los argumentos
    main(args.target_folder, args.path_to_change, args.new_path)
