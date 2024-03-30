#Classificação de imagens do zero

#Descrição: Treinamento de um classificador de imagens do zero no conjunto de dados Kaggle Cats vs Dogs.

#Introdução
#Este exemplo mostra como fazer a classificação de imagens do zero, começando com arquivos de imagem JPEG no disco, sem aproveitar pesos pré-treinados ou um modelo de aplicativo Keras pré-fabricado. Demonstramos o fluxo de trabalho no conjunto de dados de classificação binária Kaggle Cats vs Dogs.
#Usamos o image_dataset_from_directoryutilitário para gerar os conjuntos de dados e usamos camadas de pré-processamento de imagem Keras para padronização de imagens e aumento de dados.

#Importando as bibliotecas 
import os
import numpy as np
import keras
from keras import layers
from tensorflow import data as tf_data
import matplotlib.pyplot as plt

#Download dos arquivos 
#Dezipando
#Exibindo
#!curl -O https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip
#!unzip -q kagglecatsanddogs_5340.zip
#!ls
#!ls PetImages

#Filtre imagens corrompidas
#Ao trabalhar com muitos dados de imagens do mundo real, imagens corrompidas são uma ocorrência comum. Vamos filtrar imagens mal codificadas que não apresentam a string "JFIF" em seu cabeçalho.
PetImages= 'D:/Dados/kagglecatsanddogs_5340/PetImages'
num_skipped = 0
for folder_name in ("Cat", "Dog"):
    folder_path = os.path.join(PetImages, folder_name)
    for fname in os.listdir(folder_path):
        fpath = os.path.join(folder_path, fname)
        try:
            fobj = open(fpath, "rb")
            is_jfif = b"JFIF" in fobj.peek(10)
        finally:
            fobj.close()

        if not is_jfif:
            num_skipped += 1
            # Delete corrupted image
            os.remove(fpath)

print(f"Deleted {num_skipped} images.")

#Gere um Dataset
image_size = (180, 180)
batch_size = 128

train_ds, val_ds = keras.utils.image_dataset_from_directory(
    PetImages,
    validation_split=0.2,
    subset="both",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)

#Visualize os dados
plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(np.array(images[i]).astype("uint8"))
        plt.title(int(labels[i]))
        plt.axis("off")

#Usando aumento de dados de imagem
#Quando você não tem um grande conjunto de dados de imagens, é uma boa prática introduzir artificialmente a diversidade de amostras aplicando transformações aleatórias, porém realistas, às imagens de treinamento, como inversão horizontal aleatória ou pequenas rotações aleatórias. Isso ajuda a expor o modelo a diferentes aspectos dos dados de treinamento, ao mesmo tempo que retarda o overfitting.
data_augmentation_layers = [layers.RandomFlip("horizontal"),layers.RandomRotation(0.1),]


def data_augmentation(images):
    for layer in data_augmentation_layers:
        images = layer(images)
    return images

#Vamos visualizar a aparência das amostras aumentadas, aplicando-as data_augmentation repetidamente às primeiras imagens do conjunto de dados:
plt.figure(figsize=(10, 10))
for images, _ in train_ds.take(1):
    for i in range(9):
        augmented_images = data_augmentation(images)
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(np.array(augmented_images[0]).astype("uint8"))
        plt.axis("off")


#Padronizando os dados
#Nossas imagens já estão em tamanho padrão (180x180), pois estão sendo produzidas em float32lotes contíguos por nosso conjunto de dados. No entanto, os valores dos canais RGB estão dentro do [0, 255]intervalo. Isto não é ideal para uma rede neural; em geral, você deve tentar diminuir os valores de entrada. Aqui, padronizaremos os valores [0, 1]usando uma Rescalingcamada no início do nosso modelo.
#Duas opções para pré-processar os dados
#Existem duas maneiras de usar o data_augmentationpré-processador:

#Opção 1: Torne-o parte do modelo , assim:
#Com esta opção, o aumento dos seus dados acontecerá no dispositivo , de forma síncrona com o restante da execução do modelo, o que significa que ele se beneficiará da aceleração da GPU.
#Observe que o aumento de dados está inativo no momento do teste, portanto, as amostras de entrada só serão aumentadas durante fit(), não ao chamar evaluate()ou predict().
#Se você estiver treinando em GPU, esta pode ser uma boa opção.
#input_shape = (28, 28, 1)  # Para imagens de 28x28 pixels em escala de cinza
#inputs = keras.Input(shape=input_shape)
#x = data_augmentation(inputs)
#x = layers.Rescaling(1./255)(x)
#...  # Rest of the model

