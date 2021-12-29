#Phase has range [0, 2*pi], normalized to [0,1]
#Amplitude is normalized.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

path_phase = 'clown_phase.png'
path_amplitude = 'clown_amplitude.png'
path_amplitude_mdf = 'clown_amplitude_mdf.png'

#Discrete Fourier Transformation
def DFT(arr):
    M = arr.shape[0]
    N = arr.shape[1]
    n = np.arange(N)
    k_n = n.reshape((N, 1))
    m = np.arange(M)
    k_m = n.reshape((M, 1))
    e_n = np.exp(-2j * np.pi * k_n * n / N)
    e_m = np.exp(-2j * np.pi * k_m * m / M)
    return np.matmul(np.matmul(e_m, arr), e_n)

#Inverse Discrete Fourier Transformation
def inverse_DFT(arr):
    M = arr.shape[0]
    N = arr.shape[1]
    n = np.arange(N)
    k_n = n.reshape((N, 1))
    m = np.arange(M)
    k_m = n.reshape((M, 1))
    e_n = np.exp(2j * np.pi * k_n * n / N)
    e_m = np.exp(2j * np.pi * k_m * m / M)
    return np.matmul(np.matmul(e_m, arr), e_n)

def read_image(file):
    #Read image.
    img = mpimg.imread(file)
    #Fourier transform 3 matrices: R, G, B.
    R = DFT(img[:,:,0])
    R_phase = np.angle(R)
    R_amplitude = np.absolute(R)
    G = DFT(img[:,:,1])
    G_phase = np.angle(G)
    G_amplitude = np.absolute(G)
    B = DFT(img[:,:,2])
    B_phase = np.angle(B)
    B_amplitude = np.absolute(B)
    #Plot amplitude and phase
    img_amplitude = np.concatenate((np.expand_dims(R_amplitude, 2), np.expand_dims(G_amplitude, 2), np.expand_dims(B_amplitude, 2)), axis = 2)
    img_amplitude_tf = np.tanh(0.01 * img_amplitude)
    img_phase = np.concatenate((np.expand_dims(R_phase, 2), np.expand_dims(G_phase, 2), np.expand_dims(B_phase, 2)), axis = 2)
    img_phase[img_phase < 0] = img_phase[img_phase < 0] + 2*np.pi
    img_phase_tf = img_phase / (2*np.pi)
    plt.imsave(path_phase, img_phase_tf)
    plt.imsave(path_amplitude, img_amplitude_tf)
    '''
    #Transform Fourier transformed matrices.
    #Remove edges.
    G[0:10, 0:10] = 0
    G[0:10, -10:-1] = 0
    G[-10:-1, 0:10] = 0
    G[-10:-1, -10:-1] = 0
    R[0:10, 0:10] = 0
    R[0:10, -10:-1] = 0
    R[-10:-1, 0:10] = 0
    R[-10:-1, -10:-1] = 0
    B[0:10, 0:10] = 0
    B[0:10, -10:-1] = 0
    B[-10:-1, 0:10] = 0
    B[-10:-1, -10:-1] = 0
    #Remove middle part
    R[R.shape[0]//2 - 5 : R.shape[0]//2 + 5, R.shape[1]//2 - 5 : R.shape[1]//2 + 5] = 0
    G[G.shape[0]//2 - 5 : G.shape[0]//2 + 5, G.shape[1]//2 - 5 : G.shape[1]//2 + 5] = 0
    B[B.shape[0]//2 - 5 : B.shape[0]//2 + 5, B.shape[1]//2 - 5 : B.shape[1]//2 + 5] = 0
    #Remove top layer
    G[0:5,:] = 0
    R[0:5,:] = 0
    B[0:5,:] = 0
    #Remove Right layer
    G[:, 0:5] = 0
    R[:, 0:5] = 0
    G[:, 0:5] = 0
    #Preserve edges only.
    i = 30
    G[i:-i, :] = 0
    G[:, i:-i] = 0
    R[i:-i, :] = 0
    R[:, i:-i] = 0
    B[i:-i, :] = 0
    B[:, i:-i] = 0
    '''
    #Remove specified frequencies.
    w = 5 #Area to be removed.
    locs = [(21,12), (85,24), (42,103), (107,116)] #Location to be removed.
    for y, x in locs:
        R[x - w : x + w, y - w : y + w] = 0
        G[x - w : x + w, y - w : y + w] = 0
        B[x - w : x + w, y - w : y + w] = 0
    #Plot frequencies graph again.
    R_amplitude = np.absolute(R)
    G_amplitude = np.absolute(G)
    B_amplitude = np.absolute(B)
    img_amplitude = np.concatenate((np.expand_dims(R_amplitude, 2), np.expand_dims(G_amplitude, 2), np.expand_dims(B_amplitude, 2)), axis = 2)
    img_amplitude_tf = np.tanh(0.01 * img_amplitude)
    plt.imsave(path_amplitude_mdf, img_amplitude_tf)
    #Inverse Fourier Transform.
    R = inverse_DFT(R)
    G = inverse_DFT(G)
    B = inverse_DFT(B)
    #Join R,G,B together to form a coloured picture.
    img = np.concatenate((np.expand_dims(R, 2), np.expand_dims(G, 2), np.expand_dims(B, 2)), axis = 2)
    plt.imsave('clown_mdf.png', np.absolute(img)/np.max(np.absolute(img)))


read_image('clown_orig.png')
