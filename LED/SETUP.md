# Configuração e Instalação 

Este guia auxiliará você a configurar o ambiente necessário para rodar o detector de Libras.

## Pré-requisitos
Certifique-se de ter o **Python 3.8** ou superior instalado em sua máquina.

## Instale facilmente utilizando

    ```bash
    pip install -r requirements.txt
    ```
## Passo a Passo

1. **Clone o repositório:**

   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio
   ```
2. **Crie um ambiente virtual (Opcional, mas recomendado):**

    ```bash
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No Linux/Mac: 
    source venv/bin/activate
    ```
3. **Instale as dependências:**
O projeto utiliza OpenCV para processamento de imagem e MediaPipe para a detecção dos pontos da mão.

    ```bash
    pip install opencv-python mediapipe
    ```
4. **Execute o projeto**

    ```bash
    python detector.py
    ```
5. **Modelos Necessários**

1. Baixe o arquivo [hand_landmarker.task](https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task).

2. Salve-o na raiz do projeto (mesma pasta do arquivo `detector.py`).