#Opção 2: aplique ao conjunto de dados , de modo a obter um conjunto de dados que produza lotes de imagens aumentadas, assim:
#Com esta opção, o aumento de seus dados acontecerá na CPU , de forma assíncrona, e será armazenado em buffer antes de entrar no modelo.
#Se você estiver treinando em CPU, esta é a melhor opção, pois torna o aumento de dados assíncrono e sem bloqueio.
#No nosso caso, optaremos pela segunda opção. Se você não tiver certeza de qual escolher, esta segunda opção (pré-processamento assíncrono) é sempre uma escolha sólida.
augmented_train_ds = train_ds.map(lambda x, y: (data_augmentation(x, training=True), y))

#Configure o conjunto de dados para desempenho
#Vamos aplicar o aumento de dados ao nosso conjunto de dados de treinamento e usar a pré-busca em buffer para que possamos gerar dados do disco sem que a E/S se torne um bloqueio:
# Apply `data_augmentation` to the training images.
train_ds = train_ds.map(lambda img, label: (data_augmentation(img), label),num_parallel_calls=tf_data.AUTOTUNE,)
# Prefetching samples in GPU memory helps maximize GPU utilization.
train_ds = train_ds.prefetch(tf_data.AUTOTUNE)
val_ds = val_ds.prefetch(tf_data.AUTOTUNE)

#Construiremos uma versão pequena da rede Xception. Não tentamos particularmente otimizar a arquitetura; se você quiser fazer uma busca sistemática pela melhor configuração do modelo, considere usar KerasTuner .
#Observe que:
#Iniciamos o modelo com o data_augmentationpré-processador, seguido de uma Rescalingcamada.
#Incluímos uma Dropoutcamada antes da camada de classificação final.
def make_model(input_shape, num_classes):
    inputs = keras.Input(shape=input_shape)

    # Entry block
    x = layers.Rescaling(1.0 / 255)(inputs)
    x = layers.Conv2D(128, 3, strides=2, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    previous_block_activation = x  # Set aside residual

    for size in [256, 512, 728]:
        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

        # Project residual
        residual = layers.Conv2D(size, 1, strides=2, padding="same")(previous_block_activation)
        x = layers.add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    x = layers.SeparableConv2D(1024, 3, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    x = layers.GlobalAveragePooling2D()(x)
    if num_classes == 2:
        units = 1
    else:
        units = num_classes

    x = layers.Dropout(0.25)(x)
    # We specify activation=None so as to return logits
    outputs = layers.Dense(units, activation=None)(x)
    return keras.Model(inputs, outputs)


model = make_model(input_shape=image_size + (3,), num_classes=2)
keras.utils.plot_model(model, show_shapes=True)

#Treine o modelo
#Chegamos a mais de 90% de precisão de validação após treinar por 25 épocas no conjunto de dados completo (na prática, você pode treinar por mais de 50 épocas antes que o desempenho da validação comece a diminuir)
epochs = 25

callbacks = [keras.callbacks.ModelCheckpoint("save_at_{epoch}.keras"),]
model.compile(optimizer=keras.optimizers.Adam(3e-4),loss=keras.losses.BinaryCrossentropy(from_logits=True),metrics=[keras.metrics.BinaryAccuracy(name="acc")],)
model.fit(train_ds,epochs=epochs,callbacks=callbacks,validation_data=val_ds,)

#Execute inferência em novos dados
#Observe que o aumento e a eliminação de dados estão inativos no momento da inferência.

img = keras.utils.load_img("PetImages/Cat/6779.jpg", target_size=image_size)
plt.imshow(img)

img_array = keras.utils.img_to_array(img)
img_array = keras.ops.expand_dims(img_array, 0)  # Create batch axis

predictions = model.predict(img_array)
score = float(keras.ops.sigmoid(predictions[0][0]))
print(f"This image is {100 * (1 - score):.2f}% cat and {100 * score:.2f}% dog.")



