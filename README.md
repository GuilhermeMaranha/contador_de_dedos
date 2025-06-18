-Contador de Dedos com Visão Computacional e IA
Este projeto é uma aplicação prática que utiliza Visão Computacional e Inteligência Artificial para contar o número de dedos levantados em uma mão, em tempo real, usando a webcam. Resolve um problema cotidiano demonstrando a interação entre IA e o ambiente.


-Descrição do Projeto
O objetivo é detectar e contar os dedos de uma mão em tempo real. A aplicação captura o vídeo da webcam, usa modelos de IA para identificar a mão e 21 pontos de referência (landmarks), e então, com base na posição desses pontos, determina e exibe quantos dedos estão levantados.


-Tecnologias Utilizadas
Python: Linguagem principal do desenvolvimento.
OpenCV (cv2): Biblioteca para Visão Computacional, usada para captura de vídeo, processamento de frames e exibição.
MediaPipe (mediapipe): Framework do Google para IA, especificamente MediaPipe Hands, que fornece os modelos de detecção de mãos e estimativa de marcos 3D.


-Instalação e Dependências
Obtenha o arquivo contador_dedos.py.
Instale as dependências via pip: pip install opencv-python mediapipe
Execute o script Python: python contador_dedos.py


-Explicação das Técnicas de IA Envolvidas
O MediaPipe Hands, da Google, utiliza uma CNN pré-treinada para identificar 21 landmarks por mão em tempo real. Com essas informações de posição, o código calcula a quantidade de dedos levantados com base na geometria dos pontos.

Modelo de Detector de Palma/Mão: Detecta a presença de mãos na imagem.

Modelo de Estimativa de Marcos da Mão : Após a detecção, prevê a localização de 21 landmarks em 3D na mão.


-Lógica de Contagem Baseada em landmarks (Pós-IA): A partir dos 21 landmarks fornecidos pela IA, uma lógica programática simples analisa as coordenadas:
Dedos (exceto polegar): Compara a posição Y da ponta do dedo com a articulação abaixo.
Polegar: Compara a diferença na posição X da ponta do polegar com a articulação próxima, verificando seu afastamento.
Essa combinação de modelos de IA pré-treinados com lógica programática permite a contagem eficaz de dedos em tempo real.
