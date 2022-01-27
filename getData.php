<?php
$dsn = 'mysql:dbname=pm;host=127.0.0.1;port=3306';
$username = 'root';
$password = '12332144';
try {
    $db = new PDO($dsn, $username, $password);
} catch(PDOException $e) {
    die('Could not connect to the database:
' . $e);
}
$db->query('set names utf8');
$sql = "select * from pm order by time desc limit 1";
$obj = $db->prepare($sql);
$obj->execute(array(1));
$arr = $obj->fetchAll(PDO::FETCH_ASSOC);
$data = array("pm"=>$arr[0]['data'],"date"=>$arr[0]['time']);
echo json_encode($data);
//print_r($arr[0][time]);
?>
