### Computação Cognitiva - Reconhecimento Automático de Placas de Carro usando algoritmos de OCR

Dataset público do Kaggle: https://www.kaggle.com/datasets/andrewmvd/car-plate-detection

Nesse projeto, foi-se utilizado 4 algoritmos diferentes de OCR (Optical Character Recognition) a fim de realizar uma comparação e identificar qual seria o melhor para o dataset que está sendo utilizado. O diagrama abaixo demonstra o processo desenvolvido para checar a essas comparações e como foi o fluxo de trabalho proposto.

![Diagrama do Projeto](https://imgur.com/Iwwj8rq)

### Como utilizar o código

O código foi construído no Google Colab, então precisamos utilizar para que algumas coisas dentro do código deem certo, como a parte da criação dos diretórios, etc.

Essa classe criada contém duas propostas de solução:

    1. Abordagem mais clássica, usando detecção de borda (OpenCV) para identificar as placas de carro e depois disso se foi usado easyOCR para a transcrição da imagem para texto.

        Para a utilização dessa solução, basta passar o comando abaixo, rodando a classe que está em [final_class.py]

        *Lembre-se que nesses métodos, precisa do dataset com as imagens originais, do próprio dataset provido do kaggle.

        -> Car().OpenCVeasy(path = "/content/dataset/images", folder_name = "detection_classic", show_steps = False)

        onde 

            * path = local onde foi colocado o dataset
            * folder_name = nome da pasta que será criada e alocada os resultados do script
            * show_steps = bom método para quando está utilizando uma detecção manual, onde pode mostrar o passo a passo do que está ocorrendo com a imagem para ser transcrita.

    2. A segunda utilizando yolov5, fazendo o treinamento do modelo e utilizando o próprio recurso do yolo para fazer o recorte das imagens onde estão as placas das respectivas imagens. Após isso, tem-se três opções para a extração dos caracteres das placas, usando EasyOCR, Pytesseract ou KerasOCR.

        Para a utilização dessa solução, basta passar o comando abaixo, rodando a classe que está em [final_class.py]

        *Lembre-se que nesses métodos, precisa do dataset com a imagens recortadas devidamente, utilizando o [yolo_cropped_images.ipynb] para isso.

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








