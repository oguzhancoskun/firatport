<script type="text/javascript">
/*$(document).ready(function() {
	$.timer(1000,function(){
		diveyaz();
	});
});
function diveyaz(){
	$.ajax({type:'GET',
			url:
			success: function(msj){
				$('div#istekler').html(msj);

			}
		});
}*/
/*

$(document).ready(function () {

$("#istekler").html("İçerik Değişti. Şimdi Üzerime Bolca Tıkla..");
});
*/
/*

$(document).ready(function () {
    $.ajax({
        url: 'http://localhost:8888/fpNew/pages/ips.xml',
        type: 'GET',
        dataType: "xml",
        success: function(data) {
           parseXml(data);
        }
    });
});

</script>
<?php include_once "pgconn.php";?>


<div class="panel panel-default" >
	<div class="panel-heading">Trafik 
		<i>
				<?php echo " ---------  // ".pg_fetch_assoc($result)["ipa"]; ?>
		</i>
	</div>
  	<div id="istekler" class="panel-body row fill" >
		<?php 
		while($row=pg_fetch_assoc($result))
		echo "<b>".$row["ipb"]."</b><br><span>".substr($row["tarih"],11)."</span><br>";
		?>
  	</div>
</div>