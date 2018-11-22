<?php
$servername = "192.168.4.50";
$username = "userweb";
$password = "123456";
$dbname = "gamedb";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("link fail: " . $conn->connect_error);
}else {echo "link mysql Ok"; echo "       ";}

$username=$_POST['name'];
$userpassword=$_POST['password'];


$sql="insert into regtab (username,password) values ('$username','$userpassword')";

if($conn->query($sql)){echo "insert data ok"; }
$conn->close();

?>
