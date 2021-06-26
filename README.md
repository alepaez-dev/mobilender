# mobilender api

### This repository is based on an orders system that allows us to create Clients, Providers, Items, Orders, Centers, etc
#### The technologies that were used are Django, Postgresql, Docker, Docker-compose, Swagger, RestAPI among others.

### DATABASE
1. First I observed the important points that were given to create the database. ![Screenshot from 2021-06-26 16-51-32](https://user-images.githubusercontent.com/74441510/123526628-6dc50900-d696-11eb-9741-5735837c6b16.png)
https://docs.google.com/spreadsheets/d/1cn750cEmG6AtyOyyqi6EAMryWIjPOWYMhsGZ-BM6aQA/edit?usp=sharing

2. After the points were I use a database diagram page to create the database more visually.
![Screenshot from 2021-06-26 16-54-48](https://user-images.githubusercontent.com/74441510/123526698-df04bc00-d696-11eb-9a45-2921499b142c.png)
https://dbdiagram.io/d/60d0cdff0c1ff875fcd5d074

3. After the structure of our database was completed and clear, I choose then to start our Django Project and configure our Docker Compose files.

#### All our database structure and relations are in our Django Project in the models.py file.



### Instructions
- FOR the execution some docker images and docker files were sent in a zip.
- All the swagger documentation can be found in the initial path http://127.0.0.1:8000/
- There is also a postman link to make test of all the CRUD, and the organization of the urls https://app.getpostman.com/join-team?invite_code=6648011be2fe43f8bfac9d7edcabe62d&ws=e89d18b8-98bf-45ab-a0b7-eb76338e329e 


### System flow
- The purposes of the data table Order are 2.
- 1. The first one is for the client to create an order with all the information. Order values associated_company, distribution_center, sucursal and stocked_date are set to null. This values are going to be changed and controlled by an administrador of the system
- 2. Once the order is created, the administrador is the one that is going to decide where is coming from. For that the administrador just needs to chose which one(Distribution Center, Associated Company, Sucursal) and the id of the one chosen. The stocked_date will be automatically fill once we change our order.

### Here are some mockups explaining the system flow above. This mockups are just to explain the flow, the design and some values are not important.
https://www.figma.com/file/9pbwPaCDg8lespNBfICqAO/Mobilender?node-id=0%3A1



