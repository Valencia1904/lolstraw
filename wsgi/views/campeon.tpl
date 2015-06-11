% include('head.tpl')
		<!-- Banner -->
			<section id="banner">
				<h2><a href="/">LoL  Straw</h2>
				<p>Bienvenidos a la calculadora del Leage of legends</p>
			</section>

		<!-- Main -->
			<section id="main" class="container">

				<section class="box special">
				<span class="image featured"><img src="/static/images/{{nombre}}_0.jpg" alt="" /></span>
					<h3>{{nombre}}</h3>

				<div class="row">

				</div>
		<!-- Formulario -->
			</section>
			<section class="box">
				
					<div>
						<h3>Niveles</h3>
						
%for i in xrange(1,19):
						<a href="/campeones/{{nombre}}/{{i}}">{{i}}</a>
%end

						
					</div>
					
					
		<!-- Table -->

				<h3>Datos de nivel {{nivel}}</h3>
				<div class="table-wrapper">
					<table>
					

%for key, value in datos.iteritems():
						<tr>
							<td>{{key}} </td>
							<td>{{value}} </td>
						</tr>
%end
					</table>

				</div>
			</section>
% include('foot.tpl')

