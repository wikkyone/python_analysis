{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP5WfyXRWsiE7XpIYiTOtRx",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/wikkyone/python_analysis/blob/main/task7_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "ptNAsvdC_aSC"
      },
      "outputs": [],
      "source": [
        "def check_input(elements):\n",
        "    \"\"\"\n",
        "    Находит самую длинную строку в массиве\n",
        "    Возвращает строку и её индекс\n",
        "    Args:\n",
        "        elements (list): входной массив данных\n",
        "\n",
        "    Returns:\n",
        "            int: индекс строки\n",
        "            str: самая длинная строка\n",
        "    \"\"\"\n",
        "    max_len = 0\n",
        "    index = -1\n",
        "    max_string = \"\"\n",
        "\n",
        "    for i, el in enumerate(elements):\n",
        "        if isinstance(el, str):\n",
        "            if len(el) > max_len:\n",
        "                max_len = len(el)\n",
        "                index = i\n",
        "                max_string = el\n",
        "    return index, max_string\n",
        "\n",
        "\n",
        "def get_substring(s):\n",
        "    \"\"\"\n",
        "    Находит самую длинную подстроку в строке\n",
        "    Возвращает строку и её индекс\n",
        "\n",
        "    Args:\n",
        "        s (str): исходная строка\n",
        "\n",
        "    Returns:\n",
        "            str: самая длинная подстрока\n",
        "    \"\"\"\n",
        "    max_len = 0\n",
        "    start = 0\n",
        "    char_index = {}\n",
        "\n",
        "    for i in range(len(s)):\n",
        "        if s[i] in char_index and char_index[s[i]] >= start:\n",
        "            start = char_index[s[i]] + 1\n",
        "        char_index[s[i]] = i\n",
        "        current_len = i - start + 1\n",
        "        if current_len > max_len:\n",
        "            max_len = current_len\n",
        "            max_start = start\n",
        "\n",
        "    return s[max_start:max_start + max_len]\n",
        "\n",
        "\n",
        "def main(elements):\n",
        "    \"\"\"\n",
        "    Принимает на вход список, находит самую длинную строку списка\n",
        "    Полученную строку передает на метод get_substring\n",
        "    Печатает на экран (с помощью print) индекс самой длинной строки в массиве\n",
        "    и найденную подстроку.\n",
        "\n",
        "    Args:\n",
        "        elements (list): входной массив данных\n",
        "\n",
        "    Returns:\n",
        "        None\n",
        "    \"\"\"\n",
        "    index, max_string = check_input(elements)\n",
        "    if index == -1:\n",
        "        print(-1, '')\n",
        "    else:\n",
        "        longest_substring = get_substring(max_string)\n",
        "        print(index, longest_substring)"
      ]
    }
  ]
}