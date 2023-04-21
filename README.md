# MontionDetective
Detecção e Rastreio de Pessoas em Vídeo

## Descrição
Este projeto consiste em uma aplicação que utiliza técnicas de detecção e rastreio de objetos para identificar e acompanhar pessoas em um vídeo. O objetivo é fornecer uma solução para monitorar locais públicos, por exemplo, para garantir a segurança em eventos, shoppings, escolas, etc.

## Funcionalidades
Detectar e rastrear pessoas em um vídeo; <br>
Exibir o vídeo com as pessoas marcadas e rastreadas; <br>
Salvar o vídeo com as pessoas marcadas e rastreadas para análise posterior; <br>
Permitir a analise comportamental das pessoas no vídeo, como quantidade de pessoas, tempo em vídeo, velocidade de movimento; <br>

## Tecnologias Utilizadas
Python 3 <br>
OpenCV <br>
TensorFlow <br>
YOLOv8 <br>
PyQt5 <br>

## Estrutura do Projeto

[apenas exemplo - será modificado]

main.py: ponto de entrada do programa, contém a lógica principal;
detector.py: módulo responsável por detectar as pessoas em um quadro do vídeo;
tracker.py: módulo responsável por rastrear as pessoas detectadas entre os quadros do vídeo;
video.py: módulo para lidar com leitura, gravação e exibição do vídeo;
settings.py: arquivo para ajuste de parâmetros do sistema;
templates/ (opcional): pasta com arquivos HTML para a interface web;
static/ (opcional): pasta com arquivos CSS, JS, imagens, etc., para a interface web.

## Como Utilizar
Clone o repositório em sua máquina local; <br>
Instale as dependências listadas no arquivo requirements.txt; <br>
Execute o arquivo main.py; <br>
Escolha o vídeo de entrada; <br>
Ajuste os parâmetros, se necessário; <br> 
Assista ao vídeo com as pessoas marcadas e rastreadas. <br>

## Contribuição
Contribuições são bem-vindas! Para reportar bugs, sugestões de melhorias ou novas funcionalidades, por favor, crie uma issue no GitHub. Para enviar correções ou novas funcionalidades, por favor, crie um pull request e descreva suas alterações.

## Licença
Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.
