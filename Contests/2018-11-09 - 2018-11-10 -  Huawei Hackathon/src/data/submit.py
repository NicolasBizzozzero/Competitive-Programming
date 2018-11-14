import zipfile


def generate_submit(tab):
    """ tab->list  :    prediction
        create the file and write the prediction
        have to be in the good order
       """
    with open("answer.txt", 'w') as f:
        for i in tab:
            f.write(str(i) + '\n')


def zipped(file_name='answer.zip', file_to_zip='answer.txt'):
    """ file_name -> str the name of the zipped file
        file_to_zip -> str the name of the file to zip
        zip the file file_to_zip"""
    zip = zipfile.ZipFile(file_name, 'w')
    zip.write(file_to_zip)
    zip.close()


if __name__ == '__main__':
    generate_submit([1, 0, 2, 3, 5, 6, 4])
    zipped(file_to_zip='answer.txt')
