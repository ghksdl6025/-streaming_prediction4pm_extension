import imageio
import matplotlib.pyplot as plt
import os
import numpy as np

datalabel = 'synthetic_log_bc1c2'
classifier = 'efdt'
counter = '200'

filenames = []
for p in range(2, 13):
    filenames.append('./img/%s/%s/result%s prefix%s.png'%(datalabel,classifier,counter,p))
# filenames=['./img/synthetic_log_bc1/efdt/result200 prefix2.png',
# './img/synthetic_log_bc1/efdt/result200 prefix3.png',
# './img/synthetic_log_bc1/efdt/result200 prefix4.png',
# './img/synthetic_log_bc1/efdt/result200 prefix5.png',
# './img/synthetic_log_bc1/efdt/result200 prefix6.png',
# './img/synthetic_log_bc1/efdt/result200 prefix7.png',
# './img/synthetic_log_bc1/efdt/result200 prefix8.png',
# './img/synthetic_log_bc1/efdt/result200 prefix9.png',
# './img/synthetic_log_bc1/efdt/result200 prefix10.png',
# './img/synthetic_log_bc1/efdt/result200 prefix11.png',
# './img/synthetic_log_bc1/efdt/result200 prefix12.png']

gifname = './img/%s/%s %s.gif'%(datalabel,classifier,counter)
with imageio.get_writer(gifname, mode='I', duration='0.7') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
