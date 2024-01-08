require 'uri'
require 'net/http'
require 'openssl'

url = URI("https://discord.com/api/v9/users/@me/guilds")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
http.verify_mode = OpenSSL::SSL::VERIFY_NONE

request = Net::HTTP::Get.new(url)
request["cookie"] = '__dcfduid=0b146740ad5f11ee96168ac23b560257; __sdcfduid=0b146740ad5f11ee96168ac23b560257d4bd5cfaab160db990170e9fdc1012dc4d7359664deadd0e14fe658ae4af9982; __cfruid=faf601ad29e6e5f972031e50e0c2c68668a67544-1704633421; _cfuvid=yg0ciMaKfyW_P_FI1le5HeteuqFNiCTUrC3DQ_pCu9U-1704633421506-0-604800000'
request["User-Agent"] = 'insomnia/8.5.1'
request["Authorization"] = 'ODk1NzIyMjYwNzI2NDQwMDA3.GHoV5X.F-3exoyipoMkWVVMdqxYr-XTWPtxHMF8jcm7mk'

response = http.request(request)
puts response.read_body