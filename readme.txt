Definir parametros en gsi-parametros.sty, hay tres: Autor, asignatura y carrera.

Compilacion condicionada:

\IfStrEq{\modo}{MASTER-INDUSTRIALES}{
    Codigo LaTeX aqui
}{}

Para meter en todo menos MASTER-INDUSTRIALES:

\IfStrEq{\modo}{MASTER-INDUSTRIALES}{}
{
	Codigo LaTeX aqui
}

Se puede generar PDF con 4 diapositivas por pagina se puede utilizar:

pdfnup --nup 2x2 --scale 0.9 --no-landscape --delta "1cm 8cm" mi-archivo.pdf 

Se puede cambiar el parametro --nup para dar el layout que prefiramos, --no-landscape para controlar si se pone apaisado o no, y --delta para modificar los margenes.

Puede realizarse fusiones de diapositivas masivamente mediante un bucle en shell script:

for I in *; do  pdfnup --nup 2x2 --scale 0.9 --no-landscape --delta "1cm 8cm" $I; done

Poner en * una expresion regular para localizar los PDFs que queremos tratar.
