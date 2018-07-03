#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

print('\n-------- H-ENCORE HELPER V0.1 --------')
print('\nHecho por Lord_Friky.')
print('Basado en HiyaCFW Helper de jerbear64.')
print('\n--------------------------------------')

if os.name == 'nt':
    print('\nSistema operativo detectado: Windows!')
elif os.name == 'posix':
    print('\nSistema operativo detectado: macOS!')
else:
    print('\nSistema operativo detectado: Otro')

print('\nVerificando...')

windependencies = ['psvmd-decrypt.exe', "psvimg-keyfind.exe", "psvimg-extract.exe", "psvimg-create.exe", "cygz.dll", "cygwin1.dll", "cygintl-8.dll", "cygiconv-2.dll", "cyggpg-error-0.dll", "cyggcrypt-20.dll"]
otherdependencies = ['psvmd-decrypt', "psvimg-keyfind", "psvimg-extract", "psvimg-create"]

try:
    if sys.version_info.major != 3:
        raise Exception('Se requiere Python 3 para ejecutar este script. Tú estás usando: {}.{}.{}'.format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro))
    if os.name == 'nt':
        char = "\\"
    else:
        char = "/"

    if os.getcwd().split(char)[-1].replace("\\", "") != 'h-encore':
        raise Exception('El script no está alojado en la carpeta "h-encore". Por favor, pon este script en el directorio correcto antes de proceder.')
    if os.name == 'nt':
        for dependency in windependencies:
            if not os.path.isfile(dependency):
                raise Exception('El archivo {} no ha sido encontrado. ¿Has bajado la versión correcta de psvimgtools?'.format(dependency))
    else:
        for dependency in otherdependencies:
            if not os.path.isfile(dependency):
                raise Exception('El archivo {} no ha sido encontrado. ¿Has bajado la versión correcta de psvimgtools?'.format(dependency))
except Exception as e:
    print('¡Verificación fallida! {}'.format(e))
    input('Pulsa enter para continuar...')
    sys.exit()

print('¡Verificación completada!')

if sys.version_info.minor != 6:
        print('\nEste script sólo ha sido probado en Python 3.6. Puede funcionar en otras versiones, pero por favor actualiza Python si el script falla.\nTú versión de Python es: {}.{}.{}'.format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro))
        input('Pulsa enter para continuar...')

print('\nIngresa tu llave:')
AIDkey = input()

print('\nEncriptando app...')
if os.name == 'nt':
    print('\n------------------- app -------------------\n')
    subprocess.call(["psvimg-create.exe", "-n", "app", "-K", f"{AIDkey}", "app", "PCSG90096/app"])
    print('\n------------------- appmeta -------------------\n')
    subprocess.call(["psvimg-create.exe", "-n", "appmeta", "-K", f"{AIDkey}", "appmeta", "PCSG90096/appmeta"])
    print('\n------------------- licence -------------------\n')
    subprocess.call(["psvimg-create.exe", "-n", "license", "-K", f"{AIDkey}", "license", "PCSG90096/license"])
    print('\n------------------- savedata -------------------\n')
    subprocess.call(["psvimg-create.exe", "-n", "savedata", "-K", f"{AIDkey}", "savedata", "PCSG90096/savedata"])
else:
    print('\n------------------- app -------------------\n')
    subprocess.call(["./psvimg-create", "-n", "app", "-K", f"{AIDkey}", "app", "PCSG90096/app"])
    print('\n------------------- appmeta -------------------\n')
    subprocess.call(["./psvimg-create", "-n", "appmeta", "-K", f"{AIDkey}", "appmeta", "PCSG90096/appmeta"])
    print('\n------------------- licence -------------------\n')
    subprocess.call(["./psvimg-create", "-n", "license", "-K", f"{AIDkey}", "license", "PCSG90096/license"])
    print('\n------------------- savedata -------------------\n')
    subprocess.call(["./psvimg-create", "-n", "savedata", "-K", f"{AIDkey}", "savedata", "PCSG90096/savedata"])

print('\nPor favor revisa los logs en búsqueda de algún error que se haya podido cometer.')
print('Copia la carpeta PCSG90096 dentro de tu ruta configurada de apps de PS VITA en QCMA (comúnmente la encontrarás como PS Vita/APP/xxxx-tu-aid-xxxx/).')
print('Finalmente copia la app de h-encore a tu dispositivo y estarás listo para disfrutar de HENkaku :)')
input('\nPulsa enter para salir...')
sys.exit()
