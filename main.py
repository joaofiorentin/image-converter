from PIL import Image
import pillow_heif
import os

diretorio = 'caminho/para/meu/diretorio'
files = [f for f in os.listdir(diretorio) if f.lower().endswith('.heic')]

output_dir = os.path.join(diretorio, 'output')
os.makedirs(output_dir, exist_ok=True)

for filename in files:
    input_path = os.path.join(diretorio, filename)
    output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.jpg')

    try:
        heif_file = pillow_heif.open_heif(input_path)
        image = Image.frombytes(
            heif_file.mode, heif_file.size, heif_file.data, "raw", heif_file.mode
        )
        image.convert('RGB').save(output_path, "JPEG")

        print(f"Convertido: {filename} -> {output_path}")

    except Exception as e:
        print(f"Erro ao processar {filename}: {e}")

print("Conversão concluída!")
