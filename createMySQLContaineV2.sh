#/bin/bash
sudo docker run --name melMySQL --network=host -p 3306:3307 -e MYSQL_ROOT_PASSWORD=senhas123 -e MYSQL_USER=rtrovato \
-e MYSQL_PASSWORD=senhas123 -e MYSQL_DATABASE=melproject -d mysql 

