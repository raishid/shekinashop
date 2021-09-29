from modules import public_wp
from modules import variables_data as var


def main():
    wp = public_wp.SkPublic(var.domain)
    datos = wp.readData('shekina.json')
    for product in datos:
        wp.PublicProduct(product)
        exit()


if __name__ == '__main__':
    main()