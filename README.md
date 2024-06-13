<h1>Inventory Management API</h1>

<h2>Overview</h2>
<p>This API allows for managing suppliers and items. It provides endpoints to create, retrieve, update, and delete suppliers and items, as well as associating items with multiple suppliers.</p><hr/>

<h2>Prerequisites</h2>
<ul>
<li>Python 3.10</li>
<li>Django 5.0.6</li>
<li>djangorestframework 3.15.1</li></ul><hr>

<h2>Setup</h2>
<h3>Clone the repository to your local machine:</h3>
<cite>git clone </cite><br>
<cite>cd Inventory</cite>
<h3>Create and Activate Virtual environment:</h3>
<cite>python -m venv venv</cite><br>
<cite>source venv\Scripts\activate</cite>
<h3>Install Dependencies:</h3>
<cite>pip install -r requirements.txt</cite>
<h3>Setup the database:</h3>
<cite>python manage.py migrate</cite><br>
<h3>Run Development Server:</h3>
<cite>python manage.py runserver</cite><br>
<p><b>API would be accessible on <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a></b></p><hr>

<h2>Interacting with API</h2>
<p><b>Please refer to <a href="https://documenter.getpostman.com/view/29653047/2sA3XPC2rZ">Postman collection of tests</a> to see tests and interactions with the API</b></p>
<hr>

<h2>Models</h2>
<h3>ContactInfo</h3>
<ul>
<li><b>address:</b> Charfield, maxlength 255</li>
<li><b>email:</b> Emailfield</li>
<li><b>telephone:</b> Charfield, maxlength 15</li></ul>
<h3>Supplier</h3>
<ul>
<li><b>id: </b>Integer, primary key</li>
<li><b>name: </b>Charfield, maxlength 100</li>
<li><b>contact_info: </b>OnetoOnefield with <b>Contact_info</b></li></ul>
<h3>Item</h3>
<ul>
<li><b>id:</b> Integer, primary key</li>
<li><b>name:</b> Charfield, maxlength 100</li>
<li><b>description:</b> Charfield, maxlength 150</li>
<li><b>price: </b> Integer</li>
<li><b>date:</b> DateTimefield</li>
<li><b>suppliers:</b> ManytoManyfield to <b>Supplier</b></li></ul><hr>

<h2>Serializers</h2>
<h3>ContactInfoSerializer</h3>
<p>Serializes ContactInfo data.</p>
<h3>SupplierSerializer</h3>
<p>Serializes supplier data as well as the associated <cite>contact_info</cite> and list of <cite>items</cite> that shows just item id. It also handles creation and updating of supplier data</p>
<h3>ItemSerializer</h3>
<p>Serializes item data as well as the associated <cite>supplier</cite>.</p>
<h3>ItemCreateSerializer</h3>
<p>Handles creation and updating of item data.</p><hr>

