This is a KAIST CS470 team 27's project: Introduction to A.I. The original repo is from here: https://github.com/liusongxiang/StarGAN-Voice-Conversion.


# StarGAN-Voice-Conversion
This is a pytorch implementation of the paper: StarGAN-VC: Non-parallel many-to-many voice conversion with star generative adversarial networks  https://arxiv.org/abs/1806.02169 .
Note that the model architecture is a little different from that of the original paper.

# Dependencies
* Python 3.6 (or 3.5)
* Pytorch 0.4.0
* pyworld
* tqdm
* librosa
* tensorboardX and tensorboard

# Training
## Download Dataset

Download and unzip [VCTK](https://homepages.inf.ed.ac.uk/jyamagis/page3/page58/page58.html) corpus to designated directories.

```bash
mkdir ./data
wget https://datashare.is.ed.ac.uk/bitstream/handle/10283/2651/VCTK-Corpus.zip?sequence=2&isAllowed=y
unzip VCTK-Corpus.zip -d ./data
```
If the downloaded VCTK is in tar.gz, run this:

```bash
tar -xzvf VCTK-Corpus.tar.gz -C ./data
```

## Preprocess data

We will use Mel-cepstral coefficients(MCEPs) here.

```bash
python preprocess.py --sample_rate 16000 \
                    --origin_wavpath data/VCTK-Corpus/wav48 \
                    --target_wavpath data/VCTK-Corpus/wav16 \
                    --mc_dir_train data/mc/train \
                    --mc_dir_test data/mc/test
```


Or, you can run the preproess.ipynb in the Colab.


## Train model

Note: you may need to early stop the training process if the training-time test samples sounds good or the you can also see the training loss curves to determine early stop or not.

```
python main.py
```


Or, you can run the main.ipynb in the Colab.


# Convert


Here, you should have two -> 보컬 샘플 p229~ 등에 저장해서 쓰기.
For example: restore model at step 200000 and specify the source speaker and target speaker to `p262` and `p272`, respectively.

```
convert.py --resume_iters 200000 --src_spk p262 --trg_spk p272
```


Or, you can run the convert.ipynb in the Colab.

# Split and Merge .wav file

- We use python library spleeter to split song file to vocal and accompaniment file.
For example: split song file named song.mp3 and store result in output folder
```
spleeter separate -i song.mp3 -o output
```
- We use pydub to merge converted file and mr


Or, you can run the split.ipynb in the Colab.


# Evaluation

## Signal-to-Noise-Ratio (SNR)




