import scipy.io.wavfile as wavfile
import numpy as np
import os.path
import scipy.stats as stats
import scipy.io

# def signaltonoise(a, axis=0, ddof=0):
#     a = np.asanyarray(a)
#     m = a.mean(axis)
#     sd = a.std(axis=axis, ddof=ddof)
#     return np.where(sd == 0, 0, m/sd)

def signaltonoise(a, axis=0, ddof=0):
  mx = np.amax(a)
  a = np.divide(a,mx)
  a = np.square(a)
  a = np.asanyarray(a)
  m = a.mean(axis)
  sd = a.std(axis=axis, ddof=ddof)
  return np.where(sd == 0, 0, m/sd)

def snr(file):
  if (os.path.isfile(file)):
    data = wavfile.read(file)[1]
    singleChannel = data
    try:
      singleChannel = np.sum(data, axis=1)
    except:
      pass
    norm = singleChannel / (max(np.amax(singleChannel), -1 * np.amin(singleChannel)))
    return signaltonoise(norm)

# %%
print(snr('./SNR/CycleGAN/you are my eveything - gummy.wav'))
print(snr('./SNR/CycleGAN/you are my everything - iu.wav'))
print(snr('./SNR/CycleGAN/Kwill.wav'))
print(snr('./SNR/CycleGAN/10cm.wav'))

# %%
print(snr('./SNR/StarGAN/100000/p229_009.wav'))
print(snr('./SNR/StarGAN/100000/아이유 거미노래.wav'))
print(snr('./SNR/StarGAN/100000/square.wav'))
print(snr('./SNR/StarGAN/100000/백예린_변환.wav'))

# %%
print(snr('./data/VCTK-Corpus/cs/p229/p229_009.wav'))
print(snr('./converted/50000/밤편지 권정열.wav'))
print(snr('./converted/100000/p229_009-vcto-p232.wav'))
print(snr('./converted/1000/p292_021-vcto-p293.wav'))