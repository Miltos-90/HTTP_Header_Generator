# TODO Packaging: https://www.freecodecamp.org/news/build-your-first-python-package/

from http_headers import HeaderGenerator

if __name__ == "__main__":
    
    cookies = {'cookie1': 'value1', 'cookie2': 'value2'}
    
    #f = './common_agents.txt'
    #f = './agents_for_testing.txt'
    #headers = HeaderGenerator(by = 'file', filename = f)
    #headers = HeaderGenerator(user_agents = 'program')
    
    #for _ in range(5):
    #    h = headers(httpVersion = 1)

    #    print(h)
    

    generator = HeaderGenerator()
    headers   = generator(
        country     = 'de', 
        httpVersion = 2)
    
    for k, v in headers.items():
        print(f'{k}: {v}')