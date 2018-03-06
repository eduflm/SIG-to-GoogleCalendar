# SIG-to-GoogleCalendar

## Um script em python para pegar os horários de aula do SIG e converter para um arquivo .csv para ser usado no Google Agenda

[English Documentation](https://github.com/LimaEduardo/SIG-to-GoogleCalendar/tree/master/docs/englishDoc.md)

### Pré-requisitos

O que você precisa para rodar esse script

```
Python 3.x.x

Beautiful Soup 4
pip install beautifulsoup4

Numpy
pip install numpy

urllib3
pip install urllib3
```

### Rodando

Apenas rode no terminal

``` python3 sigToCalendar.py ```

Você vai precisar fornecer algumas informações para rodar o script

* Login - Seu login do SIG
* Password - Sua senha do SIG
* Start Date - A partir de qual dia você quer replicar seus horários
* End Date - Até que dia você quer replicar seus horários

Depois disso, um arquivo .csv vai ser gerado. Vá em "calendar.google.com > Importar > Selecionar um arquivo do seu computador" e escolha o arquivo .csv gerado.

É fortemente recomendado criar uma nova agenda para importar o arquivo .csv


### Contribuindo

Sinta-se a vontade para dar feedback, abrir novas issues e pull requests
