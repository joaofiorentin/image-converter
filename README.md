# Conversor de Imagens em Python (Ex: HEIC para PNG)

Este projeto tem como objetivo desenvolver um **conversor de imagens** em Python, capaz de converter imagens de diferentes formatos, como **HEIC** para **PNG**, **JPEG**, **TIFF**, entre outros. O projeto utiliza bibliotecas Python para manipulação e conversão de imagens de maneira eficiente e simples.

## Objetivos do Projeto:
- **Conversão de Formatos de Imagens**: Desenvolver uma ferramenta para converter imagens entre diferentes formatos (ex: HEIC, PNG, JPEG, TIFF).
- **Suporte a Diversos Formatos**: Implementar suporte para formatos de imagem comuns e menos comuns, incluindo formatos de imagens de câmeras modernas como **HEIC** (High Efficiency Image Coding).
- **Facilidade de Uso**: Oferecer uma interface simples para que usuários possam facilmente converter imagens com apenas alguns comandos.

## Funcionalidades Implementadas:
- **Conversão de HEIC para PNG**: Utiliza bibliotecas Python para converter imagens no formato **HEIC** (usado principalmente em dispositivos Apple) para o formato **PNG**, que é amplamente compatível.
- **Conversão entre outros formatos populares**: Suporte para conversão entre formatos como **JPEG**, **TIFF**, **BMP**, e **GIF**.
- **Manipulação de Qualidade**: Opção de ajustar a qualidade da imagem durante a conversão, mantendo um bom equilíbrio entre qualidade e tamanho do arquivo.
- **Interface de Linha de Comando (CLI)**: Permite que o usuário execute a conversão diretamente do terminal ou prompt de comando, tornando o processo rápido e fácil.
- **Automação**: Permite a conversão em lote de várias imagens de uma vez, sem a necessidade de intervenção manual para cada arquivo.

## Tecnologias Utilizadas:
- **Python**: Linguagem principal para o desenvolvimento do conversor de imagens.
- **Pillow**: Biblioteca Python para abertura, manipulação e conversão de imagens.
- **pyheif**: Biblioteca para suporte ao formato **HEIC**, usada para abrir e converter arquivos HEIC.
- **os**: Para manipulação de arquivos e diretórios no sistema operacional.
- **argparse**: Para criar a interface de linha de comando (CLI), permitindo que o usuário forneça parâmetros de conversão de maneira simples.
