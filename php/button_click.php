<?PHP
// JQuery AJAX Tests
// Dommert Enterprises
?>
<html>
<head>

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js">
</script>
<script>
$(document).ready(function(){
$("button").click(function(){
       $('#results').load('button_output.php'); 
       
    });
});



</script>

</head>

<body>

<?PHP
// JQuery AJAX and PHP Tests
// Dommert Enterprises
?>

<p>Dont Not Click This Button!: <button>Click Me</button></p>

<P id="container"><!-- currently it's empty --></p>

<div id="results"></div>

</bodY>
</html>