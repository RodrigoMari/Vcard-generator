# Vcard Generator

Este proyecto genera archivos de contactos en formato vCard a partir de datos de un archivo Excel. Los datos incluyen información como teléfono, canal, categoría y código. Está diseñado para ser fácil de usar y probado con carga masiva de contactos.

## Requisitos

Antes de ejecutar el proyecto, necesitarás tener instalado lo siguiente:

**Deberá bajar en la pagina hasta casi el final y apretar [DESCARGAR] a la derecha de donde dice [Build Tools para Visual Studio 2022]**
- [Instalador visual studio build tools](https://visualstudio.microsoft.com/es/downloads/?q=build+tools)

No se incluyó en el archivo ejecutable debido a que requiere permisos de administrador

## Uso

1. **Clonar el repositorio o descargar el ZIP**:

   Si no tenes Git, podes descargar el archivo ZIP desde GitHub.

   - Descargar ZIP desde GitHub: [Vcard Generator en GitHub](https://github.com/RodrigoMari/Vcard-generator)
   - O clona el repositorio usando Git:

     ```sh
     git clone https://github.com/RodrigoMari/Vcard-generator.git
     ```

2. **Navegar al directorio del proyecto**:

   Una vez descargado el proyecto, descomprima el archivo zip y entre a la carpeta

3. **Carga de datos**
   
   - En dicho directorio encontrará una carpeta llamada "Archivos_necesarios", metase
   - Encontrará 3 archivos:
      - **contactos.vcf**: archivo con todos los contactos que deberá abrir con el celular al final de estos pasos
      - **Maestro.xlsx**: excel en el que se cargaran los datos con el siguiente formato
         - **Canal**: opciones disponibles["ALMACENES", "AUTOSERVICIOS", "CORPORATIVOS", "DIETETICAS", "ESTABL. EDUCATIVOS", "ESTACIONES DE SERVIC", "KIOSCOS", "NO TRADICIONALES"]
         - **Categoria**: opciones disponibles["CLIENTE A", "CLIENTE B1", "CLIENTE B2", "CLIENTE C", "CLIENTE D"]
         - **Codigo**: cantidad aleatoria de 0's y el codigo del cliente
         - **Telefono**: 3 guiones medios separados por un espacio en el que **despues de cada guion** se va encontrar el codigo de pais, el codigo de area y el teléfono respectivamente. Para que sea un teléfono válido alcanza con tener al menos ingresado el teléfono
      - **Maestro_limpio**: excel que va a tener los datos del maestro limpios para su guardado. Si quiere ver cómo es su versión final puede abrirlo luego de ejecutar el ejecutable

4. **Ejecutar archivo final**
   
   Dentro del directorio principal encontrará el archivo ejecutable llamado "Vcard.bat" al que deberá darle doble click. Este archivo reproduce varios pasos en consola, entre ellos descargar python, pip y las dependencias necesarias, por lo que deberá ser paciente. No debe temer de dichas descargas ya que, ademas de ser aplicaciones de Microsoft, se ejecutan en un entorno virtual ajeno a su computadora (cuando termine sera borrado todo lo instalado)

   [URGENTE] **Hay un error de descarga con python en el que luego de su descarga se cierra la consola, simplemente debe darle nuevamente doble click al ejecutable**

5. **Pasar el archivo creado a su telefono**

   Métase a la carpeta llamada "Archivos_necesarios", ahí encontrará el archivo **contactos.vcf**, archivo que deberá pasarle al telefono que quiere agendar todos los contactos (el método más sencillo es mediante Whatsapp). 
   
   Acto seguido apriete el archivo en su celular, dandole la opcion de agendarlos a todos
