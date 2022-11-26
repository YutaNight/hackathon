FROM nginx:1.21.6

ENV TZ='Asia/Tokyo'

COPY default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

COPY dist/index.html /usr/share/nginx/html/index.html
COPY dist/static/ /usr/share/nginx/html/static/
COPY dist/favicon.ico/ /usr/share/nginx/html/favicon.ico
COPY dist/assets/ /usr/share/nginx/html/assets/
COPY 404.html /usr/share/nginx/html/404.html
COPY 50x.html /usr/share/nginx/html/50x.html

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]