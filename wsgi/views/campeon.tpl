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

			</section>
			<section class="box">
				<h3>Datos</h3>
				<div class="table-wrapper">
					<thead>
						<tr>
%for dato in datos.keys()
							<th>{{dato}}</th>
%end
						</tr>
					</thead>
<!---					<tbody>
						<tr>
%for dato in datos;
							<td>dato[] 	</td>

						</tr>
					</tbody>--->
				</div>
			</section>
% include('foot.tpl')

