
# import numpy as np

def AME46:
    """
    2020-09-02 
    2021-01-11

    Suhail Ahmad Rather
    Adam Burchardt
    Wojciech Bruzda
    Grzegorz Rajchel-Mieldzioc
    Arul Lakshminarayan
    Karol Zyczkowski

    https://arxiv.org/abs/2104.05122
 
    ------------------------------------------------------------------------
 
    it returns U such that
    svd(U) = svd(U^R) = svd(U^G) = [1 1 1 ... 1] = vector of 36 ones
    where ^R := reshuffling
          ^G := partial transpose (w.r.t. 2nd subsystem)

    in other words
    it returns a complex representation of the AME(4,6) state
    """

    a = 1 / np.sqrt(5.0 + np.sqrt(5.0))
    b = np.sqrt(5.0 + np.sqrt(5.0)) / np.sqrt(20.0)
    c = 1 / np.sqrt(2.0)
    w = np.exp(1j * np.pi / 10.0)
    U = np.zeros((d**2, d**2), dtype = np.complex)

    # 20 non-zero entries of 1st six rows:
    U[1, 1] = c*(w**3);
    U[5, 0] = c/w
    U[0, 7] = b/w;
    U[2, 6] = a/(w**7);
    U[3, 6] = b*(w**2);
    U[5, 7] = a/(w**3)
    U[0, 15] = a/(w**2);
    U[1, 14] = b*(w**9);
    U[4, 14] = a*(w**5);
    U[5, 15] = b*(w**6)
    U[2, 20] = a/(w**6);
    U[3, 20] = b/w;
    U[4, 21] = c/w
    U[1, 29] = a;
    U[2, 28] = b*(w**7);
    U[3, 28] = a*(w**2);
    U[4, 29] = b*(w**6)
    U[0, 34] = c*(w**6);
    U[2, 35] = b/(w**5);
    U[3, 35] = a/(w**6)

    # 20 non-zero entries of 2nd six rows:
    U[6, 0] = c
    U[10, 1] = c/(w**4)
    U[6, 7] = a*(w**8)
    U[8, 6] = b/(w**8)
    U[9, 6] = a/(w**9)
    U[11, 7] = b/(w**4)
    U[6, 15] = b/(w**3)
    U[7, 14] = a*(w**6)
    U[10, 14] = b/(w**8)
    U[11, 15] = a/(w**5)
    U[8, 20] = b*w
    U[9, 20] = a/(w**4)
    U[7, 21] = c*(w**10)
    U[8, 28] = a/(w**4)
    U[9, 28] = b*w
    U[7, 29] = b*(w**7)
    U[10, 29] = a*(w**3)
    U[8, 35] = a/(w**8)
    U[9, 35] = b*w
    U[11, 34] = c/(w**7)

    # 18 non-zero entries of 3rd six rows:
    U[13, 5] = b/(w**3)
    U[14, 4] = b/(w**4)
    U[15, 4] = a/w
    U[16, 5] = a*(w**9)
    U[12, 11] = a*(w**4)
    U[13, 10] = a*(w**6)
    U[16, 10] = b*(w**8)
    U[17, 11] = b
    U[15, 13] = c/(w**5)
    U[16, 12] = c*w
    U[14, 18] = c;
    U[17, 19] = c/(w**6)
    U[12, 26] = c*(w**8)
    U[14, 27] = a*(w**6)
    U[15, 27] = b/w
    U[12, 33] = b/(w**6)
    U[13, 32] = c/(w**6)
    U[17, 33] = a

    # 18 non-zero entries of 4th six rows:
    U[19, 5] = a/(w**3)
    U[20, 4] = a/(w**8)
    U[21, 4] = b*(w**5)
    U[22, 5] = b/w
    U[18, 11] = b*(w**2)
    U[19, 10] = b/(w**4)
    U[22, 10] = a*(w**8)
    U[23, 11] = a*(w**8)
    U[19, 12] = c/w
    U[20, 13] = c/(w**2)
    U[18, 19] = c*(w**6)
    U[21, 18] = c/w
    U[23, 26] = c*(w**2)
    U[20, 27] = b/(w**8)
    U[21, 27] = a/(w**5)
    U[18, 33] = a*(w**2)
    U[22, 32] = c*(w**6)
    U[23, 33] = b/(w**2)

    # 18 non-zero entries of 5th six rows:
    U[24, 2] = a
    U[26, 3] = a*w
    U[27, 3] = b*(w**2)
    U[29, 2] = b
    U[25, 9] = b*w
    U[26, 8] = b*w**3
    U[27, 8] = a/(w**6)
    U[28, 9] = a*w
    U[24, 16] = b/(w**4)
    U[26, 17] = c/(w**5)
    U[29, 16] = a*(w**6)
    U[24, 23] = c/(w**7)
    U[25, 22] = a/(w**2)
    U[28, 22] = b*(w**8)
    U[25, 25] = c/(w**6)
    U[29, 24] = c
    U[27, 31] = c/(w**2)
    U[28, 30] = c/(w**6)

    # 18 non-zero entries of last six rows:
    U[30, 2] = b/(w**9)
    U[32, 3] = b
    U[33, 3] = a/(w**9)
    U[35, 2] = a*w
    U[31, 9] = a/(w**6)
    U[32, 8] = a/(w**8)
    U[33, 8] = b/(w**7)
    U[34, 9] = b*(w**4)
    U[30, 16] = a/(w**3)
    U[33, 17] = c/(w**5)
    U[35, 16] = b/(w**3)
    U[31, 22] = b*w
    U[34, 22] = a*w
    U[35, 23] = c*(w**4)
    U[30, 24] = c*w
    U[34, 25] = c*(w**7)
    U[31, 30] = c/(w**3)
    U[32, 31] = c*(w**6)

