from modules import public_wp
from modules import variables_data as var
import traceback

def main():
    try:
        wp = public_wp.SkPublic(var.domain)
        index = var.id['index']
        datos = wp.readData('shekina.json')
        while index <= len(datos):
            product = datos[index]
            wp.PublicProduct(product)
            index += 1
            file = open('index.json', 'w', encoding='UTF-8')
            file.write('{"index": ' + str(index) + '}')
            file.close()
    except:
        print('Error.')
        open('error.log', 'a', encoding='UTF-8').writelines(traceback.format_exc()+'\n')


if __name__ == '__main__':
    main()