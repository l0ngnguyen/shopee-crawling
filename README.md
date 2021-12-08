# shopee-crawling
Crawling data from shopee shop by scrapy-splash
# Cài đặt môi trường 
## Cài đặt python
Hướng dẫn tại: https://www.python.org/downloads/
## Cài môi trường ảo của python
> `cd "đường dẫn đến thư mục chứa source code"`  
> `python3 -m venv .venv`  
> `source .venv/bin/activate`  
> `pip install -r requirements.txt`
## Cài đặt docker
hướng dẫn tại: https://docs.docker.com/engine/install/
## Cài đặt splash trên docker
### Chạy lần đầu để tải splash trên docker về
> `sudo docker pull scrapinghub/splash`

# Hướng dẫn crawl dữ liệu 
## Chỉnh sửa config.yaml
File này chứa các thông tin config của bài toán, tất cả config cần thiết đều sửa ở đây  
- selectors: các css selector sẽ được shopee thay đổi thường xuyên nên phải cập nhật lại nếu chạy ra kết quả ko như ý.
- start_urls: các url bắt đầu để crawl dữ liệu, thêm bớt url để lấy dữ liệu từ các trang mong muốn
- download_delay: độ trễ mỗi lần gửi request, càng cao thì càng lâu, nhưng nếu quá thấp dẫn tới gửi request liên tục, dễ bị cấm bởi server
- output: đường dẫn của file đích
## Mở dịch vụ Splash trên cổng 8050 của máy tính cục bộ
> `sudo docker run -p 8050:8050 scrapinghub/splash`
## Chạy file main.py
> `python3 main.py`

