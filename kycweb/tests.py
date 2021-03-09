from django.test import TestCase

# # Create your tests here.
# {% load static %}
# <!DOCTYPE html>
# <html>
# <head>
# 	<title>Digital KYC</title>
# 	<!-- CSS only -->
# 	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
# 	<!-- JavaScript Bundle with Popper -->
# 	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
# 	<meta charset="utf-8">
# 	<meta name="viewport" content="width=device-width, initial-scale=1">
# 	<style>
# 		#videoElement {
# 			width: 600px;
# 			height: 450px;
# 			background-color: #666;
# 		}
# 	</style>
# </head>
# <body>
# 	<div class="container">
# 		<div class="row">
# 			<div class="col-lg-6" style="padding-top: 10%; padding-left: 5%">
# 				{% comment %} <video autoplay="true" id="videoElement">
# 				</video> {% endcomment %}
# 				<img src="{% url 'video_feed' %}">
#     {% comment %} <img src="{% url 'webcam_feed' %}"> {% endcomment %}
# 			</div>
# 			<div class="col-lg-6" style="padding-top: 13%; padding-left: 15%">
# 				{% comment %} <form action="/home/" method="post">
#                 {% csrf_token %}
# 					<div class="dropdown" style="padding-top: 14%;">
# 						<button class="btn btn-primary dropdown-toggle" style="width: 300px; height: 50px" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
# 							Select Document
# 						</button>
# 						<ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1" >
# 							<li><a class="dropdown-item" href="#" style="width: 300px; height: 50px">Aadhar</a></li>
# 							<li><a class="dropdown-item" href="#" style="width: 300px; height: 50px">Pan Card</a></li>
# 							<li><a class="dropdown-item" href="#" style="width: 300px; height: 50px">Driving License</a></li>
# 							<li><a class="dropdown-item" href="#" style="width: 300px; height: 50px">Passport</a></li>
# 							<li><a class="dropdown-item" href="#" style="width: 300px; height: 50px">Voter Card</a></li>
# 							<li><a class="dropdown-item" href="#" style="width: 300px; height: 50px">Bank Statement</a></li>
# 							<li><a class="dropdown-item" href="#" style="width: 300px; height: 50px">Passbook</a></li>
# 						</ul>
# 					</div>
# 					<div style="padding-top: 10%;">
# 						<input type="file" id="myFile" name="img"  style="width: 300px; height: 50px">
# 					</div>
# 					<div style="padding-top: 10%;">
# 						<button type="submit" class="btn btn-success"  style="width: 300px; height: 50px">Confirm</button>
# 					</div>
# 				</form>	 {% endcomment %}
#                 <hr>
# <form action="/home/" method="POST" style="border:1px solid #ccc" enctype="multipart/form-data">
#     {% csrf_token %}
#     <div class="contain">
# <div class="form-control">
#                 <label for="id">Choose Document:</label>
#                 <select id="filetype" name="filetype">
#                 <option value="sem0">- - -</option>
#                 <option value="sem1">Adhar Card</option>
#                 <option value="sem2">Pan Card</option>
#                 <option value="sem3">Driving License</option>
#                 <option value="sem4">Password</option>
#                 <option value="sem5">Votercard</option>
#                 <option value="sem4">Bank Statement</option>
#                 <option value="sem5">Passbook</option>
#                 </select><br>
#                 <label for="id">Choose File to Upload:</label>
#                 <input type="file" id="myFile" name="file">
#                 </div></div>
# <br>
# <div class="clearfix">
#       <button type="reset" class="cancelbtn" id="">Reset</button>
#       <button type="submit" class="signupbtn">upload</button>
#     </div>
# </form>
# <hr>
#                 <h1>{{msg}}</h1>
# 			</div>
# 		</div>
# 		<script>
# 			var video = document.querySelector("#videoElement");

# 			if (navigator.mediaDevices.getUserMedia) {
# 				navigator.mediaDevices.getUserMedia({ video: true })
# 				.then(function (stream) {
# 					video.srcObject = stream;
# 				})
# 				.catch(function (err0r) {
# 					console.log("Something went wrong!");
# 				});
# 			}
# 		</script>
# 	</body>
# 	</html>