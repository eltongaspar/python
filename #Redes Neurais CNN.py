#Redes Neurais CNN
#Criar convoluções e executar pools

#2. O que são convoluções?
#Uma convolução é um filtro que passa por uma imagem, processo e extrai elementos importantes.
#Digamos que você tenha uma imagem de uma pessoa usando um tênis. Como você detectou a presença de um tênis na imagem? Para que seu programa "veja" a imagem como um tênis, você precisará extrair os elementos importantes e desfocar os recursos não essenciais. Isso é chamado de mapeamento de recursos .
#Em teoria, o processo de mapeamento de recursos é simples. Você digitalizará cada pixel da imagem e analisará seus pixels vizinhos. Multiplique os valores desses pixels pelos pesos equivalentes em um filtro.

#3. Comece a programar
#Importando as bibliotecas 
import cv2
import numpy as np
from scipy import misc
i = misc.ascent()

#Em seguida, use a biblioteca Pyplot matplotlibpara desenhar a imagem e ver qual é a aparência dela:
import matplotlib.pyplot as plt
plt.grid(False)
plt.gray()
plt.axis('off')
plt.imshow(i)
plt.show()

#A imagem é armazenada como uma matriz NumPy, então podemos criar a imagem transformada apenas copiando essa matriz. As variáveis ​​size_x e size_y conterão as dimensões da imagem para que você possa repeti-la mais tarde.
i_transformed = np.copy(i)
size_x = i_transformed.shape[0]
size_y = i_transformed.shape[1]

#Primeiro, crie uma matriz de convolução (ou kernel) como uma matriz 3x3:
# Este filtro detecta bem as bordas
# Ele cria um filtro que passa apenas por arestas vivas e linhas retas.
# Experimente valores diferentes para obter efeitos divertidos.
#filter = [ [0, 1, 0], [1, -4, 1], [0, 1, 0]] 
# Mais alguns filtros para experimentar por diversão!
filter = [ [-1, -2, -1], [0, 0, 0], [1, 2, 1]]
#filter = [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
 # Se todos os dígitos no filtro não somarem 0 ou 1, você
# provavelmente deveria fazer um peso para conseguir isso
# sentão, por exemplo, se seus pesos forem 1,1,1 1,2,1 1,1,1
# Eles somam 10, então você definiria um peso de 0,1 se quiser normalizá-los
weight  = 1
#Agora, calcule os pixels de saída. Itere na imagem, deixando uma margem de 1 pixel e multiplique cada um dos vizinhos do pixel atual pelo valor definido no filtro.
#Isso significa que o vizinho do pixel atual acima e à esquerda será multiplicado pelo item superior esquerdo no filtro. Em seguida, multiplique o resultado pelo peso e verifique se ele está no intervalo de 0 a 255.

#4. Crie uma matriz de convolução
#Por fim, carreguei o novo valor na imagem transformada:
for x in range(1,size_x-1):
  for y in range(1,size_y-1):
      output_pixel = 0.0
      output_pixel = output_pixel + (i[x - 1, y-1] * filter[0][0])
      output_pixel = output_pixel + (i[x, y-1] * filter[0][1])
      output_pixel = output_pixel + (i[x + 1, y-1] * filter[0][2])
      output_pixel = output_pixel + (i[x-1, y] * filter[1][0])
      output_pixel = output_pixel + (i[x, y] * filter[1][1])
      output_pixel = output_pixel + (i[x+1, y] * filter[1][2])
      output_pixel = output_pixel + (i[x-1, y+1] * filter[2][0])
      output_pixel = output_pixel + (i[x, y+1] * filter[2][1])
      output_pixel = output_pixel + (i[x+1, y+1] * filter[2][2])
      output_pixel = output_pixel * weight
      if(output_pixel<0):
        output_pixel=0
      if(output_pixel>255):
        output_pixel=255
      i_transformed[x, y] = output_pixel

#5. Analisar os resultados
#Agora, trace uma imagem para ver o efeito que transmite o filtro sobre ela:
      # Plot the image. Note the size of the axes -- they are 512 by 512
plt.gray()
plt.grid(False)
plt.imshow(i_transformed)
plt.axis('off')
plt.show()   

#6. Como entender o pool
#Agora que você exige os recursos essenciais da imagem, o que fazer? Como usar o mapa de recursos resultante para classificar imagens?
#Assim como as convoluções, o pooling ajuda na detecção de recursos. As camadas de piscina reduzem a quantidade total de informações em uma imagem e mantêm os recursos detectados como presentes.
#Existem vários tipos diferentes de pool, mas você usará um que chama de pool máximo (máximo).
#Itere na imagem e, em cada ponto, considere o pixel e seus vizinhos imediatos para a direita, abaixo e abaixo dele. Use a maior delas (portanto, o pool max ) e carregue-a na nova imagem. Assim, a nova imagem terá um quarto do tamanho da antiga.Piscina máxima

#7. Escreva o código para pooling
#O código a seguir mostra um pooling (2, 2). Execute-o para ver a saída.
#Você verá que, embora a imagem tenha um quarto do tamanho do original, todos os recursos foram mantidos.
new_x = int(size_x/2)
new_y = int(size_y/2)
newImage = np.zeros((new_x, new_y))
for x in range(0, size_x, 2):
  for y in range(0, size_y, 2):
    pixels = []
    pixels.append(i_transformed[x, y])
    pixels.append(i_transformed[x+1, y])
    pixels.append(i_transformed[x, y+1])
    pixels.append(i_transformed[x+1, y+1])
    pixels.sort(reverse=True)
    newImage[int(x/2),int(y/2)] = pixels[0]
 
# Plot the image. Note the size of the axes -- now 256 pixels instead of 512
plt.gray()
plt.grid(False)
plt.imshow(newImage)
#plt.axis('off')
plt.show()