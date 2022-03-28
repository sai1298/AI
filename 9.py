{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "9.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 279
        },
        "id": "RprBLnOGhpqS",
        "outputId": "4bc474fe-1b6c-4d08-fcc4-03661949d62e"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "def kernel(point,xmat, k):\n",
        "    m,n = np.shape(xmat)\n",
        "    weights = np.mat(np.eye((m)))\n",
        "    for j in range(m):\n",
        "        diff = point - X[j]\n",
        "        weights[j,j] = np.exp(diff*diff.T/(-2.0*k**2))\n",
        "    return weights\n",
        "def localWeight(point,xmat,ymat,k):\n",
        "    wei = kernel(point,xmat,k)\n",
        "    W = (X.T*(wei*X)).I*(X.T*(wei*ymat.T))\n",
        "    return W\n",
        "def localWeightRegression(xmat,ymat,k):\n",
        "    m,n = np.shape(xmat)\n",
        "    ypred = np.zeros(m)\n",
        "    for i in range(m):\n",
        "        ypred[i] = xmat[i]*localWeight(xmat[i],xmat,ymat,k)\n",
        "    return ypred\n",
        "def graphPlot(X,ypred):\n",
        "    sortindex = X[:,1].argsort(0) \n",
        "    xsort = X[sortindex][:,0]\n",
        "    fig = plt.figure()\n",
        "    ax = fig.add_subplot(1,1,1)\n",
        "    ax.scatter(bill,tip, color='green')\n",
        "    ax.plot(xsort[:,1],ypred[sortindex], color = 'red', linewidth=5)\n",
        "    plt.xlabel('Total bill')\n",
        "    plt.ylabel('Tip')\n",
        "    plt.show();\n",
        "data = pd.read_csv('data10_tips.csv')\n",
        "bill = np.array(data.total_bill) \n",
        "tip = np.array(data.tip)\n",
        "mbill = np.mat(bill) \n",
        "mtip = np.mat(tip)\n",
        "m= np.shape(mbill)[1]\n",
        "one = np.mat(np.ones(m))\n",
        "X = np.hstack((one.T,mbill.T)) \n",
        "ypred = localWeightRegression(X,mtip,8) \n",
        "graphPlot(X,ypred)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "f6lHwBWvi8TI"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
