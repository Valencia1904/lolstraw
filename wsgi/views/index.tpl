% include('head.tpl')
		<!-- Banner -->
			<section id="banner">
				<h2>LoL  Straw</h2>
				<p>Bienvenidos a la calculadora del Leage of legends</p>
			</section>

		<!-- Main -->
			<section id="main" class="container">

				<!--<section class="box special">
				<span class="image featured"><img src="static/images/Akali_Splash_6.jpg" alt="" /></span>
					<h3>Sed lorem adipiscing</h3>-->

				<div class="row">
%for i in personajes:
					<div class="6u 12u(narrower)">

						<section class="box special">
							<span class="image featured"><img src="static/images/Akali_Splash_6.jpg" alt="" /></span>
							<h3>{{i}}</h3>
							<ul class="actions">
								<li><a href="#{{i}}" class="button alt">seleccionar</a></li>
							</ul>
						</section>

					</div>
%end
				</div>

			</section>
% include('foot.tpl')
