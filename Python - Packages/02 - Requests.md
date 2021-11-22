# Requests

( DOC : https://docs.python-requests.org/en/latest/ )

( UYGULAMA : https://httpbin.org/ )

- GET, POST ve diğer requestsleri oluşturma
- Requests yapılandırma;
    - Request içinde `params`, `data` ve `json` ile veri gönderme
    - Request headers bilgisini düzenleme `headers`
    - Dosya gönderme ([url](https://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file)) `files`
    - `allow_redirects` > default `True`
    - `timeout` ile timeout bilgisi girme
    - `proxies` ile proxy kullanımı ([url](https://docs.python-requests.org/en/latest/user/advanced/#proxies))
- Response içeriğini yazdırma 
    - `status_code`
    - `text`(string) & `content`(binary) & `raw`(raw)
    - `headers`
    - Response içerini json formatına çevirme (`r.json()`)
    - `cookies`
- Session objesi oluşturma ve cookie'lerin uzun süreli kullanımı 
- Authentication işlemleri ([url](https://docs.python-requests.org/en/latest/user/authentication/))

