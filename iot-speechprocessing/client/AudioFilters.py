#!/usr/bin/env python3
import scipy.signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import decimate

def highPassFilter(inputSignal, threshold):
    threshold = max(0, threshold)
    outputSignal = inputSignal.copy()
    for i in range(0, threshold):
        outputSignal[i] = 0
    return outputSignal
    
def lowPassFilter(inputSignal, threshold):
    threshold = min(len(inputSignal), threshold)
    outputSignal = inputSignal.copy()
    for i in range(threshold, len(inputSignal)-1):
        outputSignal[i] = 0
    return outputSignal

def bandpassFilter(inputSignal, lowerThreshold, higherThreshold):
    return highPassFilter(lowPassFilter(inputSignal, higherThreshold), lowerThreshold)
    
def downsample(signal, factor):
    return decimate(signal, factor)

def getGaussianAtX(x, sigma):
    return np.exp( - np.power(x, 2.) / 2 * np.power(sigma, 2.))
        
def getGaussian(sigma, start, stop):
    x_values = np.linspace(start, stop, abs(start)+ stop)
    return getGaussianAtX(x_values, sigma)

def noiseFilter(inputSignal, value):
    kernel = [1/3, 1/3, 1/3]
    return np.convolve(inputSignal, kernel)

def noiseFilterGaussian(inputSignal, value):
    kernelSize = 5
    kernel = getGaussian(value, -kernelSize, kernelSize)
    outputSignal = inputSignal.copy()
    convolution = np.convolve(inputSignal, kernel)
    for i in range(kernelSize , len(inputSignal)+kernelSize):
        outputSignal[i - kernelSize] = convolution[i]
    return outputSignal
    
#only for testing purposes
def addNoise(inputData, amount):
    noise = np.random.randn(len(inputData)) * amount
    return inputData + noise
    
def convertToMono(inputData):
    try: 
        return inputData.sum(axis=1)/2
    except ValueError:
        return inputData