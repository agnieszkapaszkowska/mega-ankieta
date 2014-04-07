function equalArrays(array1, array2) {
    for (var i = 0; i < array1.length; i++)
        if (array2.indexOf(array1[i]) == -1)
            return false;
    for (var i = 0; i < array2.length; i++)
        if (array1.indexOf(array2[i]) == -1)
            return false;
    return true;
}

