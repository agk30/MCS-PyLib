import scipy.special

k = 3.0
x = 0.5

reg_gamma =  scipy.special.gammaincinv(k/2, (x**2 / 2))

print (reg_gamma)