<?php

include_once './pages/controller.php';
include_once './pages/header.php';

$parola="zenci";

if (isset($_POST['parola']) and $_POST['parola']==$parola) {
	# code...

include_once './pages/container.php';
//include_once './pages/footer.php';
}
elseif (isset($_POST['parola']) and $_POST['parola']!=$parola) {
 	die("Hatalı Parola!");
 }
 else echo "<center>Anlık Port Dinleme ve STS, çağımız internetinin getirdiği güvenlik konusunu konu almaktadır.<br>
		Kullanılan teknolojiler ve geliştirme ortamları özgür olup Creative-Common lisansı ile lisanslanmıştır.<br>
		Proje  geliştirilebilir ve lisans şartları altında dağıtılabilir.<br>
		<br>
		Anlık Port Dinleme ve STS projesi anlık olarak portları tarayıp, ağ üzerinden herhangi bir saldırıyı tanımlayıp<br>
		harita üzerinde konum bilgisi ile bilgilendirme yeteneğine sahiptir. Saldırının şiddeti ve merkezinin bilinmesi sistemin <br>
		arka tarafında yer alan kullanıcılar için koruma imkanı tanır. Bu amaçla hayata geçirilmiştir.<br>
		Gelen saldırılara karşı sistem tarafındaki kullanıcıların tedbir alması amacıyla tasarlanmıştır.</center>"; //include pls
?>
