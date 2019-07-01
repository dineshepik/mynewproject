FROM devopsedu/webapp
Maintainer "Edu Project"
ADD projCert-master/website /var/www/html
RUN apt-get update
RUN rm -rf /var/www/html/index.html

~                                                    

