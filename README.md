# Keypoints-Detection-of-an-image
Write programs to detect keypoints in an image according to the following steps, which are also the first three steps of Scale-Invariant Feature Transform (SIFT).
1. Generate four octaves. 
Each octave is composed of five images blurred using Gaussian kernels. 
For each octave, the bandwidth parameters σ (five different scales) of the Gaussian kernels are shown in Tab. 1. 

2. Compute Difference of Gaussian (DoG) for all four octaves. 
3. Detect keypoints which are located at the maxima or minima of the DoG images. 

Detected keypoints are shown as white dots
