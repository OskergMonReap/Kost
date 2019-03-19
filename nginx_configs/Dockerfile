FROM nginx:latest

COPY ./nginx.conf /etc/nginx/conf.d

RUN cp /etc/nginx/conf.d/nginx.conf /etc/nginx/nginx/conf && rm -rf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
