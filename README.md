
# Walmart Trailer Management System

The Walmart Trailer Management System is a web-based application built using Django, designed to manage trailers transporting Walmart goods between Distribution Centers (DCs), Fulfillment Centers (FCs), and stores. 

## About WalmartTMS
The system includes three types of users: Admin, Driver, and Trailer Manager, each with distinct roles and access to specific features.

- Admin Dashboard

    Pending Consignments: View and allocate trucks and drivers to pending consignments.

    Consignment Status: Track the status of all consignments.
    Driver Management: Manage driver details, including salary, and view driver ratings.

    Trailer Management: Oversee all trailers, including their status and availability.

    Trailer Manager Requests: Approve or reject requests from trailer managers.

    Feedback/Issues: Address feedback or issues submitted by drivers or trailer managers.

- Driver Dashboard

    Trip Allocation: View assigned trips along with trailer details and necessary paperwork.

    General Information: Access personal information such as salary, rating, and work history.

- Trailer Manager Dashboard

    Application Process: Submit a form including rental service quotation parameters.

    Post-Approval Access: Manage rentals and view related information once approved by the Admin


## Run Locally

- Clone the project

```bash
  git clone https://github.com/rahulks01/WalmartTMS.git
```

- Go to the project directory

```bash
  cd WalmartTMS
```
- Initialize a python virtual environment

```bash
  python -m venv env
```

- Activate the virtual environment

```bash
  env\Scripts\activate      (On Windows)
  source venv/bin/activate  (On MacOS / Linux)
````

- Install dependencies

```bash
  pip install -r requirements.txt
```

- Check for migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
```

- Start the server

```bash
  python manage.py runserver
```
  Open your web browser and go to `http://127.0.0.1:8000/`
    
## Contributors
- [@bhaskar-nie](https://github.com/bhaskar-nie) 
- [@tahiramaan](https://github.com/tahiramaan)
- [@rahulks01](https://github.com/rahulks01)
- [@Ayush-5k](https://github.com/Ayush-5k)

