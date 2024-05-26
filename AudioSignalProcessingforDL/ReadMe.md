This repo will contain all the resources for audio signal processing using ML/DL

Complete playlist
https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0
 
Github page for all the notes:
https://github.com/musikalkemist/AudioSignalProcessingForML
 

Aliasing to the point:
https://www.youtube.com/watch?v=CTllCx5pHvM
https://www.youtube.com/watch?v=v7qjeUFxVwQ
 
 
Anti aliasing or how to avoid aliasing:
Using low pass filter in time domain: https://www.youtube.com/watch?v=KT_xYgjM7L8


 Key take points from Lecture 1-6:
 *********************************
* "For understanding Timbre, just think of two instruments (violin and piano) being played at the same frequency, pitch, scale, and intensity. Now take the difference of these two sounds and that is your timbre. Timbre is synonymous with colour in audio.” Please note that “Timber” is a term used for wood, especially when it is suitable for building or carpentry. In the context of music, the term you’re looking for is “Timbre”, which refers to the quality of a musical note or sound that distinguishes different types of sound production, such as voices or musical instruments. The term “Timbre” is often likened to the ‘colour’ of a sound.

* The sample rate is the number of samples taken each second. It is described as Sr = 1/Tf
 where Tf is the fixed time interval between two samples. Note that the smaller the Tf the more accurate the sampling approximation is to the original signal.”
Please note that in the context of digital audio, the sample rate (often denoted as Sr) is the number of samples of a sound that are taken per second to represent the event digitally. The term Tf represents the fixed time interval between two samples. The smaller the value of Tf, the higher the sample rate and thus the more accurate the digital representation of the sound. This is because a higher sample rate allows the sound to be sampled more frequently, which provides a more accurate approximation of the original analog signal.

* Sampling is done in the x-axis (time) and Quantization is done in the y-axis (no of bits for amplitude)
* Nyquist frequency >= 2 * Maximum frequency in the signals
* While doing quantization we just quantize the value of amplitude to the closest value that we have available in the y-axis. By applying quantization we create the quantization error just like the sampling error when we do sampling.
* If Bit depth = 16 in case of quantization then the no of possible amplitude values is (2 power 16).
* For avoiding aliasing, we can have a low pass filter (see the above link provided for it) that cut off all the frequencies that are above the Ny-frequency. 
* For time domain (waveform) and for frequency domain (Spectogram)
* Wheneve we want to have the information from both the time and frequency doman then we need the time-frequency representation. For this we have representation such as Spectogram and Melspectogram and constant-Q transform that captures both the information from both domains. 
* Spectogram is a graph with different frequency components are represented with respect to different time component. It represemts the amount of contribution of each frequency band has at that particular time. It is described using a colour. Brighter the colour, nore the contribution at that frequency band at that time. 
* In DL, we generally work on the unstructured data like the input audio or spectogram. Where as in ML, we do feature engineering. In DL, we do automatic feature extraction.




