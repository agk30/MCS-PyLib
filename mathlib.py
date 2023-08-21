def threshold_post_process(image, shape, threshold):
    
    for i in range(shape[0]):
        for j in range(shape[1]):
            if image[i,j] < threshold:
                image[i,j] = threshold

    return image