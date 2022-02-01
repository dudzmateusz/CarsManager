# cars
The project presents a web application based on the framework : Django REST framework. The application has its own REST linked to REST data from an external database having vehicle information. Using the application we can send POST, GET API requests and receive feedback in JSON form.

![image](https://user-images.githubusercontent.com/80208983/152037824-a9392c43-f41a-47ed-ac1d-1d957dce0f09.png)

The application has no graphical interface. It is used only for data exchange. Data exchange is best performed using POSTMAN application.
https://www.postman.com/

The API data is stored in a PostgreSQL database under the database name - VA. The database contains the table myapi_vehicles and has the following columns:
![image](https://user-images.githubusercontent.com/80208983/152041197-79ea65e0-d86a-4dbd-881f-85fc4579a780.png)


Possible options: <br>
POST - cars/ ; rate/ ; <br>
DELETE - cars/{ id } ; <br>
GET - cars/ ; popular/ ;


Example POST request:
![image](https://user-images.githubusercontent.com/80208983/152038893-4dfc9a06-e841-4971-a2ad-0204570d6a1f.png)

Example GET response:
![image](https://user-images.githubusercontent.com/80208983/152039104-ff8db360-12f2-4e18-aee3-4ebc193ffa49.png)

Example of DELETE response:
![image](https://user-images.githubusercontent.com/80208983/152039657-2808e364-816c-4350-98ca-81d520c747b3.png)


