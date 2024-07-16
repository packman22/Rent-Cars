Con esta aplicación se utiliza las capacidades y servicios que brinda Tableau Server y Tableau Prep como herramienta de ETL (Extract, Transform and Load) para inyectar información a Tenebit CRM.
Las integraciones con aplicaciones tipo ERP, por lo general incluye la información de Clientes, Facturas e Inventarios Valorizados.

## Preparación del Entorno de desarrollo
Estos comando se corren una sola vez al inicio del proyecto:

Crear Entorno Python por primera vez
```bash
virtualenv python3.12 -m venv rent-cars-env   
```

Iniciar el Entorno
```bash
source rent-cars-env/bin/activate
```

Instalar librerías requeridas del archivo requirementes.txt
```bash
pip install -r requirements.txt 
```

## Inicializar el Entorno de Desarrollo
Iniciar el entorno
```bash
source rent-cars-env/bin/activate
```

Detener el entorno
```bash
deactivate
```

## Crear y compilar máquina Docker
Para construir la aplicación en el entorno Docker. Esto se debe hacer cada vez que se suba un cambio
```bash
docker build --tag myapp .
```

Lanzar la aplicación utilizando la máquina virtual de Docker
```bash
docker run --rm -ti myapp
```



## Uso

### Elaborar las definiciones de tablas
En el archivo main.py encuentran 3 variables: clientes_table, facturas_cabecera_table, facturas_items_table. Cada definición de tablas corresponde a la forma como llega la información desde el ERP del Cliente.

Lo primero que debemos hacer es modificar estas variables para ajustarlas a la realidad de la integración.

### Modificar los métodos de integración clienteservice.py


## Resolución de problemas comunes
Tener en cuenta que los Personal Access Token se vencen después de 15 días de no uso o al año. Para crear uno nuevo se debe ir a la configuración de mi cuenta en el servidor de Tableau

## Contribuir
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)


Para casos arquitectura ARM (Macbook M1, M2...) se debe utilizar estos comandos tanto para instalar como para correr el script

arch -x86_64 /usr/bin/python3 -m pip install tableauhyperapi
arch -x86_64 /usr/bin/python3 main.py






