def mapping(img_flatten_array,list_classes):
    '''
    This function Create links to pixels and categories
    e.g. The image contains pixel values{0,255,40,20,190}
         The image is devided into 5 classes[0,1,2,3,4]
         Then replace the pixel values in the image with the category


    Parameters:
        img_flatten_array：Convert the image to 'P' and then pull it into one dimension
        list_classes：The list of Classes from 0 to n-1 classes

    Returns:
        Image dimension after substitution with category is 1

    '''

    img_set = list(set(img_flatten_array))
    dictionary = dict(zip(img_set, list_classes))
    list_numpy_array = img_flatten_array.tolist()
    classes_img = list()
    for index in range(len(list_numpy_array)):
        temp = dictionary[list_numpy_array[index]]
        classes_img.append(temp)
    classes_img = np.array(classes_img)

    return classes_img