# TODO Check this when writing readme: https://github.com/AhmedSakrr/Fake-Headers, https://github.com/ua-parser/uap-python, 
# https://github.com/MichaelTatarski/fake-http-header/blob/main/README.md
# TODO Packaging: https://www.freecodecamp.org/news/build-your-first-python-package/

from http_headers import HeaderGenerator

if __name__ == "__main__":

    
    cookies = {'cookie1': 'value1', 'cookie2': 'value2'}
    
    f = './common_agents.txt'
    #f = './agents_for_testing.txt'
    headers = HeaderGenerator(by = 'file', filename = f)
    #headers = HeaderGenerator(by = 'scrape')
    e = 0
    for _ in range(2):
        h = headers(httpVersion=1, cookies=cookies, device='mobile', browser='safari', domain = 'pl')

        for k, v in h.items():
            print(k, v)
        
        if not bool(h): e+= 1
    #print()
    print(e)
