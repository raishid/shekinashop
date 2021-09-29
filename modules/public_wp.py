import requests
from requests_toolbelt import MultipartEncoder
from lxml import html
from modules import variables_data as var
from datetime import datetime
import cloudscraper
from time import sleep
import json
import csv
from datetime import datetime


class SkPublic:
    def __init__(self, domain):
        self.domain = domain
        session = requests.Session()
        session.headers = var.user_agent_login
        data_login = var.data_login
        url = f'https://{self.domain}/wp-login.php'
        while True:
            print('Iniciando Sesion.')
            s = cloudscraper.create_scraper(sess=session)
            r = s.post(url, data=data_login, allow_redirects=True)
            if r.status_code == 200:
                break
            else:
                sleep(5)
        self.s = s
        #self.s.get(f'https://{self.domain}/wp-admin')


    def readData(self, filejson):
        file = open(filejson, 'r', encoding='UTF-8').read()
        data = json.loads(file)
        return data['data']['products']['results']
    """
    "name": titulo,
          "techReport": descripcion corta,
          "externalId": SKU,
          "availableQuantity": stock,
          "description": "descipcion larga",
          "newBasePrice": precio,
          "category": {
            "name": categoria
          },
          "vendor": {
            "businessName": etiqueta
          },
    """
    def PublicProduct(self, data_public):
        titulo = data_public['name']
        desc_corta = data_public['techReport']
        sku = data_public['externalId']
        stock = data_public['availableQuantity']
        desc_larga = data_public['description']
        precio = data_public['newBasePrice']
        categoria = var.categorias[data_public['category']['name']]
        tag = data_public['vendor']['businessName']
        imagenes = data_public['images']
        imagenes_galeria = list()
        if len(imagenes) > 1:
            count = 1
            imagen_principal = imagenes[0]['url']
            while True:
                imagenes_galeria.append(imagenes[count]['url'])
                count += 1
                if count == len(imagenes):
                    break
        else:
            imagen_principal = imagenes[0]

        #print(self.s.cookies)
        r = self.s.get(f'https://{self.domain}/wp-admin/post-new.php?post_type=product')
        soup = html.fromstring(r.text)
        wpnonce = soup.xpath('//input[@name="_wpnonce"]/@value')[0]
        post_id = soup.xpath('//input[@name="post_ID"]/@value')[0]
        samplepermalinknonce = soup.xpath('//input[@name="samplepermalinknonce"]/@value')[0]
        ajax_nonce_add_product_cat = soup.xpath('//input[@name="_ajax_nonce-add-product_cat"]/@value')[0]
        woocommerce_meta_nonce = soup.xpath('//input[@name="woocommerce_meta_nonce"]/@value')[0]
        #ajax_nonce = soup.xpath('//input[@name="_ajax_nonce"]/@value')[0]
        wd_metabox_nonce_class_metaboxphp = soup.xpath('//input[@name="wd-metabox-nonce_class-metaboxphp"]/@value')[0]
        elementor_edit_mode_nonce = soup.xpath('//input[@name="_elementor_edit_mode_nonce"]/@value')[0]
        joinchat_nonce = soup.xpath('//input[@name="joinchat_nonce"]/@value')[0]

        fecha_actual = datetime.today()
        dia = fecha_actual.day
        mes = fecha_actual.month
        ano = fecha_actual.year
        hora = fecha_actual.hour
        minuto = fecha_actual.minute
        yesterday = int(dia) - 1

        request_data = {
            '_wpnonce': wpnonce,
            'user_ID': '2',
            'action': 'editpost',
            'originalaction': 'editpost',
            'post_author': '2',
            'post_type': 'product',
            'original_post_status': 'auto-draft',
            'post_ID': post_id,
            'original_post_title': '',
            'post_title': titulo,
            'samplepermalinknonce': samplepermalinknonce,
            '_elementor_edit_mode_nonce': elementor_edit_mode_nonce,
            'wp-preview': '',
            'content': desc_larga,
            'hidden_post_status': 'draft',
            'post_status': 'draft',
            'hidden_post_password': '',
            'hidden_post_visibility': 'public',
            'visibility': 'public',
            'post_password': '',
            'jj': str(dia),
            'mm': str(mes),
            'aa': str(ano),
            'hh': str(hora),
            'mn': str(minuto),
            'ss': '00',
            # LA FECHA HIDDEN DEBE SER MENOR AL ACTUAL
            'hidden_mm': str(mes - 1),
            'hidden_jj': str(yesterday),
            'hidden_aa': str(ano),
            'hidden_hh': '00',
            'hidden_mn': '00',
            'current_visibility': 'visible',
            'current_featured': 'no',
            '_visibility': 'visible',
            'original_publish': 'Publicar',
            'publish': 'Publicar',
            'tax_input[product_cat][]': (0, categoria,),
            'newproduct_cat': 'Nombre de la nueva categoría',
            'newproduct_cat_parent': '-1',
            '_ajax_nonce-add-product_cat': ajax_nonce_add_product_cat,
            'tax_input[product_tag]': tag,
            'newtag[product_tag]':'',
            'page_template': 'default',
            'gla_channel_visibility_visibility': 'sync-and-show',
            'joinchat_nonce': joinchat_nonce,
            'joinchat_telephone': '',
            'joinchat_message': '',
            'joinchat_message_send': '',
            'joinchat_view': '',
            '_thumbnail_id': '-1',
            'knawatfibu_url': imagen_principal,
            'woocommerce_meta_nonce': woocommerce_meta_nonce,
            'product-type': 'simple',
            'product_image_gallery': '',
            'product_360_image_gallery': '',
            'product_url': '',
            '_button_text': '',
            '_regular_price': str(precio),
            '_sale_price': '',
            '_sale_price_dates_from': '',
            '_sale_price_dates_to': '',
            '_download_limit': '',
            '_download_expiry': '',
            '_sku': sku,
            '_manage_stock': 'yes',
            '_stock': str(stock),
            '_original_stock': '0',
            '_backorders': 'no',
            '_low_stock_amount': '',
            '_stock_status': 'instock',
            'woodmart_total_stock_quantity': '',
            'sp_wc_barcode_type_field': 'none',
            'sp_wc_barcode_field': '',
            '_weight': '',
            '_length': '',
            '_width': '',
            '_height': '',
            'product_shipping_class': '-1',
            '_shipping_custom_price_product_smp[14743]': '',
            'attribute_taxonomy': '',
            '_purchase_note': '',
            'menu_order': '0',
            'comment_status': 'open',
            #'_ajax_nonce': ajax_nonce,
            'excerpt': desc_corta,
            'wd-metabox-nonce_class-metaboxphp': wd_metabox_nonce_class_metaboxphp,
            '_woodmart_whb_header': 'none',
            '_woodmart_product_design': 'inherit',
            '_woodmart_single_product_style': 'inherit',
            '_woodmart_thums_position': 'inherit',
            '_woodmart_product-background': '',
            '_woodmart_main_layout': 'default',
            '_woodmart_sidebar_width': 'default',
            '_woodmart_custom_sidebar': 'none',
            '_woodmart_extra_content': '',
            '_woodmart_extra_position': 'after',
            '_woodmart_product_custom_tab_title': '',
            '_woodmart_product_custom_tab_content': '',
            '_woodmart_new_label_date': '',
            '_woodmart_swatches_attribute': '',
            '_woodmart_product_video': '',
            '_woodmart_product_hashtag': '',
        }
        if len(imagenes_galeria) > 0:
            for index, img in enumerate(imagenes_galeria):
                index += 1
                request_data[f'knawatfibu_wcgallary[{str(index)}][url]'] = img

        print(request_data)

        r = self.s.post(f'https://{self.domain}/wp-admin/post.php', data=request_data)
        print(r.status_code)
        print(r.url)



    def Leer_csv(self):
        data = list()
        with open('1.csv', 'r', encoding='UTF-8', newline='') as db:
            w = csv.DictReader(db)
            for row in w:
                valores = {
                    'id': row['id'],
                    'descripción_corta': row['descripción_corta'],
                    'SKU': row['SKU'],
                    'name': row['name'],
                    'inventario': row['inventario'],
                    'description': row['description'],
                    'precio': row['precio_normal'],
                    'etiquetas': row['etiquetas'],
                    'categorias': row['categorias'],
                    'image/url': row['image/url'],
                    'images/0/url': row['images/0/url'],
                    'images/1/url': row['images/1/url'],
                    'images/2/url': row['images/2/url'],
                    'images/3/url': row['images/3/url'],
                    'images/4/url': row['images/4/url'],
                    'images/5/url': row['images/5/url'],
                    'images/6/url': row['images/6/url'],
                    'images/7/url': row['images/7/url'],
                    'images/8/url': row['images/8/url'],
                    'images/9/url': row['images/9/url'],
                    'images/10/url': row['images/10/url'],
                    'images/11/url': row['images/11/url'],
                    'images/12/url': row['images/12/url'],
                    'images/13/url': row['images/13/url'],
                    'images/14/url': row['images/14/url'],
                    'images/15/url': row['images/15/url'],
                    'images/16/url': row['images/16/url'],
                    'images/17/url': row['images/17/url'],
                    'images/18/url': row['images/18/url'],
                    'images/19/url': row['images/19/url'],
                    'images/20/url': row['images/20/url'],
                }
                data.append(valores)
            return data
