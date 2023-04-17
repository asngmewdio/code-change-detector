// #WJ 2022-04-28 Changed default value of modifiedBubbleSort swaooed value to false
#include <iostream>
#include <algorithm>
#include <chrono>
#include <random>

using namespace std;
using namespace std::chrono;
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

void modifiedBubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = false;
            }
        }
        if (!swapped) {
            break;
        }
    }
}