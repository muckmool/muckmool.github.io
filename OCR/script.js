console.log('Hello TensorFlow');

import { MnistData } from 'https://muckmool.github.io/OCR/data.js'

async function showExamples(data) {
  // Create a container in the visor
  const surface = tfvis
    .visor()
    .surface({ name: 'Input Data Examples', tab: 'Input Data' })

  // Get the examples
  const examples = data.nextTestBatch(20)
  const numExamples = examples.xs.shape[0]

  // Create a canvas element to render each example
  for (let i = 0; i < numExamples; i++) {
    const imageTensor = tf.tidy(() => {
      // Reshape the image to 28x28 px
      return examples.xs
        .slice([i, 0], [1, examples.xs.shape[1]])
        .reshape([28, 28, 1])
    })

    const canvas = document.createElement('canvas')
    canvas.width = 28
    canvas.height = 28
    canvas.style = 'margin: 4px;'
    await tf.browser.toPixels(imageTensor, canvas)
    surface.drawArea.appendChild(canvas)

    imageTensor.dispose()
  }
}

async function run() {
  const data = new MnistData()
  await data.load()
  await showExamples(data)
}

document.addEventListener('DOMContentLoaded', run)

  function getModel() {
    const model = tf.sequential();
  
    const IMAGE_WIDTH = 28;
    const IMAGE_HEIGHT = 28;
    const IMAGE_CHANNELS = 1;
  
    // 첫번째 covolutional 신경망에서는 input 이미지의 형태를 넣어둔다.
    // 그 다음 합성곱 연산에 필요한 파라미터를 정의한다.
    model.add(tf.layers.conv2d({
      inputShape: [IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS],
      kernelSize: 5,
      filters: 8,
      strides: 1,
      activation: 'relu',
      kernelInitializer: 'varianceScaling'
    }));
  
  
    // MaxPooling Layer는 평균값을 내는 것이 아니라, 영역의 최대값을 활용해서 다운샘플링을 진행한다.
    model.add(tf.layers.maxPooling2d({poolSize: [2, 2], strides: [2, 2]}));
  
  
    // conv2d와 maxpooling을 반복한다.
    // 이 convolution에서 더 많은 필터가 있다는 것을 기억하자.
    model.add(tf.layers.conv2d({
      kernelSize: 5,
      filters: 16,
      strides: 1,
      activation: 'relu',
      kernelInitializer: 'varianceScaling'
    }));
    model.add(tf.layers.maxPooling2d({poolSize: [2, 2], strides: [2, 2]}));
  
    // 2D형태의 필터를  1D 벡터 형태로 평평하게 하여, 마지막 layer에 인풋으로 넣을 수 있도록 한다.
    // 이는 고차원의 데이터를 마지막 분류 레이어에 전달할 때 하는 일반적인 과정이다.
    model.add(tf.layers.flatten());
  
    // 마지막 레이어는 10개의 값이 나오게 된다.
    // output class (i.e. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9).
    const NUM_OUTPUT_CLASSES = 10;
    model.add(tf.layers.dense({
      units: NUM_OUTPUT_CLASSES,
      kernelInitializer: 'varianceScaling',
      activation: 'softmax'
    }));
  
  
    // optimizer, loss function, accuracy meetric을 고르고, 컴파일 후에 모델을 리턴한다.
    const optimizer = tf.train.adam();
    model.compile({
      optimizer: optimizer,
      loss: 'categoricalCrossentropy',
      metrics: ['accuracy'],
    });
  
    return model;
    
    model.add(
  tf.layers.conv2d({
    inputShape: [IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS],
    kernelSize: 5,
    filters: 8,
    strides: 1,
    activation: 'relu',
    kernelInitializer: 'varianceScaling',
  }),
)
