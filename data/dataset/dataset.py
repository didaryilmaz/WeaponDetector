import os

# YAML dosyasının hedef yolu
yaml_path = '/Users/didaryilmaz/Documents/GitHub/WeaponDetector/data/dataset/dataset.yaml'

# Dizini kontrol edip oluştur
os.makedirs(os.path.dirname(yaml_path), exist_ok=True)

# YAML içeriği
yaml_content = """
path: /Users/didaryilmaz/Documents/GitHub/WeaponDetector/data/dataset
train: images/train
val: images/test

names:
  0: weapon
  1: knife
"""

# Dosyayı oluşturma
with open(yaml_path, 'w') as file:
    file.write(yaml_content)

print(f"dataset.yaml dosyası başarıyla oluşturuldu: {yaml_path}")
