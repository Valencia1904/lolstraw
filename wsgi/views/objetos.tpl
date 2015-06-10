% include('head.tpl')
		<!-- Banner -->
			<section id="banner">
				<h2><a href="/">LoL  Straw</h2>
				<p>Bienvenidos a la calculadora del Leage of legends</p>
			</section>

		<!-- Table -->
			</section>
			<section class="box">
				<h3>Objetos</h3>
				<div class="table-wrapper">
					<table>
					

%for key, value in datos.iteritems():
						<tr>
							<td>{{value[0]}} </td>
							<td>{{!value[1]}} </td>
						</tr>
%end
					</table>

				</div>
			</section>
% include('foot.tpl')

