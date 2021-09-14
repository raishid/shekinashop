from modules import public_wp
from modules import variables_data as var


def main():
    wp = public_wp.SkPublic(var.domain)
    datos_csv = list()
    print(wp.s.headers)


if __name__ == '__main__':
    main()