% include('head.tpl')
		<!-- Banner -->
			<section id="banner">
				<h2>LoL  Straw</h2>
				<h4><a href="/">Personajes	</a></h4><h4><a href="/objetos">Objetos</a></h4>
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
							<span class="image featured"><img src="static/images/{{i}}_Square_0.png" alt="" /></span>
							<h3>{{i}}</h3>
							<ul class="actions">
								<li><a href="/campeon/{{i}}" class="button alt">seleccionar</a></li>
							</ul>
						</section>

					</div>
%end
				</div>

			</section>
% include('foot.tpl')
