{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RprBLnOGhpqS",
        "outputId": "097ca53b-7b00-405c-d59f-d7325dfc2eff"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[[{'weights': [0.13436424411240122, 0.8474337369372327, 0.763774618976614]}, {'weights': [0.2550690257394217, 0.49543508709194095, 0.4494910647887381]}], [{'weights': [0.651592972722763, 0.7887233511355132, 0.0938595867742349]}, {'weights': [0.02834747652200631, 0.8357651039198697, 0.43276706790505337]}]]\n",
            ">epoch=0, lrate=0.500, error=6.350\n",
            ">epoch=1, lrate=0.500, error=5.531\n",
            ">epoch=2, lrate=0.500, error=5.221\n",
            ">epoch=3, lrate=0.500, error=4.951\n",
            ">epoch=4, lrate=0.500, error=4.519\n",
            ">epoch=5, lrate=0.500, error=4.173\n",
            ">epoch=6, lrate=0.500, error=3.835\n",
            ">epoch=7, lrate=0.500, error=3.506\n",
            ">epoch=8, lrate=0.500, error=3.192\n",
            ">epoch=9, lrate=0.500, error=2.898\n",
            ">epoch=10, lrate=0.500, error=2.626\n",
            ">epoch=11, lrate=0.500, error=2.377\n",
            ">epoch=12, lrate=0.500, error=2.153\n",
            ">epoch=13, lrate=0.500, error=1.953\n",
            ">epoch=14, lrate=0.500, error=1.774\n",
            ">epoch=15, lrate=0.500, error=1.614\n",
            ">epoch=16, lrate=0.500, error=1.472\n",
            ">epoch=17, lrate=0.500, error=1.346\n",
            ">epoch=18, lrate=0.500, error=1.233\n",
            ">epoch=19, lrate=0.500, error=1.132\n",
            "[{'weights': [-1.4688375095432327, 1.850887325439514, 1.0858178629550297], 'output': 0.029980305604426185, 'delta': -0.0059546604162323625}, {'weights': [0.37711098142462157, -0.0625909894552989, 0.2765123702642716], 'output': 0.9456229000211323, 'delta': 0.0026279652850863837}]\n",
            "[{'weights': [2.515394649397849, -0.3391927502445985, -0.9671565426390275], 'output': 0.23648794202357587, 'delta': -0.04270059278364587}, {'weights': [-2.5584149848484263, 1.0036422106209202, 0.42383086467582715], 'output': 0.7790535202438367, 'delta': 0.03803132596437354}]\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "\n",
        "dataset = pd.read_csv('tennis.csv',names=['outlook','temperature','humidity','wind','class'])\n",
        "attributes = ('outlook','temperature','humidity','wind','playtennis')\n",
        "\n",
        "def entropy(target_col):\n",
        "    elements,counts = np.unique(target_col, return_counts=True)\n",
        "    entropy = np.sum([(-counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])\n",
        "    return entropy\n",
        "\n",
        "def InfoGain(data,split_attribute_name, target_name=\"class\"):\n",
        "    total_entropy = entropy(data[target_name])\n",
        "    val,counts = np.unique(data[split_attribute_name],return_counts=True) \n",
        "    weighted_Entropy = np.sum([(counts[i]/np.sum(counts))*entropy(data.where(data[split_attribute_name]==val[i]).dropna()[target_name]) for i in range(len(val))])\n",
        "    Information_Gain = total_entropy - weighted_Entropy\n",
        "    return Information_Gain\n",
        "\n",
        "def ID3(data, originaldata, features, target_attribute_name=\"class\",parent_node_class=None):\n",
        "    if len(np.unique(data[target_attribute_name]))<=1:\n",
        "        return np.unique(data[target_attribute_name])[0]\n",
        "    elif len(data)==0:\n",
        "        return np.unique(originaldata[target_attribute_name])[np.argmax(np.unique(originaldata[target_attribute_name], return_counts=True)(1))]\n",
        "    elif len(features)==0:\n",
        "        return parent_node_class\n",
        "    else:\n",
        "        parent_node_class = np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name],return_counts=True)[1])]\n",
        "        item_values = [InfoGain(data,feature,target_attribute_name) for feature in features]\n",
        "        best_feature_index = np.argmax(item_values)\n",
        "        best_feature = features[best_feature_index]\n",
        "        tree = {best_feature:{}}\n",
        "        features = [i for i in features if i != best_feature]\n",
        "        for value in np.unique(data[best_feature]):\n",
        "            value = value\n",
        "            sub_data = data.where(data[best_feature]==value).dropna()\n",
        "            subtree = ID3(sub_data, dataset,features, target_attribute_name, parent_node_class)\n",
        "            tree[best_feature][value]=subtree\n",
        "        return(tree)\n",
        "\n",
        "tree = ID3(dataset,dataset,dataset.columns[:-1])\n",
        "print(dataset.head())\n",
        "print(' \\nDisplay Tree\\n',tree)    \n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "f6lHwBWvi8TI"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "colab": {
      "collapsed_sections": [],
      "name": "5.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
