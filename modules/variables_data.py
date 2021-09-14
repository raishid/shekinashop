
domain = 'mundokaos.net'

login = ''
pwd = ''

data_login = {
    'log': login,
    'pwd': pwd,
    #'rememberme': 'forever',
    'wp-submit': 'Acceder',
    'redirect_to': f'https://{domain}/wp-admin/',
    'testcookie': '1'
}

user_agent_login = {
    'Referer': f'https://{domain}/wp-login.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

