# TODO Check this when writing package: https://github.com/AhmedSakrr/Fake-Headers
# Tips and tricks: https://scrapeops.io/web-scraping-playbook/web-scraping-guide-header-user-agents/#ensuring-proper-header-order

from http_headers import HeaderGenerator

if __name__ == "__main__":

    
    cookies = {'sp_landing': 'https%3A%2F%2Fopen.spotify.com%2Fcollection%2Fplaylists%3Fsp_cid%3De8417a6b1784a200a50c049666bed54a%26device%3Ddesktop', 'sp_t': 'e8417a6b1784a200a50c049666bed54a'}
    
    #f = './common_agents.txt'
    f = './agents_for_testing.txt'
    headers = HeaderGenerator(by = 'file', filename = f)
    #headers = HeaderGenerator(by = 'program')
    e = 0
    for _ in range(2):
        h = headers(httpVersion=1, cookies=cookies, device='mobile', browser='safari')

        for k, v in h.items():
            print(k, v)
        
        if not bool(h): e+= 1
    #print()
    print(e)
