{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "lab1.md",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RI0F5hBbuZWZ"
      },
      "source": [
        "#ВиИМЦС. Лабораторная работа 1 (Часть 2)\n",
        "##Подготовка Raspberry Pi\n",
        "Для реализации MobileNet v1 был использован Python и библиотека TensorFlow 2. Установка необходимых библиотек для Raspberry Pi находится в файле [tf2+rasp.py](https://github.com/rndncknm/HLIMDS/blob/master/tf2%2Brasp.py).\n",
        "##MobileNet v1\n",
        "###Описание арихтектуры\n",
        "![Архитектура MobileNet v1](https://habrastorage.org/webt/rd/0r/jl/rd0rjltrp96j3i_dyhuolbzhyig.png)  \n",
        "\n",
        "Слева нарисован блок обычной сверточной сети, а справа — базовый блок MobileNet. Сверточная часть MobileNet v1 состоит из одного обычного свёрточного слоя с 3х3 свёрткой в начале и тринадцати блоков, изображенных справа на рисунке, с постепенно увеличивающимся числом фильтров и понижающейся пространственной размерностью тензора. Особенностью данной архитектуры является отсутствие max pooling-слоёв. Вместо них для снижения пространственной размерности используется свёртка с параметром stride, равным 2. Двумя гиперпараметрами архитектуры MobileNet являются множитель ширины и множитель разрешения.  \n",
        "\n",
        "Множитель ширины отвечает за количество каналов в каждом слое. Например,  даёт нам архитектуру, описанную в статье, а  — архитектуру с уменьшенным в четыре раза числом каналов на выходе каждого блока.  \n",
        "\n",
        "Множитель разрешения отвечает за пространственные размеры входных тензоров. Например,  означает, что высота и ширина feature map, подаваемой на вход каждому слою будет уменьшена вдвое.  \n",
        "\n",
        "В [оригинальной статье](https://arxiv.org/pdf/1704.04861.pdf) множитель ширины и множитель разрешения по умолчанию равны 1.  \n",
        "***\n",
        "MobileNet v1 основана на разложимой по глубине свертке, которая разлагает стандартное объемное интегрирование на глубокую свертку и точечную свертку (1 × 1 ядро свертки). Глубокая свертка применяет каждое ядро свертки к каждому каналу, в то время как свертка 1 × 1 используется для объединения выходных данных свертки канала.   \n",
        "![Depthwise convolutional filters and pointwise convolution](https://www.programmersought.com/images/168/797830f9825145c82911d68d4ef27898.png)  \n",
        "***\n",
        "В архитектуре используется [Batchnormalization](https://en.wikipedia.org/wiki/Batch_normalization) после каждого слоя свертки. В качестве функций активации используется [ReLU](https://en.wikipedia.org/wiki/Rectifier_(neural_networks) с порогом 6 (т.е. функция вида y = min (max(x, 0), 6)).  \n",
        "\n",
        "Структура MobileNet v1 представлена в следующей таблице.  \n",
        "  \n",
        "  \n",
        "![Structure](https://raw.githubusercontent.com/joshua19881228/my_blogs/master/Computer_Vision/Reading_Note/figures/Reading_Note_20170719_MobileNet_1.png)\n",
        "###Реализация\n",
        "MobileNet v1 была реализована с помощью библиотеки TensorFlow 2.0. Функция, создающая модель нейронной сети представлена в файле [mobilenet_model.py](https://github.com/rndncknm/HLIMDS/blob/master/mobilenet_model.py)."
      ]
    }
  ]
}