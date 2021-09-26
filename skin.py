import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import urllib

# 포트 : 8000
# ngrok http 8000 하면 된다.

def skin(url='firebasestorage.googleapis.com/v0/b/test-6913b.appspot.com/o/1?alt=media&token=01c488a7-272a-4ebe-890f-ff1a9f1a18c6'):
    # Disable scientific notation for clarity
    # 명확성을 위해 과학적 표기 사용 안 함
    np.set_printoptions(suppress=True)

    # Load the model
    model = tensorflow.keras.models.load_model('keras_model.h5')

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.

    # 케라스 모델에 입력할 올바른 쉐이프의 배열을 작성합니다.
    # 배열에 넣을 수 있는 '길이' 또는 이미지 수는 다음과 같습니다.
    # 형상 튜플의 첫 번째 위치에 의해 결정됩니다(이 경우 1).
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    # 이 경로를 이미지의 경로로 대체합니다.
    
    f=open('test.jpg','wb')
    f.write(urllib.request.urlopen('https://'+url).read())
    f.close()
    image = Image.open('지루각화증.jpg')

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center

    # TM2와 동일한 전략으로 이미지 크기를 224x224로 조정합니다.
    # 이미지 크기를 최소 224x224로 조정한 다음 중앙에서 자르기
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    # 이미지를 숫자 배열로 바꾸다
    image_array = np.asarray(image)

    # display the resized image
    # 크기 조정된 이미지 표시

    # Normalize the image
    # 이미지 표준화

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    # 이미지를 배열에 로드합니다.
    prediction = model.predict(data)
    name=['대상포진','무좀','사마귀','수두','아토피','지루각화증','정상']
    
    
    a=prediction[0].argsort()
    print(name[a[-1]])
    answer1=name[a[-1]]
    
    return answer1
if __name__=='__main__':
    skin()