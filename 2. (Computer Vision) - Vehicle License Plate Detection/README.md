## Computação Cognitiva - Reconhecimento Automático de Placas de Carro usando algoritmos de OCR
![Apresentação e Processo Principal do Projeto](https://i.imgur.com/8KRkaL3.png)

### Introdução
Dataset público do Kaggle: https://www.kaggle.com/datasets/andrewmvd/car-plate-detection

Nesse projeto, foi-se utilizado 4 algoritmos diferentes de OCR (Optical Character Recognition) a fim de realizar uma comparação e identificar qual seria o melhor para o dataset que está sendo utilizado. O diagrama abaixo demonstra o processo desenvolvido para checar a essas comparações e como foi o fluxo de trabalho proposto.

![Diagrama do Projeto](https://i.imgur.com/sZLTmUC.png)

Tecnologias: 
        ```
        Python (Google Colab GPU, Jupyter)
        OpenCV
        YOLOv5
        Algoritmos de OCR (EasyOCR, Pytesseract, KerasOCR)
        ```

### Dificuldades enfrentadas e soluções impostas
O propósito do projeto em geral se resume a duas etapas:
1. Receber o dataset de imagens de carros e analisar a placa de cada uma, realizando um recorte no local correto;
2. Receber as placas de cada carro e transcrever essa imagem para texto, salvando a composição rótulo do carro | placa do carro em .csv

Desse forma, o projeto seria composto apenas pelo conjunto -> detecção de bordas + EasyOCR. Porém, a medida que se foi realizando o projeto, percebeu-se erros tanto na parte do recorte das placas de carro, como no algoritmo de OCR. Nesse sentido, tentou-se uma nova abordagem para fazer esse recorte de uma forma mais automatizada e correta. Para isso, foi-se utilizada o yolov5.

Porém, apenas a nova abordagem de recorte das placas de carro não foram suficientes visualmente para a eficácia e excelência das métricas e valores supostos. Dito isso, foi-se adicionado mais duas técnicas de OCR que foram pytesseract e KerasOCR, em que ambas se mostraram bem melhores do que o EasyOCR. Dentre elas duas, KerasOCR é um algoritmo bem mais minucioso, onde ele consegue analisar mínimos detalhes, o que pode ser bom de uma certa perspectiva e ruim para outra, pois detecta caracteres que em teoria não são relevantes para a análise da placa, como também entende melhor o espaçamento entre palavras da placa de carro, fazendo com que a transcrição da imagem para o texto tenha que passar por uma manipulação para salvar em csv. Já o Pytesseract, a depender da configuração dos parâmetros, mostra-se um bom algoritmo e potencialmente melhor do que o KerasOCR, mas, de início, o Keras é superior.

### Como utilizar o código

O código foi construído no Google Colab, então precisamos utilizar para que algumas coisas dentro do código deem certo, como a parte da criação dos diretórios, etc.

Essa classe criada contém duas propostas de solução:

    1. Abordagem mais clássica, usando detecção de borda (OpenCV) para identificar as placas de carro e depois disso se foi usado easyOCR para a transcrição da imagem para texto.

        Para a utilização dessa solução, basta passar o comando abaixo, rodando a classe que está em [plate_detection.py]

        *Lembre-se que nesses métodos, precisa do dataset com as imagens originais, do próprio dataset provido do kaggle.

        -> Car().OpenCVeasy(path = "/content/dataset/images", folder_name = "detection_classic", show_steps = False)

        onde 

            * path = local onde foi colocado o dataset
            * folder_name = nome da pasta que será criada e alocada os resultados do script
            * show_steps = bom método para quando está utilizando uma detecção manual, onde pode mostrar o passo a passo do que está ocorrendo com a imagem para ser transcrita.

    2. A segunda utilizando yolov5, fazendo o treinamento do modelo e utilizando o próprio recurso do yolov5 para fazer o recorte das imagens onde estão as placas das respectivas imagens, cujo método para a realização dessas imagens para imagens recortadas está na pasta helper. Após isso, tem-se três opções para a extração dos caracteres das placas, usando EasyOCR, Pytesseract ou KerasOCR.

        Para a utilização dessa solução, basta passar o comando abaixo, rodando a classe que está em [plate_detection.py]

        *Lembre-se que nesses métodos, precisa do dataset com a imagens recortadas devidamente, utilizando o helper/[yolo_cropped_images.ipynb] para isso.

        -> Car().YOLOeasy(path = "/content/samples", folder_name = "yolo_easy_detection")
        -> Car().YOLOpytesseract(path = "/content/samples", folder_name = "pytesseract_detection")  
        -> Car().YOLOkeras(path = "/content/samples", folder_name = "keras_detection") 

        onde 

            * path = local onde foi colocado o dataset (nesse caso já é o resultado retornado do crop do yolov5, não o dataset original)
            * folder_name = nome da pasta que será criada e alocada os resultados do script

### Next steps

1. Configurar a parte dos resultados do dataset
2. Realizar pre-processamento para melhorias nas imagens
3. Verificar a existência de uma configuração melhor para o pytesseract (parâmetro)
4. Adicionar métricas para avaliar o desempenho das OCR








