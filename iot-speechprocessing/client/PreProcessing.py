#!/usr/bin/env python3
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np

import AudioFilters as filters

noisefilter_value = 1000

bandpass_min = 50
bandpass_max = 8000

downsamplingrate = 1


def filterAudioSignal(inputFilename, outputFilename):
    
    sample_rate, wavData = wavfile.read(inputFilename)
    
    wav_Mono = filters.convertToMono(wavData)
    wav_downsampled = filters.downsample(wav_Mono, downsamplingrate)
    wav_downsampled_fft = scipy.fft(wav_downsampled)
    wav_bandpassed = fftpk.ifft(filters.bandpassFilter( scipy.fft(wav_downsampled), bandpass_min, bandpass_max))
    
    wav_denoised = filters.noiseFilter(wav_bandpassed, noisefilter_value)
    
    originalMaxAmplitude = np.max(wavData)
    currentMaxAmplitude = np.max(wav_denoised)
    normalizedSignal = (wav_denoised / currentMaxAmplitude) * originalMaxAmplitude

    wavfile.write(outputFilename, sample_rate, normalizedSignal.astype(wavData.dtype))