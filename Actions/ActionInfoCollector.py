from Actions.Abstract.Action import Action
from Events.EventEntityExtractor import EventEntityExtractor

class ActionInfoCollector(Action):

    def __init__(self, message, **kwargs):
        super().__init__(message)


        self.methods = kwargs['methods']


    def do(self):
        event_entity_extractor = EventEntityExtractor(text=self.message['text'], methods=self.methods)
        event_entity_extractor_result = event_entity_extractor.do()

        # Дозапрашиваем недостающие данные







    """
    {
    "user": {
        "chat_id": "",
        "fio": "",
        "language": "ru"
    },
    "message": {
        "date": "",
        "message_id": ""
    },
    "text": {
        "text": ""
    },
    "video": {
        "original": {
            "link": "",
            "name": "",
            "duration": 72,
            "size": 7845662
        }
        "thumb": {
            "link": "",
            "name": "",
            "duration": 72,
            "size": 7845662
        }
    },
    "photo": {
        "original": {
            "link": "",
            "name": "",
            "size": 7845662
        }
        "thumb": {
            "link": "",
            "name": "",
            "size": 7845662
        }
    },
    "file": {
        "link": "",
        "name": "",
        "size": 7845662
    },
    "contact": {
        "phone": "79611505050",
        "fio": "",
        "chat_id": ""
    },
}
    """


'''
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
#error_log /home/nginx_user/nginx_logs/error.log;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {


    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;
    error_log  /var/log/nginx/error.log notice;
    #access_log  /home/nginx_user/nginx_logs/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    # keepalive_timeout   65;
    types_hash_max_size 2048;


    default_type        application/octet-stream;
	include             /etc/nginx/mime.types;

    include /etc/nginx/conf.d/*.conf;






    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        rewrite_log on;
        resolver 127.0.0.11;    # Если в proxy_pass статичный адресс то нжинкс использует gethostbyaddr - локальный метод, если там переменная то адрес днса из резолвера, в нгинксе адрес резолвера лежит в etc/resolv.conf
        
        
        
        
        
        location ~ /chatbot/images
            
        
        
        
        
        
        
        
        
        
    	location ~ ^/(?<container>[a-zA-Z0-9_]+)/(?<port>[0-9]+)/ {

            if ($request_method = 'OPTIONS') {
                add_header 'Access-Control-Allow-Origin' '*';
                add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
                #
                # Custom headers and headers various browsers *should* be OK with but aren't
                #
                add_header 'Access-Control-Allow-Headers' 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range';
                #
                # Tell client that this pre-flight info is valid for 20 days
                #
                add_header 'Access-Control-Max-Age' 1728000;
                add_header 'Content-Type' 'text/plain; charset=utf-8';
                add_header 'Content-Length' 0;
                return 204;
            }
            if ($request_method = 'POST') {
                add_header 'Access-Control-Allow-Origin' '*';
                add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
                add_header 'Access-Control-Allow-Headers' 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range';
                add_header 'Access-Control-Expose-Headers' 'Content-Length,Content-Range';
            }
            if ($request_method = 'GET') {
                add_header 'Access-Control-Allow-Origin' '*';
                add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
                add_header 'Access-Control-Allow-Headers' 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range';
                add_header 'Access-Control-Expose-Headers' 'Content-Length,Content-Range';
            }
            # Запоминаем имя контейнера и порт из локейшена и склеиваем их в одну переменную
            
            #set $container $1;
            #set $port $2;
            set $full_host "${container}:${port}";
            #return 200 $full_host;
            
            keepalive_timeout   65;

            #rewrite ^/([a-zA-Z0-9_]+)/([0-9]+)(.*)$ $3 break; 	# $1 обозначает ту часть которая найдется в регекспе - в данном случае ищем в регекспе все что кроме /some_app и отсылаем только то что нашли на прокси
            rewrite ^/([a-zA-Z0-9_]+)/([0-9]+)/(.*)$ $3 break; 	# $1 обозначает ту часть которая найдется в регекспе - в данном случае ищем в регекспе все что кроме /some_app и отсылаем только то что нашли на прокси
            #rewrite ^/some_app(.*)$  $1 break; 	# $1 обозначает ту часть которая найдется в регекспе - в данном случае ищем в регекспе все что кроме /some_app и отсылаем только то что нашли на прокси
            
            
            proxy_pass http://$full_host;
            
            #proxy_pass http://$container:$port;
            #proxy_pass http://flask_test:5205;
            #proxy_pass http://localhost:5205;
            #proxy_pass http://os-4907:5205;

        }
        
        #location ~ ^/(receive_html|download_manifest|download_crx)


    }

}


'''